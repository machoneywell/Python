#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CS1210: Lab 2 [2 functions to complete]
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
    return(["mhoneywell","prai3"])

######################################################################
# Define the two functions isPrime and maxPrime below
######################################################################

######################################################################
# Assume that n is a positive integer
# 
# Specification: isPrime(n) returns True if n is a prime and isPrime(n) 
# returns False if n is not a prime. 
#
# Examples: isPrime(5) returns True and isPrime(6) returns False
#
# You can assume that 1 is classified as a prime.
######################################################################

def isPrime(n):
    
    #Initializing the first possible factor
    possibleFactor = 2

    #Here you should initialize any other variables you need
    #in the rest of the code
    
    while (possibleFactor < n):
        
        # Check if possibleFactor is really a factor of n
        rem = n % possibleFactor
        if rem == 0:
            # This means that possibleFactor is actually a factor of n
            # ADD CODE HERE that responds to this situation
            return False
            
        # Generate the next possibleFactor
        possibleFactor = possibleFactor + 1

        return True
    
        # end of the while-loop
        
    # Here you are outside the while-loop, which means that you have
    # completed processing all possible factors of n
    # AADD CODE HERE to return the correct answer 
    
  

######################################################################
# Assume that n1 and n2 are positive integers
# 
# Specification: maxPrime(n1, n2) returns the largest prime number n such
# that n1 <= n <= n2. If there is no prime between n1 and n2 (inclusive of
# n1 and n2) then maxPrime(n1, n2) returns None
#
# Examples: maxPrime(5, 10) returns 7
#           maxPrime(5, 20) returns 19
#           maxPrime(11, 11) returns 11 
#           maxPrime(10, 4) returns None
#           maxPrime(10, 10) returns None
#
# You can also assume that 1 is classified as a prime.
######################################################################      
        
def maxPrime(n1, n2):
    # Initialize n to n1, the first value in the range [n1, n2]
    n = n1
    
    # Initialize largestPrime to None; this variable will keep
    # track of the largest prime in the range [n1, n2]
    largestPrime = None
    
    # This while-loop generates all candidate prime numbers.
    # As this while-loop is executed n takes on the values
    # n1, n1+1, n1+2, ..., n2
    while(n <= n2):
        # You will need to ADD CODE HERE to the body of this 
        # while-loop to test if n is a prime and if largestPrime
        # needs to be updated. You should call the function isPrime
        # defined above.
        if isPrime() == True:
            largestPrime = n
        n = n + 1
        
        
        
        # end of while-loop
        
   return largestPrime
    
  
    
    
    
    
    
    
    
