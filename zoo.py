from animals import Penguin, PaintedDog
from habitats import Aquarium

Flipper = Penguin("Flipper")
Flipper.swim()
Flipper.run()

Picasso = PaintedDog("Picasso")
Picasso.run()

SanDiegoAquarium = Aquarium("San Diego Aquarium")
SanDiegoAquarium.add_swimmer_pythonic(Flipper)
SanDiegoAquarium.add_swimmer_pythonic(Picasso)
SanDiegoAquarium.add_swimmer_type_check(Picasso)

print(f"The following animals live in San Diego Aquarium:")
for animal in SanDiegoAquarium.animals:
    print(animal)
