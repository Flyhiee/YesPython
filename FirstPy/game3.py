from random import randint
secret = randint(1, 10)
print("Welcome! To the Gussing game ")
guess = 0
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You win!")
    else:
        if guess > secret:
            print("Too High")
            print(f"You Guessed the number {guess} Secret number was {secret}" )
        else:
            print("Too Low")
            print(f"You Guessed the number {guess} Secret number was {secret}" )
print("Game over!")
