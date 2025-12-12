# Solution Description
This library is designed for working with geometric shapes in Python.

# Function Descriptions
## Circle.py
### area(r)
Returns the area of a circle given its radius.

__Parameters:__  
&emsp;r (float): radius of the circle

__Return value:__  
&emsp;float: area of the circle calculated by the standard formula

__Example usage:__
&emsp;```area(4)   //50,2654824574```
### perimeter(r)
Returns the perimeter (circumference) of a circle given its radius.

__Parameters:__  
&emsp;r (float): radius of the circle

__Return value:__  
&emsp;float: circumference of the circle calculated by the standard formula

__Example usage:__
&emsp;```perimeter(4)   //25,1327411228```

## Square.py
### area(a)
Returns the area of a square given the length of its side.

__Parameters:__  
&emsp;a (float): side length of the square

__Return value:__  
&emsp; float: the area of the square calculated by the standard formula

__Example usage:__
&emsp;```area(3)   //9```

### perimeter(a)
Returns the perimeter of a square given the length of its side.

__Parameters:__  
&emsp;a (float): side length of the square

__Return value:__  
&emsp;float: perimeter of the square calculated by the standard formula

__Example usage:__
&emsp;```perimeter(3)   //12```

## Rectangle.py
### area(a, b)
Returns the area of a rectangle given the lengths of its two adjacent sides.

__Parameters:__  
&emsp;a (float): one side of the rectangle
&emsp;b (float): other side of the rectangle

__Return value:__  
&emsp;float: the area of the rectangle calculated by the standard formula

__Example usage:__
&emsp;```area(4, 2)   //8```

### perimeter(a, b)
Returns the perimeter of a rectangle given the lengths of its two adjacent sides.

__Parameters:__  
&emsp;a (float): one side of the rectangle
&emsp;b (float): other side of the rectangle

__Return value:__  
&emsp;float: perimeter of the rectangle calculated by the standard formula

__Example usage:__
&emsp;```perimeter(4, 2)   //12```

## Triangle.py
### area(a, h)
Returns the area of a triangle given its base and corresponding height.

__Parameters:__  
&emsp;a (float): base of the triangle  
&emsp;h (float): height corresponding to the base

__Return value:__  
&emsp;float:  area of the triangle calculated by the standard formula

__Example usage:__
&emsp;```area(3, 4)   //6```

### perimeter(a, b, c)
Returns the perimeter of a triangle given the lengths of its three sides.

__Parameters:__  
&emsp;a (float): one side of the triangle  
&emsp;b (float): another side of the triangle
&emsp;c (float): third side of the triangle

__Return value:__  
&emsp;float: perimeter of the triangle calculated by the standard formula

__Example usage:__
&emsp;```perimeter(3, 4, 5)   //12```

# Project History
- __Commit "Circle and square added"__
    - Created circle.py and square.py  
    - Added area and perimeter functions to each file

- __Commit "Docs added"__  
    - Created docs directory    
    - Created README.md file  
    - Added content to README

- __Commit "Add file for Ractangle"__
    - Created rectangle.py  
    - Added area and perimeter functions to rectangle.py

- __Commit "Add File for Triangle & Fix Rectangle"__
    - Created triangle.py  
    - Added area and perimeter functions to triangle.py  
    - Fixed the perimeter function in rectangle.py

- __Commit "Add descriptions for functions"__
    - Added docstrings for area and perimeter functions in all files

- __Commit "Unit tests"__
    - Added unittest in each .py file

-__Commit "CI/CD"__
    - Added main.yml file for ci/cd

- __Commit "Upgrade CI/CD"__
    - Upgrade main.yml file