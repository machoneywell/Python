#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:31:22 2023

@author: macbook_user
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:49:04 2023

@author: macbook_user
"""

# CS1210: Lab 4 [2 functions to complete]
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
    return(["mhoneywell","asicabuthahir"])

######################################################################
# Complete the function below.
#
# The argument L represents an n x n matrix for some positive integer
# n. So L contains n elements and each element is a list of length n,
# containing numbers. You can assume that L is non-empty and has exactly
# this form.
#
# Specification: The function returns the sum of the elements in the upper
# right triangle of the matrix represented by L.
#
# Example: upperRightTriangleSum([[3, 2, 1], [4, 7, 8], [0, 6, 9]]) 
# returns 30. This is because L represents the matrix 
#          
#          3   2   1
#          4   7   8
#          0   6   9
#
# and the upper right triangle of this matrix is
#
#          3   2   1
#              7   8
#                  9
# 
# The sum of the elements in this upper right triangle is 30.
######################################################################
def upperRightTriangleSum(L):
    n = len(L)
    
    # The accumulator variable to which we will add elements of the 
    # upper right triangle
    sumElements = 0

    # i will serve as the row index of the matrix
    i = 0

    # Outer while loop, which walks down each row of the matrix
    while (i < n):
        
        # Inner while loop, which walks down the columns of the current row
        # that belong to the upper right triangle
        # ADD CODE HERE: my solution contained 4 lines of code
        j = i
        while (j < n):
            sumElements = sumElements + L[i][j]
            j = j + 1
        
        
            
        i = i + 1
        
    return sumElements


######################################################################
# Complete the function below.
#
# The arguments L1 and L2 are lists and k is a non-negative integer.
#
# Specification: The function returns True if L2 is obtained by rotating
# L1 right by k steps. It returns False otherwise. 
# 
# Example: isRightRotated([8, 2, 3, 4, 1], [4, 1, 8, 2, 3], 2) returns
# True. This is because if we right rotate [8, 2, 3, 4, 1] once we get
# [1, 8, 2, 3, 4] and if we right rotate [8, 2, 3, 4, 1] twice we get
# [4, 1, 8, 2, 3]. 
#   
######################################################################
def isRightRotated(L1, L2, k):
    # When L1 and L2 are empty, then L2 can be viewed as a k-step right 
    # rotation of L1, for any k
    if (len(L1) == 0) and (len(L2) == 0):
        return True
    
    # When L1 and L2 have different lengths, then L2 cannot by obtained
    # by right rotating L1, for any k
    if (len(L1) != len(L2)):
        return False
    
    # While loop that walks down the list L1 and checks if each element
    # in L1 appears in the correct position in L2 
    # ADD CODE HERE: my solution contained 5 lines of code
    i = 0
    while (L1[i] == L2[i+k]):
        if (L1[i] == 
        
        
    return True

######################################################################
# This is a simple function you can call for testing upperRightTriangleSum. It
# contains 5 tests. You can call upperRightTriangleSumTester() and if nothing gets
# printed, then it means that upperRightTriangleSum has passed all 5 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 

def upperRightTriangleSumTester():
    test = []
    
    # Test 1
    test.append(upperRightTriangleSum([[3, 2, 1], [4, 7, 8], [0, 6, 9]]) == 30)
    
    # Test 2
    test.append(upperRightTriangleSum([[3, 2, 1, -10], [4, 7, 8, 6], [0, 6, 9, 11], [2, 4, 3, 10]]) == 47)
    
    # Test 3
    test.append(upperRightTriangleSum([[1, -10], [4, 6]]) == -3)
    
    # Test 4
    test.append(upperRightTriangleSum([[100]]) == 100)
    
    # Test 5
    test.append(upperRightTriangleSum([[8, 6, 12, 14], [3, 2, 1, 9], [4, 7, 1, 6], [3, 2, 5, 7]]) == 66)
    
    for i in range(len(test)):
        if not test[i]:
            print("digitSum Test", i, "failed")
 


######################################################################
# This is a simple function you can call for testing isRightRotated. It
# contains 5 tests. You can call isRightRotatedTester() and if nothing gets
# printed, then it means that isRightRotated has passed all 5 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 

def isRightRotatedTester():
    test = []
    
    # Test 1
    test.append(isRightRotated([8, 2, 3, 4, 1], [4, 1, 8, 2, 3], 2) == True)
    
    # Test 2
    test.append(isRightRotated([8, 2, 3, 4, 1], [4, 1, 8, 2, 3], 3) == False)
    
    # Test 3
    test.append(isRightRotated([8, 2, 3, 4, 1], [3, 4, 1, 8, 2], 3) == True)
    
    # Test 4
    test.append(isRightRotated([8, 2, 3, 4, 1], [2, 3, 4, 1, 8], 4) == True)
    
    # Test 5
    test.append(isRightRotated([], [], 4) == True)
    
    for i in range(len(test)):
        if not test[i]:
            print("digitSum Test", i, "failed")
 

