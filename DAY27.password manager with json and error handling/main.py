import pandas


data=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for index,row in data.iterrows()}
def start():
    user_word = input("enter a word :").upper()
    try:
        output_list=[phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("sorry, only letters in the alphabet.")
        start()
    else:
        print(output_list)


start()