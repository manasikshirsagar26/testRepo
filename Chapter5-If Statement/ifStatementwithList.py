###5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website . Loop through the list, and print a greeting to each user:
##          If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
##          Otherwise, print a generic greeting, such as Hello Eric, thank you for log- ging in again.###



#### Addition


#####   5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty .
#               If the list is empty, print the message We need to find some users!
#               Remove all of the usernames from your list, and make sure the correct message is printed .

usernames=["Ulka","Snehal","Admin","Murty","Manas"]

if usernames:
    print("Our userlist is:\n")
    for username in usernames:
        if username== "Admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+username+", Thank you for log- ging in again. ")
else:
    print("We need to find some users")




