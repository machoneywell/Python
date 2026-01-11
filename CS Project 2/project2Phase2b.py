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


userList = createUserList()
movieList = createMovieList()
rawRatings = readRatings()
numUsers = len(userList)
numMovies = len(movieList)
[rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)
genreList = createGenreList()


# Round 1
import copy
copyRawRatings1 = copy.deepcopy(rawRatings)
[trainingSet1, testSet1] = partitionRatings(copyRawRatings1, 20)
[trainingRLu1, trainingRLm1] = createRatingsDataStructure(numUsers, numMovies, trainingSet1)

randPrediction1 = []
meanUserPrediction1 = []
meanMoviePrediction1 = []
demPrediction1 = []
genrePrediction1 = []

actualRatings1 = []
for u, m, r in testSet1:
    actualRatings1.append(r)

for u, m, r in testSet1:
    randPrediction1.append(randomPrediction(u, m))
    meanUserPrediction1.append(meanUserRatingPrediction(u, m, trainingRLu1))
    meanMoviePrediction1.append(meanMovieRatingPrediction(u, m, trainingRLm1))
    demPrediction1.append(demRatingPrediction(u, m, userList, trainingRLu1))
    genrePrediction1.append(genreRatingPrediction(u, m, movieList, trainingRLu1))

randPredictionRMSE1 = rmse(actualRatings1, randPrediction1)
meanUserPredictionRMSE1 = rmse(actualRatings1, meanUserPrediction1)
meanMoviePredictionRMSE1 = rmse(actualRatings1, meanMoviePrediction1)
demPredictionRMSE1 = rmse(actualRatings1, demPrediction1)
genrePredictionRMSE1 = rmse(actualRatings1, genrePrediction1)


### Round 2
copyRawRatings2 = copy.deepcopy(rawRatings)
[trainingSet2, testSet2] = partitionRatings(copyRawRatings2, 20)
[trainingRLu2, trainingRLm2] = createRatingsDataStructure(numUsers, numMovies, trainingSet2)

randPrediction2 = []
meanUserPrediction2 = []
meanMoviePrediction2 = []
demPrediction2 = []
genrePrediction2 = []

actualRatings2 = []
for u, m, r in testSet2:
    actualRatings2.append(r)

for u, m, r in testSet2:
    randPrediction2.append(randomPrediction(u, m))
    meanUserPrediction2.append(meanUserRatingPrediction(u, m, trainingRLu2))
    meanMoviePrediction2.append(meanMovieRatingPrediction(u, m, trainingRLm2))
    demPrediction2.append(demRatingPrediction(u, m, userList, trainingRLu2))
    genrePrediction2.append(genreRatingPrediction(u, m, movieList, trainingRLu2))

randPredictionRMSE2 = rmse(actualRatings2, randPrediction2)
meanUserPredictionRMSE2 = rmse(actualRatings2, meanUserPrediction2)
meanMoviePredictionRMSE2 = rmse(actualRatings2, meanMoviePrediction2)
demPredictionRMSE2 = rmse(actualRatings2, demPrediction2)
genrePredictionRMSE2 = rmse(actualRatings2, genrePrediction2)

### Round 3
copyRawRatings3 = copy.deepcopy(rawRatings)
[trainingSet3, testSet3] = partitionRatings(copyRawRatings3, 20)
[trainingRLu3, trainingRLm3] = createRatingsDataStructure(numUsers, numMovies, trainingSet3)

randPrediction3 = []
meanUserPrediction3 = []
meanMoviePrediction3 = []
demPrediction3 = []
genrePrediction3 = []

actualRatings3 = []
for u, m, r in testSet3:
    actualRatings3.append(r)

for u, m, r in testSet3:
    randPrediction3.append(randomPrediction(u, m))
    meanUserPrediction3.append(meanUserRatingPrediction(u, m, trainingRLu3))
    meanMoviePrediction3.append(meanMovieRatingPrediction(u, m, trainingRLm3))
    demPrediction3.append(demRatingPrediction(u, m, userList, trainingRLu3))
    genrePrediction3.append(genreRatingPrediction(u, m, movieList, trainingRLu3))

