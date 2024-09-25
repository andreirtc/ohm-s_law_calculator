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
    def get_input_values(self):
        try:
            if self.choice.lower() == "voltage":
                self.current = float(input("Enter the current in amperes: "))
                self.resistance = float(input("Enter the resistance in ohms: "))
            elif self.choice.lower() == "current":
                self.voltage = float(input("Enter the voltage in volts: "))
                self.resistance = float(input("Enter the resistance in ohms: "))
            elif self.choice.lower() == "resistance":
                self.voltage = float(input("Enter the voltage in volts: "))
                self.current = float(input("Enter the current in amperes: "))
            else:
                print("Invalid choice. Please choose either Voltage, Current, or Resistance.")
        except ValueError:
            print("Invalid input. Please enter a number.")
# 3. Calculate their input using Ohm's Law and display the result, while alsong considering cases where division by zero might occcur.
    def calculate_result(self):
        try:
            if self.choice.lower() == "voltage":
                self.voltage = self.current * self.resistance
                print("The voltage is", self.voltage, "volts")
            elif self.choice.lower() == "current":
                if self.resistance == 0:
                    raise ZeroDivisionError
                self.current = self.voltage / self.resistance
                print("The current is", self.current, "amperes")
            elif self.choice.lower() == "resistance":
                if self.current == 0:
                    raise ZeroDivisionError
                self.resistance = self.voltage / self.current
                print("The resistance is", self.resistance, "ohms")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
# 4. Call the functions and run the program
    def run(self):
        self.get_user_choice()
        self.get_input_values()
        self.calculate_result()

calculator = OhmsLawCalculator()
calculator.run()
