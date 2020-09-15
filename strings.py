# challange
# Guessing game

answer = 7
guess = int(input("Enter your Guess:"))

if guess == answer:
    print("Hurray!...You guessed at First attempt")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess Lower")
    guess = int(input())
    if guess == answer:
        print("Correct guess..Well done!")

    else:
        print("Sorry..! Better luck next time")
string = " my name is unknown"
string.replace("unknown", "saiteja", 2)
print(string)
# converting string to ascii values
print(ord("z"))
string = "sachin tendulakar"
print(list(enumerate(string)))
print(list(enumerate(string, 100)))
str1 = "sai"
str2 = "teja"
str3 = str1.__add__(str2)
print(str3)
