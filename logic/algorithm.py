import csvfiles
import prepare

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
    # secundary parameters = Tmax, Pmax, Pinit, E
    # no idea what they are and what values they should be
    iterations = 0
    maxIterations = 3
    Pinit = 0
    P = 0
    isEmpty = False
    complexLoop()
    print('ended complex algorithm')

def loadDataSet():
    fileName = '..\data\iris.data'
    return csvfiles.loadCsv(fileName)

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
