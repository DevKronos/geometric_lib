import unittest

def area(a, b):
    '''
    Take length a and b of rectangle's adjacent sides, 
    Return area of that rectangle
    '''
    if (a < 0) or (b < 0):
        raise ValueError("Length must be non-negative number")
    
    return a*b

def perimeter(a, b):
    '''
    Take length a and b of rectangle's adjacent sides, 
    Return perimeter of that rectangle
    '''
    if (a < 0) or (b < 0):
        raise ValueError("Length must be non-negative number")
    
    return max(a, b) if (a * b == 0) else 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_length(self):
        res = area(10, 0)
        self.assertAlmostEqual(res, 0)
    
    def test_area_both_positive(self):
        res = area(10, 10)
        self.assertAlmostEqual(res, 100)
    
    def test_area_float(self):
        res = area(3.6, 7.2)
        self.assertAlmostEqual(res, 25.92)
    
    def test_area_repeat(self):
        res1 = area(5, 3)
        self.assertAlmostEqual(res1, 15)
        res2 = area(5, 3)
        self.assertAlmostEqual(res2, 15)
    
    
    def test_area_swap_args(self):
        res1 = area(5, 10)
        res2 = area(10, 5)
        self.assertAlmostEqual(res1, res2)

    def test_area_negative_first_side(self):
        with self.assertRaises(ValueError):
            area(-10, 10)
    
    def test_area_negative_second_side(self):
        with self.assertRaises(ValueError):
            area(10, -10)
    
    def test_area_both_negative(self):
        with self.assertRaises(ValueError):
            area(-10, -10)
    
    def test_perimeter_zero_length(self):
        res = perimeter(10, 0)
        self.assertAlmostEqual(res, 10)
    
    def test_perimeter_all_positive(self):
        res = perimeter(5, 10)
        self.assertAlmostEqual(res, 30)
    
    def test_perimeter_float(self):
        res = perimeter(1.5, 3.6)
        self.assertAlmostEqual(res, 10.2)
    
    def test_perimeter_repeat(self):
        res1 = perimeter(5, 3)
        self.assertAlmostEqual(res1, 16)
        res2 = perimeter(5, 3)
        self.assertAlmostEqual(res2, 16)
    
    def test_perimeter_swap_args(self):
        res1 = perimeter(10, 5)
        res2 = perimeter(5, 10)
        self.assertAlmostEqual(res1, res2)

    def test_perimeter_negative_first_side(self):
        with self.assertRaises(ValueError):
            perimeter(-1, 2)
    
    def test_perimeter_negative_second_side(self):
        with self.assertRaises(ValueError):
            perimeter(1, -2)
    
    def test_perimeter_all_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-1, -2)
    