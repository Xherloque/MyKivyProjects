from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Welcome to the Home Page", font_size=24))

class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="About Us", font_size=24))

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Contact Us", font_size=24))

class NavBar(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        
        self.screen_manager = screen_manager
        self.nav_buttons = []  # Store button references
        
        # Create buttons
        self.create_nav_button('Home', 'home')
        self.create_nav_button('About', 'about')
        self.create_nav_button('Contact', 'contact')
        
        # Set initial active button
        self.update_active_button(self.nav_buttons[0])
    
    def create_nav_button(self, text, screen_name):
        btn = Button(text=text, on_press=self.switch_screen)
        btn.screen_name = screen_name
        self.nav_buttons.append(btn)
        self.add_widget(btn)
    
    def switch_screen(self, instance):
        self.screen_manager.current = instance.screen_name
        self.update_active_button(instance)
    
    def update_active_button(self, active_button):
        for btn in self.nav_buttons:
            btn.background_color = [1, 1, 1, 1]  # Default (white)
        active_button.background_color = [0, 0.6, 1, 1]  # Highlight (blue)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ContactScreen(name='contact'))
        
        root = BoxLayout(orientation='vertical')
        navbar = NavBar(screen_manager=sm)
        root.add_widget(navbar)  # Navbar at the top
        root.add_widget(sm)  # Screen manager below navbar
        
        return root

if __name__ == '__main__':
    MainApp().run()
