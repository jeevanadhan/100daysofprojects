import art
def find_highest_bid(bid_dict):
    highest_bid = 0
    winner = ""
    for bidder in bid_dict:
        bid_amount=bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"{winner} with highest bid {bid_amount} won")
print(art.logo)

bid_dict={}
bid_continue= True
while bid_continue:
        name = input("enter your name :")
        bid_value = int(input("enter your bid :"))
        bid_dict[name] = bid_value
        should_continue=input("tp add another bidder type yes else no").lower()
        if should_continue=="no":
            find_highest_bid(bid_dict)
            bid_continue=False
        else:
            print("\n" * 5)