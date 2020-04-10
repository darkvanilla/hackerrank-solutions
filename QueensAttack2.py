# Author: Birkan Mert Erenler
# https://www.hackerrank.com/challenges/queens-attack-2/problem

def eastWest(n, k, r_q, c_q, obstacleDictByRow):
    if k == 0:
        return n - 1
    
    rowObjects = obstacleDictByRow[r_q].copy()
    rowObjects.append(c_q)
    rowObjects = sorted(rowObjects)
    indexQueen = rowObjects.index(c_q)
    movesEast = 0
    if indexQueen == len(rowObjects) - 1:
        movesEast = n - c_q
    else:
        movesEast = rowObjects[indexQueen + 1] - c_q - 1
    movesWest = 0
    if indexQueen == 0:
        movesWest = c_q - 1
    else:
        movesWest = c_q - rowObjects[indexQueen - 1] - 1
    return movesEast + movesWest

def northSouth(n, k, r_q, c_q, obstacleDictByColumn):
    if k == 0:
        return n - 1
    
    columnObjects = obstacleDictByColumn[c_q].copy()
    columnObjects.append(r_q)
    columnObjects = sorted(columnObjects)
    indexQueen = columnObjects.index(r_q)
    movesNorth = 0
    if indexQueen == len(columnObjects) - 1:
        movesNorth = n - r_q
    else:
        movesNorth = columnObjects[indexQueen + 1] - r_q - 1
    movesSouth = 0
    if indexQueen == 0:
        movesSouth = r_q - 1
    else:
        movesSouth = r_q - columnObjects[indexQueen - 1] - 1
    return movesNorth + movesSouth

def northEast(n, k, r_q, c_q, obstacleDictByRow):
    movesMax = min(n-r_q, n-c_q)
    for d in range(1, movesMax):
        if (c_q+d) in obstacleDictByRow[r_q+d]:
            return d - 1
    return movesMax

def northWest(n, k, r_q, c_q, obstacleDictByRow):
    movesMax = min(n-r_q, c_q-1)
    for d in range(1, movesMax):
        if (c_q-d) in obstacleDictByRow[r_q+d]:
            return d - 1
    return movesMax

def southEast(n, k, r_q, c_q, obstacleDictByRow):
    movesMax = min(r_q-1, n-c_q)
    for d in range(1, movesMax):
        if (c_q+d) in obstacleDictByRow[r_q-d]:
            return d - 1
    return movesMax

def southWest(n, k, r_q, c_q, obstacleDictByRow):
    movesMax = min(r_q-1, c_q-1)
    for d in range(1, movesMax):
        if (c_q-d) in obstacleDictByRow[r_q-d]:
            return d - 1
    return movesMax

def queensAttack(n, k, r_q, c_q, obstacles):
    obstacleDictByRow = {a: [] for a in range(1, n+1)}
    obstacleDictByColumn = {a: [] for a in range(1, n+1)}
    for obstacle in obstacles:
        obstacleDictByRow[obstacle[0]].append(obstacle[1])
        obstacleDictByColumn[obstacle[1]].append(obstacle[0])

    return eastWest(n, k, r_q, c_q, obstacleDictByRow) + \
              northSouth(n, k, r_q, c_q, obstacleDictByColumn) + \
              northEast(n, k, r_q, c_q, obstacleDictByRow) + \
              northWest(n, k, r_q, c_q, obstacleDictByRow) + \
              southWest(n, k, r_q, c_q, obstacleDictByRow) + \
              southEast(n, k, r_q, c_q, obstacleDictByRow)