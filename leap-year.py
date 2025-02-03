Year = int(input("Enter year: "))
if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:  # % use as a remainder (10 divided by 3 leaves a remainder of 1)
    print(Year, "is a leap year")
else:
    print(Year, "is not a leap year")