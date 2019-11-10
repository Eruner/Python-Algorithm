import csvfiles
import prepare
import output
import matrix

fuzzyCoeficien = 2 # α > 1


def complexAlgorithm():
    print('started complex algorithm')
    dataset = loadDataSet()
    numberOfItems = len(dataset)
    print('there are ' +str(numberOfItems)+ ' items')
    numberOfClusters = 3
    numberOfAttributes = 4
    centers = prepare.Centers(numberOfAttributes, numberOfClusters)
    likeliness = prepare.Likeliness(numberOfClusters, numberOfItems)
    print('likeliness ' + str(likeliness))
    weights = prepare.Weights(numberOfAttributes, numberOfClusters, numberOfItems)
    print('weights ' + str(weights))
    clusterWeights = prepare.ClusterWeights(numberOfClusters)
    print('clusterWeights ' + str(clusterWeights))
    complexLoop()
    output.Results(centers, likeliness)
    print('ended complex algorithm')

def loadDataSet():
    fileName = '..\data\iris.data'
    return csvfiles.loadCsv(fileName)

def complexLoop():
    print('complex loop:')
    # secundary parameters = Tmax, Pmax, Pinit, E
    # no idea what they are and what values they should be    Pinit = 0
    iterations = 0 # T
    maxIterations = 3 # Tmax
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
    matrix.updateLikeliness()
    # if singletons -> do magic
    matrix.updateCenters()
    # if p < pmax AND empty=False -> do history
    matrix.updateWeights()
    matrix.updateClusterWeights()

def shouldContinue():
    # difference = ABSolute value of F(t) - F(t-1)
    # is less then epsilon e
    # no idea how to implement
    return True

def distance(a,b):
    return 1 - exp(- pow(dispersion(a - b),2))

def dispersion(a,b):
    #what is I in 7th page? Ym = I / var(m) ???
    return 1

complexAlgorithm()
