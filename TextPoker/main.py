'''
Main 은 게임이 돌아가는 부분이다. 
'''
import random
import Poker
import System 

#player_num = int(input("How many players do you want to play?: \n(please input only numbers)\n"))
# 향후 다수의 플레이어가 플레이 할 수있게 하는 부분. 

players_hands = []
player_num = 2 #현재는 2인을 기본 플레이로 한다. 
for i in range(player_num):
    players_hands.append([])

''' 
here is the init points
'''
System.initPoker(players_hands)
deck = System.resetDeck()

money_set = [] # [0] : 팟 / 나머지 각 플레이어들의 돈

money_set = System.initMoneySystem(money_set,player_num)

field = [] # 바닥에 깔리는 패

#각 플레이어에게 핸드 제공
System.draw(players_hands[0],deck)
System.draw(players_hands[1],deck)
System.draw(players_hands[0],deck)
System.draw(players_hands[1],deck)

# 바닥에 3장 세트
System.draw(field,deck)
System.draw(field,deck)
System.draw(field,deck)

System.userinterface(players_hands,field)

print("your hand is:")
System.showCurrenthands(players_hands,field)
System.waitInput('')
System.draw(field,deck)
System.showCurrenthands(players_hands,field)
System.waitInput('')
System.draw(field,deck)
System.showCurrenthands(players_hands,field)
System.waitInput('next?')

print(money_set)

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
