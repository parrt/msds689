def subsetsum(A, n):
    A = sorted(A)
    return subsetsum_(A, len(A)-1, n)


def subsetsum_(A, i, n):
    "Return true if there is a subset within A[0:i+1] that sums to n"
    if n==0:
        return True
    if n<0 or i<0:
        return False
    if subsetsum_(A, i-1, n-A[i]) or subsetsum_(A, i-1, n):
        return True
    return False


for i in range(30):
    print(i, subsetsum([7, 3, 2, 5, 8], i))