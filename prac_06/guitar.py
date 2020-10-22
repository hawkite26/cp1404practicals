"""CP1404/CP5632 Practical - Programming guitar class"""


class Guitar:
    """Define Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def age(self):
        age = 2020-self.year
        return age

    def is_vintage(self):
        if self.age() >= 50:
            return True
        else:
            return False

    def __str__(self):
        return "{} ({}): {}".format(self.name, self.year, self.cost)
