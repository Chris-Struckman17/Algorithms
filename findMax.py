#!/usr/bin/python

#This Code finds the maximum digit in an array using divide and conquer algorithm that takes O(logn).
def findMax(a,l,r):
    mid = int ((l+r)/2)
    if (a[mid] > a[mid+1] and a[mid] > a[mid-1] ):
        return a[mid]
    else:
        if(a[mid] < a[mid-1]):
            return findMax(a,l,mid)
        else:
            return findMax(a,mid,r)
