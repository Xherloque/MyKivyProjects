from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout


class AnchorLayTest(App):
    def build(self):
        main_layout = AnchorLayout(anchor_x="left",anchor_y="center")
        
        
        but1=Button(text="Button 1")
        lab1=Label(text="Label1")
        xtx1=TextInput()
        but2=Button(text="Button 2")
        lab2=Label(text="Label 2")
        xtx2=TextInput()
        
        main_layout.add_widget(but1)
        main_layout.add_widget(lab1)
        main_layout.add_widget(xtx1)
        main_layout.add_widget(but2)
        main_layout.add_widget(lab2)
        main_layout.add_widget(xtx2)
        
        return main_layout
    
    
if __name__ == "__main__":
    AnchorLayTest().run()