randPredictionRMSE3 = rmse(actualRatings3, randPrediction3)
meanUserPredictionRMSE3 = rmse(actualRatings3, meanUserPrediction3)
meanMoviePredictionRMSE3 = rmse(actualRatings3, meanMoviePrediction3)
demPredictionRMSE3 = rmse(actualRatings3, demPrediction3)
genrePredictionRMSE3 = rmse(actualRatings3, genrePrediction3)

### Round 4
copyRawRatings4 = copy.deepcopy(rawRatings)
[trainingSet4, testSet4] = partitionRatings(copyRawRatings4, 20)
[trainingRLu4, trainingRLm4] = createRatingsDataStructure(numUsers, numMovies, trainingSet4)

randPrediction4 = []
meanUserPrediction4 = []
meanMoviePrediction4 = []
demPrediction4 = []
genrePrediction4 = []

actualRatings4 = []
for u, m, r in testSet4:
    actualRatings4.append(r)

for u, m, r in testSet4:
    randPrediction4.append(randomPrediction(u, m))
    meanUserPrediction4.append(meanUserRatingPrediction(u, m, trainingRLu4))
    meanMoviePrediction4.append(meanMovieRatingPrediction(u, m, trainingRLm4))
    demPrediction4.append(demRatingPrediction(u, m, userList, trainingRLu4))
    genrePrediction4.append(genreRatingPrediction(u, m, movieList, trainingRLu4))

randPredictionRMSE4 = rmse(actualRatings4, randPrediction4)
meanUserPredictionRMSE4 = rmse(actualRatings4, meanUserPrediction4)
meanMoviePredictionRMSE4 = rmse(actualRatings4, meanMoviePrediction4)
demPredictionRMSE4 = rmse(actualRatings4, demPrediction4)
genrePredictionRMSE4 = rmse(actualRatings4, genrePrediction4)

### Round 5
copyRawRatings5 = copy.deepcopy(rawRatings)
[trainingSet5, testSet5] = partitionRatings(copyRawRatings5, 20)
[trainingRLu5, trainingRLm5] = createRatingsDataStructure(numUsers, numMovies, trainingSet5)

randPrediction5 = []
meanUserPrediction5 = []
meanMoviePrediction5 = []
demPrediction5 = []
genrePrediction5 = []

actualRatings5 = []
for u, m, r in testSet5:
    actualRatings5.append(r)

for u, m, r in testSet5:
    randPrediction5.append(randomPrediction(u, m))
    meanUserPrediction5.append(meanUserRatingPrediction(u, m, trainingRLu5))
    meanMoviePrediction5.append(meanMovieRatingPrediction(u, m, trainingRLm5))
    demPrediction5.append(demRatingPrediction(u, m, userList, trainingRLu5))
    genrePrediction5.append(genreRatingPrediction(u, m, movieList, trainingRLu5))

randPredictionRMSE5 = rmse(actualRatings5, randPrediction5)
meanUserPredictionRMSE5 = rmse(actualRatings5, meanUserPrediction5)
meanMoviePredictionRMSE5 = rmse(actualRatings5, meanMoviePrediction5)
demPredictionRMSE5 = rmse(actualRatings5, demPrediction5)
genrePredictionRMSE5 = rmse(actualRatings5, genrePrediction5)

### Round 6
copyRawRatings6 = copy.deepcopy(rawRatings)
[trainingSet6, testSet6] = partitionRatings(copyRawRatings6, 20)
[trainingRLu6, trainingRLm6] = createRatingsDataStructure(numUsers, numMovies, trainingSet6)

randPrediction6 = []
meanUserPrediction6 = []
meanMoviePrediction6 = []
demPrediction6 = []
genrePrediction6 = []

actualRatings6 = []
for u, m, r in testSet6:
    actualRatings6.append(r)

for u, m, r in testSet6:
    randPrediction6.append(randomPrediction(u, m))
    meanUserPrediction6.append(meanUserRatingPrediction(u, m, trainingRLu6))
    meanMoviePrediction6.append(meanMovieRatingPrediction(u, m, trainingRLm6))
    demPrediction6.append(demRatingPrediction(u, m, userList, trainingRLu6))
    genrePrediction6.append(genreRatingPrediction(u, m, movieList, trainingRLu6))

