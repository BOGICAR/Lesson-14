import random


class House:
    def __init__(self, _id):
        self.amount_people = random.randint(1, 100)
        self.id = _id


class Street:
    def __init__(self, _id):
        self.list_of_houses = []
        self.create_houses()
        self.id = _id

    def create_houses(self):
        for i in range(random.randint(5, 20)):
            self.list_of_houses.append(House(i))


class City:
    def __init__(self):
        self.list_of_streets = []
        self.create_streets()

    def create_streets(self):
        for i in range(random.randint(3, 10)):
            self.list_of_streets.append(Street(i))
        with open('city_1.txt', 'w') as file:
            self.population = 0
            file.write(f'Streat\t     House\t     Population\n')
            for street in self.list_of_streets:
                for house in street.list_of_houses:
                    file.write(f'Streat {street.id}\t House {house.id}\t {house.amount_people}\n')
                    self.population += house.amount_people

    def population(self):
        return self.population


voznesensk = City()
print(voznesensk.population)
