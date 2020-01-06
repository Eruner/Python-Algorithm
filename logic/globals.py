
# global variables
fuzziness = 2                   # α > 1
numberOfItems = 0               #   N
numberOfClusters = 3            #   K
numberOfAttributes = 4          #   M
objectiveFunction = None        #   F
objectiveFunctionBefore = None        #   F

# global data structures
dataset = None                  #   N x M
centers = None                  #   K x M
membershipDegree = None         #   N x K    MEMBERSHIP DEGREES
weights = None                  #   K x M    w = vahy atributov
clusterWeights = None           #   1 x K    z = vahy zhlukov


