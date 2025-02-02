from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout


#This helps you put the widgets at a specific point

class FloatLayTest(App):
    def build(self):
        main_layout = FloatLayout()
        
        
        but1=Button(text="Button 1",size_hint = (0.2,0.2),pos=(10,500))
        lab1=Label(text="Label1",size_hint = (0.2,0.2),pos=(150,500))
        xtx1=TextInput(size_hint = (0.2,0.2),pos=(230,430))
        but2=Button(text="Button 2",size_hint = (0.2,0.2),pos=(40,40))
        lab2=Label(text="Label 2",size_hint = (0.2,0.2),pos=(50,50))
        xtx2=TextInput(size_hint = (0.2,0.2),pos=(10,390))
        
        main_layout.add_widget(but1)
        main_layout.add_widget(lab1)
        main_layout.add_widget(xtx1)
        main_layout.add_widget(but2)
        main_layout.add_widget(lab2)
        main_layout.add_widget(xtx2)
        
        return main_layout
    
    
if __name__ == "__main__":
    FloatLayTest().run()