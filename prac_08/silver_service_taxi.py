"""
CP1404
Silver Service Taxi Class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A specialised Taxi class for more expensive Taxis"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super(SilverServiceTaxi, self).__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with Flagfall."""
        return "{} plus a flagfall of ${:.2f} ".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

