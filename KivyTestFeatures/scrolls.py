from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TableApp(App):
    def build(self):
        scroll = ScrollView()  # Create a ScrollView

        # Create a GridLayout with 3 columns
        layout = GridLayout(cols=3, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # Adjust height dynamically

        # Add 50 rows to the table
        for i in range(50):  # simulate 50 rows
            for j in range(3):  # 3 columns
                cell = Label(
                    text=f"Row {i+1} Col {j+1}",
                    size_hint_y=None,  # Prevents compression
                    height=40  # Ensures proper row height
                )
                layout.add_widget(cell)

        scroll.add_widget(layout)  # Add the GridLayout inside the ScrollView
        return scroll  # Return the ScrollView to display it

if __name__ == "__main__":
    TableApp().run()
