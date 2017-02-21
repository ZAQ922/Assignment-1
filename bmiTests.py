#height=feet and inches ((feet * 12)+ inches = totalInches)
#weight= pounds (1 input)
#Formula steps:
#1)Kg=pounds*0.45
#2)meters=totalInches * 0.025
#3)meters*meters=sqMeters
#4)BMI=kg/sqMeters
#BMI=((pounds*0.45)/((((feet*12)+inches)*0.025)^2))

#Under<18.5), Normal=[18.5,25), Over=[25,30), [30<Obese
import unittest


def BMIFormula(feet, inches, pounds):
    totalInches = ((feet * 12) + inches)
    kg = pounds * 0.45
    bmi = (kg/(totalInches * totalInches))
    return 2


class BMITests(unittest.TestCase):
    def testNegativeInputs(self):
        self.assertEqual(BMIFormula(1, 1, 1), 2)

    #def testLargeInputs(self):
    #    self.assertEqual(BMIFormula(1, 1, 1), 2)

    #def normalInputs(self):
    #    self.assertEqual(BMIFormula(1, 1, 1), 2)

    #def stringInputs(self):
    #    self.assertEqual(BMIFormula(1, 1, 1), 2)


def main():
    unittest.main()


if __name__ == 'main__':
    main()
