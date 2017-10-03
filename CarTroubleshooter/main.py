import os
import sys
import random

# Car Troubleshooter program will ask questions on car no-start
# Eventually add ability to troubleshoot running problems
# Also keep profile of user's car, input miles and condition, last oil change, last brake service, etc, & set reminders for future service

# Input symptoms and algorithm would match possible problem to solution; if solution doesn't work, go to next possible solution.
# Input tools available to use, so as to only run tests according to what tools are available


# ---Class Definitions

class MyCar:
    def __init__(self, pumpok, carFixed):
        self.pumpok = pumpok
        self.carFixed = carFixed

    def set_pump(self, pumpok):
        self.pumpok = pumpok

    def get_pump(self):
        return self.pumpok

    def ask_fixed(self):
        x = input("Does it work now? Yes or No?\n")
        if x.lower() == 'y':
            car.carFixed = True
            print("Awesome! We're done here!\n")
        elif x.lower() == 'n':
            print("That's too bad! Next test then...\n")
        else:
            print("I'm sorry, I don't know that input...\n")
            ask_fixed()


# add My Person class with attributes for tools like hasVoltmeter, hasSparktester, hasComptester, hasFueltester
# run tests only if equipped with these tools, otherwise offer alternative

class MyPerson:
    def __init__(self, hasVolt, hasSpark, hasComp, hasFuel):
        self.hasVolt = hasVolt
        self.hasSpark = hasSpark
        self.hasComp = hasComp
        self.hasFuel = hasFuel


# ---Global Functions

def check_tools():
    print("Firstly, let's take account of what tools you have...\n")

    x = input("Do you have a Voltmeter?\n")
    if x.lower() == 'y':
        me.hasVolt = True
        print("Voltmeter set to ", me.hasVolt, "\n")
    else:
        print("Voltmeter set to ", me.hasVolt, "\n")
    x = input("Do you have a Spark Plug Wire Tester?\n")
    if x.lower() == 'y':
        me.hasSpark = True
        print("Spark Plug Wire Tester set to ", me.hasSpark, "\n")
    else:
        print("Spark Plug Wire Tester set to ", me.hasSpark, "\n")
    x = input("Do you have a Compression Tester?\n")
    if x.lower() == 'y':
        me.hasComp = True
        print("Compression Tester set to ", me.hasComp, "\n")
    else:
        print("Compression Tester set to ", me.hasComp, "\n")
    x = input("Do you have a Fuel Pressure Tester\n")
    if x.lower() == 'y':
        me.hasFuel = True
        print("Fuel Pressure Tester set to ", me.hasFuel, "\n")
    else:
        print("Fuel Pressure Tester set to ", me.hasFuel, "\n")

    print("Excellent, moving on!\n")


def check_corrosion(answer):
    if answer == 'no' or answer == 'No' or answer == 'n' or answer == 'N':
        print("That could be a problem! Make a paste out of baking soda and distilled water and apply.\n")
        check_corrosion(input("Is the Battery now free of Corrosion?\n"))

    elif answer == 'yes' or answer == 'Yes' or answer == 'y' or answer == 'Y':
        print("Excellent! Moving on then...\n")
    else:
        print("Sorry, I don't know that input, please try again.\n")
        check_corrosion(input("Is the Battery free of Corrosion?\n"))


def second_question(answer):
    if answer == 'a' or answer == 'A':
        print("Bummer!\n")
        no_power_troubleshoot()
    elif answer == 'b' or answer == 'B':
        print("No worries, we'll come back to this later.\n")
        car.set_pump(False)
        print("Pump OK set to ", car.get_pump(), "\n")
    elif answer == 'c' or answer == 'C':
        print("Great! Moving on!\n")
    else:
        print("I'm sorry, what was that?\n")
        second_question(input("Please enter selection again...\n"))


