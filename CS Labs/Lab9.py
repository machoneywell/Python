# CS1210: Lab 9 [2 functions to complete]
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
# 
# ADDITIONALLY: Please replace your "groupcode" by the code for your 
# group shown by your Lab TA. 
#
######################################################################

def signed():
    return(["mhoneywell","dyakub", "1461530"])


######################################################################
#
# Complete the function below.
#
# SPECIFICATION
# text is an arbitrary, possible empty, string. The
# function is required to return the list of words in text, in the order
# in which they appear in text. The case of the letters in the extracted
# words should exactly match their case in text. 
#
# A word is defined to be a contiguous sequence of letters (lower or 
# upper case). Each word should be preceded by a non-letter, unless it
# starts text. Similarly, each word should be succeeded by a non-letter,
# unless it ends text.
#
# EXAMPLES: 
#    extractWords("Best? Not, really!")
#    returns ['Best', 'Not', 'really']
#    
#    extractWords("Ten = 10, Twenty=20")
#    returns ['Ten', 'Twenty']
#    
#    extractWords("conda: base (Python 3.9.13)")
#    returns ['conda', 'base', 'Python']
#    
#    extractWords("TestBestLest")
#    returns ['TestBestLest']
#    
#    extractWords("")
#    returns []
#   
######################################################################
def extractWords(text):

    # Initialize a string of ALL  characters
    allchrs = "".join([chr(x) for x in range(32, 127)])
    
    # Initialize a string of lower case letters 
    letters = "abcdefghijklmnopqrstuvwxyz"
    newText = ""
    for ch in text:
        if (ch.aplha()):
            newText += ch
        elif not(ch.alpha()):
            text.replace(ch, " ")
            newText += ch
    return newText
    

    # Walk through the sequence of characters and for every
    # character that is not a letter (upper case or lower case),
    # replace it by a space. Then split the text.
    # ADD CODE HERE. My solution contains 4 lines of code including
    # the return statement

print(extractWords("Best? Not, really!"))

######################################################################
# Complete the function below.
#
# SPECIFICATION
# The function reads the 128 cities from "miles.dat" and returns their
# names in a list, sorted in "east to west" order. The names of the cities
# should be exactly as specified in Project 1, with the city name followed
# by a single space followed by the state code.
#
# EXAMPLE
# The first five elements in this list should be
#
# 'Worcester MA', 'Saint Johnsbury VT', 'Springfield MA', 'Rutland VT', 'Waterbury CT',
# 
# in that order. And the last five elements in the list should be
#
# 'San Francisco CA', 'Tacoma WA', 'Santa Rosa CA', 'Salem OR', 'Vancouver BC'
#
# in that order
#
# ALGORITHM
# In order to sort the cities in "east to west" order you should extract the city
# name, state code, and longitude from the "city lines" in miles.dat and 
# construct a list
# 
# [[longitude1, city1], [longitude2, city2], [longitude3, city3],....]
#
# Then you can simply call the sort method on this list and it will sort the
# list in increasing order of longitude, which corresponds to an "east to west"
# order.
# 
# Finally, you need to pick out the names of cities from this sorted list
# in order.
#
######################################################################
def sortCitiesEastToWest():
    
    f = open("miles.dat")
    longCityList = []
    for line in f:
        # Check if line starts with an upper case letter. Such lines contain
        # information about cities. From such lines extract city name, state code
        # and longitude and append to longCityList
        # ADD CODE HERE. My solution contains 5 lines of code
        if (line[0].isupper()):
            i = 0
            while (line[i] != ","):
                i = i + 1
                
            cityName = line[:i]
            stateCode = line[i + 2:i + 4] 
            cityAndState = (cityName + " " + stateCode)

            #lomg finder
            commaIndex = line.rindex(",")
            bracketIndex = line.rindex("]")

            longitude = int(line[commaIndex + 1: bracketIndex])

            longCityList.append([longitude, cityAndState])
    

         

    # Sort the list of longitudes and cities. Since longitudes appear before cities
    # in each sublist, the sorting is on the basis of the longitudes
    longCityList.sort()
    # Walk down the sorted list of longitudes and cities and pick out the cities
    # and place them in a list
    # ADD CODE HERE. My solution contains 4 lines of code, including a return 
    # statement.
    longCityListNew = []
    for i in longCityList:
        j = 1
        longCityListNew.append(i[1])
        j = j + 1
    

    return longCityListNew




    
