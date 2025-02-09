subject = ("Doreamon", "Ben10", "Tom And Jerry", "Oggy") #it's starts from 0 so (Doreamon=0), (Ben10=1), (Tom And Jerry=2), (Oggy=3)

print(subject)

print(subject[3]) #it will print 3 = (output: Oggy) it only print oggy

print(subject[2:]) #it will print 2 = (output: Tom And Jerry, Oggy) it will print 2 and after all what ever left

print(subject[-2]) #it will start from behind -2 = (output: Tom And Jerry) it only print Tom And Jerry

print("Doreamon" in subject) #output = True, beacuse it's in the subject 

print("Rick And Morty" in subject) #output = False, beacuse it's not in the subject 

print("Rick And Morty" not in subject) #output = True, beacuse it's not in the subject 

print(subject + ("Rick And Morty", 27)) #Too add with subject

print(subject * 2) #it will print it twise

print(subject [2]* 2) #it will print only that one twise (it will go with every rule)