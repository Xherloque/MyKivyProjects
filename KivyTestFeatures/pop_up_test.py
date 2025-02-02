from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

class OptionsMenu(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)  # Popup will have a fixed size
        self.size = (200, 150)  # Width 200, height 150 pixels
        self.auto_dismiss = False  # Popup won't automatically dismiss
        self.background = ''  # Remove background color
        self.background_color = (1, 1, 1, 0)  # Transparent background to avoid dimming
        self.title = "OPTIONS"
        layout = GridLayout(cols=1, padding=10, spacing=10)  # Vertical Layout for the button
        layout.add_widget(Button(text="Option 1", size_hint_y=None, height=40))
        layout.add_widget(Button(text="Option 2", size_hint_y=None, height=40))
        layout.add_widget(Button(text="Option 3", size_hint_y=None, height=40))

        self.add_widget(layout)

class MainApp(App):
    def build(self):
        self.root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Add 10 buttons to the layout
        for i in range(1, 10):
            btn = Button(text=f"Button {i}", size_hint_y=None, height=50)
            btn.bind(on_release=self.show_options_menu)
            self.root.add_widget(btn)

        # Bind a dismiss method to clicks outside the popup
        Window.bind(on_touch_down=self.dismiss_popup)

        self.current_popup = None  # This keeps track of the currently open popup

        return self.root

    def show_options_menu(self, instance):
        # If a popup is already open, dismiss it
        if self.current_popup:
            self.current_popup.dismiss()

        # Create a new options menu
        popup = OptionsMenu()

        # Get the button's position relative to the root window
        btn_pos = self.root.to_window(instance.x, instance.y)

        # Set the popup position relative to the button
        popup.pos = (btn_pos[0] + instance.width, btn_pos[1])

        popup.open()  # Open the popup
        self.current_popup = popup  # Keep track of the currently open popup

    def dismiss_popup(self, window, touch):
        # Dismisses the current popup if a touch is outside the popup and its buttons
        if self.current_popup and not self.current_popup.collide_point(*touch.pos):
            self.current_popup.dismiss()
            self.current_popup = None

if __name__ == "__main__":
    MainApp().run()
