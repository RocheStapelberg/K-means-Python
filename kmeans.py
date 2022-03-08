from math import sqrt
#TODO - Increase number of cluster that can be classified
def euclideanDistance(pointA, pointB) :
    sum = (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2
    distance = sqrt(sum)
    return distance
#1
def MakePointMatrix(data):
    points = []
    for i in range(len(data[0])):
        col = [row[i] for row in data]
        points.append(col)
    return points
#2
def CalculateDistanceMatrix(points, centroids):
    distMatrix = []
    for i in range(len(points)):
        distMatrix.append([euclideanDistance(points[i],centroids[0]),euclideanDistance(points[i],centroids[1])])
    return distMatrix
#3
def DetermineGroupMatrix(distMatrix):
    groupMatrix = []
    for point in distMatrix:
        if point[0] < point[1]:
            groupMatrix.append([1,0])
        else:
            groupMatrix.append([0,1])
    return groupMatrix
#4
def CalculateCentroids(groupMatrix, points, oldCentroids):
    #Concat groupmatrix
    groupA = []
    groupB = []

    for point in groupMatrix:
        groupA.append(point[0]) 
        groupB.append(point[1])

    newCentroid1 = []
    SumArrA = []
    sumAx = 0
    sumAy = 0

    if groupA.count(1) > 1:
        for i in range(len(groupA)):
            if groupA[i] == 1:
                SumArrA.append(points[i])
        for point in SumArrA:
            sumAx += point[0]
            sumAy += point[1]
        newCentroid1.append(sumAx/len(SumArrA))
        newCentroid1.append(sumAy/len(SumArrA))
    else:
        newCentroid1 = oldCentroids[0]

    newCentroid2 = []
    SumArrB = []
    sumBx = 0
    sumBy = 0

    if groupB.count(1) > 1:
        for i in range(len(groupB)):
            if groupB[i] == 1:
                SumArrB.append(points[i])
        for point in SumArrB:
            sumBx += point[0]
            sumBy += point[1]
        newCentroid2.append(sumBx/len(SumArrB))
        newCentroid2.append(sumBy/len(SumArrB))
    else:
        newCentroid2 = oldCentroids[1]

    return newCentroid1,newCentroid2
#5
def CompareGroupMatrix(grpMatrixA, grpMatrixB):
    for i in range(len(grpMatrixA)):
        if grpMatrixA[i] != grpMatrixB[i]:
            return False
    return True

def MakeGroups(points, grpMatrixB):
    groupA = []
    groupB = []
    grpAPoints = []
    grpBPoints = []
    fnlGroups = []

    for point in grpMatrixB:
        groupA.append(point[0])
        groupB.append(point[1])

    for i in range(len(points)):
        if groupA[i] == 1:grpAPoints.append(points[i])
        if groupB[i] == 1:grpBPoints.append(points[i])
    
    fnlGroups = [grpAPoints,grpBPoints]
    
    return fnlGroups
