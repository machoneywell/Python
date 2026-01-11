#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CS1210: WPS2 [2 functions to complete]
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
######################################################################
def numberOfDays(m):
    if m == 0:
        m = 0
        return m
    
    if m == 1:
        m = 31
        return m
    
    if m == 2:
        m = 59
        return m
    
    if m == 3:
        m = 90
        return m
    
    if m == 4:
        m = 120
        return m
    
    if m == 5:
        m = 151
        return m
    
    if m == 6:
        m = 181
        return m
    
    if m == 7:
        m = 212
        return m
    
    if m == 8:
        m = 243
        return m
    
    if m == 9:
        m = 273
        return m
    
    if m == 10:
        m = 304
        return m
    
    if m == 11:
        m = 334
        return m
    
    if m >= 12:
        m = 365
        return m
    
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
    if month > 12 or day > 31:
        return ""

    if month == 1 and day > 31:
        return ""
    if month == 2 and day > 28:
        return ""
    if month == 3 and day > 31:
        return ""
    if month == 4 and day > 30:
        return ""
    if month == 5 and day > 31:
        return ""
    if month == 6 and day > 30:
        return ""
    if month == 7 and day > 31:
        return ""
    if month == 8 and day > 31:
        return ""
    if month == 9 and day > 30:
        return ""
    if month == 10 and day > 31:
        return ""
    if month == 11 and day > 30:
        return ""
    if month == 12 and day > 31:
        return ""

    daysInMonth = numberOfDays(month-1)
    daysPassed = daysInMonth + day
    
    rem = daysPassed % 7

    if rem == 0:
        return "Saturday"
    if rem == 1:
        return "Sunday"
    if rem == 2:
        return "Monday"
    if rem == 3:
        return "Tuesday"
    if rem == 4:
        return "Wednesday"
    if rem == 5:
        return "Thursday"
    if rem == 6:
        return "Friday"










