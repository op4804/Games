import random
import Poker
import System 



'''
player_num = int(input("How many players do you want to play?: \n(please input only numbers)\n"))

'''
players_hands = []
player_num = 2
for i in range(player_num):
    players_hands.append([])

''' 
here is the init points
'''
System.initPoker(players_hands)
deck = System.resetDeck()
field = []

players_hands[0].append(deck.pop(random.randrange(1,len(deck))))

players_hands[1].append(deck.pop(random.randrange(1,len(deck))))

players_hands[0].append(deck.pop(random.randrange(1,len(deck))))

players_hands[1].append(deck.pop(random.randrange(1,len(deck))))

field.append(deck.pop(random.randrange(1,len(deck))))
field.append(deck.pop(random.randrange(1,len(deck))))
field.append(deck.pop(random.randrange(1,len(deck))))

System.showCurrenthands(players_hands,field)
System.waitInput()
field.append(deck.pop(random.randrange(1,len(deck))))
System.showCurrenthands(players_hands,field)
System.waitInput()
field.append(deck.pop(random.randrange(1,len(deck))))
System.showCurrenthands(players_hands,field)
System.waitInput()

