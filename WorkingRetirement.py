bob = True
while bob:
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
                ageGoalMet = savingsGoal/(annualSalary*percentageSaved/100)+currentAge

                # You can assume death at 100 years (therefore, indicate if the savings goal is not met).
                if ageGoalMet > 99:
                    print('Savings goal not met... Happy 100th?')
                    bob = False
                else:
                    print('You will meet your savings goal at the age of: ', ageGoalMet)
                    bob = False
            else:
                print("Savings > 0!")
        else:
            print("annual salary > 0!")
    else:
        print("current age > 0!")

