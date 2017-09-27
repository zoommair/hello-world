import os
import sys
import random

# Car Troubleshooter program will ask questions on car no-start
# Eventually add ability to troubleshoot running problems
# Also keep profile of user's car, input miles and condition, last oil change, last brake service, etc, & set reminders for future service

# Input symptoms and algorithm would match possible problem to solution; if solution doesn't work, go to next possible solution.



# ---Class Definitions
class MyCar:
    def __init__(self, fuseok,pumpok):
        self.fuseok = fuseok
        self.pumpok = pumpok

    def set_pump(self,pumpok):
        self.pumpok = pumpok

    def get_pump(self):
        return self.pumpok

# ---Global Functions
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
        print("Pump OK set to ", car.get_pump())
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
        #ecuDiag()
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

    elif x == 'd' or x == 'D':
        print("If Pump Ok is False, start with Fuel Pump Voltage Test")
        print("If Pump Ok is True, start with MAFS Check, Spark & compression, then Fuel Pressure")

    elif x == 'e' or x == 'E':
        print("Mafs check,  Spark & Compression, Fuel Pressure")

    elif x == 'f' or x == 'F':
        print("Awesome, exiting!")

    else:
        print("Come again?\n")
        turn_over()

def jumpstart():
    print("A: It still just clicks")  # will go to check_starter
    print("B: It does something else")  # goes back to turn_over()
    print("C: It Works!")  # exit function

def jumpstart2():
    print("A: It just clicks now")  # will go to check_starter
    print("B: Still not starting!")  # wil go to Fuel Pump Voltage if Pumpok false, MAFS Check, Fuel Pump Pressure check


# ---Start of Program---
car = MyCar(True, True)

print("Oh No! Your car isn't starting? That's ok, I'm here to help!\n")
print("Is the battery plugged in with absolutely no corrosion? \n")

check_corrosion(input("Type Yes or No and Enter"))

print("Insert the key and turn to first position, prime the fuel pump, and get the electronics on.\n")
print("Do you get power to everything and hear the fuel pump prime?")
print("Choices:")
print("A: I don't get any power.")
print("B: I get power, but I can't hear the fuel pump prime.")
print("C: I get power and can hear the fuel pump prime.\n")

second_question(input("Select the Best Answer "))



turn_over()

print("Congratulations! I hope this program helped you fix your car! If it didn't, well, I'm sorry, this is still in Alpha")
print("Support development of this app by leaving feedback. Thanks for using CarTroubleshooter 0.1a\n")

print("End of Line...")




# Did this fix the issue?
# If yes, go to ItWorks
# If yes, but another problem, Go to SecondQuestion
# If no, go to EcuDiag




# EcuDiag
# This one is tricky, you will need to trace the wires leading from the positive battery terminal to the ECU.
# IF you are uncomfortable with this, DO NOT PROCEED, have your car towed to a technician.
# If you are comfortable, trace the wires to the ECU and use the Voltmeter to see the ECU is getting power.

# Is the ECU getting power?
# If yes, Go to Replace ECU
# If no, Go to Replace wiring harness.

# Did this fix the issue?
# If Yes, Go to ItWorks
# If Yes, but another issue, go to SecondQuestion
# If No, go to SorryPrompt











# FuseNotice






# TapStarter








# JumpStart








# FullDiagnose











# GasDiagnose









# ElecDiagnose









# ItWorks






# SorryPrompt