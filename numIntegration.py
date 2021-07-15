import math

#print(math.pi)

def main_func(x):
    
    fx = 2 * math.sin(4*x)
    return fx

#x = (math.pi/4)
#print(main_func(x))

def solve_deltaX(b, a, n):
    
    temp = b - a
    deltX = (temp/n)
    return deltX

def solve_gridpoint(a, n, deltX):
    
    gridlist = []
    for x in range(n+1):
        temp = a + (x * deltX)
        #print(temp)
        gridlist.append(temp)
    
    return gridlist

def find_midPoint(gPoints):
    
    midP = []
    for x in range(len(gPoints)-1):
        #print(gPoints[x])
        #print(gPoints[x+1])
        temp = gPoints[x] + gPoints[x+1]
        temp2 = (temp/2)  
        midP.append(temp2)
    return midP

def midPoint_Formula(mPoints, deltX):
    
    fSum = 0
    for x in range(len(mPoints)):
        #print(mPoints[x])
        fSum = fSum + main_func(mPoints[x])
    fSum = fSum * deltX
    
    return fSum

def trapezoid_Rule(gPoints, deltX):
    
    fSum = 0
    print(gPoints)
    #gPoints[0] = gPoints[0] * (1/2)
    #print(gPoints[len(gPoints) - 1])
    #gPoints[len(gPoints) - 1] = gPoints[len(gPoints) - 1] * (1/2)
    #print("\n gridPoint values after mod")
    #print("\n")
    #rint(gPoints)

    for x in range(len(gPoints)):
        if (x == len(gPoints) - 1):
            #print(gPoints[x])
            fSum = fSum +((1/2) * main_func(gPoints[x]))
        else:
         fSum = fSum + main_func(gPoints[x])
    fSum = fSum * deltX
    
    return fSum

b = (math.pi/8)
a = 0
n = 32 

deltX = solve_deltaX(b, a, n)
#print(deltX)

gPoints = solve_gridpoint(a, n, deltX)
#print(gPoints)
mPoints = find_midPoint(gPoints)
#print(mPoints)
#result = midPoint_Formula(mPoints, deltX)
#print(result)
result = trapezoid_Rule(gPoints, deltX)
print(result)



