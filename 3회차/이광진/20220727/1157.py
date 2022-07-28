# 단어 공부
s = input().upper()
s_set = list(set(s)) # .set() 으로 중복 값 제거 후 list 생성
cnt = []

for i in s_set:
    cnt.append(s.count(i)) # cnt 리스트에 입력받은 문자열의 알파벳 갯수 추가

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(s_set[cnt.index(max(cnt))])
# s_set 리스트와 cnt 리스트의 알파벳 갯수 순서가 동일함
# 가장 높은 숫자 위치를 s_set으로 적용