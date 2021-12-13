'''
랭킹 점수를 줄때 족보
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
내가 가지고있는 모든 핸드에 대한 정보
[
[[1,2,3,4,5],'1'],
[[1,2,3,4,5],'1'],
[[1,2,3,4,5],'1'],
[[1,2,3,4,5],'1']
]
'''

'''
TODOLIST 211214

같은 랭킹일때 최고를 뽑는 함수 구현@@@



'''

'''

메모

핸드 / 카드 
핸즈 / 카즈
구별할것 

플레이어들 끼리 비교할때는 
핸드 / 랭킹
이겼다 졌다만 출력하면 그만 


'''




# 가지고있는 핸드중 가장 높은 숫자의 카드를 돌려주는 함수
def findTopCard(hands:list):
    topnumber = 0
    cards = hands.copy()
    cards = changeRoyal(cards) 
    cards = removeShape(cards)
    cards.sort()
    topnumber = int(cards[4])
    if topnumber < 10:
        topnumber = ('0' + str(topnumber))
    return topnumber

# 풀하우스, 포카드, 트리플, 투페어, 원페어일때 페어인 카드를 출력해주는 함수 
def findMatchCard(hands:list):
    match_card = 0
    cards = hands.copy()
    tier = checkPair(cards)
    cards = changeRoyal(cards)
    cards = removeShape(cards)
    cards_set = deleteSame(cards)
    
    if tier == 1 or tier == 3 or tier == 4:
        for i in range(len(cards_set)):
            if cards_set[i] in cards:
                cards.remove(cards_set[i])
        match_card = cards[0]
    elif tier == 2:
        
        for i in range(len(cards_set)):
            if cards_set[i] in cards:
                cards.remove(cards_set[i])
        cards.sort()
        match_card = cards[1]
    elif tier == 6:
        for i in range(len(cards_set)):
            if cards_set[i] in cards:
                cards.remove(cards_set[i])
        for i in range(len(cards_set)):
            if cards_set[i] in cards:
                cards.remove(cards_set[i])
        match_card = cards[0]

    if match_card < 10:
        match_card = ('0' + str(match_card))
    return match_card

# 제시한 7개의 카드로 가능한 모든 핸드의 리스트를 반환해주는 함수
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

# 리스트에서 중복을 제거해주는 함수
def deleteSame(lst:list): 
    newlist = []
    for i in range(len(lst)):
        if lst[i] in newlist:
            pass
        else:
            newlist.append(lst[i])
    newlist.sort()
    return newlist 

# 리스트에서 replacy를 찾아 replacer로 바꿔주는 함수
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

# hand 에서 A,J,Q,K를 숫자로 바꿔주는 함수
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

# hand에서 앞에 문양을 없애고 숫자만돌려주는 함수
def removeShape(hands:list):
    nums = []
    for i in range(len(hands)):
        nums.append(int(hands[i][1:]))
    nums.sort()
    return nums

# Straight인지 판별해주는 함수 Retrun type : bool
def checkStraight(hands:list):
    cards = hands.copy()
    cards = changeRoyal(cards)
    nums = removeShape(cards)
    
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

# Flush인지 판단해주는 함수 Retrun type : bool
def checkFlush(hands:list):
    shapes = []
    isFlush = False
    for i in range(len(hands)):
        shapes.append(hands[i][:1])
    if shapes[0] == shapes[1] == shapes[2] == shapes[3] == shapes[4]:
        isFlush = True

    return isFlush

# Pair 와 나머지를 판별해주는 함수 리턴값 0 : 아님 / 1 : 원페어 / 2 : 투페어
# 3 : 트리플 / 4 : 포카드 / 6 : 풀하우스 <-왜 5를 건너 뛰었지..?
def checkPair(hands:list):
    hands = changeRoyal(hands)
    nums = removeShape(hands)
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

# 자신이 될 수 있는 모든 패중 가장 높은 핸드를 돌려주는 함수 (제작중)
def MakeStrongestHand(handslist:list):
    allhands = makeHand(handslist)
    handsranking = []
    toprank = 0
    alltophands = []
    tophands = []
    for i in range(len(allhands)):
        handsranking.append([calcRank(allhands[i]),allhands[i]])

    toprank = handsranking[0][0]
    for i in range(len(handsranking)):
        if toprank < handsranking[i][0]:
            toprank = handsranking[i][0]
    

    for i in range(len(handsranking)):
        if toprank == handsranking[i][0]:
            alltophands.append(handsranking[i][1])
    if len(alltophands) == 1:
        tophands = alltophands[0]
    else:
        tophands = findHigestHand(alltophands)

    return tophands

