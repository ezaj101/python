num = list(range(10)) # It starts with 0, so if you count from 0 to 9, it's a 10 number.
print(num) # Output = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print(num[2]) # Output = 2. If you put 0, it will print 0; if you put 1, it will print 1.


num = list(range(10,20)) # You can give a starting point and ending point
print(num) #output = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]. 
#Because range always stops before the stop value. If you want 20 to be included, you need to use range(10, 21).

num = list(range(10,21,2)) # Starts at 10, goes up to 20, adds 2 each time
print(num) #output = [10, 12, 14, 16, 18, 20]. If it was (10,20,2) output would be [10, 12, 14, 16, 18] because the Range function doesn't print the ending point.

