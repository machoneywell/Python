# CS1210: Lab 6 [3 functions to complete]
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
    return(["mhoneywell","jjohnson199"])

######################################################################
# Complete the function below.
#
# w1 and w2 are strings. You can assume that len(w2) is exactly 1 more than len(w1)
#
# SPECIFICATION
# The function returns True if w2 is obtained from w1 by inserting one character
# into w1; otherwise the function returns False. 
#
# EXAMPLES
# isInserted("hello", "helloo") returns True
# isInserted("hello", "felloo") returns False
# isInserted("hello", "Thello") returns True
# isInserted("hello", "hebllo") returns True
# isInserted("", "y") returns True
#
######################################################################
def isInserted(w1, w2):
    
    # k will stand for the index of the inserted letter; it can have any index
    # from 0 through len(w2) - 1.
    k = 0
    while (k < len(w2)):
        
        # We split w2 into two substrings at index k. 
        
        # firstString will be w2[0..k-1]
        # ADD CODE HERE to compute firstString
        # I used 5 lines of code including a while-loop
        i = 0
        firstString = ""
        while (i <= k - 1):
            firstString = firstString + w2[i]
            i = i + 1
        
        
            
        # secondString will be w2[k+1..len(w2)-1] 
        # ADD CODE HERE to compute secondString
        # I used 5 lines of code including a while-loop
        i = k+1
        secondString = ""
        while (i < len(w2)):
            secondString = secondString + w2[i]
            i = i + 1

            
        if (w1 == firstString + secondString):
            return True
        
        k = k + 1
        
    return False

######################################################################
# Complete the function below.
# 
# w1 and w2 are strings. You can assume that w1 and w2 have the same length
#
# SPECIFICATION
# The function returns True if w2 is obtained from w1 by replacing one character
# in w1 by another character; otherwise the function returns False. 
#
# Note: The replacement character may be identical to the character being replaced.
#
# EXAMPLES
# isSubstituted("Hello", "cello") returns True
# isSubstituted("Hello", "cells") returns False
# isSubstituted("Hello", "hello") returns True
# isSubstituted("Hello", "belto") returns False
# isSubstituted("Hello", "Hello") returns True
#
######################################################################
def isSubstituted(w1, w2):
    # ADD CODE HERE to implement the following algorithm
    # Algorithm: Walk down both strings w1 and w2 and count the number of indices 
    # at which w1 and w2 have distinct characters. If this count <= 1, then the function
    # should return True; otherwise False
    count = 0
    for x in range(len(w1)):
        if (w1[x] != w2[x]):
            count = count + 1
    if (count <= 1):
            return True
    else:
            return False


######################################################################
# Complete the function below.
#
# w1 and w2 are strings. You can assume that either len(w2) == len(w1) or 
# len(w2) == len(w1) + 1 or len(w2) == len(w1) - 1.
#
# SPECIFICATION
# The function returns True if w2 is obtained from w1 by (i) replacing one character
# in w1 by another character or (ii) inserting a charecter into w1 or (iii) deleting
# a charecter from w1; otherwise the function returns False. 
#
# Note: The replacement character may be identical to the character being replaced.
#
# EXAMPLES
#
# isClose("hello", "hell") returns True
# isClose("hello", "cello") returns True
# isClose("hello", "Hello") returns True
# isClose("hello", "Helloo") returns False
# isClose("hello", "helloo") returns True
# isClose("test", "rest") returns True
# isClose("", "x") returns True
# isClose("x", "") returns True
# isClose("bell", "belt") returns True
# isClose("boll", "ball") returns True
# isClose("boll", "bales") returns False
#
######################################################################
def isClose(w1, w2):
    # ADD CODE HERE. You will need to check the lengths of w1 and w2 and
    # call isInserted and isSubstituted
    pass
    
    
    

######################################################################
# This is a simple function you can call for testing isInserted. It
# contains 8 tests. You can call isInsertedTester() and if nothing gets
# printed, then it means that isInserted has passed all 8 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 
def isInsertedTester():
    test = []
    
    # Test 1
    test.append(isInserted("hello", "helloo") == True)
    
    # Test 2
    test.append(isInserted("hello", "felloo") == False)
    
    # Test 3
    test.append(isInserted("hello", "Thello") == True)
    
    # Test 4
    test.append(isInserted("hello", "hebllo") == True)
    
    # Test 5
    test.append(isInserted("", "y") == True)
    
    # Test 6
    test.append(isInserted("bob", "blob") == True)
    
    # Test 7
    test.append(isInserted("aa", "abb") == False)
    
    # Test 8
    test.append(isInserted(" ", " ?") == True)
    
    
    for i in range(len(test)):
        if not test[i]:
            print("isInserted Test", i+1, "failed")
 

isInsertedTester()
######################################################################
# This is a simple function you can call for testing isSubstituted. It
# contains 8 tests. You can call isSubstitutedTester() and if nothing gets
# printed, then it means that isSubstituted has passed all 8 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 
def isSubstitutedTester():
    test = []
    
    # Test 1
    test.append(isSubstituted("hello", "cello") == True)
    
    # Test 2
    test.append(isSubstituted("hello", "fellw") == False)
    
    # Test 3
    test.append(isSubstituted("hello", "hexlo") == True)
    
    # Test 4
    test.append(isSubstituted("x", "y") == True)
    
    # Test 5
    test.append(isSubstituted("xx", "yy") == False)
    
    # Test 6
    test.append(isSubstituted("blow", "blob") == True)
    
    # Test 7
    test.append(isSubstituted("Jill", "Jack") == False)
    
    # Test 8
    test.append(isSubstituted("!", "?") == True)
    
    
    for i in range(len(test)):
        if not test[i]:
            print("isSubstituted Test", i+1, "failed")
 
######################################################################
# This is a simple function you can call for testing isClose. It
# contains 8 tests. You can call isCloseTester() and if nothing gets
# printed, then it means that isClose has passed all 8 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 
def isCloseTester():
    test = []
    
    # Test 1
    test.append(isClose("cello", "cell") == True)
    
    # Test 2
    test.append(isClose("hello", "fellw") == False)
    
    # Test 3
    test.append(isClose("hello", "hellos") == True)
    
    # Test 4
    test.append(isClose("x", "y") == True)
    
    # Test 5
    test.append(isClose("xx", "yy") == False)
    
    # Test 6
    test.append(isClose("blow", "blob") == True)
    
    # Test 7
    test.append(isClose("Jill", "Jack") == False)
    
    # Test 8
    test.append(isClose("!", "?") == True)
    
    
    for i in range(len(test)):
        if not test[i]:
            print("isClose Test", i+1, "failed")
 
