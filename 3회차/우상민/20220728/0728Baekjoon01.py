# 백준 SASA 모형을 만들어보자 23825
#당신은 SASA 연못에서 알파벳 S 모양의 블록 $N$개와 알파벳 A 모양의 블록 $M$개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.

# SASA 모형 $1$개를 만들기 위해서는, 알파벳 S 모양의 블록 $2$개와 알파벳 A 모양의 블록 $2$개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

SA = []
S, A = map(int, (input().split()))
SA.append(S)
SA.append(A)

if SA[0] > SA[1]:
    print(SA[1] // 2)
elif SA[0] < SA[1]:
    print(SA[0] // 2)
else:
    print(SA[0] // 2)

