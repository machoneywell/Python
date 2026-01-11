# Gets info from file into lists
def loadData(cityList, coordList, popList, distanceList):
    f = open("miles.dat")
    cityAndState(cityList)
    coordinates(coordList)
    population(popList)
    distances(distanceList)


# Gets city name and state code from file into cityList    
def cityAndState(cityList):
    f = open("miles.dat")
    for line in f:
        if ("A" <= line[0]) and (line[0] <= "Z"):
            i = 0
            while (line[i] != ","):
                i = i + 1
                
            cityName = line[:i]
            stateCode = line[i + 2:i + 4] 
            cityList.append(cityName + " " + stateCode)
    return cityList

    
# Gets coordinates from file into coordList
def coordinates(coordList):
    f = open("miles.dat")
    for line in f:
        if ("A" <= line[0]) and (line[0] <= "Z"):
            s = line.split(",")
            coordList.append([int(s[1].split("[")[1]), int(s[2].split("]")[0])])
    return coordList


# Gets population of city from file into popList
def population(popList):
    f = open("miles.dat")
    for line in f:
        if ("A" <= line[0]) and (line[0] <= "Z"):
            s = line.split("]")
            popList.append(int(s[1]))
    return popList


# Puts distances from each city to the cities before it into distanceList
def distances(distanceList):
    f = open("miles.dat")
    distanceList.append([])
    for line in f:
        if (line[0].isnumeric()):
            nextLine = f.readline().strip()
            while (nextLine[0].isnumeric()):
                line = line + " " + nextLine
                nextLine = f.readline().strip()
            nums = line.split()
            nums = [int(num) for num in nums]
            nums.reverse()
            distanceList.append(nums)
            line = nextLine
    return distanceList


# Gets coordinates of city 'name'
def getCoordinates(cityList, coordList, name):
    cityNameIndex = cityList.index(name)
    coordinates = coordList[cityNameIndex]
    return coordinates


# Gets population of city 'name'
def getPopulation(cityList, popList, name):
    cityNameIndex = cityList.index(name)
    population = popList[cityNameIndex]
    return population


# Gets distance between the two cities 'name1' and 'name2'
def getDistance(cityList, distanceList, name1, name2):
    city1Index = cityList.index(name1)
    city2Index = cityList.index(name2)
    if (city1Index == 0 and city2Index == 0):
        return 0
    elif (city1Index > city2Index):
        return distanceList[city1Index][city2Index]
    elif (city1Index < city2Index):
        return distanceList[city2Index][city1Index]
    elif (city1Index == city2Index):
        return distanceList[city1Index][city1Index]


# Gets all cities that are within 'r' miles of city 'name'
def nearbyCities(cityList, distanceList, name, r):
    cityNameIndex = cityList.index(name)
    nearbyList = []
    for i in range(cityNameIndex):
        if (distanceList[cityNameIndex][i] <= r):
            nearbyList.append(cityList[i])
    for i in range(cityNameIndex+1, len(cityList)):
        if (distanceList[i][cityNameIndex] <= r):
            nearbyList.append(cityList[i])
    return nearbyList


# Gets a list of cities which facilities are located
def locateFacilities(cityList, distanceList, r):
    served = [False] * len(cityList)
    facilities = []
    while (False in served):
        maxCount = 0
        i = 1
        for i in cityList:
            countAndCities = unserved(cityList, distanceList, served, r, i)
            count = countAndCities[0]
            if (count > maxCount):
                maxCount = count
                maxCity = i
                cities = countAndCities[1]
        served[cityList.index(maxCity)] = True
        facilities.append(cityList[cityList.index(maxCity)])
        for name in cities:
            served[cityList.index(name)] = True
    
    return facilities

def unserved(cityList, distanceList, served, r, i):
    count = 0
    j = 0
    cities = []
    nearbyCityList = nearbyCities(cityList, distanceList, i, r)
    if (served[cityList.index(i)] == False):
        count = count + 1
    while (j < len(nearbyCityList)):
        if (served[cityList.index(nearbyCityList[j])] == False):
            count = count + 1
            cities.append(nearbyCityList[j])
        j = j + 1
    return [count, cities]






