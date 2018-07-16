#!/bin/python3

import os
import sys
import copy
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print ('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed


def getPossibleMoves():
    return zip([1, -1, 0, 0], [0, 0, 1, -1])

def isEven(num):
    return True if num % 2 == 0 else False

def getEmptyState(h, v):
    return [copy.copy([False]* h) for _ in range(v)]

def getCost(horziontal, vertical, position, x_step, y_step):
    if (x_step != 0):
        return horizontal[position[1]][position[0] if x_step > 0 else position[0]+x_step]
    else:
        return vertical[position[1] if y_step > 0 else position[1]+y_step][position[0]]
    
def isValidTarget(m, n, target):
    if min(target) < 0 or target[0] >= n or target[1] >= m:
        return False
    else:
        return True
    
def getSolutionsFromState(m, n, horizontal, vertical, visited, position, cost):
    visited = copy.deepcopy(visited)
    solutions = []
    #print('Visiting {0}'.format(position))
    if position == [0,0] and min([min(row) for row in visited]):
        #print('Found solution with cost {0}.'.format(cost))
        return [cost]
    elif visited[position[0]][position[1]]:
        #print('Revisiting Field.')
        pass
    else:
        visited[position[0]][position[1]] = True
        for x_step, y_step in getPossibleMoves():
            target = [position[0]+x_step, position[1]+y_step]
            if isValidTarget(m, n, target):
                #print('Moving to {0}.'.format(target))
                moveCost = getCost(horizontal, vertical, position, x_step, y_step)
                #print('Move costs: {0} ({1} total)'.format(moveCost, cost+moveCost))

                solutions.extend(
                    getSolutionsFromState(m, n, horizontal, vertical, visited, 
                                          target,
                                          cost+moveCost))
            #else:
                #print('Will not move to {0}.'.format(target))
    return solutions
        
    
#
# Complete the tspGrid function below.
#
@timeit
def tspGrid(m, n, horizontal, vertical):
    
    if not isEven(m) and not isEven(n):
        return 0
    else:
        visited = getEmptyState(m, n)
        return min(getSolutionsFromState(m, n, horizontal, vertical, visited, [0,0], 0))

if __name__ == '__main__':

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    horizontal = []

    for _ in range(m):
        horizontal.append(list(map(int, input().rstrip().split())))

    vertical = []

    for _ in range(m-1):
        vertical.append(list(map(int, input().rstrip().split())))

    result = tspGrid(m, n, horizontal, vertical)

    print(result)
