from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager
from kivymd.uix.filemanager import MDFileManager
from  sql_app import User , session
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
import smtplib
import tensorflow as tf
import cv2
from tensorflow.keras import models
import numpy as np
import os
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import threading
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.list import  IconLeftWidget, IconRightWidget
from kivy.properties import BooleanProperty
from kv import helper1
from kivy.core.window import Window  
from kivy.animation import Animation
from  kivymd.uix.floatlayout import FloatLayout
from  kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.graphics import Canvas 
from kivy.graphics import Rectangle 
from kivymd.uix.button import MDIconButton
from voice import voice_detect
import time
import tensorflow_hub as hub
import pyrebase
from download_vid import fire_base_download




############################################## Fire Base Keys#############################################################################
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
###################################################### Models ###################################################################################

model1 = hub.load('https://tfhub.dev/google/movenet/multipose/lightning/1')
movenet_multi = model1.signatures['serving_default']

model = hub.load('https://www.kaggle.com/models/google/movenet/TensorFlow2/singlepose-thunder/4')
movenet = model.signatures['serving_default']


# model_num1 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\model_semi_final1.h5')
# model_num2 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\model_semi_final.h5')
# model_num3 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\model_semi_final2.h5')
# model_num4 =  models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\model_final1.h5')
# model_num5 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\model_final.h5')
# model_num6 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\model_final2.h5')

