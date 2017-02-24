from retirement import calculateAgeGoalMet, agePositive, salPositive, perSavPositive, savGlPositive
import unittest

class TestRetirement(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(calculateAgeGoalMet(0, 0, 0, 0), 0)

    def test_age_positive(self):
        self.assertTrue(agePositive(1))

    def test_sal_positive(self):
        self.assertTrue(salPositive(1))

    def test_perSav_positive(self):
        self.assertTrue(perSavPositive(1))

    def test_savGl_positive(self):
        self.assertTrue(savGlPositive(1))


if __name__ == 'main__':
	unittest.main()