def no_power_troubleshoot():
    print("If you are without any power, Do the following")
    print("- Check the Fuses")
    print("- Double-check the connection to the battery")
    print("- Test the battery or replace battery with another one handy.")
    print("- Battery should show 12V-14V, if not, replace.\n")
    print("Do you have power now?\n")
    x = input("Press Y or N\n")

    if x == 'y' or x == 'Y':
        print("Try starting the car now!\n")
        y = input("Did it work now? Y or N... \n")
        if y == 'y' or y == 'Y':
            car.carFixed = True
            print("Great! We're done here!\n")
        elif y == 'n' or y == 'N':
            print("Ok, let's go back\n")
            print("Insert the key and turn to first position, prime the fuel pump, and get the electronics on.\n")
            print("Do you get power to everything and hear the fuel pump prime?")
            print("Choices:")
            print("A: I don't get any power.")
            print("B: I get power, but I can't hear the fuel pump prime.")
            print("C: I get power and can hear the fuel pump prime.\n")
            second_question(input("Select the Best Answer \n"))

        else:
            print("Come Again?\n")
            no_power_troubleshoot()
    elif x == 'n' or x == 'N':
        print("This one's tricky!\n")
        ecuDiag()
    else:
        print("Come again?\n")
        no_power_troubleshoot()


def turn_over():
    print("Try starting the car now. What happened?\n")
    print("A: It just clicked, but nothing else. ")
    print("B: Engine tries to turn over, but weakly.")
    print("C: It turns over and tries to start, but doesn't.")
    print("D: It turns over and starts for a moment then dies!")
    print("E: It starts, but dies after a while")
    print("F: It starts and works!\n")

    x = input("Please Select the best option...\n")

    if x == 'a' or x == 'A':
        print("Check the Fuses, Tap the starter, then Jumpstart\n")
        jumpstart()

    elif x == 'b' or x == 'B':
        print("Check the Fuses, then JumpStart\n")
        jumpstart2()

    elif x == 'c' or x == 'C':
        print("Check the Fuses, If Pump Ok is false, start with Fuel Pump voltage test")
        print("If Pump Ok is true, go right into MAFS Check, Fuel Pressure check, then Spark, and compression test")

        while car.pumpok is False:
            fuel_pump_volt()
            break

        mafs_test()  # MAFS check
        fuel_pump_press()  # Fuel Pressure
        spark_test()  # Spark Test
        comp_test()  # Compression test

    elif x == 'd' or x == 'D':
        print("If Pump Ok is False, start with Fuel Pump Voltage Test")
        print("If Pump Ok is True, start with MAFS Check, Spark & compression, then Fuel Pressure")

        while car.pumpok is False:
            fuel_pump_volt()
            break

        batt_test()  # Battery Test
        mafs_test()  # MAFS Check
        spark_test()  # Spark Test
        comp_test()  # Compression
        fuel_pump_press()  # Fuel Pressure

    elif x == 'e' or x == 'E':
        print("Mafs check,  Spark & Compression, Fuel Pressure")

        batt_test()  # Battery Test
        mafs_test()  # MAFS check
        alt_test()  # Alternator
        spark_test()  # Spark Test
        comp_test()  # Compression
        fuel_pump_press()  # Fuel Pressure

    elif x == 'f' or x == 'F':
        print("Awesome, exiting!\n")
        car.carFixed = True

    else:
        print("Come again?\n")
        turn_over()


def jumpstart():
    print("A: It still just clicks")
    print("B: It does something else")
    print("C: It Works!\n")

    x = input("Please Choose: ")
    if x.lower() == 'a':
        print("Looks like it's the starter, let's check that out. \n")
        check_starter()

    elif x.lower() == 'b':
        print("Ok, let's go back then...\n")
        turn_over()

    elif x.lower() == 'c':
        print("Awesome!!! \n")

    else:
        print("Come again?\n")
        jumpstart()


def jumpstart2():
    print("A: It just clicks now")
    print("B: Still not starting!")
    print("C: It Works!")

    x = input("Please Choose: ")
    if x.lower() == 'a':
        print("Looks like it's the starter, let's check that out. \n")
        check_starter()

    elif x.lower() == 'b':
        print("Oh No! Let's check things out then...\n")

        while car.pumpok is False:
            fuel_pump_volt()
            break

        mafs_test()  # Mafs check
        fuel_pump_press()  # Fuel Pressure
        spark_test()  # Spark
        comp_test()  # Compression

    elif x.lower() == 'c':
        print("Awesome!!! \n")

    else:
        print("Come again?\n")
        jumpstart2()


