from dataclasses import dataclass


class Creature:
    def __init__(self, name, type, age, prey):
        self.name = name
        self.type = type
        self.age = age
        self.prey = prey

    def __str__(self):
        return f"{self.name} {self.type} {self.age}"


class Plant(Creature):
    def __init__(self, name, type, age, prey):
        super().__init__(name, type, age, prey)

    def __str__(self):
        return super().__str__()


class Animal(Creature):
    def __init__(self, name, type, age, prey):
        super().__init__(name, type, age, prey)

    def __str__(self):
        return super().__str__()


class Ecosystem:
    def __init__(self):
        self.creatures: list[Creature] = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def remove_creature_by_name(self, name):
        elements = self.search_creature_by_name(name)
        self.remove_creatures(elements)

    def remove_creature_by_type(self, type):
        elements = self.search_creature_by_type(type)
        self.remove_creatures(elements)

    def search_creature_by_type(self, type):
        return list(filter(lambda x: x.type == type, self.creatures))

    def search_creature_by_name(self, name):
        return list(filter(lambda x: x.name == name, self.creatures))

    def remove_creatures(self, creatures):
        self.creatures = [e for e in self.creatures if e not in creatures]

    def get_plants(self):
        return filter(lambda x: type(x) is Plant, self.creatures)

    def get_animals(self):
        return filter(lambda x: type(x) is Animal, self.creatures)

    def display(self):
        print("Растения:")
        for plant in self.get_plants():
            print(plant)
        print("Животные:")
        for animal in self.get_animals():
            print(animal)


ecosystem = Ecosystem()

trava = Plant("Трава", "Наземные", 10, [])
baran = Animal("Баран", "Млекопитающее", 25, [trava])

ecosystem.add_creature(trava)
ecosystem.add_creature(Plant("Водоросли", "Подводные", 15))
ecosystem.add_creature(baran)
ecosystem.add_creature(Animal("Сова", "Птица", 8))
ecosystem.display()
ecosystem.remove_creature_by_name("Трава")
ecosystem.remove_creature_by_type("Млекопитающее")
print("===========================================")
ecosystem.display()
print("Конец")
