import random
from art import logo

print(logo)
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Draw two cards
def starting_deck():
    cards = []
    draw_card(cards)
    draw_card(cards)
    return cards

# Draw single card
def draw_card(deck):
    deck.append(random.choice(card_list))
    return deck

# Total points in hand
def add_deck(deck):
    total = 0
    for card in deck:
        total += card
    return total

# Converts ace to 1 if total is greater than 21
def check_for_ace(total, deck):
    if total > 21 and 11 in deck:
        index = deck.index(11)
        deck[index] = 1
        new_total = add_deck(deck)
        print(f"Because of the ace, your new hand is: {deck}\n")
        print(f"Because of the ace, your new total is: {new_total}")
        return new_total
    else:
        return total

# Method for game
def blackjack():
    computer_hand = starting_deck()
    user_hand = starting_deck()
    # shows points in your hang
    print(f"\n The dealers first hand is: {computer_hand[0]}\n")
    print(f"Your total points are: {add_deck(user_hand)}\n Your hand is: {user_hand}\n")
    # prompts to draw another card
    while True:
        draw_again = input(
            "Would you like to draw another hand? Yes or No\n").lower()
        if draw_again == "yes":
            draw_card(user_hand)
            print(
                f"Your total points are: {add_deck(user_hand)}\n Your hand is: {user_hand}\n")
            continue
        elif draw_again == "no":
            print(f"\nYour total is: {add_deck(user_hand)}")
            print(f"Your deck is {user_hand}\n")
            break
        else:
            print("\nPlease submit a valid response.\n")
            continue
    # computer draws additional card if total < 16
    while True:
        if int(add_deck(computer_hand)) < 16:
            computer_hand = draw_card(computer_hand)
            continue
        else:
            print(f"The dealers total is: {add_deck(computer_hand)}")
            print(f"The dealers hand is: {computer_hand}\n")
            break
    # Converts total hand value from cards, and changes ace to 1 if total > 21
    user_total = add_deck(user_hand)
    user_total = check_for_ace(user_total, user_hand)
    computer_total = add_deck(computer_hand)
    computer_total = check_for_ace(computer_total, computer_hand)
    # Computes whether you win or lose.
    if user_total < 21 and user_total > computer_total:
        print("You win!")
    elif computer_total > 21 and user_total < 21:
        print("You win!")
    else:
        print("You lose!")
    cont_choice = input("Would you like to continue? Yes or No").lower()
    if cont_choice == 'yes':
        blackjack()

# Prompts to start game again
blackjack_start = input("Would you like to start a game of blackjack? Yes or "
                        "No\n").lower()
if blackjack_start == 'yes':
    blackjack()





