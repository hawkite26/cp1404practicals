"""CP1404/CP5632 Practical - Programming language class definitions"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name="", typing_style="", reflection=False, year_released=int("")):
        """Takes language variables"""
        self.name = name
        self.style = typing_style
        self.reflection = reflection
        self.year = year_released

    def is_dynamic(self):
        if self.style.lower() == "dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} typing, Reflection={}, First appeared in {}"

