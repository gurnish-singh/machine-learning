import csv
import random
import math
import operator


def handleDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r')as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        #print(dataset)
        for x in range(len(dataset)-1):  # last element of the list is always vacant
            for y in range(4):  # 4 is the no. of features change accordingly to ur dataset
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:  # random.random() gives random number between 0 and 1 exclusive
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
############################################


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x]-instance2[x], 2)
    return math.sqrt(distance)


def getKNeighbours(trainingSet, testInstance, k):
    distances = []
    length = len(trainingSet[0])-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distances[x][0])
    return neighbours
#############################################


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),
                         key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
##################################################


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0


# Driver Code
trainingSet = []
testSet = []
with open(filename, 'r')as csvfile:
        lines = csv.reader(csvfile)
        dataset1 = list(lines)

handleDataset(r'iris.data', .66, trainingSet, testSet)

print('Train: ' + repr(len(trainingSet)))
print('Test: ' + repr(len(testSet)))
k=3
predictions=[]
for i in (testSet):
    neighbors=getKNeighbours(trainingSet,i,k)
    predictions.append(getResponse(neighbors))
Accuracy=getAccuracy(testSet,predictions)
print(Accuracy)
    




