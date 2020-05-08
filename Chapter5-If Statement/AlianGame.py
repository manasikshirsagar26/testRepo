###5-3. Alien Colors #1: Imagine an alien was just shot down in a game . 
#       Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red' .
#           Write an if statement to test whether the alien's color is green.If it is, print a message that the player just earned 5 points .
#           Write one version of this program that passes the if test and another that fails.(The version that fails will have no output .)

## Fail the test
alian_color="Red"
if alian_color.lower()=="green":
    print("The Player has earned 5 points")

## Test Success
alian_color="Green"
if alian_color.lower() == "green":
    print("The Player has earned 5 points")

### 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain .
#            If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien .
#            If the alien's color isn't green, print a statement that the player just earned 10 points .
#            Write one version of this program that runs the if block and another that runs the else block .

alian_color="red"
if alian_color.lower == "green":
    print("Alian colour is "+ alian_color+ " and The Player has earned 5 points")
else:
    print("Alian colour is "+ alian_color+ " and The Player has earned 10 points")

alian_color="Green"
if alian_color.lower() == "green":
    print("Alian colour is "+ alian_color+ " and The player has earned 5 points")
else:
    print("Alian colour is "+ alian_color+ " and The Player has earned 10 points")



##  5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif- else chain .
#               If the alien is green, print a message that the player earned 5 points .
#               If the alien is yellow, print a message that the player earned 10 points .
#               If the alien is red, print a message that the player earned 15 points .
#               Write three versions of this program, making sure each message is printed for the appropriate color alien .


alian_color="Red"
if alian_color.lower() == "green":
    print("Alian colour is "+ alian_color+ " and The player has earned 5 points")
elif alian_color.lower() =="yellow":
    print("Alian colour is "+ alian_color+ " and The Player has earned 10 points")
elif alian_color.lower() =="red":
    print("Alian colour is "+ alian_color+ " and The Player has earned 15 points")
else:
    print("Alian color does not match the colour in database")
