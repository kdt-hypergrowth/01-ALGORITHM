# programmers Lv 1 숫자 문자열과 영단어

def solution(s):
    num2str = {
        'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 
        'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7',
        'eight' : '8', 'nine' : '9'}
    # 각 숫자와 영단어를 딕셔너리로 생성
    for i in num2str.keys() : # 딕셔너리의 key, 즉 영단어가 주어진 단어 s에 있을 시 replace로 숫자로 바꿔줌
        if i in s :
            s = s.replace(i, num2str[i])
    answer = int(s)
    return answer