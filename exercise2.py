#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """

    # print("Error")

    # Working code appended from here

    # Key-Value mapping shapes in dictionary
    shapes = {
        3: "Triangle",
        4: "Quadrilateral",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Enneagon",
        10: "Decagon"
    }

    while True:
        # The Frontend - what the user sees
        shape_sides = raw_input("How many sides does your shape have? ")

        # The Backend - processes, calculations
        # Sanitize the input, convert values to type 'int'
        shape_sides = shape_sides.strip()  # Strip out trailing spaces
        try:
            shape_sides = int(float(shape_sides))  # Input may be a float, convert to int
        except ValueError:
            try:
                shape_sides = int(shape_sides)
            except ValueError:
                pass

        # Conditionals for values from 3 .. 10
        if shape_sides < 3 or shape_sides > 10:
            # error_message_v2 = "Error. Sorry, your value of {} is not valid.".format(shape_sides)
            print "Error"
            break
        else:
            # User input value used to look up value in shapes dictionary 
            value_message = "{} sides! That's a {}.".format(shape_sides, shapes[shape_sides])
            print value_message
            break

name_that_shape()

""" Tests

1. Input: ten
Expected Output: Error
Actual Output: Error

    >>> ten
    Error

2. Input: 10.0
Expected Output: 10 sides! That's a Decagon.
Actual Output: 10 sides! That's a Decagon.

    >>> 10.0
    10 sides! That's a Decagon.

3. Input: 10.0
Expected Output: 10 sides! That's a Decagon.
Actual Output: 10 sides! That's a Decagon.

    >>> 10
    10 sides! That's a Decagon.

4. Input: 2
Expected Output: Error
Actual Output: Error

    >>> 2
    Error

4. Input: 13
Expected Output: Error
Actual Output: Error

    >>> 13
    Error

5. Input: " " (whitespace)
Expected Output: Error
Actual Output: Error

    >>>
    Error

"""
