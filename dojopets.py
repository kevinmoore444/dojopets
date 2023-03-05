class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()



class Pet:
    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise

    def sleep(self):
        self.energy +=25
        print(f"energy={self.energy}")
        return self
    
    def eat(self):
        self.energy +=5
        self.heatlh +=10
        print(f"energy={self.energy}")
        print(f"health={self.health}")
        return self

    def play(self):
        self.health +=5
        print(f"health={self.health}")
        return self

    def makenoise(self):
        print(self.noise)
        return self


pet_1 = Pet("Duke", "Bulldog", "Backflip", 100, 100, "Bark Bark")
ninja_1 = Ninja("Kevin", "Moore", "Chips", "DogChow", pet_1)


ninja_1.walk()
# ninja_1.feed()
# ninja_1.bath()

# pet_1.sleep()
# pet_1.eat()
# pet_1.play()
# pet_1.makenoise()