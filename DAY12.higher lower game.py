import game_data, art,random
from game_data import data

should_continue = True
score = 0
print(art.logo)
n=random.randint(0,49)
j=random.randint(0,49)

while should_continue:
    if n==j:
        j=random.randint(0,49)
    # Define the keys to show relevant information for each person
    keys = ["name", "country", "description"]

    # Print details for person A
    print(f"Compare A: {', '.join(data[n].get(i) for i in keys)}")

    # Print VS separator
    print(art.vs)

    # Print details for person B
    print(f"Compare B: {', '.join(data[j].get(i) for i in keys)}")

    # Get user input (A or B)
    ans = input("Who has more followers? A or B: ").lower()

    # Determine the correct answer based on follower count
    if data[n]['follower_count'] > data[j]['follower_count']:
        correct_answer = "a"
    else:
        correct_answer = "b"
        n=j
    j=random.randint(0,49)

    # Check if the user’s answer is correct
    if ans == correct_answer:
        print("\n"*20)
        print(art.logo)
        score += 1
        print(f"You got it! Current score: {score}")
        # Prints the score immediately after a correct answer

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False
