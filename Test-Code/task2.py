# IMPORTS HERE

import sys

###############################################
#
#   Made by: Albert Garcia Sanchez
#   Task 2 - Positive Integers List
#   We assume positive integers do not include the number 0
#
###############################################

'''
REFERENCES

https://wiki.python.org/moin/TimeComplexity
http://leadsift.com/loop-map-list-comprehension/

'''


# ---------------DEFINITIONS-------------------#

def main():
    # Verifications
    if len(sys.argv) != 2:
        print "Incorrect number of parameters!"
        return
    elif len(sys.argv[1]) <= 0:
        print "Incorrect file path!"
        return

    # Input reading
    with open(sys.argv[1]) as f:
        intList = [int(x) for x in f.read().split(",")]

    # Verifications of the read data
    if len(intList) <= 0:
        print "Input text file empty!"
        return

    # Declaration of variables and Set Up
    i, currentInt = 0, 0
    correctInteger = True
    intList.sort()  # O(n log n) both in average and worst cases

    # Computing Algorithm
    while i < len(intList) and correctInteger:
        lastNumber = currentInt
        currentInt = int(intList[i])

        if lastNumber != currentInt:
            correctInteger = (lastNumber+1) == currentInt
        i += 1

    # Output
    if not correctInteger:
        print str(lastNumber+1)
    else:
        print str(currentInt+1)

# ---------------------------------------------#


# -----------------CALLS-----------------------#

main()

# ---------------------------------------------#
