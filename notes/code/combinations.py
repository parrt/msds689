def combinations(A):
    """
    Just as an exercise to think about all combinations...
    Powerset: all subsets of A, including empty set. Grab the first value in A,
    then find all combinations for the remaining elements. The result is those
    combinations plus those combinations prefixed with A[0].
    """
    if len(A)==0:
        return [[]]
    pre = A[0]
    r = combinations(A[1:])
    return r + [[pre] + v for v in r]

A = [1,2,3,4]
print(list(combinations(A)), "len =", len(combinations(A)))

