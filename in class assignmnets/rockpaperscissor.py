import random

def rockPaperScissors():
    pcinput = random.randint(1, 3)
    choice = input("Rock, Paper, or Scissors: ").lower()

# 1 = rock
# 2 = paper
# 3 = scissors

    if choice == "rock" and pcinput == 1:
        score("tie")
        
    if choice == "rock" and pcinput == 2:
        score("lose")

    if choice == "scissors" and pcinput == 3:
        score("win")




    return choice
    return pcChoice

def score(outcome):
    if outcome == "tie":
        print()
    if outcome == "win":
        print()
    if outcome == "lose":
        print()
