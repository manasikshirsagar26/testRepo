##### 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd .
#                Most ordinal numbers end in th, except 1, 2, and 3 .
#                       Store the numbers 1 through 9 in a list .
#                       Loop through the list .
#                       Use an if-elif-else chain inside the loop to print the proper ordinal end- ing for each number . 
#Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line .

Ordinal_numbers =[1,2,3,4,5,8,9,6,7]

for numb in Ordinal_numbers:
    if numb==Ordinal_numbers[0]:
        print("1st number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[1]:
        print("2nd number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[2]:
        print("3rd number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[3]:
        print("4th number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[4]:
        print("5th number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[5]:
        print("6th number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[6]:
        print("7th number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[7]:
        print("8th number in the list is:"+str(numb))
    elif numb==Ordinal_numbers[8]:
        print("9th number in the list is:"+str(numb))