from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout

class HybridLayouts(App):
    def build(self):
        mother_layout = BoxLayout(orientation="vertical")
        
        box_lay = BoxLayout(orientation="horizontal")
        grid_lay = GridLayout(rows=2,cols=5)
        anch_lay = AnchorLayout(anchor_x="left",anchor_y="center")
        stack_lay = StackLayout(orientation="tb-lr")
        float_lay = FloatLayout()
         
        but1=Button(text="Button 1",size_hint = (0.2,1))
        lab1=Label(text="Label1",size_hint = (0.2,1))
        xtx1=TextInput(size_hint = (0.2,1))
        but2=Button(text="Button 2",size_hint=(0.2,0.2))
        lab2=Label(text="Label 2",size_hint=(0.2,0.2))
        xtx2=TextInput(size_hint = (0.2,0.2),pos=(500,10))
        but3=Button(text="Button 3",size_hint = (0.2,0.2))
        lab3=Label(text="I'm Label 3 and at The anchor Level")
        
        box_lay.add_widget(but1)
        grid_lay.add_widget(lab1)
        grid_lay.add_widget(but3)
        anch_lay.add_widget(xtx1)
        anch_lay.add_widget(lab3)
        stack_lay.add_widget(but2)
        stack_lay.add_widget(lab2)
        float_lay.add_widget(xtx2)
        
        mother_layout.add_widget(box_lay)
        mother_layout.add_widget(grid_lay)
        mother_layout.add_widget(anch_lay)
        mother_layout.add_widget(stack_lay)
        mother_layout.add_widget(float_lay)
        
        
        return mother_layout
    
    
    
    
    
if __name__ == "__main__":
    HybridLayouts().run()