# CS1210: Lab1 [2 functions to complete]
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
    return(["mhoneywell","khernandez"])

######################################################################
# Define the two functions CollatzLength and CollatzMax below
######################################################################

def CollatzLength(x):
    counter = 1
    while x > 1:
        if x % 2 == 0:
            x = x / 2
            counter = counter+1
        else:
            x = x * 3 + 1
            counter = counter+1
            
    return counter


def CollatzMax(x):
    pass
    

y = CollatzLength(12)
print (y)


















