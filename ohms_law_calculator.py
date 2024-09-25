# 0. To have a more organized code, use OOP. First create a class and initialize instance variables needed for the program.
class OhmsLawCalculator:
    def __init__(self):
        self.choice = None
        self.current = None
        self.voltage = None
        self.resistance = None
# 1. Ask the user what they want to calculate: Voltage, Current, or Resistance
    def get_user_choice(self):
        self.choice = input("What do you want to calculate? Voltage, Current, or Resistance: ")
# 2. Based on their choice, prompt the user to input the appropriate values. 
# 3. Calculate their input using Ohm's Law and display the result, while alsong considering cases where division by zero might occcur.

