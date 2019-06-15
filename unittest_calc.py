import calc
import unittest


class TestCalc(unittest.TestCase):


    def test_add(self):
        result = calc.add(10, -5)
        self.assertEqual(result, 5)

    
    def test_subtrack(self):
        result = calc.subtrack(10, 5)
        self.assertEqual(result, 5)
    

    def test_multiply(self):
        result = calc.multiply(3, -5)
        self.assertEqual(result, -15)


    def test_divide(self):
        result = calc.divide(10, 5)
        self.assertEqual(result, 2)


    def test_divide1(self):
        result = calc.divide(3, 0)
        self.assertEqual(result, 0)

    
    def test_divide2(self):
        result = calc.divide(0, 5)
        self.assertEqual(result, 0)


if __name__ == "__main__":
   unittest.main()
 