marks = 80
if marks >=80 and marks <=100: 
    print("A+")
elif marks >=70 and marks <=79: #iF WE WANT MORE LINE TO ADD THEN TYPE (elif)
    print("A")
elif marks <= 70:
    print("F")

#Or short way with different code

marks = 80
if 80 <= marks <= 100:
    print("A+")
elif 70 <= marks <= 79:
    print("A")
else:
    print("F")
