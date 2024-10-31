import random,art
from sys import set_asyncgen_hooks


def blackjack():
    print(art.logo)
    def defcards(card):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card.append(random.choice(cards))

    def calcards(cards):
        result = sum(cards)
        if 11 in cards and result>21:
            cards.remove(11)
            cards.append(1)
            result=sum(cards)
        if result > 21:
            result = 0
        return result
    def winner_check(user,comp):
        if user==comp:
            print("it is draw")
        elif user==0:
            print("you lose the game")
        elif comp==0:
            print("you won the game")
        elif user>comp:
            print("you won the game")
        else:
            print("you lose the game")
    user_cards = []
    comp_cards = []
    for i in range(2):
        defcards(user_cards)
        defcards(comp_cards)
    print(f"your cards : {user_cards}")
    print(f"computer first card : {comp_cards[0]}")
    game_over=False
    while not game_over:
        collect_card=input("type y to get another card else type n").lower()
        if collect_card=="y":
            defcards(user_cards)
        else:
            game_over= True
        comp_score = calcards(comp_cards)
        if comp_score!=0 and comp_score<14:
            defcards(comp_cards)
            comp_score = calcards(comp_cards)
        user_score=calcards(user_cards)
        print(f"your cards {user_cards} current score {sum(user_cards)} \ncomputer first card {comp_cards[0]}")
        if user_score==0 or comp_score==0 or user_score>21:
            game_over=True

    print(f"final cards{user_cards} your final score {sum(user_cards)}")
    print(f"computer cards{comp_cards} computer score {sum(comp_cards)}")
    winner_check(user_score,comp_score)
should_play=input("do you want to play blackjacl type y or n").lower()
if should_play=="y":
    blackjack()
