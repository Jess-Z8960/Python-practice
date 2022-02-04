# Lesson 16.1 MaxNonoverlappingSegments: Find a maximal set of non-overlapping segments.
def solution(A, B):
    # write your code in Python 3.6

    if len(A) < 1 or len(B) < 1:
        return 0

    n = 1
    end = B[0]

    for i in range(1, len(A)):
        if A[i] > end:
            n += 1
            end = B[i]

    return n
    pass
# Score 100%! by moving 'end = B[0]' under 'if len(A) < 1 ...' = 100% score
# Otherwise, Score 90%: 80% Correctness (failed empty and single element with run time error:
# 'IndexError: list index out of range' at end = B[0]

# Lesson 16.2 TieRopes

def solution(K, A):
    # write your code in Python 3.6
    length = 0
    n = 0

    for r in A:
        length += r

        if length >= K:
            n += 1
            length = 0

    return n
    pass