randPredictionRMSE6 = rmse(actualRatings6, randPrediction6)
meanUserPredictionRMSE6 = rmse(actualRatings6, meanUserPrediction6)
meanMoviePredictionRMSE6 = rmse(actualRatings6, meanMoviePrediction6)
demPredictionRMSE6 = rmse(actualRatings6, demPrediction6)
genrePredictionRMSE6 = rmse(actualRatings6, genrePrediction6)

### Round 7
copyRawRatings7 = copy.deepcopy(rawRatings)
[trainingSet7, testSet7] = partitionRatings(copyRawRatings1, 20)
[trainingRLu7, trainingRLm7] = createRatingsDataStructure(numUsers, numMovies, trainingSet7)

randPrediction7 = []
meanUserPrediction7 = []
meanMoviePrediction7 = []
demPrediction7 = []
genrePrediction7 = []

actualRatings7 = []
for u, m, r in testSet7:
    actualRatings7.append(r)

for u, m, r in testSet7:
    randPrediction7.append(randomPrediction(u, m))
    meanUserPrediction7.append(meanUserRatingPrediction(u, m, trainingRLu7))
    meanMoviePrediction7.append(meanMovieRatingPrediction(u, m, trainingRLm7))
    demPrediction7.append(demRatingPrediction(u, m, userList, trainingRLu7))
    genrePrediction7.append(genreRatingPrediction(u, m, movieList, trainingRLu7))

randPredictionRMSE7 = rmse(actualRatings7, randPrediction7)
meanUserPredictionRMSE7 = rmse(actualRatings7, meanUserPrediction7)
meanMoviePredictionRMSE7 = rmse(actualRatings7, meanMoviePrediction7)
demPredictionRMSE7 = rmse(actualRatings7, demPrediction7)
genrePredictionRMSE7 = rmse(actualRatings7, genrePrediction7)

### Round 8
copyRawRatings8 = copy.deepcopy(rawRatings)
[trainingSet8, testSet8] = partitionRatings(copyRawRatings1, 20)
[trainingRLu8, trainingRLm8] = createRatingsDataStructure(numUsers, numMovies, trainingSet8)

randPrediction8 = []
meanUserPrediction8 = []
meanMoviePrediction8 = []
demPrediction8 = []
genrePrediction8 = []

actualRatings8 = []
for u, m, r in testSet8:
    actualRatings8.append(r)

for u, m, r in testSet8:
    randPrediction8.append(randomPrediction(u, m))
    meanUserPrediction8.append(meanUserRatingPrediction(u, m, trainingRLu8))
    meanMoviePrediction8.append(meanMovieRatingPrediction(u, m, trainingRLm8))
    demPrediction8.append(demRatingPrediction(u, m, userList, trainingRLu8))
    genrePrediction8.append(genreRatingPrediction(u, m, movieList, trainingRLu8))

randPredictionRMSE8 = rmse(actualRatings8, randPrediction8)
meanUserPredictionRMSE8 = rmse(actualRatings8, meanUserPrediction8)
meanMoviePredictionRMSE8 = rmse(actualRatings8, meanMoviePrediction8)
demPredictionRMSE8 = rmse(actualRatings8, demPrediction8)
genrePredictionRMSE8 = rmse(actualRatings8, genrePrediction8)
##
### Round 9
copyRawRatings9 = copy.deepcopy(rawRatings)
[trainingSet9, testSet9] = partitionRatings(copyRawRatings9, 20)
[trainingRLu9, trainingRLm9] = createRatingsDataStructure(numUsers, numMovies, trainingSet9)

randPrediction9 = []
meanUserPrediction9 = []
meanMoviePrediction9 = []
demPrediction9 = []
genrePrediction9 = []

actualRatings9 = []
for u, m, r in testSet9:
    actualRatings9.append(r)

for u, m, r in testSet9:
    randPrediction9.append(randomPrediction(u, m))
    meanUserPrediction9.append(meanUserRatingPrediction(u, m, trainingRLu9))
    meanMoviePrediction9.append(meanMovieRatingPrediction(u, m, trainingRLm9))
    demPrediction9.append(demRatingPrediction(u, m, userList, trainingRLu9))
    genrePrediction9.append(genreRatingPrediction(u, m, movieList, trainingRLu9))

