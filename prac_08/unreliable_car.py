"""
CP1404
Not a very reliable car
Based on Car
"""


from prac_08.car import Car
from random import randrange


class UnreliableCar(Car):
    """Variant of Car class"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randrange(0, 101) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            print("Car broke down.")
            distance_driven = 0
        return distance_driven

