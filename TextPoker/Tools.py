'''
Tools 는 기본적인 기능을 가지고 있는 함수를 정의해 놓은 곳이다. 

'''


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