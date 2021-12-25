
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