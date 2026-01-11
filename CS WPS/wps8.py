
# CS1210: WPS8 [1 function to complete]
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
# Complete the following function by replacing pass with code.
#
# Specification: text is an arbitrary, possibly empty, string. The function 
# partitions text into sentences and returns the list of sentences. Note that
# each sentence is also a string. The definition of a sentence is that it is a 
# contiguous sequence of characters that ends with one of the following 3
# delimiters: ".", "?", or "!" 
#
# NOTES:
# (1) The last sentence may not end at one of the delimiters because text itself 
# may no end with a delimiter.
# (2) You cannot throw away any characters in text. Every character (including
# white spaces) should appear in some senetence.
#
# EXAMPLES: text = 'Quick! Find that ball. Did you find it? What is going on? Oh no!'
# createSentences(text) should return ['Quick!', ' Find that ball.', ' Did you find it?', 
# ' What is going on?', ' Oh no!']
# 
# text = "Quick! Find that ball. Did you find it? What is going"
# createSentences(text) should return ['Quick!', ' Find that ball.', ' Did you find it?', 
# ' What is going']
#
# text = "There is no deliminiter in this text"
# createSentences(text) should return ['There is no deliminiter in this text']
# 
# createSentences("....") should return ['.', '.', '.', '.']
#
# createSentences("") should return []
#
# createSentences("Okey. Let us, do it.") should return ['Okey.', ' Let us, do it.']
#
###############################################################################   
def createSentences(text):
    delimiters = [".", "?", "!"]
    final = []
    current = ""
    for i in text:
        if (i not in delimiters):
            current = current + i
        if (i in delimiters):
            final.append(current + i)
            current = ""
    if (current != ""):
        final.append(current)
    return final







