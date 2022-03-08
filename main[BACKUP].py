import kmeans
#Data Format [[x],[y]]
data = [[1,2,4,5],[1,1,3,4]]
#data = [[2,8,9,1,8.5],[4,2,3,5,1]]

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

groupA = []
groupB = []

for point in grpMatrixB:
    groupA.append(point[0]) 
    groupB.append(point[1])
print("\n----------------------")
print(f"Final Groups\nGroup A : {groupA} with centroid: {centroids[0]}\nGroup B : {groupB} with centroid: {centroids[1]}")
print("----------------------")