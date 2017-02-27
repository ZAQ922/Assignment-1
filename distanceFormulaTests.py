import unittest
from math import sqrt

def distanceFormula(x1, y1, x2, y2):
	try:
		return sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))
	except:
		print("Please provide a proper input")

class distanceFormulaTests(unittest.TestCase):
	def test_normalInputs(self):
		self.assertEqual(distanceFormula(1,1,0,0), sqrt(2))

	def test_bigInputs(self):
		self.assertEqual(distanceFormula(200, 200, -200, -200), sqrt(320000))

	def test_negativeInputs(self):
		self.assertEqual(distanceFormula(-5, -5, -6, -6), sqrt(2))

if __name__ == 'main__':
	unittest.main()