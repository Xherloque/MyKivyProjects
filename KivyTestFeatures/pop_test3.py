from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import time

class FloatingCard(App):
    def build(self):
        self.root = BoxLayout(orientation = "vertical")
        
        for i in range(1,10):
            btn = Button(text=f"Button {i}")
            print(btn.pos)
            self.root.add_widget(btn)
            if i == 5:
                btn_pos = btn.pos
                print("THE BUTTON POSITION IS",btn_pos)
                flb = FloatLayout()
                print("flb's pos = ",flb.pos)
                sbtn1 = Button(text="Kasmall Button1",size_hint = (0.2,0.3),pos=(640,560),font_size=20,background_color="black")
                sbtn2 = Button(text="Kasmall Button2",size_hint = (0.2,0.3),pos=(640,540),font_size=20,background_color="black")
                sbtn3 = Button(text="Kasmall Button3",size_hint = (0.2,0.3),pos=(640,520),font_size=20,background_color="black")
                sbtn4 = Button(text="Kasmall Button4",size_hint = (0.2,0.3),pos=(640,500),font_size=20,background_color="black")
                print("The pos for sbtn1,2,3,4 are",[sbtn1.pos,sbtn2.pos,sbtn3.pos,sbtn4.pos])
                flb.add_widget(sbtn1)
                flb.add_widget(sbtn2)
                flb.add_widget(sbtn3)
                flb.add_widget(sbtn4)
                self.root.add_widget(flb)
            # elif i == 9:
            #     # Clock.SLEEP_UNDERSHOOT()
            #     self.root.remove_widget(flb)
           
        return self.root
    
    
if __name__ == "__main__":
    FloatingCard().run()