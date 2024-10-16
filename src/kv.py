helper1 = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

ScreenManager:
    LoginScreen:
    SignupScreen:
    MainScreeen:
    ForgotScreen:
    HistoryScreen:
    Video_screen:
    About_us:
    Start_page_UI:
    Loading:
    
<LoginScreen>:
    name: 'login'
    
    MDFloatLayout:
   

        FitImage:
            id: fit_image1
            source: ''
            size_hint: None, None
            size: 100, 100  
            pos_hint: {'center_y': 0.9, 'center_x': 0.2}
            radius: [150, 150, 150, 150]

        MDLabel:
            text: "LOGIN"
            bold: True
            font_size: '24sp'
            pos_hint: {'center_y': 0.9, 'center_x': 0.8}


            
        
        MDTextField:
            id: username
            hint_text: 'Username, Email, & Phone number'
            mode: "rectangle"
            pos_hint: {'center_x': 0.5,'center_y': 0.7}
            size_hint_x: None
            helper_text: " "
            validator: "email"
            width: 300
            error_color : (0,255,0) 
            on_text: app.login_diplay()
           
            
        MDTextField:
            
            id: password
            hint_text: 'Password'
            text: root.text
            password: True
            icon_left: "key-variant"
            mode: "rectangle"
            size_hint_x: None
            width: 300  
            pos_hint: {'center_y': 0.57,'center_x': 0.5}

        MDIconButton:
            
            icon: "eye-off"
            pos_hint: {'center_y': 0.57, 'center_x': 0.72}  # Center vertically relative to MDTextField
            theme_text_color: "Hint"
            on_release:
                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                password.password = False if password.password is True else True

        MDRectangleFlatIconButton:
            text: "Forgot Password?"
            line_color: 0, 0, 0, 0
            pos_hint: {"center_x": 0.7,'center_y': 0.45}
            on_release: root.manager.current = 'forgotpass'
        
        MDRaisedButton:
            text: "Submit"
            size_hint: 0.2, None
            width: dp(100)
            pos_hint: {"center_x": 0.5,'center_y': 0.37}
            on_release: app.login_user()
            
        
      
        MDLabel:
            text: "Don't have an account?"
            
            font_style: "H5" 
            font_size: '16sp'
            pos_hint: {'center_x': 0.7,'center_y': 0.27}
            
            size_hint_x: 0.7

            

        MDRectangleFlatIconButton:
            text: "Sign up"
            
            line_color: (0, 0, 0, 0)
            pos_hint: {'center_x': 0.6,'center_y': 0.27}
            on_release:
                root.manager.transition.direction  = 'left'
                root.manager.current = 'signup'

        MDRectangleFlatIconButton:
            text: "About us"
            
            line_color: (0, 0, 0, 0)
            pos_hint: {'center_y': 0.17, 'center_x': 0.5}
            on_release: root.manager.current = 'about_us'        



<SignupScreen>:
    name: 'signup'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(5)
        spacing: dp(15)
        halign:'center'
        pos_hint: {'center_y': 0.55}
        adaptive_height: True
        adaptive_width: True
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            pos_hint: {'center_x': 0.5}

            MDIconButton:
                halign: "center"
                icon: "keyboard-backspace"
                pos_hint: {'center_y': 0.4}
                on_release: root.manager.current = 'login'

            MDLabel:
                halign: "center"
                text: "Personal Information"
                bold: True
                font_size: '24sp'
                pos_hint: {'center_y': 0.4}
        FitImage:
            id: fit_image2  
            source: ''
            size_hint: None, None
            size: 150, 150  
            pos_hint: {'center_x': 0.52}
            radius: [150, 150, 150, 150]

        MDRectangleFlatButton:
            text: "Upload Image"
            size_hint: None, None
            size: 150, 50
            pos_hint: {'center_x': 0.52}
            on_release: app.open_file_manager()
            
        MDTextField:
            id: name
            hint_text: 'Name'
            mode: "rectangle"
            pos_hint: {'center_x': 0.52}
            size_hint_x: None
            width: 300
        MDTextField:
            id: email
            hint_text: 'Email'
            mode: "rectangle"
            pos_hint: {'center_x': 0.52}
            size_hint_x: None
            width: 300
            helper_text: "user@gmail.com"
            validator: "email"
            on_text: app.error()
        BoxLayout:
            orientation: 'horizontal'
            pos_hint: {'center_x': 0.52}
            size_hint_x: None
            width: 300
            adaptive_height: True
            
               
            MDTextField:
                id: password
                hint_text: 'Password'
                text: root.text
                password: True
                icon_left: "key-variant"
                mode: "rectangle"
                size_hint_x: None
                width: 300  
                pos_hint: {'center_y': 0.56}

            MDIconButton:
                halign: "center"
                icon: "eye-off"
                pos_hint: {'center_y': 0.55} 
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    password.password = False if password.password is True else True


        
        MDRaisedButton:
            id:sig
            text: "Update"
            size_hint: None, None
            size: 150, 50
            pos_hint: {'center_x': 0.52}
            on_release: 
                app.add_user()
                
                

            

