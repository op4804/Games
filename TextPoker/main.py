import random
import Poker




'''
시작

게임반복

게임끝


게임클리어판정



돈 10000원
100원

'''
enemy_money = 10000
my_money = 10000
def gameend():
    if enemy_money < 0:
        return True
    else:
        return False
while(gameend()):
    deck = ["HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK",
"SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK",
"DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK",
"CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK"
] 

print("Welcome to Poker game")
print("shuffling...")
player_hand = []
opponent_hand = []
field = []

player_hand.append(deck.pop(random.randrange(1,len(deck))))
player_hand.append(deck.pop(random.randrange(1,len(deck))))

opponent_hand.append(deck.pop(random.randrange(1,len(deck))))
opponent_hand.append(deck.pop(random.randrange(1,len(deck))))

print("your hand is ")
print(player_hand)
input("go next step?")
#print(opponent_hand)
print("shuffling...")
field.append(deck.pop(random.randrange(1,len(deck))))
field.append(deck.pop(random.randrange(1,len(deck))))
field.append(deck.pop(random.randrange(1,len(deck))))
print("field is")
print(field)
input("go next step?")
print("shuffling...")
field.append(deck.pop(random.randrange(1,len(deck))))
print("field is")
print(field)
input("go next step?")
print("shuffling...")
field.append(deck.pop(random.randrange(1,len(deck))))
print("field is")
print(field)
my_total_hand = field + player_hand
print("your hand is")
print(Poker.MakeStrongestHand(my_total_hand))  

deck_list = []
