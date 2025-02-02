from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

class GeneralSpace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation ="vertical"
        welcome_box = Label(text="Welcome to the Community Support Management System...\n There are alot of stuff you can do with this...",
                            font_size= 23,
                            italic=True,
                            color="green",
                            outline_color='green')
        self.add_widget(welcome_box)
        recs = BoxLayout(padding=10)
        new_meeting = Button(text="Record/Start New Meeting", color="black",
                             font_size=24,background_color="cyan")
        recs.add_widget(new_meeting)
        recent_events = Button(text="Open Recent Events",color="black",font_size=24)
        recs.add_widget(recent_events)
        self.add_widget(recs)
        
        membs = BoxLayout(padding=10)
        new_member = Button(text="Register A New Member",color="black",font_size=24)
        view_members = Button(text="Members/ View Members",color="black",font_size=24)
        membs.add_widget(new_member)
        membs.add_widget(view_members)
        self.add_widget(membs)
        
        bom_list = ["Id","First Name","Last Name","Status",
                    "1","Kevin","Muturi","Chairman",
                    "2","Clifford", "Kovulo","Director",
                    "3","John","Doe","Secretary",
                    "4","Foo","Bar","Member"]+["5","Smart", "Kid", "Member"]*20#This will require modifications durong backend integartion
        bom_grid= GridLayout(cols=4,size_hint_y=None)
        ils_scroll=ScrollView()
        b_count=1
        for item in bom_list:
            if b_count <= 4:
                bom_grid.add_widget(Label(text=item,font_size=20,bold=True,
                                          size_hint_y=None,height=40))
            else:
                bom_grid.add_widget(Label(text=item,font_size=15,size_hint_y=None,
                    height=40))
            b_count+=1
        bom_grid.bind(minimum_height=bom_grid.setter('height'))  # Make GridLayout height dynamic based on content
        ils_scroll.add_widget(bom_grid)
        self.add_widget(ils_scroll)
        self.size_hint_x=0.75
    

class DashBoard(BoxLayout):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.size_hint_x=0.23
        self.add_widget(Label(text="DASHBOARD",font_size=20,bold=True))
        search_funcs=BoxLayout()
        search_bar=TextInput(size_hint_x=0.8)
        submit_but=Button(text="search",size_hint_x=0.2)
        search_funcs.add_widget(search_bar)
        search_funcs.add_widget(submit_but)
        self.add_widget(search_funcs)
        my_list = ["Registration","Members","Accounts & Contributions","Arrears",
                   "Report & Analytics", "Events + Meetings", "Notifications & Message Management",
                   "Settings","Visit Web", "Help/ COntact Us"]
        for item in my_list:
            self.add_widget(Button(text=item))

class MyScroll(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        for i in range(10):
            self.add_widget(Label(text="||"))
        self.size_hint_x=0.02
        
        
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.add_widget(Label(text="Welcome to the Home Page", font_size=24))
        home_page = GridLayout(cols=3)
        # We gon have two internal layouts, one is gon be for the dashboard then
        # the other for the general_space
        dashboard = DashBoard()
        my_scroll = MyScroll()
        general_space = GeneralSpace()
        home_page.add_widget(dashboard)
        home_page.add_widget(my_scroll)
        home_page.add_widget(general_space)
        self.add_widget(home_page)
        

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

        # Buttons for navigation
        home_btn = Button(text='Home', on_press=self.switch_screen,background_color="navy")
        about_btn = Button(text='About', on_press=self.switch_screen,background_color="navy")
        contact_btn = Button(text='Contact', on_press=self.switch_screen,background_color="navy")
        
        home_btn.screen_manager = screen_manager
        home_btn.screen_name = 'home'
        
        about_btn.screen_manager = screen_manager
        about_btn.screen_name = 'about'
        
        contact_btn.screen_manager = screen_manager
        contact_btn.screen_name = 'contact'
        
        self.add_widget(home_btn)
        self.add_widget(about_btn)
        self.add_widget(contact_btn)
    
    def switch_screen(self, instance):
        instance.screen_manager.current = instance.screen_name

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ContactScreen(name='contact'))
        
        root = BoxLayout(orientation='vertical')
        root.add_widget(Label(text="Community Support Management System",size_hint_y =0.1,font_size=35,color="blue"))
        root.add_widget(NavBar(screen_manager=sm))  # Navbar at the top
        root.add_widget(sm)  # Screen manager below navbar
        
        return root

if __name__ == '__main__':
    MainApp().run()