randPredictionRMSE9 = rmse(actualRatings9, randPrediction9)
meanUserPredictionRMSE9 = rmse(actualRatings9, meanUserPrediction9)
meanMoviePredictionRMSE9 = rmse(actualRatings9, meanMoviePrediction9)
demPredictionRMSE9 = rmse(actualRatings9, demPrediction9)
genrePredictionRMSE9 = rmse(actualRatings9, genrePrediction9)

### Round 10
copyRawRatings10 = copy.deepcopy(rawRatings)
[trainingSet10, testSet10] = partitionRatings(copyRawRatings10, 20)
[trainingRLu10, trainingRLm10] = createRatingsDataStructure(numUsers, numMovies, trainingSet10)

randPrediction10 = []
meanUserPrediction10 = []
meanMoviePrediction10 = []
demPrediction10 = []
genrePrediction10 = []

actualRatings10 = []
for u, m, r in testSet10:
    actualRatings10.append(r)

for u, m, r in testSet10:
    randPrediction10.append(randomPrediction(u, m))
    meanUserPrediction10.append(meanUserRatingPrediction(u, m, trainingRLu10))
    meanMoviePrediction10.append(meanMovieRatingPrediction(u, m, trainingRLm10))
    demPrediction10.append(demRatingPrediction(u, m, userList, trainingRLu10))
    genrePrediction10.append(genreRatingPrediction(u, m, movieList, trainingRLu10))

randPredictionRMSE10 = rmse(actualRatings10, randPrediction10)
meanUserPredictionRMSE10 = rmse(actualRatings10, meanUserPrediction10)
meanMoviePredictionRMSE10 = rmse(actualRatings10, meanMoviePrediction10)
demPredictionRMSE10 = rmse(actualRatings10, demPrediction10)
genrePredictionRMSE10 = rmse(actualRatings10, genrePrediction10)


import matplotlib.pyplot as plt
def draw_boxplot(data, labels):
    plt.boxplot(x=data, labels=labels)
    plt.title("Algorithm performance comparison")
    plt.ylabel("RMSE values")
    plt.show()
    plt.close()

algo1 = [randPredictionRMSE1, randPredictionRMSE2, randPredictionRMSE3, randPredictionRMSE4, randPredictionRMSE5, randPredictionRMSE6, randPredictionRMSE7, randPredictionRMSE8, randPredictionRMSE9, randPredictionRMSE10]
algo2 = [meanUserPredictionRMSE1, meanUserPredictionRMSE2, meanUserPredictionRMSE3, meanUserPredictionRMSE4, meanUserPredictionRMSE5, meanUserPredictionRMSE6, meanUserPredictionRMSE7, meanUserPredictionRMSE8, meanUserPredictionRMSE9, meanUserPredictionRMSE10]
algo3 = [meanMoviePredictionRMSE1, meanMoviePredictionRMSE2, meanMoviePredictionRMSE3, meanMoviePredictionRMSE4, meanMoviePredictionRMSE5, meanMoviePredictionRMSE6, meanMoviePredictionRMSE7, meanMoviePredictionRMSE8, meanMoviePredictionRMSE9, meanMoviePredictionRMSE10]
algo4 = [demPredictionRMSE1, demPredictionRMSE2, demPredictionRMSE3, demPredictionRMSE4, demPredictionRMSE5, demPredictionRMSE6, demPredictionRMSE7, demPredictionRMSE8, demPredictionRMSE9, demPredictionRMSE10]
algo5 = [genrePredictionRMSE1, genrePredictionRMSE2, genrePredictionRMSE3, genrePredictionRMSE4, genrePredictionRMSE5, genrePredictionRMSE6, genrePredictionRMSE7, genrePredictionRMSE8, genrePredictionRMSE9, genrePredictionRMSE10]
data = [algo1, algo2, algo3, algo4, algo5]
labels = ["Algo1", "Algo2", "Algo3", "Algo4", "Algo5"]
draw_boxplot(data, labels)






