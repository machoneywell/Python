# CS1210: Lab 8 [3 functions to complete]
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
    return(["hawkid1","hawkid2"])

######################################################################
# Complete the function below by replacing pass by code.
#
# SPECIFICATION
# text is a possibly empty string that contains some integers (which could 
# be negative) interspersed with a bunch of other characters. The function 
# should ignore all other characters and return the sum of the integers in text.
# Since integers can be negative, the function does need to pay attention to
# "-" when it appears just before digits.
#
#
# EXAMPLES
# sumIntegersInText("??Hello45What-45") returns 0
# sumIntegersInText("??Hello45What-45 and+2") returns 2
# sumIntegersInText("Hello-2-2") returns -4
# sumIntegersInText("") returns 0
# sumIntegersInText("-123456789") returns -123456789
# sumIntegersInText("    123     -456789    ") returns -456666
# sumIntegersInText(" 0 0  -1-123     456789    ") returns 456665
# sumIntegersInText("There-0are0a bunch of numbers123here-4    ") returns 119
#
# HINT: This function is similar to the function sumNumbersInText(text)
# you wrote for Lab 7. I am including that function below so that you
# can copy-and-paste code from that function into this function.
#
######################################################################
def sumIntegersInText(text):
    pass

######################################################################
#
# This is the function from Lab 7, for your reference.
#
######################################################################
def sumNumbersInText(text):
    
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # This is the accumulator variable that will maintain the sum of all
    # the numbers in the text
    sumOfNumbers = 0
  
    # String variable that maintains the current number as a string
    currentNumber = ""
    
    # Loop for walking down the text, character by character
    for ch in text:
        if ch in digits:
            currentNumber = currentNumber + ch
        elif currentNumber != "":
            sumOfNumbers = sumOfNumbers + int(currentNumber)
            currentNumber = ""
     
    if (currentNumber != ""):
        sumOfNumbers = sumOfNumbers + int(currentNumber)
        
    return sumOfNumbers


######################################################################
# Complete the function below by replacing pass by code.
#
# SPECIFICATION
# fileName is a string representing the name of text file. You can assume
# that this text file is in your working directory. The file contains some 
# integers (which could be negative) interspersed with a bunch of other characters. 
# The function should ignore all other characters and return the sum of all the integers 
# in the file.
#
# EXAMPLE: Suppose there is a text file called integers.txt in your working 
# directory. Then this function will be called as sumIntegersInFile("numbers.txt")
#
# NOTE: Every line ends with an "end-of-line" character. Therefore, no integer 
# occurs spread across multiple lines.
#
# HINT: You need to open a file, read it line by line, and call sumIntegersInText(line)
# (defined above) repeatedly to get the sum of integers in each line. You will
# need to add the sums you get for all the lines to get the final sum.
#
# NOTE ABOUT GRADING: Even if you cannot get sumIntegersInText completed correctly,
# you can get full points for this function by making sure that it correctly
# works when we assume that integers in the text are non-negative.
######################################################################
def sumIntegersInFile(fileName):
    # My function has 5 lines of code
    pass

######################################################################
# Complete the function below.
#
# SPECIFICATION
# cityList is an empty list when it is passed in. The function should read
# from the file "miles.dat" that has been posted for Project 1. The function
# should load the names of the 128 cities in this data file into cityList.
# Since the names of cities are not all distinct (e.g., there are
# two Wilmington’s) you should store the name of the city along with the name 
# of the state that the city belongs to. One way to do this would be to represent 
# each city by a string “cityName stateName”. For example, the first city in 
# the data set is Youngstown, which is a city in Ohio. You would represent 
# this city by the string “Youngstown OH” with the city name and the two-letter 
# state code being separated by a single blank. The cities should by stored in 
# the list cityList in the order in which they appear in the data file. For example, 
# cityList[0] should be “Youngstown OH”, cityList[1] should be “Yankton SD” etc.
#
#
# This function returns nothing. It simply modifies cityList in place. In
# the partial code I provide below, I use the append method to do this.
######################################################################
def loadCityData(cityList):
    
    f = open("miles.dat")
    for line in f:
        # Check if line starts with an upper case letter. Such lines contain
        # information about cities.
        if ("A" <= line[0]) and (line[0] <= "Z"):
            # ADD CODE HERE to extract cityName and stateCode
            
            
           
            
            cityList.append(cityName + " " + stateCode)