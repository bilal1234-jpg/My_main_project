import os
from pyrebase_init import storage

class fire_base_download:

    def fire(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir =  os.path.dirname(base_dir)

        output_folder = os.path.join(parent_dir,'assets','videos')
        txt_path = os.path.join(parent_dir,'other_resources')
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder, exist_ok=True)

        try:
            all_files = storage.list_files()

            # Check if ex1.txt exists before reading
            if not os.path.exists(f'{txt_path}/ex1.txt'):
                with open(f'{txt_path}/ex1.txt', 'w') as file:
                    pass  # Create an empty file if it doesn't exist

            with open(f'{txt_path}/ex1.txt', 'r') as r_file:
                r = r_file.read()

            ra = r.split(',')
            
            for i, file in enumerate(all_files):
                l = file.name
                if l not in ra:
                    with open(f'{txt_path}/ex1.txt', 'a') as a_file:
                        a_file.write(f',{l}')
                    print(l)
                    storage.download(l, f'{output_folder}/logo{i}.avi')

        except Exception as e:
            print(f"An error occurred: {e}")
            

