##4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60) . 
# Make a copy of the list of pizzas, and call it friend_pizzas . Then, do the following:

#!/usr/bin/python
# -*- coding: ascii -*-
import os, sys

my_pizza=[]
print(my_pizza)

my_pizza.append("peperoni")
my_pizza.append("peppy paneer")
my_pizza.append("margaritta")

print(my_pizza)

friend_pizza=my_pizza[:]

#friend_pizza=my_pizza.copy()

print(friend_pizza)

## Add a new pizza to the original list .
my_pizza.append("cheese burst")

##Add a different pizza to the list friend_pizzas .

friend_pizza.append("Paneer makhani")

print(friend_pizza)
print(my_pizza)
## Prove that you have two separate lists .

print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)

print("\n")

print("My friend's favorite pizzas are:")
for pizzaz in friend_pizza:
    print(pizzaz)