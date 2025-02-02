from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

#A simple calculator app illustrating the usage of the grid layout

class Calculator(App):
    def build(self):
        main_layout = BoxLayout()
        
        text_area=BoxLayout(orientation="vertical")
        self.text_part=TextInput(hint_text="Enter:",size_hint_y=0.15,multiline=False,font_size=35)
        self.answer_part=TextInput(text=" ",size_hint_y=0.30,font_size=35)
        label=Label(size_hint_y=0.55)
        text_area.add_widget(self.text_part)
        text_area.add_widget(self.answer_part)
        text_area.add_widget(label)
        num_part= GridLayout(rows=4,cols=4)
        stuff = ["+","0","1","2","-","3","4","5","*","6","7","8","/","9","Del","="]
        
        for item in stuff:
            key = Button(text=item,size_hint=(0.2,0.2),padding=50)
            if item == "=":
                key.bind(on_press = self.tryeval)
            elif item== "Del":
                key.bind(on_press = self.removeChar)
            else:
                key.bind(on_press = self.add_to_box)
            num_part.add_widget(key)
            
        main_layout.add_widget(text_area)
        main_layout.add_widget(num_part)
        
        return main_layout
    
    def add_to_box(self,instance):
        self.text_part.text+=instance.text
        
    def tryeval(self,instance):
        try:
            answer = eval(self.text_part.text)
            self.answer_part.text =self.text_part.text + " = " + str(answer)
            self.text_part.text = ""
        except Exception as e:
            self.answer_part.text = f"Error {e}"
            self.text_part.text = ""
            
    def removeChar(self,instance):
        if len(self.text_part.text) >= 1:
            rmedd = self.text_part.text[:-1]
            self.text_part.text = rmedd
        else:
            pass
        
Calculator().run()