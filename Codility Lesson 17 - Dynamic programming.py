## Lesson 17.1 NumberSolitaire: In a given array, find the subset of maximal sum in which the distance between consecutive elements is at most 6.
def solution(A):
    # write your code in Python 3.6
    maxA = [0 for x in range(len(A))]
    maxA[0] = A[0]

    for n in range(1, len(A)):
        maxA[n] = maxA[n - 1]
        for dRoll in range(1, 7):
            if dRoll > n:
                break

            else:
                maxA[n] = max(maxA[n],maxA[n - dRoll])

        maxA[n] += A[n]

    return maxA[n-1]

    pass
# 100% score

#Lesson 17.2 MinAbsSum - Given array of integers, find the lowest absolute sum of elements

def solution(A):
    # write your code in Python 3.6
    AS = [0 for x in range(len(A))]
    S = [-1, 1]
    AS[0] = A[0] * S[0]

    for n in range(1, len(A)):

        if n % 2 == 0:
            AS[n] = A[n] * S[0]
        else:
            AS[n] = A[n] * S[1]


        AS[n] = AS[n] + AS[n-1]

    return AS[-1]

    pass