# 가장 높은 함수 
def findHigestHand(cards:list):
    tophands = []
    allcards = []
    allcards_set = []
    sharedcards = []
    distinguish_cards = cards.copy()
    distinguish_nums = []
    

    for i in range(len(cards)):
        for j in range(len(cards[0])):
            allcards.append(cards[i][j])

    allcards.sort()
    allcards_set = deleteSame(allcards)

    for i in range(len(allcards_set)):
        if allcards.count(allcards_set[i]) == len(cards):
            sharedcards.append(allcards_set[i])
    tophands.append(sharedcards)
    for i in range (len(cards)):
        for j in range(len(sharedcards)):
            distinguish_cards[i].remove(sharedcards[j])
        
    print(distinguish_cards)
    while(len(tophands) != 5):
        findHighestElement(distinguish_cards)
        findHigestHand
    
    '''
    for i in range(len(distinguish_cards)):
        distinguish_nums.append(removeShape(changeRoyal(distinguish_cards[i])))
    
    print(distinguish_nums)
    print(max(distinguish_nums))
    '''
    



    return tophands


def findHighestElement(cards:list):
    have_highest_el = []
    hands = []
    for i in range(len(cards)):
        for j in range(len(cards[0])):
            hands.append(cards[i][j])
    
    hands = changeRoyal(hands)
    nums = removeShape(hands)
    nums_set = deleteSame(nums)
    print(nums_set)
    highest = max(nums_set)
    if highest > 10 :
        if highest == 11:
            highest = 'J'
        elif highest == 12:
            highest = 'Q'
        elif highest == 13:
            highest = 'K'
        elif highest == 14:
            highest = 'A'

    print(highest)
    for i in range(len(cards)):
        for j in range(len(cards[0])):
            if cards[i][j][1] == str(highest):
                have_highest_el.append(cards[i])

    have_highest_el.sort()
    return have_highest_el 
'''
구조를 짜보자.  

함수 1  
2와 3을 호출



함수 2

리스트중 중복되는거 빼고
중복되는거 반환
남는 리스트 반환



함수 3
리스트중 가장 높은 원소를 가지고 있는 리스트들을 반환





'''

# 핸드를 제공하면 카드 점수를 돌려주는 함수
def calcRank(hands:list):
    rankpoints = 0
    if bool(checkFlush(hands)) == True:
        if bool(checkStraight(hands)) == True:
            rankpoints = 8
            rankpoints = str(rankpoints) + str(findTopCard(hands))
        else:
            rankpoints = 5
            rankpoints = str(rankpoints) + str(findTopCard(hands))
    elif bool(checkStraight) == True and bool(checkFlush) == False:
        cards = changeRoyal(hands)
        nums = removeShape(cards)
        nums.sort()
        if int(nums[0]) == 2 and int(nums[1]) == 3 and int(nums[2]) == 4 and int(nums[3]) == 5:
            rankpoints = 4
            rankpoints = str(rankpoints) + "05"
        else:
            rankpoints = 4
            rankpoints = str(rankpoints) + str(findTopCard(hands))
    else:        
        checkpair = checkPair(hands)

        if checkpair == 6:
            rankpoints = 6
            rankpoints = str(rankpoints) + str(findMatchCard(hands))
        elif checkpair == 4:
            rankpoints = 7
            rankpoints = str(rankpoints) + str(findMatchCard(hands))
        elif checkpair == 3:
            rankpoints = 3
            rankpoints = str(rankpoints) + str(findMatchCard(hands))
        elif checkpair == 2:
            rankpoints = 2
            rankpoints = str(rankpoints) + str(findMatchCard(hands))        
        elif checkpair == 1:
            rankpoints = 1
            rankpoints = str(rankpoints) + str(findMatchCard(hands))
        elif checkpair == 0:
            rankpoints = 0
            rankpoints = str(rankpoints) + str(findTopCard(hands))   
    return rankpoints


testallcards = ["DA","D4","D2","D5","DJ","S2","D6"]
testhand = ["DQ","S3","SA","H2","DJ"]

rank = [0,0]

MakeStrongestHand(testallcards)


