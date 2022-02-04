# Lesson 3.1: Frog jump - Count minimal number of jumps from position X to Y.

def solution(X, Y, D):
    # write your code in Python 3.6
    Y = Y
    n = 0
    while X < Y:
        X = X + D
        n += 1
    return n
    pass
# WILL FAIL PERFORMANCE TEST e.g. [1, 1000000000, 1]

def solution(X, Y, D):
    # write your code in Python 3.6
    Z = Y - X
    N = Z // D
    if Z % D != 0:
        return N + 1
    else:
        return N
    pass
# SCORE: 100%!


# Lesson 3.2: GOLD. Perm Missing Elem: Find missing element in given permutation

def solution(A):
    # write your code in Python 3.6
    L = len(A)
    if L == 0:
        return 1
    minA = min(A)
    maxA = max(A)

    if minA > 1:
        return 1

    A.sort()
    for x in range(0, maxA - 1):
        if A[x] + 1 != A[x + 1]:
            return A[x] + 1

    else:
        return A[-1] + 1

    pass
# Score: 100% !!



# Lesson 3.3: TapeEquilibrium - Minimize the value (A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1]).
def solution(A):
    # write your code in Python 3.6
    Plist = []
    N = len(A)
    for P in range(1, N):
        A1 = sum(A[0:P])
        A2 = sum(A[P:])
        Diff = abs(A1 - A2)
        Plist.append(Diff)

    Pmin = min(Plist)
    return Pmin

    pass


# Score 53%: 100% Correctness, 0% Performance

def solution(A):
    # write your code in Python 3.6
    m = []
    s = sum(A)
    Psub = 0
    for x in A[:-1]:
        Psub += x
        m.append(abs(s - 2 * Psub))

    return min(m)

    pass
# Score 100% on everything!! https://app.codility.com/demo/results/training4Y5KNY-DZA/
