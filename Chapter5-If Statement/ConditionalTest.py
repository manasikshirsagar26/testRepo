##5-1. Conditional Tests: Write a series of conditional tests . 
# Print a statement describing each test and your prediction for the results of each test . 
# Your code should look something like this: car = 'subaru'
##print("Is car == 'subaru'? I predict True.") print(car == 'subaru')
##print("\nIs car == 'audi'? I predict False.") print(car == 'audi')
##      *Look closely at your results, and make sure you understand why each line evaluates to True or False .
##      *Create at least 10 tests . Have at least 5 tests evaluate to True and another 5 tests evaluate to False .


## if condition with string
fav_dish = 'Icecream'
if fav_dish=="Icecream":
    print("\nMy Fav dish is icecream")
else:
    print("\nMy favourite menu is not present in hotel")     

fav_dish = "pasta"
if fav_dish =="noodles":
    print("\nPasta is my fav dish")
else:
    print("\nMy fav dish is not present in the menu")


## If condition with number
lucky=10
if lucky== 9:
    print("My lucky number is 10")
else:
    print("I did not receive my lucky number this time")

### If condition with list
Fav_food = ["Pizza","puran poli","Pasta","Icecream","lemonade"]
if "pizza" in Fav_food:
    print("\nI like pizza")
else:
    print("\nwe will check some other restrarant menu because my non of my favourite dish is present here. My favourite dishes include:")
    for each in Fav_food:
        print(each)

## if condition with conditional operator
age =28
if age>=20 and age<=30:
    print("\nPeople in age group of 20 to 30 are welcome for party")
else:
    print("Why god me ?- Joe")

## If with boolen operator
game_active= True
if game_active==True:
    print("\nGame is still ON")
else:
    print("\nGame is done for the day")


