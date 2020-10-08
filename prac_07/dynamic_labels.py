"""
Dynamic labels for CP1404/CP5632, IT@JCU
Dynamically create labels based on a list of names
Kye Bryce
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Terry", "Finn", "Bobby", "Clarence"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=str(name))
            temp_label.name = name
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()
