#!/bin/python3


import os
import datetime


def parse_time(t):
    return datetime.datetime.strptime(t, '%a %d %b %Y %H:%M:%S %z')


# Complete the time_delta function below.
def time_delta(t1, t2):
    return str(int(abs((parse_time(t1) - parse_time(t2)).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()