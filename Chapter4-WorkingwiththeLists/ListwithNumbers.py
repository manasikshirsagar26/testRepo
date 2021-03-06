## 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive .
for num in range(1,21):
    print(num)

## 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers . (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .)
# for mil in range (1,10000001): 
#     print(mil)

##4-5. Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million . 
# Also, use the sum() function to see how quickly Python can add a million numbers .
mil_list=list(range (1,1000001))
print(min(mil_list))
print(max(mil_list))
print(sum(mil_list))

##4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 .
#  Use a for loop to print each number .
odd_list = list(range(1,20,2))
print("Below is the odd number list between 1 to 20:")
for odd_num in odd_list:
    print(odd_num)


##4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list .
mul_3= list(range(3,31,3))
print("Table of 3:")
for mul3 in mul_3:
    print(mul3)

##4-8. Cubes: A number raised to the third power is called a cube . For example, the cube of 2 is written as 2**3 in Python . 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube .

num_cube=list(range(1,11))
print("Cube of 1 to 10 numbers:")
for cub in num_cube:
    print(cub**3)


##4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .
Cube_list=[value**3 for value in range(1,11)]
print("list of cubes for numbers 1 to 10")
print(Cube_list)