n = int(input("Enter the last term: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i  
    i = i + 2   #calculates the sum (if the number is 5 then : 1 + 2 + 3 + 4 + 5 = 10) 
print(sum)