# Codility demo practice Q: https://app.codility.com/demo/take-sample-test/

def solution(A):
    # write your code in Python 3.6
    maxA = max(A)
    if maxA > 0:
        B = [B for B in range(1, maxA + 1)]
        C = [C for C in B if C not in A]
        try:
            D = C[0]
            return D
        except IndexError:
            return maxA + 1
    else:
        return 1
    pass
# Score 55%: 100% Correctness, 0% Performance

def solution(A):
    i = 1;
    B = set(A);
    while True:
        if i not in B:
            return i;
        i+=1
#Score 66%: 100% correctness, 25% performance


def solution(A):
    # write your code in Python 3.6
    maxA = max(A)
    B = [B for B in range(1, maxA + 2)]
    C = set(A)
    if maxA >= 1:
        for x in B:
            if x not in C:
                return x
    else:
        return 1
    pass
#Score 100%: 100% correctness, 100% performance: https://app.codility.com/c/feedback/demoH98MGV-TMU/

#CODILITY Q2
def solution(A):
    # write your code in Python 3.6

    len_count = 1
    current = A[0]
    while current != -1:
        len_count += 1
        current = A[current]
    return len_count
    pass
