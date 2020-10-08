"""CP1404 prac_07: Miles to Kilometres Kivy"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesKilometreConverterApp(App):
    """ MilesKilometreConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ Build the app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        print('convert')
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        print('increment')
        value = self.get_validated_miles() + increment
        self.root.ids.input_label.value = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        print("validating")
        try:
            value = float(self.root.ids.input_label.text)
            # For some reason, the process breaks here and I do not know why. I checked the solution and it seems right.
            return value
        except ValueError:
            print("Invalid")
            return 0


MilesKilometreConverterApp().run()
