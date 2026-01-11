# CS1210: Lab 5 [2 functions to complete]
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
# Complete the function below.
#
# The argument L is a list of numbers. It could be empty.
#
# Specification: The function returns a list of the same length as L 
# in which the element at index i is the sum of the elements in L at 
# indices 0 through i.
#
# Examples: prefixSumList([0, 1, 2, 3, 4]) returns [0, 1, 3, 6, 10]
#           prefixSumList([1]*5) returns [1, 2, 3, 4, 5]
#           prefixSumList([1, -1, 1, -1, 1, -1]) returns [1, 0, 1, 0, 1, 0]  
#
#
######################################################################
def prefixSumList(L):
    # Initialize the prefix sums list to all 0s
    prefixSums = [0]*len(L)
    
    # This variable maintains the sum of all previous elements in L
    previousSum = 0

    # Initialize the index that walks down the list L
    i = 0    
    
    # Walk down the list L
    while (i < len(L)):
        # ADD CODE HERE to update prefixSums and previousSum
        previousSum = previousSum + L[i]
        prefixSums[i] = previousSum
        
        
        
        i = i + 1
        
    return prefixSums

######################################################################
# Complete the function below.
#
# The argument L is a list of strings of length at least 2.
# 
# Specification: The function returns a list of length 2 containing
# the longest string in L followed by the second longest string. If there
# are several choices for the longest string, the first of these in L is designated
# as the longest string. Similarly, if there are several choices for the 
# second longest string, the first of these in L is designated as the second
# longest string.
#
# Examples: twoLongestStrings(["ok", "hello", "is", "bye"]) returns
#           ["hello", "bye"]
#           twoLongestStrings(["ok", "is", "bye"]) returns 
#           ["bye", "ok"]
#           twoLongestStrings(["ok", "bed", "bye"]) returns 
#           ["bed", "bye"]
#
# Notes: In the second example above, both "ok" and "is" are second longest,
#        but "ok" is returned as the second longest because it is earliest.
#
#        In the third example above, "bed" and "bye" are both contenders
#        for the longest string, but "bed" is returned as the longest string
#        because it is earliest in L. This automatically makes "bye" the second
#        longest.
#
######################################################################
def twoLongestStrings(L):
    # We initialize the variables that maintain the longest and second-longest
    # strings
    longestString = ""
    secondLongestString = ""
    
    # walk through the strings in L
    for s in L:
        # We discover a string longer than the previous longest string
        if len(s) > len(longestString):
            secondLongestString = longestString
            longestString = s
            
        
        # We discover a string longer than the previous second-longest
        # string, though not longer than the previous longest string
        elif len(s) > len(secondLongestString):
            secondLongestString = s
            
            
            
    return [longestString, secondLongestString]
    

######################################################################
# This is a simple function you can call for testing prefixSumList. It
# contains 5 tests. You can call prefixSumListTester() and if nothing gets
# printed, then it means that prefixSumList has passed all 5 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 

def prefixSumListTester():
    test = []
    
    # Test 1
    test.append(prefixSumList([10]) == [10])
    
    # Test 2
    test.append(prefixSumList([1]*5) == [1, 2, 3, 4, 5])
    
    # Test 3
    test.append(prefixSumList([1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0])
    
    # Test 4
    test.append(prefixSumList(prefixSumList([1,1,1,1])) == [1, 3, 6, 10])
    
    # Test 5
    test.append(prefixSumList([]) == [])
    
    for i in range(len(test)):
        if not test[i]:
            print("digitSum Test", i, "failed")
 

prefixSumListTester()
######################################################################
# This is a simple function you can call for testing twoLongestStrings. It
# contains 5 tests. You can call twoLongestStringsTester() and if nothing gets
# printed, then it means that twoLongestStrings has passed all 5 tests. Otherwise,
# the output will tell you which test failed.
#
# Disclaimer: This simple tester is provided to help you gain some confidence
# that your function may be correct. The autograder will test your function more 
# extensively and may discover errors not discovered by this simple tester.
#    
###################################################################### 

def twoLongestStringsTester():
    test = []
    
    # Test 1
    test.append(twoLongestStrings(["oxygen", "chains", "second"]) == ["oxygen", "chains"])
    
    # Test 2
    test.append(twoLongestStrings(["ok", "bed", "bye"]) == ["bed", "bye"])
    
    # Test 3
    test.append(twoLongestStrings(["ok", "is", "bye"]) == ["bye", "ok"])
    
    # Test 4
    test.append(twoLongestStrings(["ok", "hello", "is", "bye"]) == ["hello", "bye"])
    
    # Test 5
    test.append(twoLongestStrings(["iron", "chlorine"]) == ["chlorine", "iron"])
    
    for i in range(len(test)):
        if not test[i]:
            print("digitSum Test", i, "failed")

