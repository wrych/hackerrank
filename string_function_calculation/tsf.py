#!/bin/python3

import os
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Elapsed time: {}'.format(end - start))
        return result

    return wrapper


def addOrIncrement(pointer, t):
    try:
        pointer[t] += 1
        # print('incrementing {0}'.format(t))
    except KeyError as _:
        pointer[t] = 1
        #print('adding {0}'.format(t))


def stringEndChopper(pointer, t):
    for end in range(1, len(t) + 1):
        addOrIncrement(pointer, t[:end])


def stringStartChopper(results, t):
    for start in range(len(t)):
        stringEndChopper(results, t[start:])


@timing
def stringChopper(results, t):
    stringStartChopper(results, t)


# Complete the maxValue function below.
def maxValue(t):
    results = {}
    stringChopper(results, t)
    #print(results)
    return max([results[key] * len(key) for key in results])


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)

    print(result)

    import time
    time.sleep(200)

    #fptr.write(str(result) + '\n')

    #fptr.close()
