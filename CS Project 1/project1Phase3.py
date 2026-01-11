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


# Creates kml files to display cities and facilities with r radius
def display(facilities, cityList, distanceList, coordList, r):
    f = open("visualization"+str(r)+".kml", "w")
    f.write('<Document>')

    # Facility icon style
    f.write('<Style id="facility">')
    f.write('<IconStyle>')
    f.write('<scale>1.2</scale>')
    f.write('<Icon>')
    f.write('<href>https://cdn-icons-png.flaticon.com/512/10112/10112418.png</href>')
    f.write('</Icon>')
    f.write('</IconStyle>')
    f.write('</Style>')
    
    # Puts a facility icon at each facility in facilities
    for i in range(len(cityList)):
        if (cityList[i] in facilities):
            f.write('<Placemark>')
            f.write('<name>'+cityList[i]+'</name>')
            f.write('<styleUrl>#facility</styleUrl>')
            f.write('<Point>')
            formattedLong = '-'+str(coordList[i][1])[:-2]+'.'+str(coordList[i][1])[-2:]
            formattedLat = str(coordList[i][0])[:-2]+'.'+str(coordList[i][0])[-2:]
            f.write('<coordinates>'+formattedLong+','+formattedLat+',0</coordinates>')
            f.write('</Point>')
            f.write('</Placemark>')
            

    # Non-facility cities style
    f.write('<Style id="city">')
    f.write('<IconStyle>')
    f.write('<scale>0.65</scale>')
    f.write('<Icon>')
    f.write('<href>https://cdn-icons-png.flaticon.com/512/5293/5293804.png</href>')
    f.write('</Icon>')
    f.write('</IconStyle>')
    f.write('</Style>')

    # Puts a city icon at each city not in facilities
    for i in range(len(cityList)):
        if (cityList[i] not in facilities):
            f.write('<Placemark>')
            f.write('<name>'+cityList[i]+'</name>')
            f.write('<styleUrl>#city</styleUrl>')
            f.write('<Point>')
            formattedLong = '-'+str(coordList[i][1])[:-2]+'.'+str(coordList[i][1])[-2:]
            formattedLat = str(coordList[i][0])[:-2]+'.'+str(coordList[i][0])[-2:]
            f.write('<coordinates>'+formattedLong+','+formattedLat+',0</coordinates>')
            f.write('</Point>')
            f.write('</Placemark>')
            
    # Line style
    f.write('<Style id="blueLine">')
    f.write('<LineStyle>')
    f.write('<color>FFE6E6E6</color>')
    f.write('<width>2</width>')
    f.write('</LineStyle>')
    f.write('</Style>')

    # Connects each city without a facility to the nearest facility, with a line
    for j in range(len(cityList)):
        if (cityList[j] not in facilities):
            closest = closestFacility(cityList, distanceList, coordList, facilities, j)
            facilityIndex = cityList.index(closest)
            f.write('<Placemark>')
            f.write('<name>Line'+str(j)+'</name>')
            f.write('<styleUrl>#blueLine</styleUrl>')
            f.write('<LineString>')
            formattedLong1 = '-'+str(coordList[j][1])[:-2]+'.'+str(coordList[j][1])[-2:]
            formattedLat1 = str(coordList[j][0])[:-2]+'.'+str(coordList[j][0])[-2:]
            formattedLong2 = '-'+str(coordList[facilityIndex][1])[:-2]+'.'+str(coordList[facilityIndex][1])[-2:]
            formattedLat2 = str(coordList[facilityIndex][0])[:-2]+'.'+str(coordList[facilityIndex][0])[-2:]
            f.write('<coordinates>'+formattedLong1+','+formattedLat1+',0,'+formattedLong2+','+formattedLat2+',0</coordinates>')
            f.write('</LineString>')
            f.write('</Placemark>')
    f.write('</Document>')
    f.close()

# Helper function to get the closest city with a facility to city j
def closestFacility(cityList, distanceList, coordList, facilities, j):
    distances = []
    for i in range(len(facilities)):
        distances.append(getDistance(cityList, distanceList, cityList[j], facilities[i]))
    closest = facilities[distances.index(min(distances))]
    return closest

cityList = []
coordList = []
popList = []
distanceList = []
loadData(cityList, coordList, popList, distanceList)

facilities300 = locateFacilities(cityList, distanceList, 300)
facilities800 = locateFacilities(cityList, distanceList, 800)
display(facilities300, cityList, distanceList, coordList, 300)
display(facilities800, cityList, distanceList, coordList, 800)












