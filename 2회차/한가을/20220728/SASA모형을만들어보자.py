# 백준 23825
# SASA 연못에서 알파벳 S 모양의 블록 N개와
# 알파벳 A모양의 블록 M개를 던졌다.
# 연못에서 건진 블록을 이용해 SASA 모형을 최대한 많이 만들려고 한다.
# 모형 1개를 만들기 위해서는 S 모양 블록 2개와
# A 모양 블록 2개가 필요하다.
# 만들 수 있는 모형 개수의 최대값

# 첫째 줄에 알파벳 S 모양의 블록 개수 N과
# 알파벳 A 모양의 블록 개수 M이 공백으로 구분되어 주어진다.

N, M = map(int, input().split())

if N % 2 == 0 or M % 2 == 0:
    print(min(N, M) // 2)
elif N % 2 == 1 or M % 2 == 1:
    print(min(N, M) // 2)