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
    Loading:
    Start_page_UI:
    LoginScreen:
    SignupScreen:
    MainScreeen:
    ForgotScreen:
    HistoryScreen:
    Video_screen:
    

<Loading>:
    name: 'load'
    FloatLayout:

        Image:
            id: gif
            source: 'assets/images/vid4.gif' 
            size: 10, 10
            allow_stretch: True
            anim_delay: 0.1
            anim_loop: 1000
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        MDLabel:
            text:"Wait a minute, Model is Loading..."
            text_color:255,255,255,0
            font_size:"20sp"
            pos_hint:{"center_x":.51,'center_y':0.2}
            color:"white"
            bold:True
            halign:"center"

        MDProgressBar:
            id:pd
            orientation: "horizontal"
            value:0
            min:0
            max:100
            pos_hint:{"center_x":.51,'center_y':0.1}
            size_hint_x:0.5
            size_hint_y:0.1
            color: app.theme_cls.accent_color


<Start_page_UI>:
    name: 'start_page'
    BoxLayout:
        orientation:"horizontal"

        BoxLayout:
            orientation:"vertical"

            FloatLayout:
                FitImage:
                    id: fit_image45
                    source: 'assets/images/bg4.png'
                    size_hint: None, None
                    size: 300, 300  
                    pos_hint: {'center_y': 0.6,'center_x': 0.5}
                    radius: [350, 350, 350, 350]
                MDLabel:
                    id:M1
                    text:""
                    pos_hint: {'center_y': 0.25,'center_x': 0.91}
                    font_size: '60sp'
                    bold:True
                    color:"white"


<LoginScreen>:
    name: 'login'

    BoxLayout:
        orientation:"horizontal"

        BoxLayout:
            orientation:"vertical"
            
            BoxLayout:
                orientation:"vertical"
                padding:dp(20)

                MDLabel:
                    id:MD
                    text: ""
                    font_style: "H3"
                    color:"white"
                    bold: True
                    markup: True
                    size_hint_y: 3
                    pos_hint: {"center_x": 0.55, "center_y": 0.1}
                    height: self.texture_size[1]

        MDCard:
            size_hint: None, 1
            size: 400, 700
            pos_hint: {"center_x": 0.77, "center_y": 0.5}
            elevation: 10
            padding: 20
            spacing: 40
            width:700
            orientation: "vertical"

            BoxLayout:
                orientation: "vertical"
                padding: 20, 20, 20, 50
                spacing: 40
            

                FitImage:
                    id: fit_image1
                    source: 'assets/images/bg4.png'
                    size_hint: None, None
                    size: 150, 150  
                    pos_hint: {'center_x': 0.5}
                    radius: [150, 150, 150, 150]

                MDLabel:
                    text: "LOGIN"
                    bold: True
                    font_size: '35sp'
                    pos_hint: { 'center_x': 0.92}
                    height: self.texture_size[1]

                MDLabel:
                    text: "Welcome back! Please login to your account."
                    size_hint_y: None
                    pos_hint: { 'center_x': 0.75}
                    height: self.texture_size[1]
                
                
                
                MDTextField:
                    id: username
                    hint_text: 'Username, Email'
                    mode: "rectangle"
                    pos_hint: {'center_x': 0.5,'center_y': 0.7}
                    size_hint_x: None
                    helper_text: " "
                    validator: "email"
                    width: 400
                    write_tab: False
                    multiline: False
                    error_color : (0,255,0) 
                    md_bg_color: 0.8, 0.8, 0.8, 1
                    on_text: app.login_diplay()
            
                MDFloatLayout:
                    pos_hint: {'center_y': 0.5, 'center_x':0.5}
                    spacing:20
                        
                    MDTextField:
                        id: password
                        hint_text: 'Password'
                        password: True
                        icon_left: "key-variant"
                        mode: "rectangle"
                        width: 400 
                        write_tab: False
                        multiline: False
                        size_hint:None,None
                        pos_hint: {'center_y': 0.57, 'center_x':0.5}
                        height:self.minimum_height
                        multiline:False
                        md_bg_color: 0.8, 0.8, 0.8, 1
                        padding:18

                    MDIconButton:
                        
                        icon: "eye-off"
                        pos_hint: {'center_y': 0.56, 'center_x':0.75}
                        theme_text_color: "Hint"
                        on_release:
                            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                            password.password = False if password.password is True else True


                MDRectangleFlatIconButton:
                    text: "Forgot Password?"
                    line_color: 0, 0, 0, 0
                    pos_hint: {'center_y': 0.99, 'center_x':0.75}
                    multiline:False
                    padding:18
                    text_color: 0.2705882352941176, 0.1882352941176471, 0.7411764705882353, 1
                    on_release: root.manager.current = 'forgotpass'
                
                MDRaisedButton:
                    text: "Submit"
                    size_hint: 0.4, None
                    width: dp(200)
                    pos_hint: {'center_y': 0.8, 'center_x':0.5}
                    multiline:False
                    padding:18
                    md_bg_color: 0.2705882352941176, 0.1882352941176471, 0.7411764705882353, 1
                    on_release: 
                        app.login_user()

                BoxLayout:
                    orientation:"horizontal"
                    padding:dp(165)

                    MDLabel:
                        text: "Don't have an account?"
                        size_hint_y: None
                        pos_hint: {'center_y':0.5}

                    MDRectangleFlatIconButton:
                        text: "Sign up"
                        font_size: '10sp'
                        font_style: "H6" 
                        line_color: (0, 0, 0, 0)
                        pos_hint: {'center_y':0.5}
                        multiline:False
                        padding:18
                        text_color: 0.2705882352941176, 0.1882352941176471, 0.7411764705882353, 1
                        on_release:
                            root.manager.transition.direction  = 'left'
                            root.manager.current = 'signup'          


