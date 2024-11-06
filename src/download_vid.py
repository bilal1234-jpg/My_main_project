import os
from pyrebase_init import storage
from datetime import datetime
class fire_base_download:

    def fire(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir =  os.path.dirname(base_dir)

        output_folder = os.path.join(parent_dir,'assets','videos')
        txt_path = os.path.join(parent_dir,'other_resources')
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder, exist_ok=True)

        if storage != 0:
            try:
                all_files = storage.list_files()

                # Check if ex1.txt exists before reading
                if not os.path.exists(f'{txt_path}/ex1.txt'):
                    with open(f'{txt_path}/ex1.txt', 'w') as file:
                        pass  # Create an empty file if it doesn't exist

                with open(f'{txt_path}/ex1.txt', 'r') as r_file:
                    r = r_file.read()
                    r_file.close()

                ra = r.split(',')
                
                for i, file in enumerate(all_files):
                    l = file.name
                    if l not in ra:
                        with open(f'{txt_path}/ex1.txt', 'a') as a_file:
                            a_file.write(f',{l}')
                        print(l)
                        now = datetime.now()
                        video_time = now.strftime("%d-%m-%Y_%H-%M-%S").replace(':', '-')
                        storage.download(l, os.path.join(output_folder, f'video_time--{video_time}.avi'))

            except Exception as e:
                pass
                

