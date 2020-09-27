"""CP1404 prac_07: Miles to Kilometres Kivy"""

from kivy.app import App
from kivy.lang import Builder


class MilesKilometreConverterApp(App):
    """ MilesKilometreConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ Build the app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_up_calculate(self, value):
        result = value + 1
        self.root.ids.input_label.text = str(result)

    def handle_down_calculate(self, value):
        result = value - 1
        self.root.ids.input_label.text = str(result)


MilesKilometreConverterApp().run()
