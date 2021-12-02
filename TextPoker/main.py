import random

def resetDeck(deck:list):
    reseted = ["HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK",
"SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK",
"DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK",
"CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK"
]
    return reseted

def calcRanking(cards:list):
    objhands = makeHand(cards)

def deleteSame(lst:list):
    newlist = []
    for i in range(len(lst)):
        if lst[i] in newlist:
            pass
        else:
            newlist.append(lst[i])
    newlist.sort()
    return newlist 


def makeHand(cards:list):
    clone = []
    hand_list = []
    for i in range(len(cards)):
        clone = cards.copy()
        clone.pop(i)
        for j in range(len(clone)):
            cclone = clone.copy()
            cclone.pop(j)
            hand_list.append(cclone)
    return deleteSame(hand_list)

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


#print(deck)
'''
cnt=0
for i in range(5):
    print(deck.pop(random.randrange(1,len(deck))),end=" ")
#print(deck)

'''



'''
두명 대결해서 확률 보여주는걸로 하자.

'''


'''
7개의 카드중 5개를 뽑는 경우의 수
7*6*5*4*3

5!

중복 없으면? 

어떻게 해야할까

7개중 5개를 넣어서 
소트를 해서 중복제거?
 

'''


deck_list = []
