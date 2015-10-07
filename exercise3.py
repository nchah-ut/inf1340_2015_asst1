#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

    # print("The battery cables may be damaged. Replace cables and try again.")

    # Questions
    q1 = "Is the car silent when you turn the key? "
    q2 = "Are the battery terminals corroded? "
    q3 = "Does the car make a clicking noise? "
    q4 = "Does the car crank up but fail to start? "
    q5 = "Does the engine start and then die? "
    q6 = "Does your car have fuel injection? "

    # Answers
    # Variables named based on "ans_" + decision tree paths
    ans_yy = "Clean terminals and try starting again."
    ans_yn = "Replace cables and try again."
    ans_ny = "Replace the battery."
    ans_nny = "Check spark plug connections."
    ans_nnnn = "Engine is not getting enough fuel. Clean fuel pump."
    ans_nnnyn = "Check to ensure the choke is opening and closing."
    ans_nnnyy = "Get it in for service."

    # TODO: try JSON
    decision_tree = {
        q1: {"y": {q2:
                      {"y": ans_yy,
                       "n": ans_yn}
                   },
             "n": {q3:
                      {"y": ans_ny,
                       "n": {q4:
                                  {"y": ans_nny},
                                   "n": {q5:
                                           {"y": {
                                           q6:
                                               {"n": ans_nnnyn,
                                                "y": ans_nnnyy}}
                                           }
                                   }
                             }
                       }
                   }
             }
    }

    error_message = "Sorry, please input 'y' or 'n' for the question: '{}'."

    # TODO: Update code if errors should terminate the program instead of looping for assignment
    # TODO: Refactor variable names
    while True:
        answer1 = raw_input(q1)
        if answer1 == "Y":
            while True:
                answer2 = raw_input(q2)
                if answer2 == "Y":
                    print(ans_yy)
                    break
                elif answer2 == "N":
                    print(ans_yn)
                    break
                else:
                    print(error_message.format(q2))
            break

        elif answer1 == "N":
            while True:
                answer3 = raw_input(q3)
                if answer3 == "Y":
                    print(ans_ny)
                    break
                elif answer3 == "N":
                    while True:
                        answer4 = raw_input(q4)
                        if answer4 == "Y":
                            print(ans_nny)
                            break
                        elif answer4 == "N":
                            while True:
                                answer5 = raw_input(q5)
                                if answer5 == "Y":
                                    answer6 = raw_input(q6)
                                    if answer6 == "N":
                                        print(ans_nnnyn)
                                        break
                                    elif answer6 == "Y":
                                        print(ans_nnnyy)
                                        break
                                    else:
                                        print(error_message.format(q6))
                                elif answer5 == "N":
                                    print(ans_nnnn)
                                    break
                                else:
                                    print(error_message.format(q5))
                            break
                        else:
                            print(error_message.format(q4))
                    break
                else:
                    print(error_message.format(q3))
            break
        else:
            print(error_message.format(q1))

diagnose_car()

""" Tests

# Testing outcomes

1. Input: Y > Y
Expected Output: Clean terminals and try starting again.
Actual Output:

    Is the car silent when you turn the key? Y
    Are the battery terminals corroded? Y
    Clean terminals and try starting again.

2. Input: Y > N
Expected Output: Replace cables and try again.
Actual Output:

    Is the car silent when you turn the key? Y
    Are the battery terminals corroded? N
    Replace cables and try again.

3. Input: N > Y
Expected Output: Replace the battery.
Actual Output:

    Is the car silent when you turn the key? N
    Does the car make a clicking noise? Y
    Replace the battery.

4. Input N > N > Y
Expected Output: Check spark plug connections.
Actual Output:

    Is the car silent when you turn the key? N
    Does the car make a clicking noise? N
    Does the car crank up but fail to start? Y
    Check spark plug connections.

5. Input: N > N > N >
Expected Output: Engine is not getting enough fuel. Clean fuel pump.
Actual Output

    Is the car silent when you turn the key? N
    Does the car make a clicking noise? N
    Does the car crank up but fail to start? N
    Does the engine start and then die? N
    Engine is not getting enough fuel. Clean fuel pump.

5. Input: N > N > N > Y > N
Expected Output: Check to ensure the choke is opening and closing.
Actual Output:

    Is the car silent when you turn the key? N
    Does the car make a clicking noise? N
    Does the car crank up but fail to start? N
    Does the engine start and then die? Y
    Does your car have fuel injection? N
    Check to ensure the choke is opening and closing.

6. Input: N > N > N > Y > Y
Expected Output: Get it in for service.
Actual Output:

    Is the car silent when you turn the key? N
    Does the car make a clicking noise? N
    Does the car crank up but fail to start? N
    Does the engine start and then die? Y
    Does your car have fuel injection? Y
    Get it in for service.


# Testing errors

6. Input: y > do not know > n
Expected Output: Replace cables and try again.
Actual Output:

    Is the car silent when you turn the key? y
    Are the battery terminals corroded? do not know
    Sorry, please input 'y' or 'n' for the question: 'Are the battery terminals corroded? '.
    Are the battery terminals corroded? n
    Replace cables and try again.

"""
