# CS1210: WPS9 [4 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
# 1) the code below is entirely your work, and
# 2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid" between the two double quote marks
# to match your own hawkid. Your hawkid is the "login identifier" you use
# to login to all University services, like `https://myUI.uiowa.edu/'
#
#
# Note: we are not asking for your password, just the login
# identifiers: for example, mine is "sriram".
#
# Replace the pass statement below by your code
######################################################################
def signed():
    return(["mhoneywell"])

#######################################################################
# SPECIFICATION: n is a non-negative integer and binaryString is a recursive
# function that returns the binary string that represents n.
#
# EXAMPLES:
#>>> binaryString(22)
#'10110'
#>>> binaryString(31)
#'11111'
#>>> binaryString(32)
#'100000'
#>>> binaryString(8)
#'1000'
#>>> binaryString(9)
#'1001'
#
# IMPLEMENT THE FOLLOWING RECURSIVE ALGORITHM:
# If n is even, the last bit of the binary representation is 0 and the
# rest of the binary representation is the binary representation of n/2.
# If n is odd, the last bit of the binary representation is 1 and the
# rest of the binary representation is the binary representation of (n-1)/2.
#
# NOTE: My implementation contains two base cases. The recursive case
# consists of just a return statement.
#######################################################################
def binaryString(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    elif n % 2 == 0:
        return binaryString(n / 2) + '0'
    else:
        return binaryString((n-1) / 2) + '1'

#######################################################################
# SPECIFICATION: s is a non-empty string  and isPalindrome is a recursive
# function that returns True if s is a palindrome and returns False otherwise.
#
# EXAMPLES:
# >>> isPalindrome("axa")
# True
# >>> isPalindrome("axar")
# False
# >>> isPalindrome("a")
# True
# >>> isPalindrome("abba")
# True
# >>> isPalindrome("madam")
# True
# >>> isPalindrome("nurses run")
# False
# >>> isPalindrome("nur ses run")
# True
# >>> isPalindrome("yy")
# True
#
# IMPLEMENT THE FOLLOWING RECURSIVE ALGORITHM:
# s is a palindrome is the first and last characters are identical and the
# substring obtained by removing the first and last characters is a
# palindrome.
#
# NOTE: My implementation contains a base case dealing with a string of
# length 1. The recursive case consists of just a return statement.
#######################################################################
def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])

#######################################################################
# SPECIFICATION: a list of numbers is said to be quickly increasing if each
# number in the list (except the first) is at least 10 more than the
# previous number. The function returns True if the given list of numbers
# is quickly increasing; otherwise it returns False.
#
# >>> isQuicklyIncreasing([10, 21, 32, 43, 55, 66, 77, 88])
# True
# >>> isQuicklyIncreasing([10, 210, 3000, 4000])
# True
# >>> isQuicklyIncreasing([10, 11, 200, 300])
# False
# >>> isQuicklyIncreasing([10, 31, 32])
# False
# >>> isQuicklyIncreasing([110, 9, 8, 7, 6])
# False
# >>> isQuicklyIncreasing([100])
# True
# >>> isQuicklyIncreasing([10, 1000])
# True
# isQuicklyIncreasing([10, 20, 30])
# True
#
# IMPLEMENT THE FOLLOWING RECURSIVE ALGORITHM:
# L is quickly increasing if the second number in L is at least 10 more
# than the first number and the list, with the first number removed, is
# quickly increasing.
#
# NOTE: My implementation contains a base case dealing with a list of
# length 1. The recursive case consists of just a return statement.
#######################################################################
def isQuicklyIncreasing(L):
    if len(L) == 1:
        return True
    elif L[1] < L[0] + 10:
        return False
    else:
        return isQuicklyIncreasing(L[1:])
    
#######################################################################
# SPECIFICATION: n is a non-negative integer. The function returns the list
# of all binary strings of length n.
#
# EXAMPLES:
# >>> generateBinaryStrings(2)
# ['00', '01', '10', '11']
# >>> generateBinaryStrings(3)
# ['000', '001', '010', '011', '100', '101', '110', '111']
# >>> generateBinaryStrings(4)
# ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
# '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
# >>> generateBinaryStrings(1)
# ['0', '1']
# >>> generateBinaryStrings(0)
# [''] 
#
# IMPLEMENT THE FOLLOWING RECURSIVE ALGORITHM:
# Suppose L is the list of all binary strings of length n-1. Then the list
# of all binary strings of length n is obtained by (i) constructing the list
# L0 obtained by sticking a "0" before each string in L, (ii) constructing
# the list L1 obtained by sticking a "1" before each string in L, and (iii)
# constructing the list L0 + L1.
# 
# NOTE: My implementation contains a base case dealing n = 0 and two
# additional lines for the the recursive case.
#######################################################################
def generateBinaryStrings(n):
    if n == 0:
        return ['']
    else:
        L = generateBinaryStrings(n-1)
        L0 = ['0' + s for s in L]
        L1 = ['1' + s for s in L]
        return L0 + L1

