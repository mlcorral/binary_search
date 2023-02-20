#!/bin/python3:
def find_smallest_positive(xs):
    if len(xs) == 0:
        return None
    
    def go(left, right):
        if xs[left] > 0:
            return left
        if left == right:
            return None
        
        mid = (left + right) // 2
        
        if xs[mid] > 0 and (mid == left or xs[mid-1] <= 0):
            return mid
        
        if xs[mid] <= 0:
            left = mid + 1
        else:
            right = mid - 1
        
        return go(left, right)
    
    return go(0, len(xs) - 1)

def count_repeats(xs, x):
    def find_first(xs, x):
        left, right = 0, len(xs)
        while left < right:
            mid = (left + right) // 2
            if xs[mid] < x:
                right = mid
            else:
                left = mid + 1
        return left

    def find_last(xs, x):
        left, right = 0, len(xs)
        while left < right:
            mid = (left + right) // 2
            if xs[mid] >= x:
                left = mid + 1
            else:
                right = mid
        return left

    return find_last(xs, x) - find_first(xs, x)

def argmin(f, lo, hi, epsilon=1e-3):
    while hi - lo > epsilon:
        mid1 = lo + (hi - lo) / 3
        mid2 = hi - (hi - lo) / 3
        if f(mid1) < f(mid2):
            hi = mid2
        else:
            lo = mid1
    return (lo + hi) / 2

def find_boundaries(f):
    lo, hi = -1, 1
    while f(hi) < f(lo):
        lo, hi = hi, 2 * hi
    return lo, hi

def argmin_simple(f, epsilon=1e-3):
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)


