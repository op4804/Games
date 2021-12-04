'''
스트레이트 플러쉬 8 , 
포카드 7 
풀하우스6 
플러쉬5 
스트레이트 4 
트리플 3 
투페어 2
원페어 1
탑 0
'''

'''
[
[[1,2,3,4,5],'1'],
[[1,2,3,4,5],'1'],
[[1,2,3,4,5],'1'],
[[1,2,3,4,5],'1']
]

'''

def MakeStrongestHand(handslist:list):
    handsranking = [] 
    for i in range(len(handslist)):
        handsranking.append([handslist[i],calcRank(handslist[i])])
    
    print(handsranking)

    return handsranking

def calcRank(hands:list):
    rankpoints = 0






    return rankpoints

    return 0 

def findTopCard(hands:list):
    topnumber = 0
    cards = hands.copy()
    cards = changeRoyal(cards) 
    cards = eraseShape(cards)
    cards.sort()
    topnumber = int(cards[4])
    if topnumber < 10:
        topnumber = ('0'+str(topnumber))
    return topnumber
    
#조합이다! 
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

#리스트에서 중복을 제거해주는 함수
def deleteSame(lst:list): 
    newlist = []
    for i in range(len(lst)):
        if lst[i] in newlist:
            pass
        else:
            newlist.append(lst[i])
    newlist.sort()
    return newlist 

#리스트에서 replacy를 찾아 replacer로 바꿔주는 함수
def replaceHand(hands:list, replacy:str, replacer:str):
    temp = 0
    for i in range(len(hands)):
        if hands[i] == replacy:
            temp = i
    origin_card = hands.pop(temp)
    origin_shape = origin_card[0]
    addable_card = origin_shape + replacer
    hands.append(addable_card)
    return hands

#hand 에서 A,J,Q,K를 숫자로 바꿔주는 함수
def changeRoyal(hands:list):
    cards = hands.copy()

    for i in range(len(hands)):
        if hands[i][1] == 'A' or 'J' or 'Q' or 'K': 
            if hands[i][1] == 'A':           
                replaceHand(cards,'A','14')
            elif hands[i][1] == 'J':
                replaceHand(cards,'J','11')
            elif hands[i][1] == 'Q':
                replaceHand(cards,'Q','12')
            elif hands[i][1] == 'K':
                replaceHand(cards,'K','13')
            else:
                replaceHand(cards,hands[i][1:],hands[i][1:])
    return cards

def eraseShape(hands:list):
    nums = []
    for i in range(len(hands)):
        nums.append(int(hands[i][1:]))
    nums.sort()
    return nums

def checkStraight(hands:list):
    nums = eraseShape(hands)
    
    isstraight = True
    if int(nums[0]) + 1 != int(nums[1]):
        isstraight = False
    elif int(nums[1]) + 1 != int(nums[2]):
        isstraight = False
    elif int(nums[2]) + 1 != int(nums[3]):
        isstraight = False
    elif int(nums[3]) + 1 != int(nums[4]):
        isstraight = False
    if isstraight == False and int(nums[4]) == 14:
        if int(nums[0]) == 2 and int(nums[1]) == 3 and int(nums[2]) == 4 and int(nums[3]) == 5:
            isstraight = True
    return isstraight 

def checkFlush(hands:list):
    shapes = []
    isFlush = False
    for i in range(len(hands)):
        shapes.append(hands[i][:1])
    if shapes[0] == shapes[1] == shapes[2] == shapes[3] == shapes[4]:
        isFlush = True

    return isFlush

def checkPair(hands:list):
    nums = eraseShape(hands)

    nums_set = deleteSame(nums)
    
    if len(nums_set) == 5:
        return 0
    elif len(nums_set) == 4:
        return 1
    elif len(nums_set) == 3:
        twoortriple = nums.copy()
        for i in range(len(nums_set)):
            if nums_set[i] in twoortriple:
                twoortriple.remove(nums_set[i])
        if twoortriple[0] == twoortriple[1]:
            return 3
        else:
            return 2
    elif len(nums_set) == 2: # 풀하우스 일수도 있다 / 포카드랑 
        fullhouseorfourcard = nums.copy()
        for i in range(len(nums_set)):
            if nums_set[i] in fullhouseorfourcard:
                fullhouseorfourcard.remove(nums_set[i])
        if fullhouseorfourcard[0] == fullhouseorfourcard[1] == fullhouseorfourcard[2]:
            return 4
        else:
            return 6
    else:
        return -1 #오류



testhand = ["H4","S7","S4","C4","D6"]

rank = [0,0]
print(findTopCard(testhand))
