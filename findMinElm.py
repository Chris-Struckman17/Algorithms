#!/usr/bin/python

# Finds Minimun element in the array. The nth element in the array "smallest" is
#the minimum element in the nth subspace of A
def findMinElm(A,i):
    smallest =[A[0]]

    mini = A[0]
    counter = 0
    while(0 <= counter <= i-1):
        if (A[counter] < A[counter+1]):

            if(A[counter]<= mini):
                smallest.append(A[counter])
                mini = A[counter]
            else:
                smallest.append(mini)

            counter = counter + 1
        else:
            if(A[counter+1]<= mini):
                smallest.append(A[counter+1])
                mini = A[counter+1]
            else:
                smallest.append(mini)
            counter = counter + 1
    return smallest[len(A)-1]

#A = [12,2,3,6,7,1,10,15]
#print findMinElm(A,4)



#Finds the max profit over time of the data.
def findMaxProfit(B,smallest):
    i = 0
    maximum = B[0]

    while(i< len(B)-1):
        if(B[i] >= B[i+1]):
            if( maximum <= B[i]):
                profit = B[i] - smallest
                maximum = B[i]
                i = i+1
            else:
                i = i+1;

        else:
            if( maximum <= B[i+1]):
                profit = B[i+1] - smallest
                maximum = B[i+1]
                i = i+1
            else:
                i = i+1;


    print smallest
    return profit

B = [12,5000,3,6,300,1,10,150000]
print findMaxProfit(B, findMinElm(B,len(B)-1))
