# CS1210: Lab 10 [4 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partners, and
#  2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid1" and "hawkid2" between the two
# double quote marks to match your own hawkids. Your hawkid is the
# "login identifier" you use to login to all University services, like
# `https://myUI.uiowa.edu/'
#
# Note: we are not asking for your passwords, just the login
# identifiers: for example, mine is "sriram".
#
# Note: if there are 3 of you, add a third string to the list returned.
# 
# ADDITIONALLY: Please replace your "groupcode" by the code for your 
# group shown by your Lab TA. 
#
######################################################################

def signed():
    return(["mhoneywell","lgsitumeang", "1881189"])

######################################################################
# NOTE: EVERY FUNCTION IN YOUR LAB SOLUTION NEEDS TO HAVE A SINGLE LINE 
# OF CODE OF THE FORM
#
#       return expression
#
# WHERE expression CONTAINS A LIST COMPREHENSION.
###################################################################### 

######################################################################
#
# Complete the function below.
#
# SPECIFICATION
# n is an integer that is 2 or larger. The function returns True if
# n is a prime; False otherwise.
#
# Algorithm suggestion: Use a list comprehension to generate all factors 
# of n, between 2 and n-1. Then check if this list has length 0.
#
# EXAMPLES: 
#    isPrime(2), isPrime(3), isPrime(5), isPrime(7), isPrime(97) should all
#    return True. isPrime(4), isPrime(6), isPrime(10), isPrime(91) should
#    all return False.
#
######################################################################
def isPrime(n):
    # Fill the BLANK below
    return 



######################################################################
#
# Complete the function below.
#
# SPECIFICATION
# N is an integer that is 2 or larger. The function returns the list 
# of an primes in the range 2 through N, in increasing order.
#
# Algorithm suggestion: use the isPrime function defined above
#
# EXAMPLES: 
# allPrimes(20) returns [2, 3, 5, 7, 11, 13, 17, 19]
# allPrimes(30) returns [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#
######################################################################
def allPrimes(N):
    # Fill the BLANK below
    return BLANK


######################################################################
# Complete the function below.
#
# SPECIFICATION
# L is a list of integers of size at least 2. The function returns True if L is
# an arithmetic progression. 
#
# Definition: A sequence of integers is an arithmetic progression if
# the difference between a number and its previous number is the same
# for all numbers. For example, 13, 18, 23, 28, 33, 38, 43 is an arithmetic
# progression because 5 is the common difference between a number an its
# previous number. Similarly, 8, 4, 0, -4, -8, -12 is an arithmetic 
# progression. But, 8, 9, 12, 15 is not an arithmetic progression.
#
# Algorithm suggestion: Use a list comprehension to generate all 
# len(L)-1 differences, between a number and its previous number. Then
# check if all numbers in this list of differences are identical.
#
# EXAMPLES:
#    isAP([8, 13, 18, 23, 28, 33]) returns True
#    isAP([8, 4, 0, -4, -8]) returns True
#    isAP([8, 9, 13, 18, 19]) returns False
#    isAP([10, 20]) returns True
#    isAP([10, 20, 30, 40, 49]) returns False
#
######################################################################
def isAP(L):
    # Fill the BLANK below
    return BLANK

######################################################################
# Complete the function below.
#
# SPECIFICATION
# s is a string of length at least 1. The function should return the string
# obtained by rotating the characters of s to the right by 1 position. 
#
# EXAMPLES:
# rotateString("hello") should return 'elloh'
# rotateString("above") should return 'bovea'
# rotateString("True") should return 'rueT'
# rotateString("count") should return 'ountc'
#
######################################################################
def rotateString(s):
    # Fill the BLANK below
    return BLANK