<MainScreeen>:
    name: 'main'
                        
    MDScreen:

        MDNavigationLayout:

            MDScreenManager:

                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: dp(10)
                        padding: dp(5)
                        halign :'center'
                        size_hint:1,1

                        MDTopAppBar:
                            id: email
                            title: " "
                            use_overflow: True
                            elevation: 4
                            pos_hint: {"top": 1}
                            specific_text_color: "#4a4939"
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            right_action_items:[['camera-flip',lambda x:app.camera_flip(),'Front']]
                                                     
                        FloatLayout:
                            
                            
                            Image:
                                id: camera_feed
                                source: '' 
                                size_hint_x: 2
                               
                                pos_hint: {'center_y': 0.5, 'center_x':0.5} 
                                allow_stretch: True 
                                

                            # MDIconButton:  
                            #     icon: 'fullscreen'
                            #     size_hint_y: None  
                            #     pos_hint: {'center_y': 0.02, 'center_x':0.7} 
                            #     on_release: app.toggle_fullscreen()  

                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)
                            padding:dp(20)
                            size_hint_y: None
                            pos_hint: {'center_x': 0.5} 
                            height: dp(50)

                            MDRectangleFlatButton:
                                text: 'Start Detection'
                                halign:'center'
                                size_hint: 0.1,None
                                pos_hint: {'center_y': 0.001} 
                                on_release: app.main_page()

                            MDRectangleFlatButton:
                                text: 'Stop Detection'
                                halign:'center'
                                size_hint: 0.1,None
                                pos_hint: {'center_y': 0.001} 
                                on_release: app.stop()
                        
                        BoxLayout:
                            orientation: 'horizontal'
                            padding:dp(20)
                            size_hint_y: None
                            
                            

                            MDBottomNavigation:
                                panel_color: "lightgrey"
                                selected_color_background: 0, 0, 1, .4
                                text_color_active: 0, 0, 0, 1
                                text_color_normal: 0, 0, 0.5, 1
                                shadow_radius: 6
                                pos_hint: {'center_y': 0.1}

                                MDBottomNavigationItem:
                                    id:upload_btn_vid
                                    text: 'Upload'
                                    icon: 'image'
                                    on_tab_release:
                                        
                                        app.open_file_manager()

                                MDBottomNavigationItem:
                                    id:mic
                                    text: 'Mic off'
                                    icon: 'microphone-variant-off'
                                    on_tab_release:app.mic_open()
                                    

                                MDBottomNavigationItem:
                                    
                                    text: 'History'
                                    icon: 'history'
                                    on_tab_release : 
                                        root.manager.current = 'history'
                                        app.history_view()
                                

                             


            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)

                BoxLayout:
                    orientation: 'vertical'

                    MDNavigationDrawerMenu:

                        FitImage:
                            id: fit_image3
                            source: ''
                            size_hint: None, None
                            size: dp(150), dp(150)  
                            radius: [150, 150, 150, 150]
                            halign: 'right'
                    

                        MDNavigationDrawerHeader:
                            id: draw_name
                            title: "Welcome"
                            title_color: "#4a4939"
                            text: "Header text"
                            spacing: "4dp"
                            padding: "12dp", 0, 0, "56dp"

                        MDNavigationDrawerLabel:
                            id:email_drawer
                            bold: True
                            font_size : '24sp'
                            text: " "

                        DrawerClickableItem:
                            icon: "face-man-profile"
                            text_right_color: "#4a4939"
                            text: "Profile"

                        DrawerClickableItem:
                            icon: "account-details"
                            text: "Detail"

                        DrawerClickableItem:
                            icon: "logout"
                            text: "Logout"
                            on_release: app.logout()


                        MDNavigationDrawerDivider:

                    

                        DrawerClickableItem:
                            
                            text: 'Dark or Light'
                            icon: 'theme-light-dark'
                            on_release:app.switch_theme_style()    

                    
            
            
                
                

