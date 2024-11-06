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
    Start_page_UI:
    Loading:
    
<LoginScreen>:
    name: 'login'
    
    BoxLayout:
        size_hint: [.9, .9]
        pos_hint: { 'top' : .95, 'right': .95}

        # Add padding and spacing
        orientation: 'vertical'
        padding: 10
        spacing: 20

        canvas:
            Color:
                rgb: [1, 1, 1]
            Rectangle:
                pos: self.pos
                size: self.size
        
        BoxLayout:
            orientation:'vertical'

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
                width: 400
                error_color : (0,255,0) 
                on_text: app.login_diplay()
        
        MDFloatLayout:
            pos_hint: {'center_y': 0.5, 'center_x':0.5}
            spacing:20
              
            MDTextField:
                
                id: password
                hint_text: 'Password'
                text: root.text
                password: True
                icon_left: "key-variant"
                mode: "rectangle"
                width: 400 
                size_hint:None,None
                pos_hint: {'center_y': 0.57, 'center_x':0.5}
                height:self.minimum_height
                multiline:False
                padding:18


                

            MDIconButton:
                
                icon: "eye-off"
                pos_hint: {'center_y': 0.56, 'center_x':0.66}
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    password.password = False if password.password is True else True

       
        
        MDFloatLayout:
            pos_hint: {'center_y': 0.7, 'center_x':0.5}
            spacing:20

            MDRectangleFlatIconButton:
                text: "Forgot Password?"
                line_color: 0, 0, 0, 0
                pos_hint: {'center_y': 0.99, 'center_x':0.7}
                multiline:False
                padding:18
                on_release: root.manager.current = 'forgotpass'
            
            MDRaisedButton:
                text: "Submit"
                size_hint: 0.2, None
                width: dp(200)
                pos_hint: {'center_y': 0.8, 'center_x':0.5}
                multiline:False
                padding:18
                on_release: 
                    app.login_user()

                    
            MDRectangleFlatIconButton:
                text: "Don't have an account? -> Sign up"
                font_size: '10sp'
                font_style: "H6" 
                line_color: (0, 0, 0, 0)
                pos_hint: {'center_y': 0.4 , 'center_x':0.5}
                multiline:False
                padding:18
                on_release:
                    root.manager.transition.direction  = 'left'
                    root.manager.current = 'signup'


            MDRectangleFlatIconButton:
                text: "About us"
                
                line_color: (0, 0, 0, 0)
                pos_hint: {'center_y': 0.2, 'center_x':0.5}
                multiline:False
                padding:18
                on_release: root.manager.current = 'about_us'        



<SignupScreen>:
    name: 'signup'
    BoxLayout:
        size_hint: [.9, .9]
        pos_hint: { 'top' : .95, 'right': .95}

        # Add padding and spacing
        orientation: 'vertical'
        padding: 10
        spacing: 20

        canvas:
            Color:
                rgb: [1, 1, 1]
            Rectangle:
                pos: self.pos
                size: self.size
        
        
        
        MDFloatLayout:
            pos_hint: {'center_y': 0.99, 'center_x':0.5}

            MDIconButton:
                halign: "center"
                icon: "keyboard-backspace"
                pos_hint: {'center_x': 0.1, 'center_y':0.9}
                on_release: root.manager.current = 'login'

            MDLabel:
                halign: "center"
                text: "Personal Information"
                bold: True
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y':0.8}

        BoxLayout:
            orientation:'vertical'
            spacing:dp(20)
            padding:dp(10)

            FitImage:
                id: fit_image2  
                source: ''
                size_hint: None, None
                size: dp(150), dp(150)
                pos_hint: {'center_x': 0.5, 'center_y':0.7}
                radius: [dp(75), dp(75), dp(75), dp(75)]

            MDRectangleFlatButton:
                text: "Upload Image"
                size_hint: None, None
                size: dp(150), dp(50)
                pos_hint: {'center_x': 0.5, 'center_y':0.6}
                on_release: app.open_file_manager()
                
            MDTextField:
                id: name
                hint_text: 'Name'
                mode: "rectangle"
                pos_hint: {'center_x': 0.5, 'center_y':0.5}
                height:self.minimum_height
                multiline:False
                padding:18
                size_hint_x: None
                width: 400

            MDTextField:
                id: email
                hint_text: 'Email'
                mode: "rectangle"
                pos_hint: {'center_x': 0.5,'center_y':0.4}
                height:self.minimum_height
                multiline:False
                padding:18
                size_hint_x: None
                width: 400
                helper_text: "user@gmail.com"
                validator: "email"
                on_text: app.error()

        MDFloatLayout:
            pos_hint: {'center_y': 0.8, 'center_x':0.5}
        
            
            MDTextField:
                
                id: password
                hint_text: 'Password'
                text: root.text
                password: True
                icon_left: "key-variant"
                mode: "rectangle"
                width: 400 
                size_hint:None,None
                pos_hint: {'center_y': 0.8, 'center_x':0.5}
                height:self.minimum_height
                multiline:False
                padding:18


                
            MDIconButton:
                
                icon: "eye-off"
                pos_hint: {'center_y': 0.8, 'center_x':0.66}
                theme_text_color: "Hint"
                on_release:
                    self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                    password.password = False if password.password is True else True


        
        MDRaisedButton:
            id: sig
            text: "Update"
            size_hint: 0.4, None
            height: dp(50)
            pos_hint: {'center_x': 0.5}
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
                            pos_hint_x:None
                            width: 500
                            radius:[ dp(10),  dp(10), dp(75), dp(75)]
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
    BoxLayout:
        size_hint: [.9, .9]
        pos_hint: { 'top' : .95, 'right': .95}

        # Add padding and spacing
        orientation: 'vertical'
        padding: 10
        spacing: 20

        canvas:
            Color:
                rgb: [1, 1, 1]
            Rectangle:
                pos: self.pos
                size: self.size
            

        MDFloatLayout:
            pos_hint: {'center_y': 0.99, 'center_x':0.5}
            

            MDIconButton:
                icon: "keyboard-backspace"
                pos_hint: {'center_y': 0.8,'center_x': 0.1}
                on_release: root.manager.current = 'login'

            MDLabel:
                halign: "center"
                text: "Forgot Password"
                bold: True
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y':0.8}
        
        Image:
            id:detect_screen
            pos_hint: {'center_x': 0.5}
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


<Start_page_UI>:
    name: 'start_page'

<Loading>:
    name: 'load'
    MDBoxLayout:
        orientation: 'vertical'
        pos_hint:{"center_x":.5, "center_y":.5}
        padding: "100dp"
        
        MDLabel:
            text:"Wait a minute, Model is Loading"
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