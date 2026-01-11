
# CS1210: WPS4 [2 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your work, and
#  2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid" between the two double quote marks
# to match your own hawkid. Your hawkid is the "login identifier" you use 
# to login to all University services, like  `https://myUI.uiowa.edu/'
#
#
# Note: we are not asking for your password, just the login
# identifiers: for example, mine is "sriram".
#
# Replace the pass statement below by your code
######################################################################

def signed():
    return(["mhoneywell"]) 
    
######################################################################
# Complete this function
#
# Specification: L and sL are lists, p is an integer between 0 and len(L) 
# (inclusive of 0 and len(L)), and c is a non-negative integer. The function 
# returns a new list obtained by inserting c copies of sL into L, immediately 
# before the element at index p. If p equals len(L), the c copies of sL are 
# inserted at the end of L.
#
# Examples
#
#   insertList([3, 2, 8, 4], [1, 2], 3, 4) returns 
#   [3, 2, 8, 1, 2, 1, 2, 1, 2, 1, 2, 4]. 
#
#   insertList([1, 2, 3, 4], [8, 9], 0, 2) returns [8, 9, 8, 9, 1, 2, 3, 4]
#
#   insertList([1, 2, 3, 4], [8, 9], 1, 2) returns [1, 8, 9, 8, 9, 2, 3, 4]
#
#   insertList([1, 2, 3, 4], [8, 9], 4, 2) returns [1, 2, 3, 4, 8, 9, 8, 9]
#
#   insertList([1, 2, 3, 4], [8, 9], 4, 4) returns [1, 2, 3, 4, 8, 9, 8, 9, 8, 9, 8, 9]
#
######################################################################
def insertList(L, sL, p, c):
    if (p >= 0 and p <= len(L)):
        i = 0
        while (i < c):
            for x in sL:
                L.insert(p, x)
                p = p + 1
            i = i + 1
        return L
    elif (p == len(L)):
        i = 0
        while (i < c):
            for x in sL:
                L.append(x)
                p = p + 1
            i = i + 1
        return L


######################################################################
# Complete this function
#
# Specification: Given a nested list representation L of a matrix, the function
# should return the nested list representation of the transpose of the matrix.
#
# Examples:
# 
#   matrixTranspose([[3, 10, 5], [2, 4, 11]]) should return [[3, 2], [10, 4], [5, 11]]
#   matrixTranspose([[2], [5], [7]]) should return [[2, 5, 7]]
#   matrixTranspose([[2, 3], [5, 7], [7, 9], [9, 11]]) should return [[2, 5, 7, 9], [3, 7, 9, 11]]
#   matrixTranspose([[1, 1, 1, 1]]) should return [[1], [1], [1], [1]]
#
#
# Replace the pass statement below by your code
######################################################################
def matrixTranspose(L):

    return [[L[j][i]
            for j in range(len(L))]
            for i in range(len(L[0]))]










    
    
    
