import random
import art
print(art.logo)
print("welcome to the number guessing game:\n i'm thinking of a number between 1 to 100")
level=input("choose a difficulty level easy or hard:")
def num_guess(level):
    if level=="easy":
        attempts=10
    else:
        attempts=5
    crt_num=random.randint(1,100)
    while attempts!=0:
        print(f"you have {attempts} attempts remaining to guess")
        guess_num=int(input("make a guess "))
        if guess_num==crt_num:
            return f"you got it the answer was {crt_num}"
        if guess_num > crt_num:
            attempts-=1
            print("too high")
        if guess_num < crt_num:
            attempts-=1
            print("too low")
    return "you have run out of gases"
print(num_guess(level))