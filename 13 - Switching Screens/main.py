# KivyMD changed. Now, lets do it in kivymd 2.0.0
from kivymd.app import MDApp # This is cool...
from kivy.lang.builder import Builder # This is also cool
from kivy.uix.screenmanager import ScreenManager, Screen # This is also cool, but you could use kivymd.uix.screen import MDScreenManager...
# Now, Lets do it the easier way. 
screen_helper = """

MDScreenManager:
    id: sm

    MDScreen: # change it from class name, to just calling the class directly in kv file.
        name: 'menu'
        MDButton:
            pos_hint: {'center_x':0.5,'center_y':0.6}
            on_press: sm.current = 'profile'
            MDButtonText:
                text: 'Profile'
        MDButton:
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_press: sm.current = 'upload'
            MDButtonText:
                text: 'Upload'
    
    MDScreen:
        name: 'profile'
        MDLabel:
            text: 'Profile'
            halign: 'center'
        MDButton:
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: sm.current = 'menu'
            MDButtonText:
                text: 'Back'
        
    MDScreen:
        name: 'upload'
        MDLabel:
            text: 'Upload'
            halign: 'center'
        MDButton:
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_press: sm.current = 'menu'
            MDButtonText:
                text: 'Back'
        
"""
# Now, we do away with the weird classes.
"""
class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass
"""

# we already defined this in our kv file, so, we gonna do away with it also.
"""
# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

"""
class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
# Yeah, cool. there you go.
