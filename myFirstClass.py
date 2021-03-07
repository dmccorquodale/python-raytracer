def addVector (x, y):
    print ("adding the vectors " + str(x) + " and " + str(y))
    result = []
    result.append(x[0] + y[0])
    result.append(x[1] + y[1])
    result.append(x[2] + y[2])
    print (result)

def subtractVector(x, y):
    print ("subtracting the vectors " + str(x) + " and " + str(y))
    result = []
    result.append(x[0] - y[0])
    result.append(x[1] - y[1])
    result.append(x[2] - y[2])
    print (result)

def multiplyVector(x, y):
    print ("multiplying the vector " + str(x) + " by " + str(y))
    result = []
    result.append(x[0] * y)
    result.append(x[1] * y)
    result.append(x[2] * y)
    print (result)

def divideVector(x,y):
    print ("dividing the vector " + str(x) + " by " + str(y))
    result = []
    result.append(vectorB[0] / y)
    result.append(vectorB[1] / y)
    result.append(vectorB[2] / y)
    print (result)