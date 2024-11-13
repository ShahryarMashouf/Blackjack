import random
logo = """ ===========================================================
    |                       LET'S PLAY BLACKJACK!             |
    |   Try to get as close to 21 as possible without going    |
    |   over! The dealer plays against you, and the best hand |
    |   wins!                                                 |
    ===========================================================
    """
def deal_card():
    # Returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # Take a list of cards and return the score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert Ace (11) to 1 if the score goes over 21

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lost, opponent has Blackjack"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(logo)
    user_card = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_double_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()  # Handle case insensitivity
            if user_double_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to draw cards until it reaches at least 17 or gets Blackjack
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Play the game in a loop
while input("Do you want to play a game of Blackjack? 'y' or 'n'").lower() == 'y':
    print("\n" * 20)
    play_game()
