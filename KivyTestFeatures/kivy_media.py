#Working with images, colors,shapes, drawings...

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle,Color #--> For more Graphics
from kivy.uix.video import Video #--> for playing video
from kivy.animation import Animation

class TestMedia(App):
    def build(self):
        main_layout = BoxLayout()
        image= Image(source="Billie eilish.jpeg")
        label = Label(text="I'm who I am")
        btn = Button(text="Sellment",size_hint=(0.2,0.2))
        video = Video(source="/home/kevin/Documents/Learn_Advanced Python/PythonScripts/KivyTestProject/Pomme   La lumière.mp4")
        video.state = "play"
        anime = Animation(x=400,y=500, duration= 5)
        anime.start(btn)
        
        main_layout.add_widget(image)
        main_layout.add_widget(video)
        main_layout.add_widget(label)
        main_layout.add_widget(btn)
        #main_layout.add_widget(anime)
        return main_layout
    
    
    
TestMedia().run()