def ecuDiag():
    print("It might be an ECU issue.")
    print("Check ECU...\n")

    print("This one is tricky, you will need the wiring diagram from your service manual.")
    print("IF you are uncomfortable with this, DO NOT PROCEED, have your car towed to a technician.")
    print("If you are comfortable, follow the wiring diagram, from the battery to the ECU.\n"
          "Use your service manual to find where the ECU is located, sometimes under the glove box\n"
          "Unplug the ECU and use the voltmeter to test the pin that provides power to the ECU.\n\n"
          "Is the ECU getting power?\n")
    x = input("Y or N")
    if x.lower() == 'y':
        print("Replace ECU\n")
        replace_ecu()
    elif x.lower() == 'n':
        print("Replace Harness\n")
        replace_harness()
    else:
        print("Come again?\n")
        ecuDiag()

    print("Do you have power now?\n")

    x = input("Y or N\n")
    while True:
        if x.lower() == 'y':
            print("Awesome! Let's try starting!\n")
            car.pumpok = False
            turn_over()
            break
        elif x.lower() == 'n':
            print("I'm sorry, if there's still no power, I'm at a loss of words...\n"
                  "If the fuses, battery, ecu, and wiring harness are all OK, then you should have at least electricity.\n"
                  "I'm Sorry, but looks like We're out of the scope of what I can offer at the moment....\n")
            car.carFixed = True
            break
        print("Come again big fudge?\n")
        x = input("Y or N\n")

    input("Exiting ECU Diag - Press Enter to continue...\n")


def check_starter():
    print("Might be the Starter.")
    print("Check Starter...\n")

    car.ask_fixed()

    if car.carFixed is False:
        print("If all it does it click when you have check the starter, then there is something else wrong...\n")
        print("It was most likely the starter, but if you would like to continue testing other components, it might\n"
              "be the ECU.")
        x = input("Would you like to try diagnosing the ECU?\n")
        while True:
            if x.lower() == 'y':
                ecuDiag()
                break
            elif x.lower() == 'n':
                print("Ok, Exiting then...\n")
                break

            print("Come again big fudge?\n")
            x = input("Y or N?\n")

    else:
        input("Exiting Check_Starter function... Press Enter to Continue")


def fuel_pump_volt():
    print("Might be the Fuel Pump.")
    print("Check Fuel Pump Voltage...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def batt_test():
    print("Might be the Battery.")
    print("Check the Battery...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def mafs_test():
    print("Might be the MAF sensor.")
    print("Check the MAF sensor...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def alt_test():
    print("Might be the alternator.")
    print("Check the Alternator...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def spark_test():
    print("Might be the Spark Plugs.")
    print("Check the Spark Plugs...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def comp_test():
    print("Might be low compression.")
    print("Check Cylinder Compression...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def fuel_pump_press():
    print("Might be low fuel pressure or clogged fuel filter.")
    print("Check the Fuel Pressure...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def replace_harness():
    print("Might be the Wiring Harness.")
    print("Replace the Wiring Harness...\n")
    car.ask_fixed()
    input("Press Enter to continue...")

def replace_ecu():
    print("Might be the ECU.")
    print("Replace the ECU...\n")
    car.ask_fixed()
    input("Press Enter to continue...")


# ---Start of Program---

me = MyPerson(False, False, False, False)
car = MyCar(True, False)

print("Oh No! Your car isn't starting? That's ok, I'm here to help!\n")
check_tools()

print("Is the battery plugged in with absolutely no corrosion? \n")

check_corrosion(input("Type Yes or No, then Enter \n"))

print("Insert the key and turn to first position, prime the fuel pump, and get the electronics on.\n")
print("Do you get power to everything and hear the fuel pump prime?")
print("Choices:")
print("A: I don't get any power.")
print("B: I get power, but I can't hear the fuel pump prime.")
print("C: I get power and can hear the fuel pump prime.\n")

second_question(input("Select the Best Answer \n"))


while car.carFixed is False:
    turn_over()
    break

print("Congratulations! I hope this program helped you fix your car!")
print("If it didn't, oh well, I'm sorry, this app is still in early stages.\n")
print("Support development of this app by leaving feedback. Thanks for using CarTroubleshooter 0.2a\n\n")

print("End of Line...")
input()






