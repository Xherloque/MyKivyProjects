from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
import os
#The boxlayout creates kind of a box that decides how his children will stay...
#It can have vertcal or horizontal orientation (How it positions it's kids)
#The size hints (x,y) really depends on how the other kids are sized

class BoxLayTest(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        
        
        for item in os.listdir():
            bt = Button(text=f"{item * 45 }")
            scroll_view = ScrollView(size_hint = (bt.size_hint_x * 100,bt.size_hint_y),do_scroll_x=True,do_scroll_y=True)
     
            scroll_view.add_widget(bt)
            main_layout.add_widget(scroll_view)
        
        return main_layout
    
    
if __name__ == "__main__":
    BoxLayTest().run()