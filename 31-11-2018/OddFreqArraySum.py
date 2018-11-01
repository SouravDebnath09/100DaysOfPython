# The objective is to find the summation of the odd elements in the array
# Define a simple array
sample =[12,33,54,89,776,3]
# Get length of the array
l= len(sample)
s=0
# Looping on the array up to max length to sum up the odd elements
for i in range(l):
    if (i%2!=0):
        s = s + int(sample[i])

#print the summation
print(s)