# model_num1 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\two_model_model_final.h5')
model_num2 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\two_model_model_final1.h5')
model_num3 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\two_model_model_final2.h5')
model_num4 = models.load_model(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\two_model_model_final3.h5')

############################################################ EDGES ###############################################################3

EDGES = {
    (0, 1): 'm',
    (0, 2): 'c',
    (1, 3): 'm',
    (2, 4): 'c',
    (0, 5): 'm',
    (0, 6): 'c',
    (5, 7): 'm',
    (7, 9): 'm',
    (6, 8): 'c',
    (8, 10): 'c',
    (5, 6): 'y',
    (5, 11): 'm',
    (6, 12): 'c',
    (11, 12): 'y',
    (11, 13): 'm',
    (13, 15): 'm',
    (12, 14): 'c',
    (14, 16): 'c'
}




####################################################### Screens Class #########################################################################




class LoginScreen(Screen):
    text = StringProperty()
class SignupScreen(Screen):
    text = StringProperty()  
    vid_img_scr = BooleanProperty(True)
class MainScreeen(Screen):
    vid_img_scr = BooleanProperty(True)
class ForgotScreen(Screen):
    pass
class HistoryScreen(Screen):
    pass
class Video_screen(Screen):
    pass
class About_us(Screen):
    pass



class Start_page_UI(Screen):
    def __init__(self, **kwargs):
        super(Start_page_UI, self).__init__(**kwargs)
        # You can still define and add widgets here
        # with self.canvas.before:
        #     Rectangle(source='bg6.jpg', pos=self.pos, size=Window.size)
        
        box_layout = FloatLayout()
        self.image = Image(source='logo2.png', pos_hint={'center_x': 0.1, 'center_y': 0.1}, size = (self.height*1, self.width*1), size_hint=(None, None))
        self.md_label = MDLabel(text='ChildGuard', halign='center', size=(self.height*0, self.width*0), size_hint_y=None, font_style='H4', bold=True, theme_text_color="Custom",
            text_color=(0,0,0,1))
        self.animate_lable()
        box_layout.add_widget(self.md_label)
        self.animate_image()
        self.add_widget(self.image)
        button1 = MDIconButton(icon = "next-button.png", pos_hint={"center_x": .5, 'center_y': 0.1} ,icon_size =  "100sp", on_release=self.login)
        
        box_layout.add_widget(button1)
        self.add_widget(box_layout)
    
    def login(self, *args):
        if self.manager:
            self.manager.current = 'login'
        else:
            print("Error: 'manager' is not defined")

    def animate_image(self, *args):
        anim = Animation(size = (self.height,self.width ))
        anim += Animation(size = (self.height*4, self.width*4),pos_hint={'center_x': 0.5, 'center_y': 0.6}, transition = 'in_quad')
        anim.start(self.image)
    def animate_lable(self, *args):
        anim_lable = Animation(size = (self.height, self.width ))
        anim_lable += Animation(size = (self.height*4, self.width*4), transition = 'in_circ')
        anim_lable.start(self.md_label)
        

################################################# Main Class #############################################################################

class apps(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager_obj =  MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager,
            search = 'all',
            
        )
        self.selected_path = 'no_select_any_image'
        self.sequence = []
        self.threshold = 0.2
        self.model_accuracy = []
        self.num_of_frame = 15
        self.number_of_dataset = 1000
        self.actions = np.array(['normal','slap','kick'])
        self.Data_path = os.path.join('MP_DATA')
        self.res = np.zeros((len(self.actions),))
        self.vid_frame = []
        self.vid_i = 0
        self.camera = False
        self.flip_camera = 0
        self.cv2_path  = None
        self.mic_0_1 = 0
        self.v = voice_detect()
        self.mic_thread = None
        self.mic_running = False
        self.sequence_length = 10
        self.confidence_thresholds = 0.3
        self.threshold = 0.3
        self.action = 'normal'
        self.color = (0,255,0)
        self.fire_base = fire_base_download()
       
####################################################### Picture change in main and sign pages #######################################################################
    def select_path(self, path):
       
        try:
            
            curr_scr = self.screen.current
            
            if curr_scr == 'signup':
                self.root.get_screen('signup').ids.fit_image2.source = path
                self.exit_manager(path)
                self.selected_path = path
            if curr_scr == 'main':
               
                self.exit_manager(path)
                self.cv2_path = path
                self.main_page()
                
        except AttributeError as e:
            
            self.exit_manager(path)
            self.selected_path = ' '
################################################## Open Folder ############################################################################        
    def open_file_manager(self):
        self.file_manager_obj.show('/')
################################################## CLose Folder #############################################################################
    def exit_manager(self, obj):
        self.file_manager_obj.close()
################################################# Check Error in signup page email #######################################################################
    def error(self):
        err = self.root.get_screen('signup').ids.email.error
        return err
################################################## Sign Up or register user #################################################################                
    def add_user(self):
        name = self.root.get_screen('signup').ids.name.text
        email = self.root.get_screen('signup').ids.email.text
        password = self.root.get_screen('signup').ids.password.text
        
        err = self.error()
        if name and email and password:
             if err != True:
                new_user = User(name=name, email=email, password = password, img_address = self.selected_path)
                session.add(new_user)
                session.commit()
                
                self.root.get_screen('signup').ids.name.text = ''
                self.root.get_screen('signup').ids.email.text = ''
                self.root.get_screen('signup').ids.password.text = ''
                self.root.get_screen('signup').ids.fit_image2.source = 'sign.png' 
                
             else:
                 self.root.get_screen('signup').ids.email.helper_text = 'Enter correct Email first'
                 
        else:
             dialog = MDDialog(
             title="Warning",
             text="Name, Email and Password cannot be empty",
             size_hint=(0.5, 0.3)
                )
             dialog.open()
################################################## Check user use name or email in login ##########################################################################
    def login_diplay(self):
        err = self.root.get_screen('login').ids.username.error
        if err == True:
            self.root.get_screen('login').ids.username.helper_text = 'Name'
            return 'name'
        else:
            self.root.get_screen('login').ids.username.helper_text = 'Email:user@gmail.com'
            return 'email'
################################################### Check Email and Password in Login page from DB ########################################################################    
    def login_user(self):
        check = self.login_diplay()
        from_username_feild = self.root.get_screen('login').ids.username.text
        from_password_feild = self.root.get_screen('login').ids.password.text
        if from_password_feild and from_username_feild:
            if check == 'name':
                user = session.query(User).filter(User.name == from_username_feild).first()
                password = session.query(User).filter(User.password == from_password_feild).first()
                if user:
                    if password:
                        self.root.get_screen('main').ids.email.title = user.name
                        self.root.get_screen('main').ids.draw_name.text = user.name
                        self.root.get_screen('main').ids.email_drawer = user.email
                        self.root.get_screen('main').ids.fit_image3.source =user.img_address
                        self.root.current = 'main'
                        self.root.get_screen('login').ids.username.text = ''
                        self.root.get_screen('login').ids.password.text =  ''
                    else:
                        dialog = MDDialog(
                        title="Warning",
                        text="Incorrect Password, click forget , if you forget password",
                        size_hint=(0.5, 0.3)
                            )
                        dialog.open()  
                else:
                    dialog = MDDialog(
                    title="Warning",
                    text="Try Email or Create a new account",
                    size_hint=(0.5, 0.3)
                        )
                    dialog.open()   
           
            if check == 'email':
                user = session.query(User).filter(User.email == from_username_feild).first()
                password = session.query(User).filter(User.password == from_password_feild).first()
            
                if user:
                    if password:
                        self.root.get_screen('main').ids.email.text = user.name
                        self.root.get_screen('main').ids.draw_name.text = user.name
                        self.root.get_screen('main').ids.email_drawer = user.email
                        self.root.get_screen('main').ids.fit_image3.source =user.img_address
                        self.root.current = 'main'
                        self.root.get_screen('login').ids.username.text = ''
                        self.root.get_screen('login').ids.password.text = ''
                    else:
                        dialog = MDDialog(
                        title="Warning",
                        text="Incorrect Password, click forgot Password , if you forget password",
                        size_hint=(0.5, 0.3)
                            )
                        dialog.open()  
                    
                    

                else:
                    dialog = MDDialog(
                    title="Warning",
                    text="Incorrect Email, Create a new account",
                    size_hint=(0.5, 0.3)
                        )
                    dialog.open()   

        else:
            dialog = MDDialog(
            title="Warning",
            text="No text feild can be empty",
            size_hint=(0.5, 0.3)
                )
            dialog.open()   
 
################################################## Forgot Password SMTP #################################################################
    def forgot_password(self):
        email_feild = self.root.get_screen('forgotpass').ids.email.text
        database_check = session.query(User).filter(User.email == email_feild).first()
        if email_feild:
            if database_check:
                try:
                    connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)  
                    connection.login(user='ijazb1622@gmail.com', password='xyz')   
                    connection.sendmail(from_addr='ijazb1622@gmail.com',
                                        to_addrs=f"{database_check.email}", 
                                        msg=f"Subject:Your reset password from Bilal Blog\n\n Your Password:{database_check.password}")

                    connection.quit() 
                    dialog = MDDialog(
                    title="Warning",
                    text="Successfully Sent.",
                    size_hint=(0.5, 0.3)
                        )
                    dialog.open()
                except:
                    dialog = MDDialog(
                    title="Warning",
                    text="Failed Internet Connection",
                    size_hint=(0.5, 0.3)
                        )
                    dialog.open()

            else:
                dialog = MDDialog(
                title="Warning",
                text="singn up not this email found in database",
                size_hint=(0.5, 0.3)
                    )
                dialog.open()
        else:
             dialog = MDDialog(
                title="Warning",
                text="No text can be empty",
                size_hint=(0.5, 0.3)
                    )
             dialog.open()
    
    ############################################ TEMP COMMENT OUT #################################################################
    ############################################# OpenCv for model detection #############################################################################
    def camera_flip(self):
        
        if self.flip_camera == 0:
            self.root.get_screen('main').ids.email.right_action_items = [["camera-flip", lambda x: self.camera_flip(), 'Back']]

            self.flip_camera = 1
            self.cv2_path = None
        else:
            self.root.get_screen('main').ids.email.right_action_items = [["camera", lambda x: self.camera_flip(), 'Front']]
            self.flip_camera = 0
            self.cv2_path = None
        
    
    def main_page(self):
        try:
            if self.cv2_path:
                self.img = self.screen.get_screen('main').ids.camera_feed
                int_cam = int(self.flip_camera)
                
                self.capture = cv2.VideoCapture(self.cv2_path)
                self.clock_event = Clock.schedule_interval(self.update, 1.0 / 30.0)
            else:    

                self.img = self.screen.get_screen('main').ids.camera_feed
                int_cam = int(self.flip_camera)
            
                self.capture = cv2.VideoCapture(int_cam)
                self.clock_event = Clock.schedule_interval(self.update, 1.0 / 30.0)
        except cv2.Error as e:

            
            dialog = MDDialog(
                title="Warning",
                text="No camera available, flip camera from top corner",
                size_hint=(0.5, 0.3)
                    )
            dialog.open()



    ###################################################################################################################
    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            height, width, _ = frame.shape
            frame = self.process_frame(frame, height, width)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img.texture = image_texture
    ###########################################################################################################
    def is_collide(self , box1, box2):
        return not (box1[2] < box2[0] or    # box1's right < box2's left
                    box1[0] > box2[2] or    # box1's left > box2's right
                    box1[3] < box2[1] or    # box1's bottom < box2's top
                    box1[1] > box2[3]) 
    

    def check_collide(self,bound_boxes):
        for i in range(len(bound_boxes)):
            for j in range(i + 1, len(bound_boxes)):
                if self.is_collide(bound_boxes[i], bound_boxes[j]):
                    return True
        return False
                
    
    def process_frame(self, frame,height,width ):
            bound_boxes = []  
            
            self.camera = True
            self.vid_frame.append(frame)
            img = frame.copy()
            img = tf.image.resize(tf.expand_dims(img, axis=0), (256, 256))
            input_img = tf.cast(img, dtype=tf.int32)
            results = movenet(input_img)
            result2 = movenet_multi(input_img)
            
            keypoints_with_scores = results['output_0'].numpy()[:, :, :51].reshape((1, 17, 3))
            keypoints_with_scores_boxes = result2['output_0'].numpy()[0]
            np.set_printoptions(precision = 8, suppress = True)
            
            # Render keypoints
            # self.loop_through_people(frame, keypoints_with_scores, EDGES, 0.2)
            for i,box in enumerate(keypoints_with_scores_boxes):
                ymin, xmin, ymax, xmax , confidence = box[-5:]
                
                if confidence > 0.10:
                    
                    
                    #make box points by mul keypoint give by movenet with frame height and width
                    
                    start_point = (int(xmin * width), int(ymin * height))  # Top-left corner
                    end_point = (int(xmax * width), int(ymax * height))
                    
                    
                        # Show to screen
                    
                    cv2.rectangle(frame, start_point, end_point, self.color,3)
                    bound_boxes.append((xmin*width, ymin*height,xmax*width, ymax*height))
                    collision_detected = self.check_collide(bound_boxes)
                    cv2.putText(frame, self.action, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.LINE_AA)

            for person_ in keypoints_with_scores:
          
                xx = []
                yy = []
                zz = []
            
                    
                
                
                for key_point in person_:
                    x, y, z = key_point
        
                    xx.append(x)
                    yy.append(y)
                    zz.append(z)
                x_axis = np.array(xx).flatten()
                y_axis = np.array(yy).flatten()
                z_axis = np.array(zz).flatten()
                final_keypoint = np.concatenate([x_axis,y_axis,z_axis])
                        
                        
                self.sequence.append(final_keypoint)
                    
                
            
                if len(self.sequence)==10:
                    
                    # res1 = model_num1.predict(np.expand_dims(sequence, axis=0), verbose=0)[0]
                    res2 = model_num2.predict(np.expand_dims(self.sequence, axis=0), verbose=0)[0]
                    res3 = model_num3.predict(np.expand_dims(self.sequence, axis=0), verbose=0)[0]
                    res4 = model_num4.predict(np.expand_dims(self.sequence, axis=0), verbose=0)[0]
                
                    
                    res = np.mean([res2,res3,res4], axis=0)
                    # res = res3
                    # print(res)
                    # print(len(sequence))
                    # res = (res1+res2)/2
                    self.sequence = []
                        
                        
                    if collision_detected: 
                        
                        if res[res.argmax()] > 0.10:
                            self.color = (0,0,255)
                            self.action = self.actions[res.argmax()]
                        
                            if self.action == 'slap' or self.action=='kick':
                                thread = threading.Thread(target = self.capture_vid)
                                thread.start()
                    else:
                        self.color = (0,255,0)
                        self.action = 'normal'
                        
                    
                    


            return frame
  ##############################################################################################################################################  
    def capture_vid(self):
            temp_filename = 'temp_video.avi'
                
            # Get the height and width of the frames
            height, width, channels = self.vid_frame[0].shape
            
            # Define the codec and create a VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_out = cv2.VideoWriter(temp_filename, fourcc, 5.0, (width, height))
            
           
            for fr in self.vid_frame[-15:]:
                video_out.write(fr)
            
            # Release the VideoWriter object
            video_out.release()

            filename = f'violence_videos/{int(time.time())}.avi'

            storage.child(filename).put(temp_filename)
            os.remove(temp_filename)
                    
