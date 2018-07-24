# IMPORTS HERE

import sys

###############################################
#
#   Made by: Albert Garcia Sanchez
#   Task 1 - Balanced brackets
#
###############################################

'''
REFERENCES

https://www.tutorialspoint.com/python/python_command_line_arguments.htm

'''


# ---------------DEFINITIONS-------------------#

def main():
    # Verifications
    if len(sys.argv) != 2:
        print "Incorrect number of parameters!"
        return
    elif len(sys.argv[1]) <= 0:
        print "Pass! There are 0 set of brackets"
        return

    # Declaration of variables
    openBrackets, closedBrackets = 0, 0
    orderedBrackets = True
    lineToRead = sys.argv[1]
    i = 0

    # Algorithm
    while i < len(lineToRead):
        letter = lineToRead[i]

        if letter == '(':
            openBrackets += 1
        elif letter == ')':
            closedBrackets += 1
        if openBrackets - closedBrackets < 0:
            orderedBrackets = False

        i += 1

    # Output
    if orderedBrackets:
        if openBrackets == closedBrackets:
            print "Pass! There are " + str(openBrackets) + " set of brackets"
        else:
            print "Fail! There are " + str(openBrackets) + " ( but only " + str(closedBrackets) + " )"
    else:
        if openBrackets == closedBrackets:
            print "Pass! There are " + str(openBrackets) + " set of brackets (not all of them ordered)"
        else:
            print "Fail! There are " + str(openBrackets) + " ( but only " + str(closedBrackets) + " ) and some of them not ordered"


# ---------------------------------------------#


# -----------------CALLS-----------------------#

main()

# ---------------------------------------------#
