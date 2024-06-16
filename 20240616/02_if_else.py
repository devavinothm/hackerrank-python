# problem: 
# n is a positive integer
# if n odd, print "Weird"
# if n is even and in the inclusive range of 2 to 5, print "Not Weird"
# if n is even and in the inclusive range of 6 to 20, print "Weird"
# if n is even and greater than 20, print "Not Weird"

# solution

n = int(input())
if n % 2 == 1:
    print("Weird")
else:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")