# [0 1 1 2 3 5 8 13]

def fibonacci(n):
    #base case: n is 0 or 1
    #cannot be calculated
    if n <= 1:
        return n 
    #recursive case: fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

#%%
num1 = 0
num2 = 1
n = 4
for x in range(n):
    if x <= 1:
        continue
    else:
        temp = num1 + num2
        num1 = num2
        num2 = temp
#%% sys library allows interaction with operating system
import sys

sys.getrecursionlimit() #depeneds on operating system and cache size
# %%
def writeVerticalIterative(n):
    if n < 10:
        print(n)
        return
    array = []
    while n >= 10:
        array.append(n % 10)
        n = n // 10

    print(n)

    for digit in range(len(array)-1, -1, -1):
        print(array[digit])
# %%
def headRecursion(n):
    if n > 0:
        headRecursion(n-1)
        print(n)

headRecursion(10)
# %%
def even_ones(listofOnes, index):
    if index == len(listofOnes):
        return "Even"
    if listofOnes[index] == '1':
        return odd_ones(listofOnes, index + 1)
    else:
        return even_ones(listofOnes, index + 1)
    
def odd_ones(listofOnes, index):
    if index == len(listofOnes):
        return "Odd"
    if listofOnes[index] == '1':
        return even_ones(listofOnes, index + 1)
    else:
        return odd_ones(listofOnes, index + 1)
# %%
import random
def userTurn():
    userInput = input("Enter rock, paper, or scissors (or exit): ").lower()
    if userInput == "exit":
        print("Thanks for playing")
        return 
    if userInput not in ['rock', 'paper', 'scissors']:
        print("Invalid, try again")
        return userTurn()
    else:
        playRound(userInput)

def playRound(userChoice):
    choices = ['rock,' 'paper', 'sciossors']
    compChoice = random.choice(choices)
    print(f"Computer chose {compChoice}")
    if userChoice == compChoice:
        print("It's a tie!")
    elif (userChoice == 'rock' and compChoice == 'scissors') or (userChoice == 'paper' and compChoice == 'rock') or (userChoice == 'scissors' and compChoice == 'paper' ):
        print("You win!")
    else:
        print("Computer wins!")

userTurn()
