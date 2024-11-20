import csv


class Database:
    def __init__(self, filename):
        self.filename = filename

    def save_ecosystem(self, ecosystem):
        with open(self.filename, mode="w", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
            file_writer.writerow(["Название", "Тип", "Возраст", "Чем питается", "Type"])
            for c in ecosystem.creatures:
                file_writer.writerow([c.name, c.type, c.age, ''.join(str(x.name) for x in c.prey), type(c).__name__])

    def read_ecosystem(self, logger):
        def get_creature(name, type, age, prey, type_as_str):
            if type_as_str == "Animal":
                return Animal(name, type, age, prey)
            else:
                return Plant(name, type, age, prey)

        ecosystem = Ecosystem(logger)
        with open(self.filename, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";", lineterminator="\r")
            next(file_reader)
            for row in file_reader:
                prey = row[3]
                prey = prey.split(" ")
                ecosystem.add_creature(get_creature(row[0], row[1], row[2], prey, row[4]))
        for c in ecosystem.creatures:
            prey = c.prey
            c.prey = []
            for prey_name in prey:
                if prey_name:
                    c.prey += ecosystem.search_creature_by_name(prey_name)
        return ecosystem


class Logger:
    def log(self, string):
        print('\033[4m' + string + '\033[0m')


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
    def __init__(self, logger):
        self.creatures: list[Creature] = []
        self.logger = logger

    def add_creature(self, creature):
        self.creatures.append(creature)

    def remove_creature_by_name(self, name):
        elements = self.search_creature_by_name(name)
        if not elements:
            self.logger.log(f"Существ с именем {name} не нашлось")
        self.remove_creatures(elements)

    def remove_creature_by_type(self, type):
        elements = self.search_creature_by_type(type)
        if not elements:
            self.logger.log(f"Существ с типом {type} не нашлось")
        self.remove_creatures(elements)

    def search_creature_by_type(self, type):
        return list(filter(lambda x: x.type == type, self.creatures))

    def search_creature_by_name(self, name):
        return list(filter(lambda x: x.name == name, self.creatures))

    def remove_creatures(self, creatures):
        for c in creatures:
            if c not in self.creatures:
                self.logger.log(f"Существа {c} не нашлось")
            else:
                self.creatures.remove(c)

    def get_plants(self):
        return filter(lambda x: type(x) is Plant, self.creatures)

    def get_animals(self):
        return filter(lambda x: type(x) is Animal, self.creatures)

    def display(self):
        print("Растения:")
        for plant in self.get_plants():
            print("\t" + str(plant))
        print("Животные:")
        for animal in self.get_animals():
            print("\t" + str(animal))


if __name__ == '__main__':
    ecosystem = Ecosystem(Logger())

    trava = Plant("Трава", "Наземные", 10, [])
    baran = Animal("Баран", "Млекопитающее", 25, [trava])
    vodorosly = Plant("Водоросли", "Подводные", 15, [])
    mysh = Animal("Мышь", "Млекопитающее", 3, [])
    sova = Animal("Сова", "Птица", 8, [mysh])

    ecosystem.add_creature(trava)
    ecosystem.add_creature(vodorosly)
    ecosystem.add_creature(baran)
    ecosystem.add_creature(sova)
    ecosystem.add_creature(mysh)

    ecosystem.display()
    print("===========================================")

    db = Database("db.csv")
    db.save_ecosystem(ecosystem)
