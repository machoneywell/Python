# CS1210: Lab 7 [2 functions to complete]
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
    return(["mhoneywell","kkhernandez"])

######################################################################
# Complete the function below.
#
#
# SPECIFICATION
# text contains some non-negative integers interspersed with a bunch of 
# other characters. The function should ignore all other characters
# and return the sum of the numbers in text. The string text can be empty.
#
# NOTES
# (i) Since all integers in the text are nonnegative, if an integer appeared 
# with a - sign just before it, the "-" character would be ignored just like any
# other non-digit character.
# (ii) Since we are only interested in integers, if "5.2" appeared in the text
# it would be treated as two separate integers "5" and "2".
#
#
# EXAMPLES
# sumNumbersInText("??Hello45What-45") returns 90
# sumNumbersInText("??Hello45What-45 ") returns 90
# sumNumbersInText("Hello") returns 0
# sumNumbersInText("") returns 0
# sumNumbersInText("123456789") returns 123456789
# sumNumbersInText("    123     456789    ") returns 456912
# sumNumbersInText(" 0 0  -1  123     456789    ") returns 456913
# sumNumbersInText("There0are0a bunch of numbers123here4    ") returns 127
#
# HINT
# The int() function is a built-in Python function that will attempt to convert
# a value of any type into an integer value. So int("345") will 
# evaluate to the integer 345, int("1") will evaluate to the integer 1, etc.
# You might want to use this function to simplify your code.
#
######################################################################
def sumNumbersInText(text):
    
    # A helpful list to check if a given character is a digit
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # This is the accumulator variable that will maintain the sum of all
    # the numbers in the text
    sumOfNumbers = 0
  
    # String variable that maintains the current number as a string
    # We use the int() function on this, to turn it into an integer
    currentNumber = ""
    
    # Loop for walking down the text, character by character
    for ch in text:
        # ADD CODE HERE: This code will be inside the body of the for-loop
        # My solution contains 5 lines of code
        if (ch in digits):
            currentNumber = currentNumber + ch

        else:
            if (currentNumber != ""):
                currentNumber = int(currentNumber)
                sumOfNumbers = sumOfNumbers + currentNumber
                currentNumber = ""
     



    # ADD CODE HERE
    # My solution had 2 lines of code here, to do some final clear up in
    # the situation where text ends with digits
    if (currentNumber != ""):
        sumOfNumbers = sumOfNumbers + int(currentNumber)
    
    
        
    return sumOfNumbers


######################################################################
# This is a function that you wrote for Lab 6. I have provided this function
# here so that you can use it in the subsequent function. 
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
    # Algorithm: Walk down both strings w1 and w2 and count the number of indices 
    # at which w1 and w2 have distinct characters. If this count <= 1, then the function
    # should return True; otherwise False
    i = 0
    count = 0
    while (i < len(w1)):
        if (w1[i] != w2[i]):
            count = count + 1
        i = i + 1

    return (count <= 1)

######################################################################
# Complete the function below.
# 
# 
# SPECIFICATION
# You are given a list L of distinct, equal-length strings. We define two distinct strings 
# w1 and w2 to be neighbors if w2 can be obtained from w1 by replacing one character
# in w1 by another character. In other words, w1 and w2 are neighbors if 
# isSubstituted(w1, w2) is True. The function is required to return the list of
# neighbor lists of each word in L. 
#
# EXAMPLE 1
# L = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 
#      'sided', 'tided']
#
# makeNeighborLists(L) returns
#
# [['anded'],
# ['aides'],
# ['aider'],
# ['aimed', 'aired'],
# ['ailed', 'aired'],
# ['ailed', 'aimed'],
# ['added'],
# ['sided', 'tided'],
# ['bided', 'tided'],
# ['bided', 'sided']]
#
# In this example, "added" is the first word in L and it has one neighbor
# in L, which is "anded". So ["anded"] is the first item in the returned list.
# The 4th word in L is "ailed" and it has two neighbors "aimed" and "aired".
# So the 4th item in the returned list is ["aimed", "aired"].
#
# EXAMPLE 2
# L = ['joked', 'poked', 'toked', 'yokel', 'yokes', 'yodel', 
#      'yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 
#      'yores', 'folks', 'yolky', 'folky', 'yolks']
#
# makeNeighborLists(L) returns
#
# [['poked', 'toked', 'yoked', 'jokes'],
# ['joked', 'toked', 'yoked', 'pokes'],
# ['joked', 'poked', 'yoked', 'tokes'],
# ['yokes', 'yodel', 'yoked'],
# ['yokel', 'yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 'yores'],
# ['yokel'],
# ['joked', 'poked', 'toked', 'yokel', 'yokes'],
# ['yokes', 'jokes', 'pokes', 'tokes'],
# ['joked', 'yokes', 'cokes', 'pokes', 'tokes'],
# ['poked', 'yokes', 'cokes', 'jokes', 'tokes'],
# ['toked', 'yokes', 'cokes', 'jokes', 'pokes'],
# ['yokes'],
# ['yokes'],
# ['folky', 'yolks'],
# ['folky', 'yolks'],
# ['folks', 'yolky'],
# ['folks', 'yolky']]
#
#
# NOTES
# (i) The neighbor lists should appear in the order corresponding to words in L. In 
# other words if we call the returned list nbrList, then the list of neighbors of
# the word L[0] should appear as nbrList[0].
# (ii) Each list of neighbors should contain words in the same order as in L. For
# example, the neighbor list of "ailed" should be ["aimed", "aired"] rather than
# ["aired", "aimed"].
# (iii) The neighbor relationship is only defined for distinct words. So a word
# cannot be its own neighbor.
# 
# There is no tester provided for this function. You should at the very least
# make sure that the function works correctly for the two examples above. 
######################################################################
def makeNeighborLists(wordList):
    # This is the neighbors list we are building. Below, every list of neighbors
    # in nbrList is initialized to []
    nbrList = [[]]*len(wordList)
    
    
    # This loops walks through the words w1 of wordList
    i = 0
    for w1 in wordList:
        
        # ADD CODE HERE
        # My solution contains 5 lines of code. In this code I use a second (inner)
        # loop to walk through the wordList, visiting each word w2 in the wordList
        # and determining if w2 should be a neighbor of w1
        
        
        
        
        
        
        i = i + 1
        
    return nbrList
    

######################################################################
# This is a simple function you can call for testing sumNumbersInText. It
# contains 8 tests. You can call sumNumbersInTextTester() and if nothing gets
# printed, then it means that sumNumbersInText has passed all 8 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 

def sumNumbersInTextTester():
    test = []
    
    # Test 1
    test.append(sumNumbersInText("??Hello45What-45") == 90)
    
    # Test 2
    test.append(sumNumbersInText("??Hello45What-45 ") == 90)
    
    # Test 3
    test.append(sumNumbersInText("Hello") == 0)
    
    # Test 4
    test.append(sumNumbersInText("123456789") == 123456789)
    
    # Test 5
    test.append(sumNumbersInText("    123     456789    ") == 456912)
    
    # Test 6
    test.append(sumNumbersInText(" 0 0  -1  123     456789    ") == 456913)
    
    # Test 7
    test.append(sumNumbersInText("There0are0a bunch of numbers123here4    ") == 127)
    
    # Test 8
    test.append(sumNumbersInText("") == 0)
    
    
    for i in range(len(test)):
        if not test[i]:
            print("isInserted Test", i+1, "failed")
 
