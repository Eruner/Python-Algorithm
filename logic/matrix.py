import globals
import prepare

def updateLikeliness():
    newLikeliness = [ [0] * globals.numberOfClusters ] * globals.numberOfItems
    for itemNumber in range(globals.numberOfItems):
        for clusterNumber in range(globals.numberOfClusters):
            oneLike = calculateOneLikeliness(clusterNumber, itemNumber)
            newLikeliness[itemNumber][clusterNumber] = oneLike
    #print('updating lineliness')
    return newLikeliness

def calculateOneLikeliness(clusterNumber, itemIndex):
    # 9) U(n,k) = 1 / SUM[..k.. / ..l..]^(1/α-1)
    sum = 0
    ourClusterWeight = globals.clusterWeights[clusterNumber]
    for line in range(globals.numberOfClusters):
        lineClusterWeight = globals.clusterWeights[line]
        clusterWeightCoeficien = ourClusterWeight / lineClusterWeight
        k = likeStuff(clusterNumber, itemIndex)
        l = likeStuff(line, itemIndex)
        #print('k = '+str(k)+', l = '+str(l))
        division = clusterWeightCoeficien * k / l
        power = 1 / (globals.fuzzyCoeficien - 1)
        powered = pow(division, power)
        sum = sum + powered
    #print(sum)
    return 1 / sum

def likeStuff(index, itemIndex):
    # k = which cluster/center = index
    # m = which attribute = attributeIndex
    # n = which item = itemIndex
    sum = 0
    for attributeIndex in range(globals.numberOfAttributes):
        # w(k,m) = w(index, attributeIndex)
        weight = globals.weights[attributeIndex][index]
        # x(n,m) = x(itemIndex, attributeIndex)
        itemLocation = globals.dataset[itemIndex][attributeIndex]
        # c(k,m) = x(index, attributeIndex)
        centerLocation = globals.centers[index][attributeIndex]
        distanceFromCenter = distance(itemLocation, centerLocation)
        sum = sum + (weight * distanceFromCenter)
    return sum

def updateCenters(centers):
    newCenters = prepare.Centers(globals.numberOfAttributes, globals.numberOfClusters)
    for clusterIndex in range(globals.numberOfClusters):
        for attributeIndex in range(globals.numberOfAttributes):
            centerAttribute = calculateOneCenterAttribute(clusterIndex, attributeIndex)
            newCenters[clusterIndex][attributeIndex] = centerAttribute
    print('updating centers')

def calculateOneCenterAttribute(clusterIndex, attributeIndex):
    sum1 = sumCenterWithItem(clusterIndex, attributeIndex)
    sum2 = sumCenter()
    return sum1 / sum2

def sumCenterWithItem(clusterIndex, attributeIndex):
    sum = 0
    for itemIndex in range(globals.numberOfItems):
        likeValue = globals.likeliness[itemIndex][clusterIndex]
        itemValue = globals.dataset[itemIndex][attributeIndex]
        centerValue = globals.centers[clusterIndex][attributeIndex]
        centerDistance = distance(itemValue, centerValue)
    return 1

def sumCenter():
    return 1

def updateWeights(weights):
    print('updating weights')

def updateClusterWeights(clusterWeights):
    print('updating cluster weights')



# for later
def distance(a,b):
    # TODO = understand
    # return 1 - exp(- pow(dispersion(a - b),2))
    return 1

def dispersion(a,b):
    # TODO = understand
    # what is I in 7th page? Ym = I / var(m) ???
    return 1
