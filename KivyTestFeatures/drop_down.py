from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

class TestDropdown(App):
    def build(self):
        box = BoxLayout()
        dropdown = DropDown()
        
        for name in ["Option 1", "Option 2"]:
            btn = Button(text=name, size_hint_y=None, height=44)
            btn.bind(on_release=lambda instance: dropdown.select(instance.text))
            dropdown.add_widget(btn)

        dropdown_btn = Button(text="Open Menu")
        dropdown_btn.bind(on_release=dropdown.open)
        
        box.add_widget(dropdown_btn)
        return box

if __name__ == "__main__":
    TestDropdown().run()
