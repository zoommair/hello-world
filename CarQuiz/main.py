# Quiz program to match interests to different cars

# ---Class Definitions---


class MyCar:
    def __init__(self, make, model, year, speed, weight, power, size, reliability, age, fun, agility, trunk, passenger, tech, price, unique, flashy, score):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.weight = weight
        self.power = power
        self.size = size
        self.reliability = reliability
        self.age = age
        self.fun = fun
        self.agility = agility
        self.trunk = trunk
        self.passenger = passenger
        self.tech = tech
        self.price = price
        self.unique = unique
        self.flashy = flashy
        self.score = score

    def add_score(self):
        self.score += 5
        # also try without "score" and just use self.score += 5

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_speed(self):
        return self.speed

    def get_weight(self):
        return self.weight

    def get_power(self):
        return self.power

    def get_size(self):
        return self.size

    def get_reliability(self):
        return self.reliability

    def get_age(self):
        return self.age

    def get_fun(self):
        return self.fun

    def get_agility(self):
        return self.agility

    def get_trunk(self):
        return self.trunk

    def get_passenger(self):
        return self.passenger

    def get_tech(self):
        return self.tech

    def get_price(self):
        return self.price

    def get_unique(self):
        return self.unique

    def get_flashy(self):
        return self.flashy

    def get_score(self):
        return self.score


# ---Function Definitions---


#def first_question():

#def second_question():

#def third_question():

#def fourth_question():

# ---Start of Program---

testcar = MyCar("BMW", "525i", "2001", 2, 3, 2, 4, 3, 3, 3, 3, 4, 5, 4, 2, 3, 2, 0)

print(testcar.score)

testcar.add_score()

print(testcar.make, testcar.model, testcar.year, testcar.score)