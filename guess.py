import random
secret = random.randint(1, 10)
guess = input("Guess 1 to 10: ")
if int(guess) == secret:
    print("YOU WIN!!!")
else:
    print("Nope, it was " + str(secret))