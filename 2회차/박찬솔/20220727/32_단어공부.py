# 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력
import sys

sys.stdin = open("32_단어공부.txt")

words = input().upper() # upper은 문자열의 문자를 모두 대문자로 바꾼다
unique_words = list(set(words))
# 입력받은 문자열에서 중복값을 제거
cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)
# count 숫자를 리스트에 append
if cnt_list.count(max(cnt_list)) > 1:
# count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
# count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])