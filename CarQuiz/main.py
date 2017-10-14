# Quiz program to match interests to different cars


# ---CLASS DEFINITIONS--------------

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


# ---GLOBAL FUNCTION DEFINITIONS------------------

def print_list():
    for i in range(car_num):
        print(car_list[i].make, ",", car_list[i].model, ",", car_list[i].score)
        i += 1
    print('')


# --- Attribute Modifiers ---
'''
#This code is unusable, but leaving for future concept. How can I reuse same code to modify different attributes?
def question_modifier(x, mod):
    if x == '1':
        for i in range(car_num):
            if car_list[i].mod == 1:
                car_list[i].score += 5
            elif car_list[i].mod <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].mod == 1:
                car_list[i].score += 3
            elif car_list[i].mod <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].mod == 5:
                car_list[i].score += 3
            elif car_list[i].mod >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].mod == 5:
                car_list[i].score += 5
            elif car_list[i].mod >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')
'''


def speed_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].speed == 1:
                car_list[i].score += 5
            elif car_list[i].speed <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].speed == 1:
                car_list[i].score += 3
            elif car_list[i].speed <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].speed == 5:
                car_list[i].score += 3
            elif car_list[i].speed >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].speed == 5:
                car_list[i].score += 5
            elif car_list[i].speed >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def speed_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].speed == 1:
                car_list[i].score += 5
            elif car_list[i].speed <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].speed == 1:
                car_list[i].score += 3
            elif car_list[i].speed <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].speed == 5:
                car_list[i].score += 3
            elif car_list[i].speed >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].speed == 5:
                car_list[i].score += 5
            elif car_list[i].speed >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def weight_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].weight == 1:
                car_list[i].score += 5
            elif car_list[i].weight <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].weight == 1:
                car_list[i].score += 3
            elif car_list[i].weight <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].weight == 5:
                car_list[i].score += 3
            elif car_list[i].weight >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].weight == 5:
                car_list[i].score += 5
            elif car_list[i].weight >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def weight_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].weight == 1:
                car_list[i].score += 5
            elif car_list[i].weight <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].weight == 1:
                car_list[i].score += 3
            elif car_list[i].weight <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].weight == 5:
                car_list[i].score += 3
            elif car_list[i].weight >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].weight == 5:
                car_list[i].score += 5
            elif car_list[i].weight >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def power_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].power == 1:
                car_list[i].score += 5
            elif car_list[i].power <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].power == 1:
                car_list[i].score += 3
            elif car_list[i].power <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].power == 5:
                car_list[i].score += 3
            elif car_list[i].power >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].power == 5:
                car_list[i].score += 5
            elif car_list[i].power >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def power_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].power == 1:
                car_list[i].score += 5
            elif car_list[i].power <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].power == 1:
                car_list[i].score += 3
            elif car_list[i].power <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].power == 5:
                car_list[i].score += 3
            elif car_list[i].power >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].power == 5:
                car_list[i].score += 5
            elif car_list[i].power >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def size_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].size == 1:
                car_list[i].score += 5
            elif car_list[i].size <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].size == 1:
                car_list[i].score += 3
            elif car_list[i].size <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].size == 5:
                car_list[i].score += 3
            elif car_list[i].size >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].size == 5:
                car_list[i].score += 5
            elif car_list[i].size >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def size_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].size == 1:
                car_list[i].score += 5
            elif car_list[i].size <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].size == 1:
                car_list[i].score += 3
            elif car_list[i].size <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].size == 5:
                car_list[i].score += 3
            elif car_list[i].size >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].size == 5:
                car_list[i].score += 5
            elif car_list[i].size >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def reliability_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].reliability == 1:
                car_list[i].score += 5
            elif car_list[i].reliability <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].reliability == 1:
                car_list[i].score += 3
            elif car_list[i].reliability <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].reliability == 5:
                car_list[i].score += 3
            elif car_list[i].reliability >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].reliability == 5:
                car_list[i].score += 5
            elif car_list[i].reliability >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def reliability_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].reliability == 1:
                car_list[i].score += 5
            elif car_list[i].reliability <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].reliability == 1:
                car_list[i].score += 3
            elif car_list[i].reliability <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].reliability == 5:
                car_list[i].score += 3
            elif car_list[i].reliability >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].reliability == 5:
                car_list[i].score += 5
            elif car_list[i].reliability >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def age_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].age == 1:
                car_list[i].score += 5
            elif car_list[i].age <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].age == 1:
                car_list[i].score += 3
            elif car_list[i].age <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].age == 5:
                car_list[i].score += 3
            elif car_list[i].age >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].age == 5:
                car_list[i].score += 5
            elif car_list[i].age >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def age_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].age == 1:
                car_list[i].score += 5
            elif car_list[i].age <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].age == 1:
                car_list[i].score += 3
            elif car_list[i].age <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].age == 5:
                car_list[i].score += 3
            elif car_list[i].age >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].age == 5:
                car_list[i].score += 5
            elif car_list[i].age >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def fun_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].fun == 1:
                car_list[i].score += 5
            elif car_list[i].fun <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].fun == 1:
                car_list[i].score += 3
            elif car_list[i].fun <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].fun == 5:
                car_list[i].score += 3
            elif car_list[i].fun >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].fun == 5:
                car_list[i].score += 5
            elif car_list[i].fun >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def fun_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].fun == 1:
                car_list[i].score += 5
            elif car_list[i].fun <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].fun == 1:
                car_list[i].score += 3
            elif car_list[i].fun <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].fun == 5:
                car_list[i].score += 3
            elif car_list[i].fun >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].fun == 5:
                car_list[i].score += 5
            elif car_list[i].fun >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def agility_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].agility == 1:
                car_list[i].score += 5
            elif car_list[i].agility <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].agility == 1:
                car_list[i].score += 3
            elif car_list[i].agility <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].agility == 5:
                car_list[i].score += 3
            elif car_list[i].agility >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].agility == 5:
                car_list[i].score += 5
            elif car_list[i].agility >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def agility_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].agility == 1:
                car_list[i].score += 5
            elif car_list[i].agility <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].agility == 1:
                car_list[i].score += 3
            elif car_list[i].agility <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].agility == 5:
                car_list[i].score += 3
            elif car_list[i].agility >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].agility == 5:
                car_list[i].score += 5
            elif car_list[i].agility >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def trunk_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].trunk == 1:
                car_list[i].score += 5
            elif car_list[i].trunk <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].trunk == 1:
                car_list[i].score += 3
            elif car_list[i].trunk <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].trunk == 5:
                car_list[i].score += 3
            elif car_list[i].trunk >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].trunk == 5:
                car_list[i].score += 5
            elif car_list[i].trunk >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def trunk_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].trunk == 1:
                car_list[i].score += 5
            elif car_list[i].trunk <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].trunk == 1:
                car_list[i].score += 3
            elif car_list[i].trunk <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].trunk == 5:
                car_list[i].score += 3
            elif car_list[i].trunk >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].trunk == 5:
                car_list[i].score += 5
            elif car_list[i].trunk >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def passenger_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].passenger == 1:
                car_list[i].score += 5
            elif car_list[i].passenger <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].passenger == 1:
                car_list[i].score += 3
            elif car_list[i].passenger <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].passenger == 5:
                car_list[i].score += 3
            elif car_list[i].passenger >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].passenger == 5:
                car_list[i].score += 5
            elif car_list[i].passenger >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def passenger_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].passenger == 1:
                car_list[i].score += 5
            elif car_list[i].passenger <= 2:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].passenger == 5:
                car_list[i].score += 3
            elif car_list[i].passenger <= 2:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].passenger == 5:
                car_list[i].score += 3
            elif car_list[i].passenger >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].passenger == 5:
                car_list[i].score += 5
            elif car_list[i].passenger >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def tech_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].tech == 1:
                car_list[i].score += 5
            elif car_list[i].tech <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].tech == 1:
                car_list[i].score += 3
            elif car_list[i].tech <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].tech == 5:
                car_list[i].score += 3
            elif car_list[i].tech >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].tech == 5:
                car_list[i].score += 5
            elif car_list[i].tech >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def tech_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].tech == 1:
                car_list[i].score += 5
            elif car_list[i].tech <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].tech == 1:
                car_list[i].score += 3
            elif car_list[i].tech <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].tech == 5:
                car_list[i].score += 3
            elif car_list[i].tech >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].tech == 5:
                car_list[i].score += 5
            elif car_list[i].tech >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def price_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].price == 1:
                car_list[i].score += 5
            elif car_list[i].price <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].price == 1:
                car_list[i].score += 3
            elif car_list[i].price <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].price == 5:
                car_list[i].score += 3
            elif car_list[i].price >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].price == 5:
                car_list[i].score += 5
            elif car_list[i].price >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def price_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].price == 1:
                car_list[i].score += 5
            elif car_list[i].price <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].price == 1:
                car_list[i].score += 3
            elif car_list[i].price <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].price == 5:
                car_list[i].score += 3
            elif car_list[i].price >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].price == 5:
                car_list[i].score += 5
            elif car_list[i].price >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def unique_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].unique == 1:
                car_list[i].score += 5
            elif car_list[i].unique <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].unique == 1:
                car_list[i].score += 3
            elif car_list[i].unique <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].unique == 5:
                car_list[i].score += 3
            elif car_list[i].unique >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].unique == 5:
                car_list[i].score += 5
            elif car_list[i].unique >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def unique_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].unique == 1:
                car_list[i].score += 5
            elif car_list[i].unique <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].unique == 1:
                car_list[i].score += 3
            elif car_list[i].unique <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].unique == 5:
                car_list[i].score += 3
            elif car_list[i].unique >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].unique == 5:
                car_list[i].score += 5
            elif car_list[i].unique >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def flashy_question(x):
    if x == '1':
        for i in range(car_num):
            if car_list[i].flashy == 1:
                car_list[i].score += 5
            elif car_list[i].flashy <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '2':
        for i in range(car_num):
            if car_list[i].flashy == 1:
                car_list[i].score += 3
            elif car_list[i].flashy <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '4':
        for i in range(car_num):
            if car_list[i].flashy == 5:
                car_list[i].score += 3
            elif car_list[i].flashy >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '5':
        for i in range(car_num):
            if car_list[i].flashy == 5:
                car_list[i].score += 5
            elif car_list[i].flashy >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


