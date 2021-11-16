#### Describe each datatype below:(4 marks)

## 4         = integer
## 5.7       = float
## True      = boolean
## Good Luck = string

#### Which datatype would be useful for storing someone's height? (1 mark)
## float

#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## string

####Create a variable tha will store the users name.(1 mark)
userName = input("Please enter your name: ")

####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
print(userName[:4])

####Convert the user's name to all uppercase characters and print the result
print(userName.upper())

####Find out how many times the letter A occurs in the user's name
print(userName.count("A"))

#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.
age = int(input("Welcome to the computer science competition!\nPlease enter you age: "))
if age >= 18:
  print("You can enter the competition!")
elif age < 18:
  print("We're sorry, but you are too young to enter the competition")

#### Create an empty list called squareNumbers (3 marks)
squareNumbers = []

#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).

for number in range(20):
  squaredNumber = number**2
  squareNumbers.append(squaredNumber)

####Print your list (1 mark)
print(squareNumbers)

####Create a variable called userSquare that asks the user for their favourite square number
squareNumbers2 = []
for number2 in range(1000000):
  squaredNumber2 = number2**2
  squareNumbers2.append(squaredNumber2)
userSquare = int(input("What's your favourite square number?\t"))
while userSquare not in squareNumbers2:
  print("This is not a square! Try again:")
  userSquare = int(input("What's your favourite square number?\t"))# I created a list with the first 1000000 square numbers to make sure that the number entered by the user is actually a square number. This does't work with all the squares but there's a great chance that the number chosen by the user is in the list

#### Add this variable to the end of your list called SquareNumbers
squareNumbers.append(userSquare)

### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.(3 marks)
import random
num1 = random.randint(0,19)
choice = squareNumbers[num1]

####Create another print statement that prints tha following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)

print("The random square number is",choice)