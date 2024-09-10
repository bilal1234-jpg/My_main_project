from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager
from  client_sql_app import client_db , session
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import smtplib
import os
from kivy.clock import Clock
import threading
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.list import  IconLeftWidget, IconRightWidget
from kivy.properties import BooleanProperty
from kv import helper1
from kivy.animation import Animation
from  kivymd.uix.floatlayout import FloatLayout
from  kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.button import MDIconButton
import pyrebase
from download_vid import fire_base_download
from kivy.graphics.texture import Texture
import cv2





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


class LoginScreen(Screen):
    text = StringProperty()
class SignupScreen(Screen):
    text = StringProperty()  
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
        self.fire_base = fire_base_download()
        self.refresh = False
       
####################################################### Picture change in main and sign pages #######################################################################
    def select_path(self, path):
       
        try:
            
            curr_scr = self.screen.current
            
            if curr_scr == 'signup':
                self.root.get_screen('signup').ids.fit_image2.source = path
                self.exit_manager(path)
                self.selected_path = path
                
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
                new_user = client_db(name=name, email=email, password = password, img_address = self.selected_path)
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
                user = session.query(client_db).filter(client_db.name == from_username_feild).first()
                password = session.query(client_db).filter(client_db.password == from_password_feild).first()
                if user:
                    if password:
                        self.root.get_screen('history').ids.email.title = user.name
                        self.root.get_screen('history').ids.draw_name.text = user.name
                        self.root.get_screen('history').ids.email_drawer = user.email
                        self.root.get_screen('history').ids.fit_image3.source =user.img_address
                        self.root.current = 'history'
                        self.root.get_screen('login').ids.username.text = ''
                        self.root.get_screen('login').ids.password.text =  ''
                        self.refresh = True
                        self.on_start()
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
                user = session.query(client_db).filter(client_db.email == from_username_feild).first()
                password = session.query(client_db).filter(client_db.password == from_password_feild).first()
            
                if user:
                    if password:
                        self.root.get_screen('history').ids.email.text = user.name
                        self.root.get_screen('history').ids.draw_name.text = user.name
                        self.root.get_screen('history').ids.email_drawer = user.email
                        self.root.get_screen('history').ids.fit_image3.source =user.img_address
                        self.root.current = 'history'
                        self.root.get_screen('login').ids.username.text = ''
                        self.root.get_screen('login').ids.password.text = ''
                        self.refresh = True
                        self.on_start()
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

    def logout(self):
        self.screen.current = 'login'
        self.refresh = False
        Clock.unschedule(self.refresh_event)

 
################################################## Forgot Password SMTP #################################################################
    def forgot_password(self):
        email_feild = self.root.get_screen('forgotpass').ids.email.text
        database_check = session.query(client_db).filter(client_db.email == email_feild).first()
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
                    
        

#############################################  Open saved violence folder and show in kivymd app  ###########################################
    def on_start(self):
        # Schedule refresh_history_view to be called every 5 seconds
        if self.refresh:
            self.refresh_event = Clock.schedule_interval(self.history_view, 5)

    def history_view(self, *args):
       
        
        history_screen = self.root.get_screen('history')
        try:
            files = os.listdir('videos')
            
        except:
            os.makedirs('videos')
            files = os.listdir('videos')
           
        thread = threading.Thread(target = self.fire_base.fire)
        thread.start()

        history_screen.ids.history_list.clear_widgets()
        for i in files:
            item = OneLineAvatarIconListItem(text=f"{i}")
            image = IconLeftWidget(icon="play-circle-outline")
            image.bind(on_release=lambda widget, text=item.text: self.on_item_click(text))
            image1 = IconRightWidget(icon="delete")
            image1.bind(on_release=lambda widget, text=item.text: self.del_item(text))

            item.add_widget(image)
            item.add_widget(image1)
            history_screen.ids.history_list.add_widget(item)

                
            

 ############################################### Dark and Light Mode Changer ################################################################################               
    def on_item_click(self, text):
        add = f"videos/{text}"
        self.root.get_screen('video_screen').ids.video_player.source = add
        self.screen.current = 'video_screen'
    
    def del_item(self, text):
        delete = f"videos/{text}"
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




########################################## Main builder for load screens layout #################################################################        
    def build(self):
        
        self.screen = Builder.load_string(helper1)
################################################ Screen Managers #######################################################################################
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name ='login'))
        sm.add_widget(SignupScreen(name='signup'))
        
        sm.add_widget(ForgotScreen(name='forgotpass'))
        sm.add_widget(HistoryScreen(name='history'))
        sm.add_widget(Video_screen(name='video_screen'))
        sm.add_widget(About_us(name='about_us'))
        sm.add_widget(Start_page_UI(name = 'start_page'))
        self.screen.current = 'start_page'
        
        return self.screen
###########################################################  END OF CODE  ######################################################   
    
    
apps().run()