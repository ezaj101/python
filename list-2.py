subject = ["Doreamon", "Ben10", "Tom And Jerry", "Oggy"] # it starts from 0 so (Doreamon=0), (Ben10=1), (Tom And Jerry=2), (Oggy=3)
#list always starts with third bracket []

print(len(subject)) #too get the value, how many subject are there.

subject.insert(2, "Rick") #2 is (Tom And Jerry) so it will print before Tom And Jerry. #output= ['Doreamon', 'Ben10', 'Rick', 'Tom And Jerry', 'Oggy']
print(subject) #it will allow you to add a subject from anywhere you want.

subject.remove("Oggy") #it will remove the subject
print(subject) #output= ['Doreamon', 'Ben10', 'Tom And Jerry']

subject.sort() #it will sort or organize subjects properly 
print(subject) #output= ['Ben10', 'Doreamon', 'Oggy', 'Tom And Jerry']

subject.reverse() #it will start from behind 
print(subject) #output= ['Oggy', 'Tom And Jerry', 'Ben10', 'Doreamon']

subject.pop() #it will clear the last one. output= ['Doreamon', 'Ben10', 'Tom And Jerry']
subject.pop() #if you did it again. it will clean last one after that. output= ['Doreamon', 'Ben10']
print(subject)

subject.clear() #it will clear everything 
print(subject) #output= []

pos = subject.index("Oggy") #position stay with a (variable = pos). it will tell you the position of the subject you need. 
print(pos) #output = 3 which is(oggy)

pos = subject.count("Oggy") #it will tell you how many same subjects are there in the same list.
print(pos) #output = 1 because oggy is only 1 in the list. if there are 2 oggy on the list then the output can be 2
