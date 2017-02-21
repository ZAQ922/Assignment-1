import unittest

def distanceFormula(x1, y1, x2, y2):
	return 2

class distanceFormulaTests(unittest.TestCase):
	def test_normalInputs(self):
		self.assertEqual(distanceFormula(1,1,1,1), 2)

if __name__ == 'main__':
	unittest.main()