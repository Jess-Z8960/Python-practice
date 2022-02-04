#

def solution(K, A):
    # write your code in Python 3.6
    L = len(A)
    bs = 0
    bs += len(A)

    for i in range(L - 1):
        for x in range(i + 1, L):
            if max(A[i:x + 1]) - min(A[i:x + 1]) <= K:
                bs += 1
            else:
                continue

    return bs

    pass

# 50% Score, 100% correctness, 0% performance O(N**3)