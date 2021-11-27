'''
스트레이트 플러쉬 
포카드
풀하우스
플러쉬
스트레이트
트리플
투페어
원페어
탑

'''

'''
연속되는 숫자. 2번째 소트해서 


'''

'''
스트레이트 판정기


'''
testhand = ["SK","HK","CJ","CQ","CA"]
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
        if hands[i][1] == 'A':           
            replaceHand(cards,'A','14')
        elif hands[i] == 'J':
            replaceHand(cards,'J','11')
        elif hands[i][1] == 'Q':
            replaceHand(cards,'Q','12')
        elif hands[i][1] == 'K':
            replaceHand(cards,'K','13')
    print(cards)
    return cards

changeRoyal(testhand)


def checkStraight():
    return 0
