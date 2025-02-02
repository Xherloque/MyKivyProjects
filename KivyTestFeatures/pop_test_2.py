from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class OptionsMenu(Popup):
    def __init__(self, video_name, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)  # Fixed size for popup
        self.size = (200, 150)
        self.auto_dismiss = False  # Don't dismiss automatically

        self.title = f"Options for {video_name}"

        layout = GridLayout(cols=1, padding=10, spacing=10)  # Layout for buttons
        layout.add_widget(Button(text="Option 1: Play"))
        layout.add_widget(Button(text="Option 2: Download"))
        layout.add_widget(Button(text="Option 3: Share"))

        self.add_widget(layout)

class VideoItem(BoxLayout):
    def __init__(self, video_name, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 50

        # Label for video name
        video_label = Label(text=video_name, size_hint_x=0.8)
        self.add_widget(video_label)

        # Colon buttons
        for _ in range(3):
            colon_button = Button(text=":", size_hint_x=None, width=30)
            colon_button.bind(on_release=self.show_options_menu)
            self.add_widget(colon_button)

    def show_options_menu(self, instance):
        # When a colon button is clicked, show the options menu
        video_name = self.children[2].text  # Get the video name from the label (last widget in BoxLayout)
        popup = OptionsMenu(video_name=video_name)
        popup.open()

class MainApp(App):
    def build(self):
        self.root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Scroll view to allow scrolling through a list of videos
        scroll_view = ScrollView()
        scroll_content = BoxLayout(orientation="vertical", size_hint_y=None)
        scroll_content.bind(minimum_height=scroll_content.setter('height'))

        # List of video names
        video_names = [
            "Video 1", "Video 2", "Video 3", "Video 4", "Video 5",
            "Video 6", "Video 7", "Video 8", "Video 9", "Video 10"
        ]

        # Add VideoItem for each video
        for video_name in video_names:
            video_item = VideoItem(video_name=video_name)
            scroll_content.add_widget(video_item)

        scroll_view.add_widget(scroll_content)

        self.root.add_widget(scroll_view)
        return self.root

if __name__ == "__main__":
    MainApp().run()
