import pyrebase
import aiohttp
import asyncio
import os

json_add = r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\Kivy_app\project_app\text_json_files'

config = {
    'apiKey': os.getenv('firebase_api_key'),
    'authDomain': "alert-sys-5b1b9.firebaseapp.com",
    'projectId': "alert-sys-5b1b9",
    'storageBucket': "alert-sys-5b1b9.appspot.com",
    'messagingSenderId': "524250563384",
    'appId': "1:524250563384:web:6e2358c3498d6b1c5d77cd",
    'measurementId': "G-EFNXPD2W04",
    'serviceAccount':os.path.join(json_add,'serviceAccount.json'),
    'databaseURL':'https://alert-sys-5b1b9-default-rtdb.firebaseio.com/'
}


fire_base = pyrebase.initialize_app(config)
db = fire_base.database()
storage = fire_base.storage()

async def download_file(session, file_name):
    """Download a file from Firebase Storage."""
    download_url = storage.child(file_name).get_url(None)  # Get the download URL
    async with session.get(download_url) as response:
        if response.status == 200:
            # Ensure the local folder exists
            local_folder = 'local_folder'
            os.makedirs(local_folder, exist_ok=True)

            local_file_path = os.path.join(local_folder, file_name)
            with open(local_file_path, 'wb') as f:
                f.write(await response.read())  # Write the response content to a file
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download {file_name}: {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            # Read previously downloaded files
            try:
                with open('ex1.txt', 'r') as r_file:
                    downloaded_files = set(r_file.read().split(','))
            except FileNotFoundError:
                downloaded_files = set()  # Initialize as empty if file not found

            # List files in the storage bucket
            all_files = storage.list_files()
            tasks = []

            for file in all_files:
                if file.name not in downloaded_files:
                    tasks.append(download_file(session, file.name))

                    # Update the downloaded files record
                    with open('ex1.txt', 'a') as a_file:
                        a_file.write(f',{file.name}')
                    downloaded_files.add(file.name)

            # Run all download tasks concurrently
            if tasks:
                await asyncio.gather(*tasks)

            # Wait before checking again
            await asyncio.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")

