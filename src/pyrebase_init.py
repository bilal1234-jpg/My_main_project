import pyrebase
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir =  os.path.dirname(base_dir)


json_add = os.path.join(parent_dir,'other_resources')

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

try:
    fire_base = pyrebase.initialize_app(config)
    db = fire_base.database()
    storage = fire_base.storage()
    db = fire_base.database()

except Exception as e:
        storage = 0
        db = 0
        print("Error {e}")
