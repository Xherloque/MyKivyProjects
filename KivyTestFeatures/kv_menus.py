from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from functools import partial

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

class ServicesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Our Services", font_size=24))

class PricingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Pricing Details", font_size=24))

class NavBar(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50

        home_btn = Button(text='Home', on_press=lambda x: setattr(screen_manager, 'current', 'home'))
        about_btn = Button(text='About', on_press=lambda x: setattr(screen_manager, 'current', 'about'))
        contact_btn = Button(text='Contact', on_press=lambda x: setattr(screen_manager, 'current', 'contact'))
        
        dropdown = DropDown()
        
        def change_screen(screen_name, *args):
            screen_manager.current = screen_name
            dropdown.dismiss()
        
        for item, screen in [('Services', 'services'), ('Pricing', 'pricing')]:
            btn = Button(text=item, size_hint=(None, None), width=150, height=44)
            btn.bind(on_release=partial(change_screen, screen))
            dropdown.add_widget(btn)
        
        dropdown_btn = Button(text='More', size_hint=(None, None), width=100, height=50)
        # dropdown_btn.bind(on_release=dropdown.open)
        dropdown_btn.bind(on_release=lambda instance: (print("Dropdown opened"), dropdown.open(instance)))


        self.add_widget(home_btn)
        self.add_widget(about_btn)
        self.add_widget(contact_btn)
        self.add_widget(dropdown_btn)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ContactScreen(name='contact'))
        sm.add_widget(ServicesScreen(name='services'))
        sm.add_widget(PricingScreen(name='pricing'))
        
        root = BoxLayout(orientation='vertical')
        root.add_widget(NavBar(screen_manager=sm))
        root.add_widget(sm)
        
        return root

if __name__ == '__main__':
    MainApp().run()
