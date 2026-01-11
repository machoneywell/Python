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
        line = line.strip()
        if (line == ""):
            continue
        s = line.split("|")
        genreList.append(s[0])
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

def main():
    userList = createUserList()
    movieList = createMovieList()
    rawRatings = readRatings()
    numUsers = len(userList)
    numMovies = len(movieList)
    [rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)

    wR45 = demGenreRatingFractions(userList, movieList, rLu, "F", [0, 100], [4, 5])
    wR45genres = [wR45[1], wR45[5], wR45[8], wR45[11], wR45[14]]
    mR45 = demGenreRatingFractions(userList, movieList, rLu, "M", [0, 100], [4, 5])
    mR45genres = [mR45[1], mR45[5], mR45[8], mR45[11], mR45[14]]

    wR12 = demGenreRatingFractions(userList, movieList, rLu, "F", [0, 100], [1, 2])
    wR12genres = [wR12[1], wR12[5], wR12[8], wR12[11], wR12[14]]
    mR12 = demGenreRatingFractions(userList, movieList, rLu, "M", [0, 100], [1, 2])
    mR12genres = [mR12[1], mR12[5], mR12[8], mR12[11], mR12[14]]

    youngR45 = demGenreRatingFractions(userList, movieList, rLu, "A", [20, 30], [4, 5])
    youngR45genres = [youngR45[1], youngR45[5], youngR45[8], youngR45[11], youngR45[14]]
    oldR45 = demGenreRatingFractions(userList, movieList, rLu, "A", [50, 60], [4, 5])
    oldR45genres = [oldR45[1], oldR45[5], oldR45[8], oldR45[11], oldR45[14]]

    youngR12 = demGenreRatingFractions(userList, movieList, rLu, "A", [20, 30], [1, 2])
    youngR12genres = [youngR12[1], youngR12[5], youngR12[8], youngR12[11], youngR12[14]]
    oldR12 = demGenreRatingFractions(userList, movieList, rLu, "A", [50, 60], [1, 2])
    oldR12genres = [oldR12[1], oldR12[5], oldR12[8], oldR12[11], oldR12[14]]

    genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance']

    dataMW45 = [[wR45[1], wR45[5], wR45[8], wR45[11], wR45[14]],
                [mR45[1], mR45[5], mR45[8], mR45[11], mR45[14]]]
    dataMW12 = [[wR12[1], wR12[5], wR12[8], wR12[11], wR12[14]],
                [mR12[1], mR12[5], mR12[8], mR12[11], mR12[14]]]
    dataYO45 = [[youngR45[1], youngR45[5], youngR45[8], youngR45[11], youngR45[14]],
                [oldR45[1], oldR45[5], oldR45[8], oldR45[11], oldR45[14]]]
    dataYO12 = [[youngR12[1], youngR12[5], youngR12[8], youngR12[11], youngR12[14]],
                [oldR12[1], oldR12[5], oldR12[8], oldR12[11], oldR12[14]]]





