import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
numSwaps = 0

while True:
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]  
            numSwaps +=1
            break
    else:
        break

print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
    