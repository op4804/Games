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
System.waitInput('')
field.append(deck.pop(random.randrange(1,len(deck))))
System.showCurrenthands(players_hands,field)
System.waitInput('')
field.append(deck.pop(random.randrange(1,len(deck))))
System.showCurrenthands(players_hands,field)
System.waitInput('next?')

money_set = []
# 0 -> 팟
# 1~ 플레이어의 돈


'''
<돈의 흐름>
각자 플레이어는 일정의 돈을 가지고있음
나 / 너 플레이어가 더 많다면 음

선 

후
내야 하는 금액


콜 / 다이 / 레이즈
팟(모인 돈)


게임 끝 / 오픈
남은사람이먹고
오픈 - > 승부 
이긴사람이 먹는다
무승부 시 
반반 나눠먹기



'''
