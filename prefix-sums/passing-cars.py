#-*- coding: utf-8 -*-
# A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
# Array A contains only 0s and/or 1s:
# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 <= P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
# For example, consider array A such that:
#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
# Write a function:
# def solution(A)
# that, given a non-empty zero-indexed array A of N integers, returns the number of passing cars.
# The function should return −1 if the number of passing cars exceeds 1,000,000,000.
# For example, given:
#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# the function should return 5, as explained above.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

def prefix_sum(A):
    n = len(A)
    p = [0] * (n + 1)
    for k in xrange(1, n + 1):
        p[k] = p[k - 1] + A[k - 1]
    return p

def solution(A):
    rst = 0
    p = prefix_sum(A)
    n = len(A)
    for i in xrange(0, n):
        if rst > 1000000000:
            return -1
        if A[i] == 0:
            if i == 0:
                rst += p[n]
            elif i == (n - 1):
                break
            else:
                rst += p[n] - p[i]
    return rst
