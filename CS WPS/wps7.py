#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:57:05 2023

@author: macbook_user
"""

# CS1210: WPS7 [1 function to complete]
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


###############################################################################
#
# Specification: The function takes 4 arguments:
#    
# cityList: is a list of strings, representing names of cities.
#
# distanceList: contains distances between pairs of cities in cityist. 
# distanceList has the same length as cityList and each element in distanceList
# is itself a list. Furthermore, distanceList[i] is a list of length i, where
# distanceList[i][j] (0 <= j <= i-1) represents the distance between cityList[i]
# and cityList[j] . 
#
# --------------
# EXAMPLE: cityList = ["X", "A", "B", "Z", "D"]
# distanceList = [[], [95], [170, 125], [150, 80, 225], [110, 175, 210, 120]]
#
# Then distanceList[2] represents the distances between city "B" and cities "X"
# and "A". More specifically, "X" is 170 miles from "B" and "A" is 125 miles from
# "B". 
#
# Note that distances between city "B" and cities "Z" and "D" appear in 
# distanceList[3][2] and distanceList[4][2] respectively. Thus the distance 
# between city "B" and "Z" is 225 and between city "B" and "D" is 210.
# --------------
# 
# name: is a name of a city; you can assume that name will be in cityList
#
# r: is a non-negative floating point number
#
# The function is required to return a list of cities at distance at most r
# from the city name. This list should contain names of cities in the same order
# as they appear in cityList.
#
# --------------
# EXAMPLE: cityList = ["X", "A", "B", "Z", "D"]
# distanceList = [[], [95], [170, 125], [150, 80, 225], [110, 175, 210, 120]]
#
# nearbyCities(cityList, distanceList, "B", 200) returns 
# ['X', 'A']
#
# nearbyCities(cityList, distanceList, "B", 210) returns
# ['X', 'A', 'D']
#
# nearbyCities(cityList, distanceList, "B", 500) returns
# ['X', 'A', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "X", 150) returns
# ['A', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "X", 0) returns
# []
#
# nearbyCities(cityList, distanceList, "X", 170) returns
# ['A', 'B', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "D", 170) returns
# ['X', 'Z']
#
# nearbyCities(cityList, distanceList, "D", 175.5) returns
# ['X', 'A', 'Z']
# 
###############################################################################

def nearbyCities(cityList, distanceList, name, r):        
    cityNameIndex = cityList.index(name)
    nearbyList = []
    for i in range(cityNameIndex):
        if (distanceList[cityNameIndex][i] <= r):
            nearbyList.append(cityList[i])
    for i in range(cityNameIndex+1, len(cityList)):
        if (distanceList[i][cityNameIndex] <= r):
            nearbyList.append(cityList[i])
    return nearbyList

    

            
                




















        
    
