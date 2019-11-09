def Centers(numberOfAttributes, numberOfClusters):
    return [ [0]*numberOfAttributes ] * numberOfClusters

def Likeliness(numberOfClusters, numberOfItems):
    return [ [0]*numberOfClusters ] * numberOfItems

def Weights(numberOfAttributes, numberOfClusters, numberOfItems):
    initialItemWeight = 1 / numberOfAttributes
    return [ [initialItemWeight]*numberOfClusters ] * numberOfItems

def ClusterWeights(numberOfClusters):
    initialClusterWeight = 1 / numberOfClusters
    return [initialClusterWeight] * numberOfClusters
