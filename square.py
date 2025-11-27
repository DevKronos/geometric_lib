import unittest

def area(a):
    '''
    Take length a of square's side,
    Return area of that square
    '''
    if a < 0:
        raise ValueError("Length must be non-negative number")
    
    return a * a


def perimeter(a):
    '''
    Take length a of square's side,
    Return perimeter of that square
    '''
    if a < 0:
        raise ValueError("Length must be non-negative number")
    
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = area(0)
        self.assertAlmostEqual(res, 0)
    
    def test_area_positive_side(self):
        res = area(10)
        self.assertAlmostEqual(res, 100)
    
    def test_area_float(self):
        res = area(3.6)
        self.assertAlmostEqual(res, 12.96)
    
    def test_area_repeat(self):
        res1 = area(5)
        self.assertAlmostEqual(res1, 25)
        res2 = area(5)
        self.assertAlmostEqual(res2, 25)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-10)
    
    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0)
    
    def test_perimeter_positive_side(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 40)
    
    def test_perimeter_float(self):
        res = perimeter(1.8)
        self.assertAlmostEqual(res, 7.2)
    
    def test_perimeter_repeat(self):
        res1 = perimeter(3)
        self.assertAlmostEqual(res1, 12)
        res2 = perimeter(3)
        self.assertAlmostEqual(res2, 12)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-10)