def flashy_question_neg(x):
    if x == '5':
        for i in range(car_num):
            if car_list[i].flashy == 1:
                car_list[i].score += 5
            elif car_list[i].flashy <= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    elif x == '4':
        for i in range(car_num):
            if car_list[i].flashy == 1:
                car_list[i].score += 3
            elif car_list[i].flashy <= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '3':
        pass

    elif x == '2':
        for i in range(car_num):
            if car_list[i].flashy == 5:
                car_list[i].score += 3
            elif car_list[i].flashy >= 3:
                car_list[i].score += 1
            else:
                pass
            i += 1

    elif x == '1':
        for i in range(car_num):
            if car_list[i].flashy == 5:
                car_list[i].score += 5
            elif car_list[i].flashy >= 3:
                car_list[i].score += 3
            else:
                pass
            i += 1

    else:
        print('Not a valid Entry...')


# --- QUESTION DEFINITIONS ---

def first_question():
    print("Rate how you like the following statement...")
    print("\"I like to go fast!\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree\n")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        speed_question(x)
    else:
        print("Not a Valid Entry...\n")
        first_question()


def second_question():
    print("\"I like to drive alone.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        passenger_question_neg(x)
    else:
        print("Not a Valid Entry... \n")
        second_question()


def third_question():
    print("\"I want something that won't give me too many problems.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        reliability_question(x)
    else:
        print("Not a valid Entry...\n")
        third_question()


def fourth_question():
    print("\"I want to be able to take lots of stuff with me.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        trunk_question(x)
    else:
        print("Not a Valid Entry...\n")
        fourth_question()


def fifth_question():
    print("\"I like to feel large and in charge on the road!\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        size_question(x)
    else:
        print("Not a Valid Entry...\n")
        fifth_question()


def sixth_question():
    print("\"I would love to own an older or classic car.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        age_question(x)
    else:
        print("Not a Valid Entry...\n")
        sixth_question()


def seventh_question():
    print("\"When I go out, I want people to notice me.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        flashy_question(x)
    else:
        print("Not a Valid Entry...\n")
        seventh_question()


def eighth_question():
    print("\"I want my car to be something not many people have.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        unique_question(x)
    else:
        print("Not a Valid Entry...\n")
        eighth_question()


def ninth_question():
    print("\"I don't mind a project car that needs a lot of maintenance, I can repair it!\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        reliability_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        ninth_question()


def question_10():
    print("\"I want something that doesn't cost a lot.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        price_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        question_10()


def question_11():
    print("\"Handling is more important to me than speed or power.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        agility_question(x)
        power_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        question_11()


def question_12():
    print("\"I want something small and fun!\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        size_question_neg(x)
        fun_question(x)
    else:
        print("Not a Valid Entry...\n")
        question_12()


def question_13():
    print("\"I want something newer with more up to date technology.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        tech_question(x)
        age_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        question_13()


def question_14():
    print("\"There's no replacement for displacement! Bigger the motor the better!\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        weight_question(x)
        power_question(x)
    else:
        print("Not a Valid Entry...\n")
        question_14()


def question_15():
    print("\"I want a sleeper, something discreet and unassuming.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        unique_question_neg(x)
        flashy_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        question_15()


def question_16():
    print("\"I need something more sensible, nothing racy.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        speed_question_neg(x)
        fun_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        question_16()


def question_17():
    print("\"Lightweight mod! Lightweight and simple is the way to go, none of this new technology.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        weight_question_neg(x)
        tech_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        question_17()


def question_18():
    print("\"Price is no object! I might even just have someone else drive me around in it.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        price_question(x)
        agility_question_neg(x)
    else:
        print("Not a Valid Entry...\n")
        question_18()


def question_19():
    print("\"I need something I can take my friends or family around in.\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        passenger_question(x)
    else:
        print("Not a Valid Entry...\n")
        question_19()


def question_20():
    print("\"I don't mind having no trunk space, it's supposed to be a fun car anyway!\"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        trunk_question_neg(x)
        fun_question(x)
    else:
        print("Not a Valid Entry...\n")
        question_20()


def question_21():
    print("\" \"")
    print("1: Strongly Disagree   2: Disagree   3: Neutral   4: Agree   5: Strongly Agree")

    x = input()
    if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        pass
    else:
        print("Not a Valid Entry...\n")
        question_21()


# ---START OF PROGRAM-----------------------

# -speed, weight, power, size, reliability, age, fun, agility, trunk, passenger, tech, price, unique, flashy, score

car1 = MyCar("Nissan", "GTR R34", "1990", 4, 4, 4, 4, 3, 3, 3, 2, 4, 4, 4, 4, 4, 3, 0)
car2 = MyCar("Mazda", "Miata", "1990", 2, 1, 1, 1, 4, 4, 5, 5, 1, 1, 1, 2, 3, 3, 0)
car3 = MyCar("Toyota", "Trueno AE86", "1990", 2, 1, 1, 2, 4, 5, 5, 5, 4, 3, 1, 4, 5, 2, 0)
car4 = MyCar("Mazda", "Rx-7", "1990", 3, 2, 3, 3, 2, 4, 4, 4, 3, 1, 2, 4, 5, 4, 0)
car5 = MyCar("Honda", "Civic", "1990", 1, 1, 1, 2, 5, 3, 2, 3, 4, 3, 2, 1, 1, 1, 0)
car6 = MyCar("Honda", "S2000", "2000", 4, 2, 3, 2, 4, 2, 5, 5, 1, 1, 2, 3, 3, 4, 0)
car7 = MyCar("Honda", "Civic R", "2000", 3, 2, 3, 2, 4, 2, 3, 4, 4, 3, 2, 3, 3, 2, 0)
car8 = MyCar("Nissan", "240sx", "1990", 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 2, 0)
car9 = MyCar("Toyota", "Supra", "2000", 4, 4, 4, 3, 3, 3, 4, 3, 2, 1, 3, 4, 4, 4, 0)
car10 = MyCar("Subaru", "WRX STi", "2000", 4, 3, 4, 2, 4, 2, 3, 4, 3, 3, 4, 3, 3, 4, 0)
car11 = MyCar("Mitsubishi", "Evo", "2000", 4, 3, 4, 2, 3, 2, 3, 4, 3, 3, 4, 3, 3, 3, 0)

car_list = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11]

car_num = len(car_list)  # number of cars


print_list()

first_question()

print_list()

second_question()

print_list()

third_question()

print_list()

fourth_question()

print_list()

fifth_question()

print_list()

sixth_question()

print_list()

seventh_question()

print_list()

eighth_question()

print_list()

ninth_question()

print_list()

question_10()

print_list()

question_11()

print_list()

question_12()

print_list()

question_13()

print_list()

question_14()

print_list()

question_15()

print_list()

question_16()

print_list()

question_17()

print_list()

question_18()

print_list()

question_19()

print_list()

question_20()

print_list()

print('')
input("End of Line...")
