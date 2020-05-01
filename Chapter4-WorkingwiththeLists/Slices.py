### 4-10. Slices: 

cakes=["Red velvet","Black forest","White forest","Cheese cake","Fruit cake","Butter cake"]
print("My 3 top favourite cakes are:")
for cake in cakes[:3]:
    print(cake)

print(len(cakes))

print("Three items from the middle of the list are:")
for cake in cakes[2:5]:
    print(cake)

print("The last three items in the list are:")
for cake in cakes[3:7]:
    print(cake)