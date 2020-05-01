##4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five simple foods,
#  and store them in a tuple .
#   * Use a for loop to print each food the restaurant offers .
#   * Try to modify one of the items, and make sure that Python rejects the change .
#   * The restaurant changes its menu, replacing two of the items with different foods . 
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu .

import os,sys

Buffet_menu=("Idli","Pizza","Pasta","Meduwada")

print("\nBuffet Menu List:")
for menu in Buffet_menu:
    print(menu)

#Buffet_menu[0]="Cold coffee"

Buffet_menu=("Cold coffee",Buffet_menu[1],Buffet_menu[2],"Lemonade")

print("\nRevised buffet menu is:")
for menu in Buffet_menu:
    print(menu)

