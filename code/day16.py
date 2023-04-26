# file created by Max Kanter

# welcome to classes
class lizard:
    def __init__(self, name, species):
#paramaters
        self.name = name 
        self.species = species
        self.coldblooded = True
    def jump(self):
        print(self.name + " has jumped...")

    def duck(self):
        print(self.name + " has ducked under a table...")

    def listen(self):
        print(self.name + " listened into your conversation...")

my_lizard = lizard("Hank", "Iguana")
Lizards = (my_lizard)

my_lizard1 = lizard("Hank", "bird")
my_lizard2 = lizard("Tom", "dog")
my_lizard3 = lizard("Bill", "mouse")

print(my_lizard1.name + " is an " + my_lizard1.species)
print(my_lizard2.name + " is an " + my_lizard2.species)
print(my_lizard3.name + " is an " + my_lizard3.species)


geckos =[]

for i in range(0, 5):
    l = lizard
    geckos.append(i)
    geckos.append(l.species)

print(geckos)

for i in geckos:
    print(geckos[1])
    # geckos[i].jump()



# def update(self):
#     self.rect.x + =1

# second_lizard = lizard("Eman")
# def cool(self):
#     print(second_lizard.name + "is a ")




# class Iguana(Lizard):
#     def __init__(self, name, species):
#         Lizard.__init__(self, name, species)
