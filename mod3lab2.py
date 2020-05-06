"""
CTEC 121
Esther  Pisano      
module 3 lab 2
unit 4 and 5
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nThere was a divide by zero error. Exiting\n")
    except:
        print("\nUnknown exception\n")
        exit


main()
