from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import re

class WeatherRoot(BoxLayout):
    pass

#Programmers hate duplicating work, and you’ll find most tasks have already been completed!
class AddLocationForm(BoxLayout):
    #Kivy properties contain all sorts of knowledge that is very useful when you’re
    #interfacing between the KV language layout file and the actual Python program.
    search_input = ObjectProperty()
    list_items = ObjectProperty()
    search_results_list=["Nairobi","Nyeri","Nyeri East","Mukuruweini, Nyeri","Nairobi West","Murang'a","Ruiru","Kiambu","Joska"]
    def search_location(self):
        self.fill_in_the_list()
    
    def fill_in_the_list(self):
        f_string = ""
        for item in self.search_results_list:
            if self.search_input.text in item:
                f_string=f_string+item+"\n"
        self.list_items.text = f_string
        print(self.list_items.text)


class WeatherApp(App):
    pass

if __name__ == "__main__":
    WeatherApp().run()