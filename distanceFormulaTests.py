import unittest
from math import sqrt

def distanceFormula(x1, y1, x2, y2):
	return 2

class distanceFormulaTests(unittest.TestCase):
	def test_normalInputs(self):
		self.assertEqual(distanceFormula(1,1,1,1), sqrt(4))

	def test_bigInputs(self):
		self.assertEqual(distanceFormula(200, 200, 200, 200), sqrt(80000))

	def test_negativeInputs(self):
		self.assertEqual(distanceFormula(-5, -5, -5, -5), sqrt(50))

if __name__ == 'main__':
	unittest.main()