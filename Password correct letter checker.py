# Return n number of characters in both A and B

A = input("Enter first string: ")
B = input("Enter second string: ")


def solution(A, B):
    Alist = list(A)
    Blist = list(B)
    n = 0
    for x in Blist:
        if x in Alist:
            n += 1
    return n
    print(Alist)


print(solution(A, B))
