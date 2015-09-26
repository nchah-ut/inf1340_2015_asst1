#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"
__version__ = "1.0"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """

    # print("Error")

    # Working code appended from here
    # TODO: reformat/refactor before submission
    # TODO: use (if allowed) math library for NaN calls


    # Key-Value mapping shapes
    shapes = {
        2: "",
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
        # The Frontend
        shape_sides = raw_input("How many sides does your shape have? ")

        # The Backend
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
            # TODO: update to just "Error" ?
            error_message = "Error. Sorry, your value of {} is not valid.".format(shape_sides)
            print error_message
        else:
            value_message = "{} sides! That's a {}.".format(shape_sides, shapes[shape_sides])
            print value_message
            break

name_that_shape()

# TODO: format tests according to guidelines
""" Tests

>>> ten
Error

>>> 10.0
10 sides! That's a Decagon.

>>> 10
10 sides! That's a Decagon.

>>> 2
Error. Sorry, your value of 2 is not valid.

>>> 13
Error. Sorry, your value of 13 is not valid.

"""
