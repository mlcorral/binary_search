#!/bin/python3:
def find_smallest_positive(xs):
    if not xs:
        return None

    def go(left, right):
        if xs[left] > 0:
            return left
        if left == right:
            return None

        mid = (left + right) // 2

        if xs[mid] > 0 and (mid == left or xs[mid - 1] <= 0):
            return mid

        if xs[mid] <= 0:
            left = mid + 1
        else:
            right = mid - 1

        return go(left, right)

    return go(0, len(xs) - 1)


def count_repeats(xs, x):
    if len(xs) == 0:
        return 0

    def go(left, right):
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        result = None
        mid = (left + right) // 2
        if xs[mid] == x:
            result = mid
            if xs[mid - 1] == x and mid != 0:
                right = mid - 1
            else:
                return result
        elif x < xs[mid]:
            left = mid + 1
        else:
            right = mid - 1
        return go(left, right)

    a = go(0, len(xs) - 1)

    def go2(left, right):
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        result = None
        mid = (left + right) // 2
        if xs[mid] == x:
            result = mid
            if xs[mid + 1] == x and (mid + 1) < len(xs):
                left = mid + 1
            else:
                return result
        elif x > xs[mid]:
            right = mid - 1
        else:
            left = mid + 1
        return go2(left, right)

    a2 = go2(0, len(xs) - 1)

    if a is not None and a2 is not None:
        return (a2 - a) + 1
    else:
        return 0


def argmin(f, lo, hi, epsilon=1e-3):
    if hi - lo <= epsilon:
        return (lo + hi) / 2
    else:
        mid1 = lo + ((hi - lo) / 3)
        mid2 = hi - ((hi - lo) / 3)
        if f(mid1) < f(mid2):
            return argmin(f, lo, mid2, epsilon)
        else:
            return argmin(f, mid1, hi, epsilon)


def find_boundaries(f):
    lo, hi = -1, 1
    while f(hi) < f(lo):
        lo, hi = hi, (hi << 1)
    return lo, hi


def argmin_simple(f, epsilon=1e-3):
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
