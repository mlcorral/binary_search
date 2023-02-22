#!/bin/python3:


def find_smallest_positive(xs):
    if not xs:
        return None

    def go(left, right):
        if xs[left] > 0:
            return left
        if left == right:
            return None

        mid = (left + right) >> 1

        if xs[mid] > 0 and (mid == left or xs[mid - 1] <= 0):
            return mid

        if xs[mid] <= 0:
            left = mid + 1
        else:
            right = mid - 1

        return go(left, right)

    return go(0, len(xs) - 1)


def count_repeats(arr, n):
    count = 0
    for i in arr:
        if i == n:
            count += 1
    return count


def argmin(f, lo, hi, epsilon=1e-3):
    while hi - lo > epsilon:
        mid1 = lo + ((hi - lo) / 3)
        mid2 = hi - ((hi - lo) / 3)
        if f(mid1) < f(mid2):
            hi = mid2
        else:
            lo = mid1
    return ((lo + hi) / 2)


def find_boundaries(f):
    lo, hi = -1, 1
    while f(hi) < f(lo):
        lo, hi = hi, (hi << 1)
    return lo, hi


def argmin_simple(f, epsilon=1e-3):
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
