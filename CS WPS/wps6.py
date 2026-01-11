#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 04:46:22 2023

@author: macbook_user
"""

# CS1210: WPS6 [2 functions to complete]
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
# Replace the pass statement by code.
#
# Specification provided in lecture on Fri, March 3rd and also in assignment.
######################################################################
def evaluateWord(hiddenWord, userGuess):
    letterStatus = [0] * 5
    i = 0
    for x in userGuess:
        if (x == hiddenWord[i]):
            letterStatus[i] = 2
            i = i + 1
        elif ((x in hiddenWord) and (x != hiddenWord[i])):
            letterStatus[i] = 1
            i = i + 1
        else:
            letterStatus[i] = 0
            i = i + 1
    return letterStatus
            
######################################################################
# Replace the pass statement by code.
#
# Specification provided in lecture on Mon, March 6th and also in assignment.
######################################################################
def updateGlobalLetterStatus(globalLetterStatus, userGuess, letterStatus):
    i = 0
    for x in userGuess:
        letterLocation = ord(x) - ord('a')
        globalLetterStatus[letterLocation] = letterStatus[i]
        i = i + 1
    return globalLetterStatus







