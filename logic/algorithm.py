import globals
import csvfiles
import prepare
import output
import matrix


def complexAlgorithm():
    print('started complex algorithm')
    initializeGlobals()
    complexLoop()
    output.Results()
    print('ended complex algorithm')

def initializeGlobals():
    globals.dataset = loadDataSet()
    globals.numberOfItems = len(globals.dataset)
    globals.centers = prepare.Centers(globals.numberOfAttributes, globals.numberOfClusters)
    globals.likeliness = prepare.Likeliness(globals.numberOfClusters, globals.numberOfItems)
    globals.weights = prepare.Weights(globals.numberOfAttributes, globals.numberOfClusters, globals.numberOfItems)
    globals.clusterWeights = prepare.ClusterWeights(globals.numberOfClusters)
    print('membershipDegree ' + str(globals.likeliness))
    print('weights ' + str(globals.weights))
    print('clusterWeights ' + str(globals.clusterWeights))

def loadDataSet():
    fileName = '..\data\iris.data'
    return csvfiles.loadCsv(fileName)

def complexLoop():
    print('complex loop:')
    # secondary parameters = Tmax, Pmax, Pinit, E
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


def computeObjectiveFunction():
    globals.objectiveFunctionBefore = globals.objectiveFunction
    # u_nk^fuzziness * w_km * z_k * vzdialenost
    globals.objectiveFunction = matrix.updateObjectiveFunction()
    #todo vypocitat


def compute():
    print('computing:')
    updateMembershipDegree()
    # if singletons -> do magic
    updateCenters()
    # if p < pmax AND empty=False -> do history
    updateWeights()
    updateClusterWeights()
    #compute objective function f
    # u_nk^fuzziness * w_km * z_k * vzdialenost
    computeObjectiveFunction()



def shouldContinue():
    # difference = ABSolute value of F(t) - F(t-1)
    # is less then epsilon e
    # no idea how to implement it
    #todo spocitat ucelovu funkciu
    return True

def updateMembershipDegree():
    globals.membershipDegree = matrix.updateMembershipDegree()

def updateCenters():
    globals.centers = matrix.updateCenters()

def updateWeights():
    globals.weights = matrix.updateWeights()

def updateClusterWeights():
    matrix.updateClusterWeights(globals.clusterWeights)

# run the algorithm
complexAlgorithm()
