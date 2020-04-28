### Guest List

guest=["Pooja","Ashutosh","Bhagi","Chaitali"]
print("Good evening "+guest[0]+", I would like you invite for dinner tonight")

print("Good evening "+guest[1]+",I would like you invite for dinner tonight")

print("Good evening "+guest[2]+",I would like you invite for dinner tonight")

print("Good evening "+guest[3]+",I would like you invite for dinner tonight")


guest_cannt_make_dinner=guest.pop(3)

guest.insert(3,"Saloni")


print("Hello , \nGood evening, Unfortunately "+guest_cannt_make_dinner.title()+ " can not make dinner tonight.I would like you invite "+guest[3]+" for dinner tonight")


#### New invitation list

print(guest)

print("Good evening "+guest[0]+", I would like you invite for dinner tonight at 8pm")

print("Good evening "+guest[1]+",I would like you invite for dinner tonight at 8pm")

print("Good evening "+guest[2]+",I would like you invite for dinner tonight at 8pm")

print("Good evening "+guest[3]+",I would like you invite for dinner tonight at 8pm")


#### More Guest 

guest.insert(3,"Abhijeet")
guest.append("Renuka")
guest.insert(1,"Durva")

print(guest)

print("Hello "+guest[0]+", \nThere is slight change in plan as guest list is updated. We should meet at 8:30pm Today")

print("Hello "+guest[1]+", \nThere is slight change in plan as guest list is updated. We should meet at 8:30pm Today")

print("Hello "+guest[2]+", \nThere is slight change in plan as guest list is updated. We should meet at 8:30pm Today")

print("Hello "+guest[3]+", \nThere is slight change in plan as guest list is updated. We should meet at 8:30pm Today")

print("Hello "+guest[4]+", \nThere is slight change in plan as guest list is updated. We should meet at 8:30pm Today")

print("Hello "+guest[5]+", \nThere is slight change in plan as guest list is updated. We should meet at 8:30pm Today")

print("Hello "+guest[6]+", \nThere is slight change in plan as guest list is updated. We should meet at 8:30pm Today")


### Calculate the number of invitees
# abc=len(guest)
# print(abc)
# print(type(abc))
print("Total number of guests coming to the party tonight : "+str(len(guest)))
### Can invite only two people now

print(guest)

print("I am really sorry for the last minute plan change. Due to unavailability of the table I can invite only two people for dinner tonight.")

popped_list=guest.pop(6)
print("Hello "+popped_list+" , I am really sorry; there is slight change in the plan of today's dinner.We can plan it for some other day")

popped_list=guest.pop(5)
print("Hello "+popped_list+" , I am really sorry; there is slight change in the plan of today's dinner.We can plan it for some other day")

popped_list=guest.pop(4)
print("Hello "+popped_list+" , I am really sorry; there is slight change in the plan of today's dinner.We can plan it for some other day")

popped_list=guest.pop(3)
print("Hello "+popped_list+" , I am really sorry; there is slight change in the plan of today's dinner.We can plan it for some other day")

popped_list=guest.pop(2)
print("Hello "+popped_list+" , I am really sorry; there is slight change in the plan of today's dinner.We can plan it for some other day")

print(guest)

print("Hello "+guest[0]+" , Please be on time and let's enjoy the dinner tonight")

print("Hello "+guest[1]+" , Please be on time and let's enjoy the dinner tonight")


## delete the remaining two members from the list
del guest[0]

del guest[0]

### Print the empty lists
print(guest)
