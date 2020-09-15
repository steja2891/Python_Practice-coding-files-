import random
highest = 20
answer = random.randint(1, highest)

while True:
    guess = int(input("Enter a number in between 1 and {} : ".format(highest)))
    if guess == answer:
        print("Hurray..Congratulations...")
        break
    elif guess != 0 and guess < answer:
        print("Please guess higher")
        print("If u want to quit, select '0'..")
    elif guess != 0 and guess > answer:
        print("Please guess lower")
        print("If u want to quit, select '0'..")
    elif guess == 0:
        print("Sorry,... Better luck next time.."
              "The Correct answer is {}".format(answer))
        break
