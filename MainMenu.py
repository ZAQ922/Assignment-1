import unittest
from math import sqrt


class main():
    def mainMenu(self):
        print('1  :   BMI Calculator')
        print('2  :   Retirement Calculator')
        print('3  :   Distance Formula')
        print('4  :   Email Verifier')
        """while loop for continual menu options?"""
        try:
            choice = int(input("Select an application number: "))
        except ValueError:
            print('What you input was not an integer!')
            return 0
        if (isinstance(choice, int)):
            if (1 <= choice <= 4):
                if choice == 1:
                    bob = True
                    feet = 0
                    inches = 0
                    pounds = 0
                    while bob:
                        try:
                            feet = int(input("Please input Feet: "))
                        except ValueError:
                            print('Feet must be an Integer!')
                        if (isinstance(feet, int) and (0 < feet <= 10)):
                            try:
                                inches = int(input("Please input Inches: "))
                            except ValueError:
                                print('Inches must be an Integer!')
                            if (isinstance(inches, int) and (0 <= inches < 12)):
                                try:
                                    pounds = int(input("Please input Pounds: "))
                                except ValueError:
                                    print('Pounds must be an Integer')
                                if (isinstance(pounds, int) and (0 < pounds <= 1000)):
                                    kg = pounds * 0.45
                                    totalInches = ((feet * 12) + inches)
                                    meters = totalInches * 0.025
                                    bmi = round((kg/(meters * meters)), 1)
                                    print('BMI = ', bmi)
                                    if(bmi < 0):
                                        print('BMI is a negative number')
                                        bob = False
                                    if(0 <= bmi < 18.5):
                                        print('Underweight')
                                        bob = False
                                    if(18.5 <= bmi < 25):
                                        print('Normal')
                                        bob = False
                                    if(25 <= bmi < 30):
                                        print('Overweight')
                                        bob = False
                                    if(30 <= bmi):
                                        print('Obese')
                                        bob = False
                                    input("Press any key to exit")
                                else:
                                    print('0 < Pounds <= 1000!')
                            else:
                                print('0 <= Inches < 12!')
                        else:
                            print('0 < Feet <= 10!')

                if choice == 2:
                    print(choice, ": Retirement chosen")

                    frank = True
                    while frank:
                        # Input user's current age
                        currentAge = input('Enter your current age: ')
                        currentAge = int(currentAge)
                        if currentAge > 0:
                            # annual salary
                            annualSalary = input('Enter your annual salary: ')
                            annualSalary = int(annualSalary)
                            if annualSalary > 0:
                                # percentage saved (savings matched by employer - so double amount saved)
                                percentageSaved = input('Enter your percentage saved as an integer value: ')
                                percentageSaved = int(percentageSaved)
                                percentageSaved *= 2
                                if percentageSaved > 0:
                                    # Input desired retirement savings goal
                                    savingsGoal = input('Enter your savings goal: ')
                                    savingsGoal = int(savingsGoal)

                                    # Output what age savings goal will be met.
                                    ageGoalMet = savingsGoal / (annualSalary * percentageSaved / 100) + currentAge

                                    # You can assume death at 100 years (therefore, indicate if the savings goal is not met).
                                    if ageGoalMet > 99:
                                        print('Savings goal not met... Happy 100th?')
                                        frank = False
                                    else:
                                        print('You will meet your savings goal at the age of: ', ageGoalMet)
                                        frank = False
                                else:
                                    print("Savings > 0!")
                            else:
                                print("annual salary > 0!")
                        else:
                            print("current age > 0!")


                if choice == 3:
                    print(choice, ": Distance chosen")
                    x1 = int(input("Enter x1: "))
                    y1 = int(input("Enter y1: "))
                    x2 = int(input("Enter x2: "))
                    y2 = int(input("Enter y2: "))
                    try:
                        print(sqrt(pow((x2-x1), 2) + pow((y2-y1), 2)))
                    except:
                        print("Please provide a proper input")
                    input("Press any key to exit")

                if choice == 4:
                    print(choice, ": Email chosen")
                    input("Press any key to exit")
            else:
                print('That number is not an option: 1, 2, 3, or 4')
                input("Press any key to exit")
        #Should never get here
        else:
            print('Something went wrong.')
            input("Press any key to exit")
        return 0


main().mainMenu()
