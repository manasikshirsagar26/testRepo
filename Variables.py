message=("I am doing Python Crash course")
print(message)

message=("Python is great language to learn")
print(message)


###String Concatenation
name="Manasi"
print("\nHello "+ name +",would you like to learn some Python today?\n")

###Uppercase lowercase TitleCase
firstname="manasi kshirsagar"
print(firstname.title())
print(firstname.lower())
print(firstname.upper())

### String with quotes
quote=('\nAlbert Einstine once said, "A person who never made mistake never tried anything new"')
print(quote)

famous_person="Albert Einstine "
quote1=(famous_person+'once said, "A person who never made mistake never tried anything new"')
print(quote1)

#### StrippingNames
myname=" Manasi Kshirsagar "
print(myname.strip())
print(myname.lstrip())
print(myname.rstrip())

myname="\tPython is my favourite language  "
print(myname.strip())
print(myname.lstrip())
print(myname.rstrip()) ## only consider \t for the rstrip function


myname="\tPython is my easy language to learn  \n"
print(myname.strip())
print(myname.lstrip()) ## only consider \n for the lstrip function
print(myname.rstrip()) ## only consider \t for the rstrip function
