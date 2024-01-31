"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

# Constants
BALANCED = 'balanced parentheses'
MORE_LEFT = 'too many left parentheses'
MORE_RIGHT = 'too many right parentheses'


def check_parentheses(expression):
    """
    -------------------------------------------------------
    Determines if expression contains valid parentheses - () - or not.
    Non-parenthesis characters are ignored.
    Must use a Stack.
    Use: checked = check_parentheses(expression)
    -------------------------------------------------------
    Parameters:
        expression - the string to check (str)
    Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
        checked - one of:
            BALANCED, MORE_LEFT, MORE_RIGHT (str)
    -------------------------------------------------------
    """
    checked = BALANCED
    countright = 0
    countleft = 0
    s = Stack()
    for i in expression:
        if i == '(' or i == ')':
            s.push(i)
    
    if s.is_empty() == True:
        checked = BALANCED
    elif s.is_empty() == False:
        for i in s:
            if i == '(':
                countleft += 1
            elif i == ')':
                countright += 1
    
    if countright > countleft:
        checked = MORE_LEFT
    elif countright < countleft:
        checked = MORE_RIGHT
    elif countright == countleft:
        checked = BALANCED
    
    return checked
