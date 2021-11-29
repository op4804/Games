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

    highest = nums[4]

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

    return 0


testhand = ["SK","SJ","S4","SQ","S2"]
rank = [0,0]

print(testhand)
testhand = changeRoyal(testhand)
print(testhand)

print(checkFlush(testhand))

