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

연속되는 숫자. 2번째 소트해서 

스트레이트 판정기
'''
def deleteSame(lst:list):
    newlist = []
    for i in range(len(lst)):
        if lst[i] in newlist:
            pass
        else:
            newlist.append(lst[i])
    newlist.sort()
    return newlist 

def replaceHand(hands:list,replacy:str, replacer:str):
    temp = 0
    for i in range(len(hands)):
        if hands[i] == replacy:
            temp = i
    origin_card = hands.pop(temp)
    origin_shape = origin_card[0]
    addable_card = origin_shape + replacer
    hands.append(addable_card)

    return hands

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

def checkStraight(hands:list):
    nums = []
    for i in range(len(hands)):
        nums.append(int(hands[i][1:]))
    nums.sort()
    
    isstraight = True
    if int(nums[0]) + 1 != int(nums[1]):
        isstraight = False
    elif int(nums[1]) + 1 != int(nums[2]):
        isstraight = False
    elif int(nums[2]) + 1 != int(nums[3]):
        isstraight = False
    elif int(nums[3]) + 1 != int(nums[4]):
        isstraight = False
    print(nums)
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
    nums = []
    for i in range(len(hands)):
        nums.append(int(hands[i][1:]))
    nums.sort()

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
        return -1



testhand = ["H4","SJ","S4","C4","D4"]
rank = [0,0]
testhand = changeRoyal(testhand)
print(checkPair(testhand))
