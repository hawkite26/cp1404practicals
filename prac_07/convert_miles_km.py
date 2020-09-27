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
        print('convert')
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, increment):
        print('increment')
        result = int(value) + increment
        print(result)
        self.root.ids.input_label.value = int(result)
        # I do not understand why this does not work. I tried .txt and str(result) and I just can't figure it out


MilesKilometreConverterApp().run()
