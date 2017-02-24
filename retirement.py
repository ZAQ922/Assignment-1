def calculateAgeGoalMet(savGl, annSal, perSav, curAge):
    return (savGl / (annSal * perSav / 100) + curAge)

def agePositive(curAge):
    if curAge >0:
        return True
    else:
        return False

def salPositive(annSal):
    if annSal >0:
        return True
    else:
        return False

def perSavPositive(perSav):
    if perSav >0:
        return True
    else:
        return False

def savGlPositive(savGl):
    if savGl >0:
        return True
    else:
        return False



# Input user's current age
currentAge = input('Enter your current age: ')
currentAge = int(currentAge)

# annual salary
annualSalary = input('Enter your annual salary: ')
annualSalary = int(annualSalary)

# percentage saved (savings matched by employer - so double amount saved)
percentageSaved = input('Enter your percentage saved as an integer value: ')

percentageSaved = int(percentageSaved)
percentageSaved *= 2

# Input desired retirement savings goal
savingsGoal = input('Enter your savings goal: ')
savingsGoal = int(savingsGoal)

# Output what age savings goal will be met.
ageGoalMet = calculateAgeGoalMet(savingsGoal, annualSalary, percentageSaved, currentAge)

# You can assume death at 100 years (therefore, indicate if the savings goal is not met).
if(ageGoalMet>99):
    print('Savings goal not met... Happy 100th?')
else:
    print('You will meet your savings goal at the age of: ', ageGoalMet)

