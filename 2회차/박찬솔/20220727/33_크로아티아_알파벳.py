# dž는 무조건 하나의 알파벳으로 쓰이고
# d와 ž가 분리된 것으로 보지 않는다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
#  몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
import sys

sys.stdin = open("33_크로아티아_알파벳.txt")

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 한 글자로 변환을 하고 이후에 변환된 문자열의 총 글자 수
word = input()

for i in croatia :               # 문자를 변환하는 함수 replace함수를 사용
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))                 # 구글링 했습니다! ㅠㅠ