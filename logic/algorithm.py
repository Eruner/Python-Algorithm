import csvfiles
import prepare
import output
import matrix

# global variables
fuzzyCoeficien = 2 # α > 1
numberOfItems = 0
numberOfClusters = 3
numberOfAttributes = 4

# global data structures
dataset = None
centers = None
likeliness = None
weights = None
clusterWeights = None

def complexAlgorithm():
    print('started complex algorithm')
    initializeGlobals()
    complexLoop()
    output.Results(centers, likeliness)
    print('ended complex algorithm')

def initializeGlobals():
    # this way we modify global variables
    global dataset
    dataset = loadDataSet()
    global numberOfItems
    numberOfItems = len(dataset)
    global centers
    centers = prepare.Centers(numberOfAttributes, numberOfClusters)
    global likeliness
    likeliness = prepare.Likeliness(numberOfClusters, numberOfItems)
    global weights
    weights = prepare.Weights(numberOfAttributes, numberOfClusters, numberOfItems)
    global clusterWeights
    clusterWeights = prepare.ClusterWeights(numberOfClusters)
    print('likeliness ' + str(likeliness))
    print('weights ' + str(weights))
    print('clusterWeights ' + str(clusterWeights))

def loadDataSet():
    fileName = '..\data\iris.data'
    return csvfiles.loadCsv(fileName)

def complexLoop():
    print('complex loop:')
    # secundary parameters = Tmax, Pmax, Pinit, E
    # no idea what they are and what values they should be    Pinit = 0
    iterations = 0 # T
    maxIterations = 2 # Tmax
    P = 0
    isEmpty = False
    # start loop
    while shouldContinue() and iterations < maxIterations:
        iterations = iterations + 1
        compute()
    print('loop ended')
    # end loop

def compute():
    print('computing:')
    updateLikeliness()
    # if singletons -> do magic
    updateCenters()
    # if p < pmax AND empty=False -> do history
    updateWeights()
    updateClusterWeights()

def shouldContinue():
    # difference = ABSolute value of F(t) - F(t-1)
    # is less then epsilon e
    # no idea how to implement it
    return True

def updateLikeliness():
    global likeliness
    likeliness = matrix.updateLikeliness(likeliness, numberOfItems, numberOfClusters, clusterWeights, numberOfAttributes, weights)

def updateCenters():
    global centers
    # centers = 
    matrix.updateCenters(centers)

def updateWeights():
    global weights
    # weights = 
    matrix.updateWeights(weights)

def updateClusterWeights():
    global clusterWeights
    # clusterWeights = 
    matrix.updateClusterWeights(clusterWeights)


# for later
def distance(a,b):
    return 1 - exp(- pow(dispersion(a - b),2))

def dispersion(a,b):
    #what is I in 7th page? Ym = I / var(m) ???
    return 1

# run the algorithm
complexAlgorithm()
