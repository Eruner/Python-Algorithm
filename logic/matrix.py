import globals

def updateLikeliness(rows, cols):
    print(str(rows)+' x '+str(cols))
    newLikeliness = [ [0] * cols ] * rows
    for row in range(rows):
        for col in range(cols):
            #print('['+str(row)+','+str(col)+']')
            newLikeliness[row][col] = calculateOneLikeliness(cols, col)
    print('updating lineliness')
    return newLikeliness

def calculateOneLikeliness(cols, ourIndex):
    sum = 0
    ourClusterWeight = globals.clusterWeights[ourIndex]
    for line in range(cols):
        lineClusterWeight = globals.clusterWeights[line]
        clusterWeightCoeficien = ourClusterWeight / lineClusterWeight
        k = likeStuff(ourIndex)
        l = likeStuff(line)
        
        #for attributeIndex in range(numberOfClusters):
            # calculate top sum
            # calculate bottom sum
        # divide and sum
    return 0

def likeStuff(index):
    #globals.numberOfAttributes
    #globals.weights
    return 1

def updateCenters(centers):
    print('updating centers')

def updateWeights(weights):
    print('updating weights')

def updateClusterWeights(clusterWeights):
    print('updating cluster weights')
