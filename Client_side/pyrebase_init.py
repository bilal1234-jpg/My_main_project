import pyrebase
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