def solution(s):
    # 인덱스 == 숫자 영어
    table = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'
        ]   

    # table 요소가 input string에 있다면 replace 적용
    for i in range(len(table)):
        if table[i] in s:
            s = s.replace(table[i], str(i))
    
    # casting
    answer = int(s)  # string은 오류...! ouput양식이 지정되어있을듯...
    
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))