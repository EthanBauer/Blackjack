import random
class Deck():
    def __init__(self):
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        score = 0
        for card in self.cards:
            if card.isdigit():
                score += int(card)
            elif card in ['J', 'Q', 'K']:
                score += 10
            elif card == 'A':
                if score + 11 <= 21:
                    score += 11
                else:
                    score += 1
        return score
    def dealer_score(self):
        if self.cards[0].isdigit():
            score = int(self.cards[0])
        elif self.cards[0] in ['J', 'Q', 'K']:
            score = 10
        elif self.cards[0] == 'A':
            score = 11
        return score

class Player:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        card = deck.deal_card()
        self.hand.add_card(card)

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        card = deck.deal_card()
        self.hand.add_card(card)

    def play_turn(self, deck):
        while self.hand.calculate_score() < 17:
            self.hit(deck)

deck = Deck()
print(deck.cards)
player = Player()
dealer = Dealer()
for _ in range(2):
    player.hit(deck)
    dealer.hit(deck)

player_score = player.hand.calculate_score()
dealer_score = dealer.hand.dealer_score()

print(f"Player Cards: {player.hand.cards[0]} {player.hand.cards[1]}")
print(f"Player Score: {player_score}")
print(f"Dealer Cards: {dealer.hand.cards[0]}")
print(f"Dealer Score: {dealer_score}")
while True:
    if player_score == 21:
        print("Player Wins!")
        break
    elif dealer_score == 21:
        print("Dealer Wins!")
        break
    print("Do you want to hit or stand?")
    choice = input()
    if choice == 'hit':
        player.hit(deck)
        player_score = player.hand.calculate_score()
        print(f"Player Cards: {player.hand.cards}")
        print(f"Player Score: {player_score}")
        print(f"Dealer Cards: {dealer.hand.cards[0]}")
        print(f"Dealer Score: {dealer_score}")
        if player_score > 21:
            print("Player Busts!")
            break
    elif choice == 'stand':
        dealer.play_turn(deck)
        dealer_score = dealer.hand.calculate_score()
        print(f"Dealer Cards: {dealer.hand.cards}")
        print(f"Dealer Score: {dealer_score}")
        if dealer_score > 21:
            print("Dealer Busts!")
            break
        elif dealer_score > player_score:
            print("Dealer Wins!")
            break
        elif dealer_score == player_score:
            print("Tie!")
            break
        else:
            print("Player Wins!")
            break
    else:
        print("Invalid input! Try again.")
        continue
