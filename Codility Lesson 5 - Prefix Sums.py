# Lesson 5.1:

def solution(A):
    # write your code in Python 3.6
    count = 0

    for x in range(len(A)):
        if count > 1000000000:
            count = -1
            break
        else:
            if A[x] == 0:
                for n in range(x, len(A)):
                    if A[n] == 1:
                        count += 1

    return count
    pass

#50% score: 100% correctness, 0% performance