import sys
sys.stdin = open('애너그램.txt')

t = int(input())                                      # 테스트 케이스 수

for i in range(t):
    a, b = map(str, input().split())                  # 두 단어 a, b

    x = sorted(list(a))                               # a의 단어를 오름차순으로 정리
    y = sorted(list(b))                               # b의 단어를 오름차순으로 정리

    if x == y:                                        # 두 단어가 같다면 순서를 바꾸어도 가능
        print("%s & %s are anagrams." %(a, b))        
    else:
        print("%s & %s are NOT anagrams." %(a, b))    