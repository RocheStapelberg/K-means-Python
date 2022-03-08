import matplotlib.pyplot as plt
import numpy # Only used to generate random values for points
import kmeans

# TODO - Optimization and code cleanup
#Data Format [[x],[y]]
data = [numpy.random.normal(10.0, 10.0, 100), numpy.random.normal(10.0, 10.0, 100)]

points = kmeans.MakePointMatrix(data)
print(points)

check = False
iniCentroids = [points[0], points[1]]

print(f"Initial Centroid 1 = {iniCentroids[0]}")
print(f"Initial Centroid 2 = {iniCentroids[1]}")

distMatrix = kmeans.CalculateDistanceMatrix(points, iniCentroids)
print(f"Initial Distance Matrix: {distMatrix}")

grpMatrixA = kmeans.DetermineGroupMatrix(distMatrix)
print(f"Initial Group Matrix: {grpMatrixA}")

while True:
    centroids = kmeans.CalculateCentroids(grpMatrixA, points, iniCentroids)
    print(f"New Centroid 1:{centroids[0]}\nNew Centroid 2:{centroids[1]}")

    distMatrix = kmeans.CalculateDistanceMatrix(points, centroids)
    print(f"New Distance Matrix: {distMatrix}")

    grpMatrixB = kmeans.DetermineGroupMatrix(distMatrix)
    print(f"Old Group Matrix : {grpMatrixA}")
    print(f"New Group Matrix : {grpMatrixB}")

    check = kmeans.CompareGroupMatrix(grpMatrixA, grpMatrixB)
    
    if check == True : break
    else : grpMatrixA = grpMatrixB

# TODO - Optimization and code cleanup
fnlGroups = kmeans.MakeGroups(points, grpMatrixB)
groupAx = []
groupAy = []
groupBx = []
groupBy = []

for point in fnlGroups[0]:
    groupAx.append(point[0])
    groupAy.append(point[1])

for point in fnlGroups[1]:
    groupBx.append(point[0])
    groupBy.append(point[1])

groupA = []
groupB = []

for point in grpMatrixB:
    groupA.append(point[0]) 
    groupB.append(point[1])
    
print("\n----------------------")
print(f"Final Groups\nGroup A : {groupA} with centroid: {centroids[0]}\nGroup B : {groupB} with centroid: {centroids[1]}")
print("----------------------")


#Data visualization
plt.title("K-Means")
plt.xlabel("Feature 1 : X-Axis")
plt.ylabel("Feature 2 : Y-Axis")
plt.plot(centroids[0][0], centroids[0][1],'ro', label="Centroid 1")
plt.plot(centroids[1][0], centroids[1][1],'ro', label="Centroid 2")
plt.scatter(groupAx, groupAy, label="Group A" ,s=10, c="blue")
plt.scatter(groupBx, groupBy, label="Group B" ,s=10, c="orange")
plt.legend()
plt.show()