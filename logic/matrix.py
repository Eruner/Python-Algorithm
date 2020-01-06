import globals
import prepare
import scipy.spatial

def updateMembershipDegree():
    #print('updating lineliness')
    newLikeliness = [ [0] * globals.numberOfClusters ] * globals.numberOfItems
    for itemNumber in range(globals.numberOfItems):
        for clusterNumber in range(globals.numberOfClusters):
            oneLike = calculateOneMembershipDegree(clusterNumber, itemNumber)
            newLikeliness[itemNumber][clusterNumber] = oneLike
    return newLikeliness

def calculateOneMembershipDegree(clusterNumber, itemIndex):
    # 9) U(n,k) = 1 / SUM[..k.. / ..l..]^(1/α-1)
    sum = 0
    ourClusterWeight = globals.clusterWeights[clusterNumber]
    for line in range(globals.numberOfClusters):
        lineClusterWeight = globals.clusterWeights[line]
        clusterWeightCoeficien = ourClusterWeight / lineClusterWeight
        k = calculateMembershipDegree(clusterNumber, itemIndex)
        l = calculateMembershipDegree(line, itemIndex)
        #print('k = '+str(k)+', l = '+str(l))
        division = clusterWeightCoeficien * k / l
        power = 1 / (globals.fuzziness - 1)
        powered = pow(division, power)
        sum = sum + powered
    print(sum)
    return 1 / sum

def calculateMembershipDegree(index, itemIndex):
    # k = which cluster/center = index
    # m = which attribute = attributeIndex
    # n = which item = itemIndex
    sum = 0
    #print('index = '+str(index)+', itemIndex = '+str(itemIndex))
    for attributeIndex in range(globals.numberOfAttributes):
        #print('attributeIndex = '+str(attributeIndex))
        # w(k,m) = w(index, attributeIndex)
        weight = globals.weights[attributeIndex][index]
        #print(type(weight))
        # x(n,m) = x(itemIndex, attributeIndex)
        itemLocation = globals.dataset[itemIndex][attributeIndex]
        #print(type(itemLocation))
        # c(k,m) = x(index, attributeIndex)
        centerLocation = globals.centers[index][attributeIndex]
        #print(type(centerLocation))
        distanceFromCenter = distance(itemLocation, centerLocation)
        #print(type(distanceFromCenter))
        sum = sum + (weight * distanceFromCenter)
    return sum

def updateCenters():
    print('updating centers:')
    newCenters = prepare.Centers(globals.numberOfAttributes, globals.numberOfClusters)
    for clusterIndex in range(globals.numberOfClusters):
        for attributeIndex in range(globals.numberOfAttributes):
            centerAttribute = calculateOneCenterAttribute(clusterIndex, attributeIndex)
            #print(type(centerAttribute))
            newCenters[clusterIndex][attributeIndex] = centerAttribute
    return newCenters

def calculateOneCenterAttribute(clusterIndex, attributeIndex):
    sum1 = sumCenterWithItem(clusterIndex, attributeIndex)
    sum2 = sumCenter(clusterIndex, attributeIndex)
    return sum1 / sum2

def sumCenterWithItem(clusterIndex, attributeIndex):
    sum = 0
    for itemIndex in range(globals.numberOfItems):
        likeValue = globals.likeliness[itemIndex][clusterIndex]
        itemValue = globals.dataset[itemIndex][attributeIndex]
        itemValue = float(itemValue)
        centerValue = globals.centers[clusterIndex][attributeIndex]
        centerDistance = distance(itemValue, centerValue)
        likehood = pow(likeValue,globals.fuzziness)
        sum = sum + ( likehood * centerDistance * itemValue )
    return 1

def sumCenter(clusterIndex, attributeIndex):
    sum = 0
    for itemIndex in range(globals.numberOfItems):
        likeValue = globals.likeliness[itemIndex][clusterIndex]
        itemValue = globals.dataset[itemIndex][attributeIndex]
        itemValue = float(itemValue)
        centerValue = globals.centers[clusterIndex][attributeIndex]
        centerDistance = distance(itemValue, centerValue)
        likehood = pow(likeValue,globals.fuzziness)
        sum = sum + ( likehood * centerDistance )
    return 1

def updateWeights():
    print('updating weights')
    newWeights = prepare.Weights(globals.numberOfAttributes, globals.numberOfClusters, globals.numberOfItems)
    for clusterIndex in range(globals.numberOfClusters):
        for attributeIndex in range(globals.numberOfAttributes):
            newWeightValue = calculateOneWeight(clusterIndex, attributeIndex)
            newWeights[attributeIndex][clusterIndex] = newWeightValue
    return newWeights

def calculateOneWeight(clusterIndex, attributeIndex):
    DifferenceOfCluster = 0
    for itemIndex in range(globals.numberOfItems):
        likeValue = globals.likeliness[itemIndex][clusterIndex]
        itemValue = globals.dataset[itemIndex][attributeIndex]
        itemValue = float(itemValue)
        centerValue = globals.centers[clusterIndex][attributeIndex]
        centerDistance = distance(itemValue, centerValue)
        u = pow(likeValue, globals.fuzziness)
        d = pow(centerDistance,2)
        toAdd = u * d
        DifferenceOfCluster = DifferenceOfCluster + toAdd
    #print(DifferenceOfCluster)
    return DifferenceOfCluster

def updateClusterWeights(clusterWeights):
    print('updating cluster weights')
    for clusterIndex in range(globals.numberOfClusters):
        newClusterWeight = calculateOneClusterWeight(clusterIndex)
        globals.clusterWeights[clusterIndex] = newClusterWeight
        print(newClusterWeight)

def calculateOneClusterWeight(clusterIndex):
    clusterWeight = 0
    for itemIndex in range(globals.numberOfItems):
        for attributeIndex in range(globals.numberOfAttributes):
            likeValue = globals.likeliness[itemIndex][clusterIndex]
            weightValue = globals.weights[itemIndex][clusterIndex]
            itemValue = globals.dataset[itemIndex][attributeIndex]
            itemValue = float(itemValue)
            centerValue = globals.centers[clusterIndex][attributeIndex]
            centerDistance = distance(itemValue, centerValue)
            q = 1 # no idea what should be q, maybe manually set
            u = pow(likeValue, globals.fuzziness)
            w = pow(weightValue, q)
            d = pow(centerDistance,2)
            toAdd = u * w * d
            clusterWeight = clusterWeight + toAdd
    return clusterWeight

# for later
def distance(a,b):
    # TODO = understand
    # return 1 - exp(- pow(dispersion(a - b),2))
    return  scipy.spatial.distance.euclidean(float(a),float(b))

def dispersion(a,b):
    # TODO = understand
    # what is I in 7th page? Ym = I / var(m) ???
    return 1

def updateObjectiveFunction() :
    # all numbers of items / elements
    # all clusters K
    # all attributes M
    globals.objectiveFunction