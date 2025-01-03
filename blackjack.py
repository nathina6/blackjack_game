import random
from art import logo

def deal_card():
    """Returns a random cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare (u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose computer has blackjack"
    elif u_score == 0:
        return "Win you have a blackjack !"
    elif c_score > 21:
        return"Opponent we over. You win !"
    elif u_score>21:
        return "YOU LOSE YOU WENT OVER 21!"
    elif u_score>c_score:
        return "You win!!!"
    else :
        return "You lose..."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current_score: {user_score}")
        print(f"Computers first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            answer = input("Do you want to draw another card? yes or no \n")
            if answer.lower() == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score  != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score =  calculate_score(computer_cards)


    print(f"Your final hand : {user_cards}, Final_score : {user_score}")
    print(f"Your final hand : {computer_cards}, Final_score : {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play another game of blackjack type 'y' or 'n'") == "y":
    play_game()
