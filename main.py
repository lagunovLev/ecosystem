from dataclasses import dataclass


class Creature:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def __str__(self):
        return f"{self.name} {self.type} {self.age}"


class Plant(Creature):
    def __init__(self, name, type, age):
        super().__init__(name, type, age)

    def __str__(self):
        return super().__str__()


class Animal(Creature):
    def __init__(self, name, type, age):
        super().__init__(name, type, age)

    def __str__(self):
        return super().__str__()


class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plants = []

    def add_animal(self, creature):
        self.animals.append(creature)

    def add_plant(self, creature):
        self.plants.append(creature)

    def remove_plant_by_name(self, name):
        elements = list(filter(lambda x: x.name == name, self.plants))
        self.plants = [e for e in self.plants if e not in elements]

    def remove_plant_by_type(self, type):
        elements = self.search_animal_by_type(type)
        self.plants = [e for e in self.plants if e not in elements]

    def remove_animal_by_name(self, name):
        elements = list(filter(lambda x: x.name == name, self.animals))
        self.animals = [e for e in self.animals if e not in elements]

    def remove_animal_by_type(self, type):
        elements = self.search_animal_by_type(type)
        self.animals = [e for e in self.animals if e not in elements]

    def search_animal_by_type(self, type):
        return list(filter(lambda x: x.type == type, self.animals))

    def search_plant_by_type(self, type):
        return list(filter(lambda x: x.type == type, self.plants))

    def display(self):
        print("Растения:")
        for plant in self.plants:
            print(plant)
        print("Животные:")
        for animal in self.animals:
            print(animal)


ecosystem = Ecosystem()
ecosystem.add_plant(Plant("Трава", "Наземные", 10))
ecosystem.add_plant(Plant("Водоросли", "Подводные", 15))
ecosystem.add_animal(Animal("Баран", "Млекопитающее", 25))
ecosystem.add_animal(Animal("Сова", "Птица", 8))
ecosystem.display()
ecosystem.remove_plant_by_name("Трава")
ecosystem.remove_animal_by_type("Млекопитающее")
print("===========================================")
ecosystem.display()