# Read the starting letter template
with open("./Input/letters/starting_letter.txt") as file:
    letters = file.read()

# Read and clean up the names list
with open("./Input/names/invited_names.txt") as file:
    names = [name.strip() for name in file.readlines()]

    # Generate a personalized letter for each name
    for i in names:
        mail = letters.replace("[name]", i)
        with open(f"./output/ReadyToSend/mail_for_{i}.txt", "w") as f:
            f.write(mail)
