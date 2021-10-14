from random import randint
from art import logo

easy_lives = 10
hard_lives = 5
keep_playing = True

#Function to check user's guess against actual answer.
def checker(guess, answer, turns):
  if guess == answer:
    print("Correct, you win!")
  elif guess < answer:
    print("Too Low, try again")
    return turns -1
  elif guess > answer:
    print("Too High! Try again")
    return turns -1
#Make function to set difficulty.
def difficulty():
  level = input("Type 'easy' or 'hard' to select level: ").lower()
  if level == "easy":
    return easy_lives
  elif level == "hard":
    return hard_lives

def game():
  turns = difficulty()
  #Choosing a random number between 1 and 100.
  answer = randint(1, 100)
  print(f"Psst, the answer is {answer}")
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts left.")
    #Let the user guess a number.
    guess = int(input("Make a guess: "))
    turns = checker(guess, answer, turns)
    #Track the number of turns and reduce by 1 if they get it wrong.
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()
