# 1157번 단어 공부

words = input().upper()
alp = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []

for x in alp :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(alp[max_index])