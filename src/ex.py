# import os

# base_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir =  os.path.dirname(base_dir)
# print(base_dir)
# print(parent_dir)

from kivy.app import App
import os

# Use the user data directory for storing files
user_data_dir = App.get_running_app().user_data_dir
output_folder = os.path.join(user_data_dir, 'project_app', 'videos')