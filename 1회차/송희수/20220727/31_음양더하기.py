def solution(absolutes, signs):
    answer = 0
    for x,y in zip(absolutes,signs):
        if y==True:
            answer+=x
        elif y==False:
            answer-=x
    return answer
