# Codility Lesson 2.1: Arrays - Cyclic Rotation. Rotate array A to the right by K times.
def solution(A, K):
    # write your code in Python 3.6
    i = 0
    L = len(A)
    if L >= 1:
        while i != K:
            x = A[-1]
            A.insert(0, x)
            A.pop()
            i += 1
        return A
    else:
        return A
    pass


solution([3, 8, 9, 7, 6], 3)

solution([], 3)


# Score 100%: empty array accounted for by adding lines 5 and 6.

# Lesson 2.2: Arrays - Odd occurences in Array. Find value that occurs in odd number of elements.
def solution(A):
    # write your code in Python 3.6
    for x in A:
        n = A.count(x)
        if n % 2 != 0:
            return x

    pass


# Score 66%: Timeout error on large N in arrays. Not efficient due to reading same info repeatedly

def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    A.sort()
    for x in range(0, len(A) - 1, 2):  # 0, 2, 4
        if A[x] != A[x + 1]:
            return A[x]

    return A[-1]

    pass
# Score 100% on both correctness and performance.
