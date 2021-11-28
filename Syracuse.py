import sys
import math

n = int(input())
def syracuse(n):
    while n <= 100:
        if n == 1:
            return [n]
        elif n % 2 == 0:
            return [n] + syracuse(n/2)
        else:
            return [n] + syracuse(n*3+1)
    else:
        print("Number is too large. Please input number under or equal to 100.")

result = syracuse(n)
print(result)