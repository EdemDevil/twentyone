import random as r

# variable
user_cards = []
dealer_cards = []
user_score = sum(user_cards)
dealer_score = sum(dealer_cards)


def rand_card():
    """Gives out a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards)
    return card


def first_hand():
    """Simulation of the first hand of cards with the output of the result"""
    for _ in range(2):
        user_cards.append(rand_card())
    for _ in range(2):
        dealer_cards.append(rand_card())

    print(f"Your cards: {user_cards}, current score: {score(sum_score=user_cards)}\n"
          f"Dealer`s first card: {dealer_cards[0]}\n")


def next_hand():
    """Simulation of the next hand of cards with the output of the result"""
    user_cards.append(rand_card())
    dealer_cards.append(rand_card())

    print(f"Your cards: {user_cards}, current score: {score(sum_score=user_cards)}\n"
          f"Dealer`s first card: {dealer_cards[0]}\n")


def score(sum_score):
    """Returns the total number of points in the deck at the moment"""
    return sum(sum_score)


def final_score():
    """Calculates the total number of points"""
    print(f"Your final hand: {user_cards}, final score: {score(sum_score=user_cards)}\n"
          f"Dealer final hand: {dealer_cards}, final score: {score(sum_score=dealer_cards)}")


def winner():
    """Determining the winner in the game"""
    user = score(sum_score=user_cards)
    dealer = score(sum_score=dealer_cards)

    if user == dealer or (user > 21 and dealer > 21):
        print("                   DRAW\n")
    elif user == 21 or (user > dealer and (user <= 21 > dealer)) or user < dealer > 21:
        print("                   WIN\n")
    elif user > 21 or (dealer == 21 and (dealer <= 21 > user)) or (user < dealer < 21):
        print("                   LOSE\n")


def main():
    """The main body of the program"""
    user_cards.clear()
    dealer_cards.clear()
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    first_hand()

    while start_game == 'y':
        cont_game = input("Type 'y' to get another card, type 'n' to pass: ")
        if cont_game == 'y':
            next_hand()
        else:
            final_score()
            winner()
            break

    main()


main()
