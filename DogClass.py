class Dog:
    """This is the beginning of a class for the loving  house dog"""

    def __init__(self, name):
        self.name = name

    def add_breed(self, breed):
        self.breed = breed

    def add_color(self, color):
        self.color = color

    def add_mass(self, mass):
        self.mass = mass

    def add_height(self, height):
        self.height = height

    def add_lifespan(self, min_life, max_life):
        self.min_life = min_life
        self.max_life = max_life

    def add_origin(self, origin):
        self.origin = origin

    def add_hypoallergenic(self, hypoallergenic):
        self.hypoallergenic = hypoallergenic

    def add_temperament(self, temperament):
        self.temperament = temperament

    def add_bark(self, bark):
        self.bark = bark

c = Dog("Apex")

c.add_breed("germanshepard")

c.add_color("black and tan")

c.add_mass(75)

c.add_height(25)

c.add_lifespan(9, 13)

c.add_origin("Germany")

c.add_hypoallergenic("no")

c.add_temperament("lively")

c.add_bark("yes")




x = Dog("Rona")

x.add_breed("Shih tzu")

x.add_color("Black")

x.add_mass(12)

x.add_height(11)

x.add_lifespan(10, 16)

x.add_origin("Tibet")

x.add_hypoallergenic("yes")

x.add_temperament("devoted")

x.add_bark("yes")

print(c.name)
print(c.breed)
print(c.color)
print(c.mass)
print(c.height)
print(c.min_life)
print(c.max_life)
print(c.origin)
print(c.hypoallergenic)
print(c.temperament)
print(c.bark)

print(x.name)
print(x.breed)
print(x.color)
print(x.mass)
print(x.height)
print(x.min_life)
print(x.max_life)
print(x.origin)
print(x.hypoallergenic)
print(x.temperament)
print(x.bark)

