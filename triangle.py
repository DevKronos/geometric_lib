import unittest

def area(a, h):
    '''
    Take length a of triangle's side and length h of triangle's height, 
    Return area of that triangle
    '''
    if (a < 0) or (h < 0):
        raise ValueError("Length must be non-negative number")
    
    return a*h/2

def perimeter(a, b, c):
    '''
    Take length a, b, and c of triangle's sides, 
    Return perimeter of that triangle
    '''
    if (a < 0) or (b < 0) or (c < 0):
        raise ValueError("Length must be non-negative number")
    
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_zero_length(self):
        res = area(10, 0)
        self.assertAlmostEqual(res, 0)
    
    def test_area_both_positive(self):
        res = area(10, 10)
        self.assertAlmostEqual(res, 50)
    
    def test_area_float(self):
        res = area(3.6, 7.2)
        self.assertAlmostEqual(res, 12.96)
    
    def test_area_repeat(self):
        res1 = area(5, 10)
        self.assertAlmostEqual(res1, 25)
        res2 = area(5, 10)
        self.assertAlmostEqual(res2, 25)
    
    def test_area_swap_args(self):
        res1 = area(5, 10)
        res2 = area(10, 5)
        self.assertAlmostEqual(res1, res2)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-10, 10)
    
    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            area(10, -10)
    
    def test_area_both_negative(self):
        with self.assertRaises(ValueError):
            area(-10, -10)
    
    def test_perimeter_zero_length(self):
        with self.assertRaises(ValueError):
            perimeter(10, 5, 0)
    
    def test_perimeter_all_positive(self):
        res = perimeter(5, 10, 14)
        self.assertAlmostEqual(res, 29)
    
    def test_perimeter_float(self):
        res = perimeter(3.6, 4.4, 2.5)
        self.assertAlmostEqual(res, 10.5)
    
    def test_perimeter_repeat(self):
        res1 = perimeter(5, 10, 6)
        self.assertAlmostEqual(res1, 21)
        res2 = perimeter(5, 10, 6)
        self.assertAlmostEqual(res2, 21)
    
    def test_perimeter_swap_args(self):
        res1 = perimeter(2, 3, 4)
        res2 = perimeter(4, 2, 3)
        res3 = perimeter(3, 4, 2)
        self.assertAlmostEqual(res1, res2)
        self.assertAlmostEqual(res2, res3)
    
    def test_perimeter_not_exists(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)

    def test_perimeter_negative_first_side(self):
        with self.assertRaises(ValueError):
            perimeter(-1, 2, 3)
    
    def test_perimeter_negative_second_side(self):
        with self.assertRaises(ValueError):
            perimeter(1, -2, 3)
    
    def test_perimeter_negative_third_side(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, -3)
    
    def test_perimeter_all_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-1, -2, -3)
    