<ForgotScreen>:
    name: 'forgotpass'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(100)
        spacing: dp(50)
        pos_hint: {'center_y': 0.6}
        

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(2)
            padding: dp(10)
            pos_hint: {'center_x': 0.5}
            

            MDIconButton:
                icon: "keyboard-backspace"
                pos_hint: {'center_y': 0.5}
                on_release: root.manager.current = 'login'

            Image:
                id:detect_screen
                pos_hint: {'center_y': 0.5}
                source: ''
                size_hint: 1.9, 1.9
                radius: [5000, 5000, 5000, 5000]
                

        MDLabel:
            id: Forgot
            text: "Forgot Password"
            halign: "center"
            bold: True
            font_size: '24sp'
            size_hint_y: None
            height: self.texture_size[1] + dp(20)
            pos_hint: {'center_x': 0.5}

        MDTextField:
            id: email
            hint_text: 'Enter your email'
            mode: "rectangle"
            size_hint_x: None
            width: dp(300)
            pos_hint: {'center_x': 0.5}
            allow_stretch: True

        MDRectangleFlatButton:
            text: "Send Password"
            size_hint: None, None
            size: dp(150), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.forgot_password()

           
<HistoryScreen>:
    name: 'history'
    BoxLayout:
        orientation: 'vertical'

        MDIconButton:
            icon: "keyboard-backspace"
            pos_hint: {'center_x': 0.1}
            on_release: root.manager.current = 'main'

        ScrollView:
            MDList:
                id: history_list

<Video_screen>:
    name: 'video_screen'
    BoxLayout:
        orientation: 'vertical'
        
        MDIconButton:
            icon: "keyboard-backspace"
            pos_hint: {'center_x': 0.1}
            on_release: root.manager.current = 'history'

        VideoPlayer:
            id: video_player
            source:''
            state: 'play'
            options:{'eos':'loop'}
            allow_stretch: True 
<About_us>:
    name: 'about_us'
    MDFloatLayout:
 
        MDLabel:
            text: "About Us"
            bold: True
            font_size: '24sp'
            pos_hint: {'center_x': 0.5, 'center_y':0.9}
            halign:'center'

        MDLabel:
            text: "At ChildGuard, we are dedicated to fostering safer environments for children and caregivers through innovative technology. Our mission is to create a world where every child feels secure and valued, and where caregivers are equipped with the resources they need to support and nurture their charges effectively. Recognizing the alarming prevalence of violence and abuse in caregiver-child interactions, we developed our flagship app, ChildGuard. This user-friendly platform serves as a vital tool in identifying and addressing instances of violence and emotional distress, ensuring that children can grow up in healthy, supportive environments. ChildGuard leverages advanced algorithms and machine learning techniques to detect patterns of behavior that may indicate potential violence or abuse. By analyzing everything from communication styles to emotional cues, ChildGuard provides caregivers, educators, and child welfare professionals with actionable insights. Our goal is to prevent violence before it happens, advocate for at-risk children, and promote positive caregiver-child relationships. At ChildGuard, we believe that knowledge is power. Our educational resources empower caregivers with information about healthy interactions and effective communication strategies. We are committed to building a community of support, where caregivers can share their experiences, learn from one another, and access the tools they need to thrive. Join us in our mission to protect and empower children and caregivers alike. Together, we can make a meaningful difference in the lives of countless families. Thank you for being a part of our journey toward a safer future for everyone."
            font_size: '18sp'
            halign:'center'

<Start_page_UI>:
    name: 'start_page'

<Loading>:
    name: 'load'
    MDBoxLayout:
        orientation: 'vertical'
        pos_hint:{"center_x":.5, "center_y":.5}
        padding: "100dp"
        
        MDLabel:
            text:"Wait a minute"
            text_color:255,255,255,0
            font_size:"20sp"
            pos_hint:{"center_x":.51}
            halign:"center"

        MDProgressBar:
            id:pd
            orientation: "horizontal"
            value:0
            min:0
            max:100
            pos_hint:{"center_x":.51}
            size_hint_x:0.5
            size_hint_y:0.1
            color: app.theme_cls.accent_color
    
        
            
'''