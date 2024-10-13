import pyrebase
# import firebase_admin
# from firebase_admin import credentials
import json
import time
import os
from playsound import playsound

class fire_base_download:

  def fire(self):
    config = {
      'apiKey': os.getenv('firebase_api_key'),
      'authDomain': "alert-sys-5b1b9.firebaseapp.com",
      'projectId': "alert-sys-5b1b9",
      'storageBucket': "alert-sys-5b1b9.appspot.com",
      'messagingSenderId': "524250563384",
      'appId': "1:524250563384:web:6e2358c3498d6b1c5d77cd",
      'measurementId': "G-EFNXPD2W04",
      'serviceAccount':'serviceAccount.json',
      'databaseURL':'https://alert-sys-5b1b9-default-rtdb.firebaseio.com/'
      }


    fire_base = pyrebase.initialize_app(config)
    storage = fire_base.storage()
    # storage.child('bilal_3.avi').put('bilal_3.avi')
    output_folder = r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\Kivy_app\project_app\videos'
    if not os.path.exists(output_folder):
      os.makedirs(output_folder, exist_ok= True)

    try:

      all_files = storage.list_files()
      
      for i, file in enumerate(all_files):
        with open('text_json_files/h.json', 'r') as f:
          data = json.load(f)
        if i > int(data['num']):
          l = file.name
          with open('text_json_files/h.json', 'w') as f:
            data['num'] = i
            json.dump(data,f)
        
          output_f = os.path.join(output_folder,f'{time.time()}-{i}.avi')
          storage.download(l,output_f)
          # sound_file = r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\Kivy_app\project_app\beep.mp3'
          # playsound(sound_file)
    except:
      print('not_found')
  
  