import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):  
    def setUp(self):
        self.calculator = Calculator()  
    
    def test_add(self):
        self.assertEqual(self.calculator.add(4,7), 11)  
    
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10,5), 5)  
    
    def test_multiply(self):
        self.assertEqual(self.calculator.product(3,7), 21)


if __name__ == "__main__":
  unittest.main()