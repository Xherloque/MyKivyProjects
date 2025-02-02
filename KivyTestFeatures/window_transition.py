from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager

class LauraFabian(App):
    def build(self):
        main_layout=BoxLayout(orientation="vertical")
        
        some_content = Label(text="Some Content")
        some_button = Button(text="Texty Button")
        
        #lay_2=BoxLayout()
        some_other_content = Label(text="Pomme is the Best")
        some_other_button = Button(text="Another Texty Button")
        #lay_2.add_widget(some_other_content)
        #lay_2.add_widget(some_other_button)
        
        anime=Animation(opacity=1,duration=1)
        anime.start(some_other_button)
        
        main_layout.add_widget(some_content)
        main_layout.add_widget(some_button)
        main_layout.add_widget(some_other_button)
        
        
        return main_layout
        


if __name__ =="__main__":
    LauraFabian().run()