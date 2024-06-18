# let n be a integer number
# if n = 1, then print 0
# if n = 2, then print 0, 1
# if n = 3, then print 0, 1, 4
# if n = 4, then print 0, 1, 4, 9
# if n = 5, then print 0, 1, 4, 9, 16

# solution:

n = int(input())

for i in range(n):
    print(i ** 2)