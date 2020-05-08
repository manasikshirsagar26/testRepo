##5-2. More Conditional Tests: You don't have to limit the number of tests you create to 10 . 
# If you want to try more comparisons, write more tests and add them to conditional_tests.py . 
# Have at least one True and one False result for each of the following:
#           Tests for equality and inequality with strings
#           Tests using the lower() function
#           Numerical tests involving equality and inequality, greater than and less than, greater than or equal to,
#            and less than or equal to
#           Tests using the and keyword and the or keyword
#           Test whether an item is in a list
#           Test whether an item is not in a list
import os, sys

#           Tests for equality and inequality with strings
movie="DDLJ"
if movie == "DDLJ":
    print("Let us watch this movie tonight. SRK is my fav actor.")
else: 
    print("Which movie you would like to watch? Make sure choose something bollywood romantic !!!")


if movie != "DDLJ":
    print("Let us watch some bollywood romantic similar to DDLJ")
else:
    print("This is the best movie. Let us watch it tonight")


#           Tests using the lower() function
#           Test whether an item is in a list
#           Test whether an item is not in a list
list_name=["manasi","sayali","anuja","akshay"]
print("\nPlease enter your name")
name="Manasi"
if name.lower() in list_name:
    print(name+" is present in the list")
else:
    print(name+" is not present in the list")

if name.lower() is not list_name:
    print(name+" is not present in the list")
else:
    print(name+" is present in the list")


#           Numerical tests involving equality and inequality, greater than and less than, greater than or equal to,
#            and less than or equal to
#           Tests using the and keyword and the or keyword

party_people= 10
child=2
if party_people<=5 and child<=5:
    print("Book a smaller table")
else :
    if party_people>=10 and child>=10   :
        print("Book a moderate table")
    else:
        if party_people>=20:
            print("Book a hall")




party_people= 2
child=2
if (party_people>2 and party_people<=5) or (child>2 and child<=5):
    print("Book a smaller table")
else :
    if party_people>=10 and party_people<=20:
        print("Book a moderate table")
    else:
        if party_people<=2 or child<=2:
            print("Cancel the party")

