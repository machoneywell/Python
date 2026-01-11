# CS1210: Lab 11 [3 functions to complete]
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
    return(["mhoneywell","kobulee", "1700100"])

###############################################################################
#
# SPECIFICATION: w1 and w2 are non-empty strings of the same length containing (only) 
# lower case letters. w1 and w2 are said to be neighbors if w2 can be obtained 
# from w1 by substituting a single letter with a DIFFERENT letter. The function 
# returns True if w1 and w2 are neighbors; False otherwise.
#
# REQUIREMENT: THE FUNCTION SHOULD CONTAIN A SINGLE LINE OF CODE, USING A LIST
# COMPREHENSION.
# 
# EXAMPLES:  nbrs("mouse", "house") returns True
# nbrs("mouse", "mouse") returns False
# nbrs("bell", "doll") returns False
# nbrs("bell", "belt") returns True
#
###############################################################################
def nbrs(w1, w2):
    return len([1 for x in range(len(w1)) if w1[x] != w2[x]]) == 1

###############################################################################
#
# SPECIFICATION: wordList is a non-empty list of distinct words made up of lower case
# letters, all of the same length. The function returns a dictionary whose keys 
# are the words in wordList and for each key w, the associated value is
# all the neighbors of w in the order in which they appear in wordList. Within this 
# function, you will need to call the function nbrs described above.
#
# EXAMPLES: createNbrDict(["boy", "bod", "bot", "got", "get", "soy", "toy", "tot"])
# should return the dictionary
#
# {'boy': ['bod', 'bot', 'soy', 'toy'],
# 'bod': ['boy', 'bot'],
# 'bot': ['boy', 'bod', 'got', 'tot'],
# 'got': ['bot', 'get', 'tot'],
# 'get': ['got'],
# 'soy': ['boy', 'toy'],
# 'toy': ['boy', 'soy', 'tot'],
# 'tot': ['bot', 'got', 'toy']}
#
#
# createNbrDict(["house", "mouse", "rouse", "above", "abode"])
# should return the dictionary 
#
# {'house': ['mouse', 'rouse'],
# 'mouse': ['house', 'rouse'],
# 'rouse': ['house', 'mouse'],
# 'above': ['abode'],
# 'abode': ['above']}
#
###############################################################################
def createNbrDict(wordList):
    dictionary = {}
    for i in range(len(wordList)):
        neighbors = []
        j = i + 1
        for j in range(len(wordList)):
            if (nbrs(wordList[i], wordList[j]) == True):
                neighbors.append(wordList[j])
        dictionary[wordList[i]] = neighbors
    return dictionary
    

###############################################################################
#
# SPECIFICATION: w is a word and nbrDict is a dictionary constructed by calling
# the createNbrDict function described above. We can assume that w is a key in nbrDict.
#  The function is required to return the list of UNIQUE words that are either neighbors
# of w or neighbors of neighbors of w. The order in which words appear in the returned
# list does not matter. Note that if w has a neighbor, then it will appear in the returned
# list because w is its own neighbors' neighbor.
#
# EXAMPLES: Suppose D = {'bot': ['bet', 'boy'], 'bet': ['bot'], 'boy': ['bot']}
# Then sorted(secondNeighbors('bet', nbrList)) should evaluate to 
# ['bet', 'bot', 'boy']
#
# Suppose D = {'aaa': ['aba'], 'aba': ['aaa', 'abb'], 'abb': ['aba', 'bbb'], 'bbb': ['abb']}
# Then sorted(secondNeighbors("bbb", D)) should return ['aba', 'abb', 'bbb'] and
# sorted(secondNeighbors("aba", D)) should return  ['aaa', 'aba', 'abb', 'bbb']
#
###############################################################################
def secondNeighbors(w, nbrDict):
    answer = nbrDict[w]
    for x in answer:
        answer = nbrDict[x] + answer
    return list(set(answer))
    
    

print(secondNeighbors('bet', {'bot': ['bet', 'boy'], 'bet': ['bot'], 'boy': ['bot']}))
    
