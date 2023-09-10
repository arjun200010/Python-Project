import random
number=random.randint(1,50)
guess=int(input("Guess a number between 1 to 50:-"))
attempt=0
while guess!=number:
    if guess<number:
        print("You guessed very low.Try again!")
        attempt=attempt+1
        print("The number of attempts you have taken are:",attempt)
        guess = int(input("Guess a number between 1 to 50:-"))
    else:
        print("You guessed very high.Try again!")
        attempt=attempt+1
        print("The number of attempts you have taken are:", attempt)
        guess = int(input("Guess a number between 1 to 50:-"))
print("\n CONGRATULATIONS")
print("YOU GUESSED CORRECTLY")

