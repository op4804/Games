import random


def initPoker(playerhands:list):
    for i in range(len(playerhands)):
        playerhands[i] = []    
    #머니 
    #내덱
    #상대덱
    #전체댁
    #
    return playerhands
def initGame():
    return 0

def resetDeck():
    reseted = ["HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK",
"SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK",
"DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK",
"CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK"
]
    return reseted

def showCurrenthands(playerhands:list,field:list):
    print('field: ',field)
    print('yourhand: ',playerhands[0])
    return 0
def resetPocker():
    return 0

def initMoneySystem(money_set:list, playernum:int):

    money_set.append(0)

    for i in range(playernum):
        money_set.append(0)

    return money_set

def printCurrentStatus():
    return 0

def checkWinner():
    return 0

def calcMoney():
    return 0

def waitInput(word:str):
    input(word)
    return 0

def initWinRate():
    return 0

def draw(drawpoint:list,draworigin:list):
    drawpoint.append(draworigin.pop(random.randrange(1,len(draworigin))))

    return 0

def userinterface(players_hands:list,field:list):
    print("what do you want to do? ")
    user_input = input("1.show current hand\n2.show field\n")
    if(user_input == 1):
        showCurrenthands(players_hands,field)   
    elif(user_input == 2):
        print(field)
    else:
        return -1
    return 0