<SignupScreen>:
    name: 'signup'
    BoxLayout:
        orientation:"horizontal"

        BoxLayout:
            orientation:"vertical"
    
                    

            MDLabel:
                id:MD1
                text: ""
                font_style: "H3"
                color:"white"
                bold: True
                markup: True
                size_hint_y: 3
                pos_hint: {"center_x": 0.95, "center_y": 0.1}
                height: self.texture_size[1]

    MDCard:
        size_hint: None, 1
        size: 400, 700
        pos_hint: {"center_x": 0.19, "center_y": 0.5}
        elevation: 10
        padding: 20
        spacing: 40
        width:600
        orientation: "vertical"
        
        
        

        MDIconButton:
            halign: "center"
            icon: "keyboard-backspace"
            pos_hint: {'center_x': 0.1, 'center_y':0.9}
            bold:True
            on_release: root.manager.current = 'login'

        MDLabel:
            halign: "center"
            text: "Signup page"
            bold: True
            font_size: '24sp'
            pos_hint: {'center_x': 0.5, 'center_y':0.8}



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
            md_bg_color: 0.2705882352941176, 0.1882352941176471, 0.7411764705882353, 1
            text_color:"white"

        MDTextField:
            id: name
            hint_text: 'Name'
            mode: "rectangle"
            pos_hint: {'center_x': 0.5, 'center_y':0.5}
            height:self.minimum_height
            write_tab: False
            multiline: False
            padding:18
            size_hint_x: None
            width: 400

        MDTextField:
            id: email
            hint_text: 'Email'
            mode: "rectangle"
            pos_hint: {'center_x': 0.5,'center_y':0.4}
            height:self.minimum_height
            write_tab: False
            multiline: False
            padding:18
            size_hint_x: None
            width: 400
            helper_text: "user@gmail.com"
            validator: "email"
            on_text: app.error()



        MDFloatLayout:
            pos_hint: {'center_y': 0.5, 'center_x':0.5}
            spacing:20
            MDTextField:

                id: password
                hint_text: 'Password'

                password: True
                icon_left: "key-variant"
                mode: "rectangle"
                width: 400 
                size_hint:None,None
                pos_hint: {'center_y': 0.8, 'center_x':0.5}
                height:self.minimum_height
                write_tab: False
                multiline: False
                padding:18



            MDIconButton:

                icon: "eye-off"
                size_hint_y:2
                pos_hint: {'center_y': 0.75, 'center_x':0.79}
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
            md_bg_color: 0.2705882352941176, 0.1882352941176471, 0.7411764705882353, 1
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
                                source: 'assets/images/bg3.jpg' 
                                size_hint_x: 2
                               
                                pos_hint: {'center_y': 0.5, 'center_x':0.5} 
                                allow_stretch: True  

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
                                md_bg_color:0,0.5490196078431373,1,1
                                text_color:'white'
                                font_size:sp(20)
                                on_release: app.main_page()

                            MDRectangleFlatButton:
                                text: 'Stop Detection'
                                halign:'center'
                                size_hint: 0.1,None
                                pos_hint: {'center_y': 0.001} 
                                md_bg_color:0,0.5490196078431373,1,1
                                text_color:'white'
                                font_size:sp(20)
                                on_release: app.stop()
                        
                        BoxLayout:
                            orientation: 'horizontal'
                            padding:dp(20)
                            size_hint_y: None
                            
                            

                            MDBottomNavigation:
                                panel_color: 0,0.5490196078431373,1,1
                                selected_color_background: 0, 0, 1, .4
                                text_color_active: 0, 0, 0, 1
                                text_color_normal: 1, 1, 1.5,1
                                shadow_radius: 6
                                radius:10
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
        orientation:"horizontal"

        BoxLayout:
            orientation:"vertical"

            MDIconButton:
                icon: "keyboard-backspace"
                size_hint_y: 0.2
                pos_hint: {'center_y': 0.9,'center_x': 0.03}
                on_release: root.manager.current = 'login'
                theme_text_color: "Custom"  
                text_color: 1, 1, 1, 1
                bold:True

            MDLabel:
                text: ""
                font_style: "H1"
                color:"white"
                bold: True
                markup: True
                size_hint_y: 1
                pos_hint: {"center_x": 0.9, "center_y": 0.1}
                height: self.texture_size[1]
        
            
    
        MDCard:
            size_hint: None, 1
            size: 400, 700
            pos_hint: {"center_x": 0.77, "center_y": 0.5}
            elevation: 10
            padding: 20
            spacing: 40
            width:600
            orientation: "vertical"

            BoxLayout:
                orientation: "vertical"
                padding: 10, 0, 0, 200
                spacing: 40

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
        canvas:
            Color:
                rgba: 0,0.5490196078431373,1,1
            Rectangle:
                size: self.size
                pos: self.pos

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



    
        
            
'''