import csvfiles

def complexAlgorithm():
    print('started complex algorithm')
    dataset = loadDataSet()
    numberOfItems = len(dataset)
    print('there are ' +str(numberOfItems)+ ' items')
    numberOfClusters = 3
    numberOfAttributes = 4
    centers = initCenters(numberOfAttributes, numberOfClusters)
    likeliness = initLikeliness(numberOfClusters, numberOfItems)
    print('likeliness ' + str(likeliness))
    weights = initWeights(numberOfAttributes, numberOfClusters, numberOfItems)
    print('weights ' + str(weights))
    clusterWeights = initClusterWeights(numberOfClusters)
    print('clusterWeights ' + str(clusterWeights))
    # secundary parameters = Tmax, Pmax, Pinit, E
    # no idea what they are and what values they should be
    iterations = 0
    Pinit = 0
    P = 0
    isEmpty = False
    complexLoop()
    print('ended complex algorithm')

def loadDataSet():
    fileName = '..\data\iris.data'
    return csvfiles.loadCsv(fileName)

def initCenters(numberOfAttributes, numberOfClusters):
    return [ [0]*numberOfAttributes ] * numberOfClusters

def initLikeliness(numberOfClusters, numberOfItems):
    return [ [0]*numberOfClusters ] * numberOfItems

def initWeights(numberOfAttributes, numberOfClusters, numberOfItems):
    initialItemWeight = 1 / numberOfAttributes
    return [ [initialItemWeight]*numberOfClusters ] * numberOfItems

def initClusterWeights(numberOfClusters):
    initialClusterWeight = 1 / numberOfClusters
    return [initialClusterWeight] * numberOfClusters

def complexLoop():
    print('complex loop')
    # start loop
    compute()
    # end loop

def compute():
    print('computing')

def distance(a,b):
    return 1 - exp(- pow(dispersion(a - b),2))

def dispersion(a,b):
    #what is I in 7th page? Ym = I / var(m) ???
    return 1

complexAlgorithm()