##########################################################################################################################################
    def loop_through_people(self, frame, keypoints_with_scores, edges, confidence_threshold):
        for person in keypoints_with_scores:
            self.draw_connections(frame, person, edges, confidence_threshold)
            self.draw_keypoints(frame, person, confidence_threshold)

##########################################################################################################################################
    def draw_keypoints(self, frame, keypoints, confidence_threshold):
        y, x, _ = frame.shape
        shaped = np.squeeze(np.multiply(keypoints, [y, x, 1]))

        for kp in shaped:
            ky, kx, kp_conf = kp
            if kp_conf > confidence_threshold:
                cv2.circle(frame, (int(kx), int(ky)), 6, (0, 255, 0), -1)

#######################################################################################################################################
    def draw_connections(self, frame, keypoints, edges, confidence_threshold):
        y, x, _ = frame.shape
        shaped = np.squeeze(np.multiply(keypoints, [y, x, 1]))

        for edge, color in edges.items():
            p1, p2 = edge
            y1, x1, c1 = shaped[p1]
            y2, x2, c2 = shaped[p2]

            if (c1 > confidence_threshold) & (c2 > confidence_threshold):
                cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (100, 34, 255), 4)

    def stop(self):
        if self.camera:
            self.capture.release()
            cv2.destroyAllWindows()
            self.root.get_screen('main').ids.camera_feed.source = 'project_app/upload.png'  
        

