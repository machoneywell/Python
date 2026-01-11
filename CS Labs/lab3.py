#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:49:04 2023

@author: macbook_user
"""

# CS1210: Lab 3 [2 functions to complete]
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
######################################################################

def signed():
    return(["mhoneywell","hawkid2"])

######################################################################
# Define the two functions digitSum and positiveEvenSum below
######################################################################

######################################################################
# Assume that n is a non-negative integer
# 
# Specification: digitSum returns the sum of the digits in n 
#
# Examples: digitSum(5891) returns 23
#           digitSum(2005731) returns 18
#           digitSum(0) returns 0
#
######################################################################

def digitSum(n):
    # sumOfDigits is the accumulator variable to which digits of n will be added
    sumOfDigits = 0 
    
    while (n > 0):
        # Extract and add the right most digit of n to sumOfDigits
        # ADD CODE HERE: one line of code is enough
        sumOfDigits = sumOfDigits + n[0]
        
        # Remove the right most n. For example if n was 5891 then
        # after executing this line of code n will become 589. 
        # ADD CODE HERE: one line of code is enough

     
    # Return the answer
    return sumOfDigits
    print(digitSum(sumOfDigits))

######################################################################
# Assume that L is a list of integers; these integers can be positive
# negative or 0.
# 
# Specification: positiveEvenSum(L) returns the sum of all the positive 
# integers in L that are even 
#
# Examples: positiveEvenSum([-6, 7, 1, 14, 3]) returns 14
#           positiveEvenSum([70, 1, -4, 32]) returns 102
#           positiveEvenSum([]) returns 0
#           positiveEvenSum([-6, 7, 1]) returns 0 
#    
######################################################################      
        
def positiveEvenSum(L):
    # i will be the index for list L
    i = 0
    
    # sumOfElements is the accumulator variable to which we will add
    # elements of L that are positive and even
    sumOfElements = 0
    
    # Here we need a while loop that visits each element in L,
    # checks if that element is positive and even, and adds it to
    # sumOfElements
    # ADD CODE HERE: my solution contains 4 lines of code


    # Return the answer
    return sumOfElements

######################################################################
# This is a simple function you can call for testing digitSum. It
# contains 5 tests. You can call digitSumTester() and if nothing gets
# printed, then it means that digitSum has passed all 5 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 

def digitSumTester():
    test = []
    
    # Test 1
    test.append(digitSum(5891) == 23)
    
    # Test 2
    test.append(digitSum(2005731) == 18)
    
    # Test 3
    test.append(digitSum(0) == 0)
    
    # Test 4
    test.append(digitSum(19876542) == 42)
    
    # Test 5
    test.append(digitSum(1) == 1)
    
    for i in range(len(test)):
        if not test[i]:
            print("digitSum Test", i, "failed")
 
######################################################################
# This is a simple function you can call for testing positiveEvenSum. It
# contains 5 tests. You can call positiveEvenSumTester() and if nothing gets
# printed, then it means that positiveEvenSum has passed all 5 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester. 
#    
###################################################################### 
            
def positiveEvenSumTester():
    test = []
    
    # Test 1
    test.append(positiveEvenSum([-6, 7, 1, 14, 3]) == 14)
    
    # Test 2
    test.append(positiveEvenSum([70, 1, -4, 32]) == 102)
    
    # Test 3
    test.append(positiveEvenSum([]) == 0)
    
    # Test 4
    test.append(positiveEvenSum([-6, 7, 1]) == 0)
    
    # Test 5
    test.append(positiveEvenSum([-6, 7, 1, 200]) == 200)
    
    for i in range(len(test)):
        if not test[i]:
            print("positiveEvenSum Test", i, "failed")
