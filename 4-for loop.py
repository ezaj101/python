num = [10, 20, 30, 40, 50] # it will calculate total
sum = 0 # Because sum is 0 that's why it calculate only num. if you put sum = 5 it will calculate total (150) and plus sum(5) = 155
for x in num:
    sum += x
print(sum)  # Output: 150

num = [10, 20, 30, 40, 50]  # A list of numbers
for x in num:                # Loop through each element in the list
    print(x)                 # Print the current element (x)
