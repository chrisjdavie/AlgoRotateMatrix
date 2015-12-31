'''
Solving the hackerrank [Algo] Matrix Rotation puzzle

(it's not a mathematical matrix rotation, it's something else)

https://www.hackerrank.com/challenges/matrix-rotation-algo

--------------------

Problem Statement

You are given a 2D matrix, a, of dimension MxN and a positive integer R. You have to rotate the matrix R times and print the resultant matrix. Rotation should be in anti-clockwise direction.

Rotation of a 4x5 matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only (refer sample tests for more clarity).

<see link for figure>

It is guaranteed that the minimum of M and N will be even.

Input Format 
First line contains three space separated integers, M, N and R, where M is the number of rows, N is number of columns in matrix, and R is the number of times the matrix has to be rotated. 
Then M lines follow, where each line contains N space separated positive integers. These M lines represent the matrix.

Output Format 
Print the rotated matrix.


--------------------

Created on 31 Dec 2015

@author: chris
'''
import copy

numRows, numCols, R = map(int, raw_input().strip().split())

grid = []
for _ in range(numRows):
    row = map(int, list(raw_input().strip().split()))
    grid.append(row)

def iterateCoords(depth):

    # Establish coordinates for rotation
        
    for i in range(0 + depth, numCols - depth):
        yield (0 + depth, i)
    for j in range(1 + depth, numRows - depth):
        yield (j, numCols - 1 - depth)
    for i in range(numCols - 2 - depth, -1 + depth, -1):
        yield (numRows -1 -depth, i)
    for j in range(numRows - 2 - depth, 0 + depth, -1):
        yield (j, 0 + depth )
        

def rotateEdge(outputGrid,depth):
    
    # get the values at those coordinates
    
    numbersToRotate = []
    for i, j in iterateCoords(depth):
        numbersToRotate.append(grid[i][j])
    
    lenNums = len(numbersToRotate)
    numbersRotated = copy.copy(numbersToRotate)
    
    
    # reorder the values in their shifted positions
    
    rotShift = R%lenNums
    for i, num in enumerate(numbersToRotate):
        rotInd = (i - rotShift)%lenNums
        numbersRotated[rotInd] = num
    
    
    # impose them on the output grid 
    
    for num, (i, j) in zip(numbersRotated,iterateCoords(depth)):
        outputGrid[i][j] = num


outputGrid = copy.deepcopy(grid)

for i in range(min(numRows,numCols)/2):
    rotateEdge(outputGrid,i)

for row in outputGrid:
    print ' '.join(map(str,row))
