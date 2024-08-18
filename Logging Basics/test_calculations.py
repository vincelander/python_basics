"""
    To run this unit testing,
    module we have to use the following script in the terminal within the directory.
        python -m unittest test_calculations.py
    
    Unless we define the code below in the module,
    then we can run as is.
        if  __name__ == '__main__':
            unittest.main()
    
    Reference: https://www.youtube.com/watch?v=6tNS--WetLI&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=21
"""

import unittest
import calculation

class TestCalculation(unittest.TestCase):
    print("Executing unit tests ...")

    def test_add(self):
        self.assertEqual(calculation.add(10, 5), 15)
        self.assertEqual(calculation.add(-1, 1), 0)
        self.assertEqual(calculation.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculation.subtract(10, 5), 5)
        self.assertEqual(calculation.subtract(-1, 1), -2)
        self.assertEqual(calculation.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculation.multiply(10, 5), 50)
        self.assertEqual(calculation.multiply(-1, 1), -1)
        self.assertEqual(calculation.multiply(-1, -1), 1)

    def test_division(self):
        self.assertEqual(calculation.devide(10, 5), 2)
        self.assertEqual(calculation.devide(-1, 1), -1)
        self.assertEqual(calculation.devide(-1, -1), 1)
        self.assertEqual(calculation.devide(5, 2), 2.5)

        # to test raise/exception block, here's 2 ways
        self.assertRaises(ValueError, calculation.devide, 10, 0)

        with self.assertRaises(ValueError):     # this approach uses context manager (: is it colon) & is a better way
            calculation.devide(10, 0)

if  __name__ == '__main__':
    unittest.main()