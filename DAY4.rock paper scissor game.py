rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list1 = [rock, paper, scissors]

# User choice
try:
    user_choice = int(input("What do you choose: type 0 for rock, 1 for paper, 2 for scissors: "))
    if user_choice > 2 or user_choice < 0:
        print("Invalid number.")
    else:
        n = list1[user_choice]
        print("Your choice:")
        print(n)

        # Random choice
        import random

        m = random.choice(list1)
        print("Computer's choice:")
        print(m)

        # Determine the winner
        if n == rock and m == scissors:
            print("You won!")
        elif n == paper and m == rock:
            print("You won!")
        elif n == scissors and m == paper:
            print("You won!")
        elif n == m:
            print("Draw")
        else:
            print("You lose.")
except ValueError:
    print("Please enter a valid integer.")
