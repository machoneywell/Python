def createUserList():
    userList = []
    f = open("ml-100k/u.user")
    for line in f:
        dictionary = {}
        s = line.split('|')
        dictionary["age"] = int(s[1])
        dictionary["gender"] = s[2]
        dictionary["occupation"] = s[3]
        dictionary["zip"] = s[4].strip()
        userList.append(dictionary)
    f.close()
    return userList

def createMovieList():
    movieList = []
    f = open("ml-100k/u.item", encoding='windows-1252')
    for line in f:
        dictionary = {}
        s = line.split('|')
        dictionary["title"] = s[1]
        dictionary["release date"] = s[2]
        dictionary["video release date"] = s[3]
        dictionary["IMDB url"] = s[4]
        genre = s[5:]
        for i in range(len(genre)):
            genre[i] = int(genre[i])
        dictionary["genre"] = genre
        movieList.append(dictionary)
    f.close()
    return movieList

def readRatings():
    rawRatings = []
    f = open("ml-100k/u.data")
    for line in f:
        s = line.split()
        rawRatings.append((int(s[0]), int(s[1]), int(s[2])))
    f.close()
    return rawRatings

def createRatingsDataStructure(numUsers, numItems, ratingTuples):
    rLu = [{} for i in range(numUsers)]
    rLm = [{} for i in range(numItems)]
    for i in ratingTuples:
        rLu[i[0] - 1][i[1]] = i[2]
        rLm[i[1] - 1][i[0]] = i[2]
    return (rLu, rLm)

def createGenreList():
    genreList = []
    f = open("ml-100k/u.genre")
    for line in f:
        s = line.split("|")
        genreList.append(s[0])
    genreList.pop()
    f.close()
    return genreList

def demGenreRatingFractions(userList, movieList, rLu, gender, ageRange, ratingRange):
    users = []
    for i in range(len(userList)):
        if ((userList[i]['age'] >= ageRange[0]) and (userList[i]['age'] < ageRange[1])):
            if ((gender == "F") and (userList[i]['gender'] == "F")):
                users.append(i)
            elif ((gender == "M") and (userList[i]['gender'] == "M")):
                users.append(i)
            elif ((gender == "A") and ((userList[i]['gender'] == "F") or (userList[i]['gender'] == "M"))):
                users.append(i)

    denominator = 0
    genreRatings = [0 for i in range(19)]
    for i in users:
        for key in rLu[i]:
            denominator += 1
            if ((rLu[i][key] >= ratingRange[0]) and (rLu[i][key] <= ratingRange[1])):
                for j in range(len(movieList[key-1]['genre'])):
                    if (movieList[key-1]['genre'][j] == 1):
                        genreRatings[j] += 1
    if (denominator == 0):
        return [None for n in genreRatings]
    return [n/denominator for n in genreRatings]














