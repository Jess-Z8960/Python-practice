# 4.4 MissingInteger: Find the smallest positive integer that does not occur in a given sequence.
def solution(A):
    maxA = max(A)
    B = [B for B in range(1, maxA + 2)]
    C = set(A)
    if maxA >=1:
        for x in B:
            if x not in C:
                return x
    else:
        return 1
pass

# Score 100% on all factors. N.B. set(A) line 5 crucial for performance! Otherwise it will fail large arrays with Timeout Error


# 4.1 FROG RIVER ONE: Find the earliest time when a frog can jump to the other side of a river.
def solution(X, A):
    # write your code in Python 3.6
    B = set(range(1, X + 1))
    lcover = 0
    for pos, leaf in enumerate(A):
        if leaf in B:
            B.discard(leaf)
            lcover += 1
            if lcover == X:
                return pos
    if lcover != X:
        return -1
# Score 100%: set() is more time efficient than list[] for in operations & membership checking!

def solution(X, A):
    # write your code in Python 3.6
    B = [B for B in range(1, X + 1)]
    lcover = 0
    for pos, leaf in enumerate(A):
        if leaf in B:
            B.remove(leaf)
            lcover += 1
            if lcover == X:
                return pos
    if lcover != X:
        return -1
    # Score 63%: 100% Correctness, 20% performance because B is list instead of set

#Draft:
def solution(X, A):
    # write your code in Python 3.6
    B = [B for B in range(1, X + 1)]
    Bsum = sum(B)
    Jump = 1
    for x in range(0, len(A)):
        if A[x] in B:
            B.remove(A[x])
            Bsum = sum(B)
            Jump += 1

    if Bsum == 0:
        return Jump
    else:
        return -1

    pass
# Was scrapped due to incorrect results with Jump value at A[-1]


# 4.2 Permutation Check: Check whether Array A is a permutation (contains 1 to N once, and ONLY once)

def solution(A):
    # write your code in Python 3.6
    if len(A) < max(A):
        return 0
    else:
        A.sort()
        for ind, N in enumerate(A):
            if ind != N -1:
                return 0
        else:
            return 1
    pass
# Score 100% !!!


# 4.3

def solution(N, A):
    # write your code in Python 3.6
    counter = [0] * N
    for K, X in enumerate(A):
        if 1 <= X <= N:
            counter[X-1] += 1
        else:
            M = max(counter)
            counter = [M] * N
    return counter
    pass
# Score 66%: 100% Correctness, 40% Performance





