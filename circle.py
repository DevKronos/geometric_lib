import math
import unittest


def area(r):
    '''
    Take length r of circle's radius,
    Return area of that circle
    '''
    if r < 0:
        raise ValueError("Length must be non-negative number")
    
    return math.pi * r * r


def perimeter(r):
    '''
    Take length r of circle's radius,
    Return perimeter of that circle
    '''
    if r < 0:
        raise ValueError("Length must be non-negative number")

    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        res = area(0)
        self.assertAlmostEqual(res, 0)
    
    def test_area_positive_radius(self):
        res = area(10)
        self.assertAlmostEqual(res, math.pi * 100)
    
    def test_area_float(self):
        res = area(3.6)
        self.assertAlmostEqual(res, math.pi * 12.96)
    
    def test_area_repeat(self):
        res1 = area(5)
        self.assertAlmostEqual(res1, math.pi * 25)
        res2 = area(5)
        self.assertAlmostEqual(res2, math.pi * 25)

    def test_area_negative_raduis(self):
        with self.assertRaises(ValueError):
            area(-10)
    
    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0)
    
    def test_perimeter_positive_radius(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, math.pi * 20)
    
    def test_perimeter_float(self):
        res = perimeter(3.6)
        self.assertAlmostEqual(res, math.pi * 7.2)
    
    def test_perimeter_repeat(self):
        res1 = perimeter(3)
        self.assertAlmostEqual(res1, math.pi * 6)
        res2 = perimeter(3)
        self.assertAlmostEqual(res2, math.pi * 6)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-10)
