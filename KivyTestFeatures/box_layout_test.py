from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

#The boxlayout creates kind of a box that decides how his children will stay...
#It can have vertcal or horizontal orientation (How it positions it's kids)
#The size hints (x,y) really depends on how the other kids are sized

class BoxLayTest(App):
    def build(self):
        main_layout = BoxLayout()
        
        
        but1=Button(text="Button 1",size_hint = (0.2,1))
        lab1=Label(text="Label1",size_hint = (0.2,1))
        xtx1=TextInput(size_hint = (0.2,1))
        but2=Button(text="Button 2",size_hint = (0.2,0.2))
        lab2=Label(text="Label 2",size_hint = (0.2,0.2))
        xtx2=TextInput(size_hint = (0.2,0.2))
        
        main_layout.add_widget(but1)
        main_layout.add_widget(lab1)
        main_layout.add_widget(xtx1)
        main_layout.add_widget(but2)
        main_layout.add_widget(lab2)
        main_layout.add_widget(xtx2)
        
        return main_layout
    
    
if __name__ == "__main__":
    BoxLayTest().run()