############################################# Open saved violence folder and show in kivymd app  ###########################################
    def history_view(self):
        self.fire_base.fire()
        
        history_screen = self.root.get_screen('history')
        files = os.listdir(r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\Kivy_app\project_app\videos')
        if self.cls:
            for i in files:
                item = OneLineAvatarIconListItem(text=f"{i}")
                image = IconLeftWidget(icon="play-circle-outline")
                image.bind(on_release=lambda widget, text=item.text: self.on_item_click(text))
                image1 = IconRightWidget(icon="delete")
                image1.bind(on_release=lambda widget, text=item.text: self.del_item(text))

                item.add_widget(image)
                item.add_widget(image1)
                history_screen.ids.history_list.add_widget(item)

            history_screen.ids.history_list.canvas.ask_update()
                
            self.cls = False

 ############################################### Dark and Light Mode Changer ################################################################################               
    def on_item_click(self, text):
        add = f"E:/Bilal/PYTHON/ML/Unsupervised/Deep_Learning/Object_detection_API/Human_pose_tensorflow/Kivy_app/project_app/videos/{text}"
        self.root.get_screen('video_screen').ids.video_player.source = add
        self.screen.current = 'video_screen'
    
    def del_item(self, text):
        delete = f"E:/Bilal/PYTHON/ML/Unsupervised/Deep_Learning/Object_detection_API/Human_pose_tensorflow/Kivy_app/project_app/videos/{text}"
        os.remove(delete)

        history_screen = self.root.get_screen('history')
        history_list = history_screen.ids.history_list
        for item in history_list.children:
            if isinstance(item, OneLineAvatarIconListItem) and item.text == text:
                history_list.remove_widget(item)
                break
    
        history_list.canvas.ask_update()

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Blue" if self.theme_cls.primary_palette == "Orange" else "Orange"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
########################################## MIC OPENER #######################################################################################
    def mic_open(self):
        text = self.root.get_screen('main').ids.mic.text
        if text == 'Mic off':
            
            self.root.get_screen('main').ids.mic.text = 'Mic on'
            self.root.get_screen('main').ids.mic.icon = 'microphone-variant'
            self.mic_0_1 = 1
            
            if not self.mic_running:
                self.mic_running = True
                self.mic_thread = threading.Thread(target=self.recognize_from_microphone)
                self.mic_thread.start()



        else:
            self.root.get_screen('main').ids.mic.text = 'Mic off'
            self.root.get_screen('main').ids.mic.icon = 'microphone-variant-off'
            self.mic_0_1 = 0
            self.mic_running = False
            if self.mic_thread is not None:
                self.mic_thread.join()  # Wait for the thread to finish
                self.mic_thread = None
    
    def recognize_from_microphone(self):
        while self.mic_running:
            try:
                # Replace with your actual microphone recognition logic
                self.v.recognize_from_microphone()
            except Exception as e:
                print(f"Error during microphone recognition: {e}")
            time.sleep(1) 
            

           
         
    def toggle_fullscreen(self):  
        if Window.fullscreen == 'auto':  
            Window.fullscreen = False  
            Window.size = (800, 600)
        else:  
            Window.fullscreen = 'auto' 
########################################## Main builder for load screens layout #################################################################        
    def build(self):
        
        self.screen = Builder.load_string(helper1)
################################################ Screen Managers #######################################################################################
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name ='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(MainScreeen(name='main'))
        sm.add_widget(ForgotScreen(name='forgotpass'))
        sm.add_widget(HistoryScreen(name='history'))
        sm.add_widget(Video_screen(name='video_screen'))
        sm.add_widget(About_us(name='about_us'))
        sm.add_widget(Start_page_UI(name = 'start_page'))
        self.screen.current = 'start_page'
        self.cls = True
        return self.screen
###########################################################  END OF CODE  ######################################################   
    
    
apps().run()