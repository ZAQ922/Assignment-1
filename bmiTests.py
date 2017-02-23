'''height=feet and inches ((feet * 12)+ inches = totalInches)
weight= pounds (1 input)
Formula steps:
1)Kg=pounds*0.45
2)meters=totalInches * 0.025
3)meters*meters=sqMeters
4)BMI=kg/sqMeters
BMI=((pounds*0.45)/((((feet*12)+inches)*0.025)^2))
Under<18.5), Normal=[18.5,25), Over=[25,30), [30<Obese
'''

import unittest


def BMIFormula(feet, inches, pounds):
    if (isinstance(feet, int) and (0 < feet <= 1000)):
        if (isinstance(inches, int) and (0 < inches < 12)):
            if (isinstance(pounds, int) and (0 < pounds <= 2000)):
                kg = pounds * 0.45
                totalInches = ((feet * 12) + inches)
                meters = totalInches * 0.025
                bmi = round((kg/(meters * meters)), 1)
                print('BMI = ', bmi)
                #BMI should never be below 0
                if(bmi < 0):
                    print('BMI is a negative number')
                if(0 <= bmi < 18.5):
                    print('Underweight')
                if(18.5 <= bmi < 25):
                    print('Normal')
                if(25 <= bmi < 30):
                    print('Overweight')
                if(30 <= bmi):
                    print('Obese')
            else:
                print('0 < Pounds <= 2000!')
        else:
            print('0 < Inches < 12!')
    else:
        print('0 < Feet <= 1000!')
    return 2


class BMITests(unittest.TestCase):
    def testObeseInputs(self):
        self.assertEqual(BMIFormula(6, 1, 250), 2)
        
    def testOverInputs(self):
        self.assertEqual(BMIFormula(6, 1, 200), 2)
        
    def testNormalInputs(self):
        self.assertEqual(BMIFormula(6, 1, 180), 2)
        
    def testUnderInputs(self):
        self.assertEqual(BMIFormula(6, 1, 90), 2)
        
    def testLargeInputs(self):
        self.assertEqual(BMIFormula(999999999999, 999999999999, 999999999999), 2)

    def testNegativeInputs(self):
        self.assertEqual(BMIFormula(-1, -1, -1), 2)

    def testStringInputs(self):
        self.assertEqual(BMIFormula('bob', 'ross', 'boss'), 2)

    def testPoundsInputs(self):
        self.assertEqual(BMIFormula(6, 1, 9999), 2)

    def testInchesInputs(self):
        self.assertEqual(BMIFormula(6, 12, 180), 2)


if __name__ == 'main__':
    unittest.main()
