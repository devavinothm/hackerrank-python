'''

In the list of array, find the send maximum value and print it.

Input:

n -> number of elements in the list
A[] -> list of elements

Sample input:

5
2 3 6 6 5

Sample output:

5

Sample input:

4
2 5 9 8

Sample output:

8
'''

n = int(input())
A = list(map(int, input().split()))

max_val = max(A)
while max_val == max(A):
    A.remove(max_val)

print(max(A))