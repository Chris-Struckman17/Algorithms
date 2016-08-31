#!/usr/bin/python
#This algorithm determines whether there is a matching element in a sorted array of size n give 2 arrays
#Repurposing the merge algorithm of merge sort, hence the name
def mergeCompare(A,B):
    i = 0
    j = 0
    while(i < len(A) and j < len(B)):
        if (A[i] == B[j]):
            return A[i]
        else:
            if(A[i] < B[j]):
                i = i+1
            elif(A[i] > B[j]):
                j = j+1
    return False

A = [1,2,4,5,7,8,9]
B = [3,5,10,15,16]
print mergeCompare(A,B)
