import random
import Poker
import System 



player_num = input("How many players do you want to play?: ")


player_hand = []
enemy_hand = []

players_hands = []


System.initPoker()
deck = System.resetDeck()




player_hand.append(deck.pop(random.randrange(1,len(deck))))
player_hand.append(deck.pop(random.randrange(1,len(deck))))
