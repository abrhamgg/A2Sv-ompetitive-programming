#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    if (grades is None) or grades[0] == 0:
        return
    new_grade = []
    for i in range(len(grades)):
        if grades[i]  < 38:
            new_grade.append(grades[i])
        elif grades[i] % 5 == 0:
            new_grade.append(grades[i])
        else:
            g = grades[i];
            for n in range(g + 1, g + 6):
                if n % 5 == 0:
                    if n - grades[i] < 3:
                        new_grade.append(n)
                    else:
                        new_grade.append(grades[i])
                    n += 6
    return new_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
