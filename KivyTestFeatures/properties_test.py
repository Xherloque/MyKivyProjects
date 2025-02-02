#Properties allow you to store and manage the state of your widgets
#Events lets you respond to user actions like touch,clicks or key presses

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton

class TestEvent(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        #When you press Enter, The stuff in the text input gets displayed on the label
        txt = TextInput(hint_text="Enter something", multiline=False,size_hint_y=0.5)
        txt.bind(on_text_validate=self.enter_stuff)
        self.label = Label(text="Jour Un",size_hint_y=0.8)
        
        #A slider
        slide = Slider(min=0,max=100)
        slide.bind(value=lambda instace,value: print(f"The value is {value}"))
        
        #Switch
        switch = Switch(active=False)
        switch.bind(active=lambda instance,value: print("value is","on" if value else "off"))
        
        #CheckBox
        check = CheckBox(active=False)
        check.bind(active=lambda instance,value: print("value is","checked" if value else "Not checked"))
        
        #Togggle
        toggle = ToggleButton(text="Togg Button")
        toggle.bind(state=lambda instace,value: print(f"The value is {value}"))
        
        layout.add_widget(slide)
        layout.add_widget(txt)
        layout.add_widget(self.label)
        layout.add_widget(switch)
        layout.add_widget(check)
        layout.add_widget(toggle)
        return layout
    
    def enter_stuff(self,instance):
        self.label.text=instance.text
    
        
        
TestEvent().run()