from . import Habitat
from movements import ISwimming


class Aquarium(Habitat):

    def __init__(self, name):
        super().__init__(name)

    # Duck Typing check
    # Using duck typing you do not check types at all.
    # Instead you check for the presence of a given method or attribute.
    def add_swimmer_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(
                f'{animal} can\'t swim, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_swimmer_type_check(self, animal):
        if isinstance(animal, ISwimming):
            self.animals.add(animal)
        else:
            print(f'{animal} can\'t swim, so please do not try to put it in the {self.name} habitat')
