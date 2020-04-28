## Create an empty list of hobbies
my_hobbies=[]

print(my_hobbies)

## Add your fav hobbies

my_hobbies.append("drawing")
my_hobbies.append("playing guitar")
my_hobbies.append("dancing")
my_hobbies.append("chitchatting")
my_hobbies.append("coding")

print(my_hobbies)

print(len(my_hobbies))

## Insert your most fav hobbies at start
my_hobbies.insert(0,"singing")

print(my_hobbies)

## Delete one hobby
del my_hobbies[4]
print(my_hobbies)

## Removed one hobby bases on index number and store it in temprary variable
not_so_like=my_hobbies.pop(1)
print("Now a days I don't prefer  "+not_so_like+" ;since I have many more other tasks to do on priority")
print(my_hobbies)

## Remove hobby if you know the name of hobby
my_hobbies.remove("dancing")
print("My latest updated hobby list is:")
print(my_hobbies)

print("My hobby sorted hobby list contains :")
print(sorted(my_hobbies))

my_hobbies.append("travelling")
##print the list in reverse order
##print(my_hobbies.reverse())  -- Can not do print and reverse operation in the same command
my_hobbies.reverse()
print(my_hobbies)

## double reverse converted list in original format
my_hobbies.reverse()

## sort the list
my_hobbies.sort()
print(my_hobbies)

print("I have "+str(len(my_hobbies))+ " favourite hobbies. Those are as follows")
print(my_hobbies)

