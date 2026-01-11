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






def randomPrediction(u, m):
    import random
    return random.randint(1, 5)

def meanUserRatingPrediction(u, m, rLu):
    ratings = 0
    if (rLu[u-1] == {}):
        return None
    for i in rLu[u-1]:
        ratings = ratings + rLu[u-1][i]
    meanRating = ratings / len(rLu[u-1]) 
    return meanRating

def meanMovieRatingPrediction(u, m, rLm):
    ratings = 0
    if (rLm[m-1] == {}):
        return None
    for i in rLm[m-1]:
        ratings += rLm[m-1][i]
    meanMovieRating = ratings / len(rLm[m-1]) 
    return meanMovieRating

def demRatingPrediction(u, m, userList, rLu):
    users = []
    gender = userList[u-1]['gender']
    ageRange = [userList[u-1]['age'] - 5, userList[u-1]['age'] + 5]
    for i in range(len(userList)):
        if (i != u-1):
            if ((userList[i]['gender'] == gender) and ((userList[i]['age'] >= ageRange[0]) and (userList[i]['age'] <= ageRange[1]))):
                users.append(i)
    if (users == []):
        return None
    ratings = []
    allRatings = 0
    for i in users:
        if (m in rLu[i]):
            ratings.append(rLu[i][m])
    for j in ratings:
        allRatings += j
    if (ratings == []):
        return None
    meanRating = allRatings / len(ratings)
    return meanRating

def genreRatingPrediction(u, m, movieList, rLu):
    movies = []
    mGenres = movieList[m-1]['genre']
    for i in range(len(movieList)):
        if (i != m-1):
            for j in range(len(mGenres)):
                if (movieList[i]['genre'][j] == 1 and mGenres[j] == 1):
                    if (i not in movies):
                        movies.append(i)
    if (movies == []):
        return None
    ratings = []
    allRatings = 0
    for i in movies:
        if (i+1 in rLu[u-1]):
            ratings.append(rLu[u-1][i+1])
    for j in ratings:
        allRatings += j
    if (ratings == []):
        return None
    meanRating = allRatings / len(ratings)
    return meanRating

def partitionRatings(rawRatings, testPercent):
    import random
    randRatings = random.sample(rawRatings, len(rawRatings))
    percentAmount = len(randRatings) * (testPercent / 100)
    percentAmount = round(percentAmount)
    return ((randRatings[percentAmount:]), (randRatings[:percentAmount]))

def rmse(actualRatings, predictedRatings):
    import math
    sums = 0
    count = 0
    for i in range(len(actualRatings)):
        if ((actualRatings[i] != None) and (predictedRatings[i] != None)):
            difference = actualRatings[i] - predictedRatings[i]
            sums += difference * difference
            count += 1
    if (count == 0):
        return None
    mean = sums / count
    return math.sqrt(mean)

def similarity(u, v, rLu):
    import math
    
    # Finding list of movies both users have rated
    movies = []
    for i in rLu[u-1]:
        if (i in rLu[v-1]):
            movies.append(i)
    if (movies == []):
        sim = 0
        return sim
    
    # Finding mean ratings for users u and v
    ratings = 0
    ri = 0
    for i in rLu[u-1]:
        ratings += rLu[u-1][i]
        ri = ratings / len(rLu[u-1])
    ratings = 0
    rj = 0
    for j in rLu[v-1]:
        ratings += rLu[v-1][j]
        rj = ratings / len(rLu[v-1])
            
    # Finding numerator
    allSimilarRatings = []
    for i in movies:
        allSimilarRatings.append((rLu[u-1][i] - ri) * (rLu[v-1][i] - rj))
        
    numerator = 0
    for i in allSimilarRatings:
        numerator += i

    # Denom for i
    diffiRatings = []
    for i in movies:
        diffiRatings.append((rLu[u-1][i] - ri) ** 2)
    sumOfi = 0
    for i in diffiRatings:
        sumOfi += i

    # Denom for j
    diffjRatings = []
    for i in movies:
        diffjRatings.append((rLu[v-1][i] - rj) ** 2)
    sumOfj = 0
    for i in diffjRatings:
        sumOfj += i
        
    denominator = (math.sqrt(sumOfi)) * (math.sqrt(sumOfj))
    if ((numerator == 0) or (denominator == 0)):
        sim = 0
    else:
        sim = numerator / denominator
    return sim

def kNearestNeighbors(u, rLu, k):
    friends = []
    for i in range(len(rLu)):
        simm = similarity(u, i+1, rLu)
        friends.append((i+1, simm))
    friends.pop(u-1)
    friends.sort(key = lambda x:x[1], reverse = True)
    friends = friends[:k]

    return friends

def CFRatingPrediction(u, m, rLu, friends):
    ratings = 0
    for i in rLu[u-1]:
        ratings += rLu[u-1][i]
        ri = ratings / len(rLu[u-1])
        
    users = []
    for i in range(len(friends)):
        if (friends[i][0] == u-1):
            continue
        if (m in rLu[friends[i][0]-1]):
            users.append(friends[i][0])
            
    if users == []:
        p = ri
        return p
            
    numSums = []
    denomSums = []
    for j in users:
        ratings = 0
        for i in rLu[j-1]:
            ratings += rLu[j-1][i]
        rj = ratings / len(rLu[j-1])
        numSums.append((rLu[j-1][i] - rj) * (similarity(u, j+1, rLu)))
        denomSums.append(abs(similarity(u, j+1, rLu)))
        
    numerator = 0
    for i in numSums:
        numerator += i

    denominator = 0
    for i in denomSums:
        denominator += i

    if ((numerator == 0) or (denominator == 0)):
        p = ri
        return p

    p = ri + (numerator / denominator)
    
    return p
            










    
