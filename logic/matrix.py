

def updateLikeliness(likeliness, rows, cols, clusterWeights, numberOfAttributes, weights):
    print(str(rows)+' x '+str(cols))
    newLikeliness = [ [0] * cols ] * rows
    for row in range(rows):
        for col in range(cols):
            #print('['+str(row)+','+str(col)+']')
            newLikeliness[row][col] = calculateOneLikeliness(cols, clusterWeights, col, numberOfAttributes, weights)
    print('updating lineliness')
    return newLikeliness

def calculateOneLikeliness(cols, clusterWeights, ourIndex, numberOfAttributes, weights):
    sum = 0
    ourClusterWeight = clusterWeights[ourIndex]
    for line in range(cols):
        lineClusterWeight = clusterWeights[line]
        clusterWeightCoeficien = ourClusterWeight / lineClusterWeight
        k = likeStuff(numberOfAttributes, weights, ourIndex)
        l = likeStuff(numberOfAttributes, weights, line)
        
        #for attributeIndex in range(numberOfClusters):
            # calculate top sum
            # calculate bottom sum
        # divide and sum
    return 0

def likeStuff(numberOfAttributes, weights, index):
    return 1

def updateCenters(centers):
    print('updating centers')

def updateWeights(weights):
    print('updating weights')

def updateClusterWeights(clusterWeights):
    print('updating cluster weights')
