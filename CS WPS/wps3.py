
# CS1210: WPS3 [2 functions to complete]
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
######################################################################

def signed():
    return(["mhoneywell"]) 
    
######################################################################
# Complete this function
#
# The argument m can be any non-negative integer
# Examples: numberOfDays(0) should be 0, numberOfDays(1) should be 31,
# numberOfDays(2) should be 59. For any m 12 or more, numberOfDays(m) should
# be 365.
#
# Replace the pass statement below by your code
######################################################################
def numberOfDays(m):
    # Initialization
    monthIndex = 1 # variable representing the current month
    daysElapsed = 0 # an accumulator variable to which we will add days in each month
    
    # This loop runs through all months 1 through m
    reducedM = min(m, 12)
    while (monthIndex <= reducedM):
    # monthIndex is the current month and depending on what the monthIndex is, we assign
    # to a variable called daysInMonth, the number of days in the current month        
        if (monthIndex == 4) or (monthIndex == 6) or (monthIndex == 9) or (monthIndex == 11):
            daysInMonth = 30
            
        elif (monthIndex == 2):
            daysInMonth = 28
    
        else:
            daysInMonth = 31
       
        # Update the accumulator variable by adding the days in the current month
        daysElapsed = daysElapsed + daysInMonth

        # Increment the monthIndex
        monthIndex = monthIndex + 1
    
    return daysElapsed


######################################################################
# Complete this function
#
# The arguments month and day can be any positive integers. 
# Examples: weekDay(1, 28) should be "Saturday" , weekDay(2, 3) should be 
# "Friday".
# weekDay(2, 30), weekDay(20, 5), and weekDay (10, 200) should all be "".
#
######################################################################
def weekDay(month, day):
    dayNumbers2Names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    if (month > 12) or (day > 31):
        return ""
    elif (month == 2) and (day > 28):
        return ""
    elif ((month == 4) or (month == 6) or (month == 9) or (month == 11) and (day > 30)):
        return ""
    
    daysInMonth = numberOfDays(month-1)
    daysPassed = daysInMonth + day

    rem = daysPassed % 7
    i = 0

    while (i <= len(dayNumbers2Names) -1):
        if (i == rem):
            return dayNumbers2Names[i]
        i = i + 1
        
    
######################################################################
# Complete this function
#
# The argument L is a list of numbers as argument. The function is required
# to return the largest sum of a pair of consecutive numbers in the list. 
# If the list has 0 elements or 1 element, the function should return None.
# Example: If L = [3, -4, 2, 10, -3, 12] then all the pairs of consecutive 
# numbers are:
#
# (3, -4), (-4, 2), (2, 10), (10, -3), (-3, 12)
#
# and these pairs have sums
#
# -1, -2, 12, 7, and 9
#
# respectively. So your function should return 12.
#
# Replace the pass statement below by your code
######################################################################
def maxPairSum(L):
    if (len(L) <= 1):
        return None
    sumsOfPairsList = []
    i = 0
    while (i < len(L)-1):
        n = L[i] + L[i+1]
        sumsOfPairsList.append(n)
        i = i + 1
        maxSum = max(sumsOfPairsList)
    return maxSum













