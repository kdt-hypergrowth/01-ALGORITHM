# 23825
#당신은 SASA 연못에서 알파벳 S 모양의 블록 N개와 알파벳 A 모양의 블록 $M$개를 건졌다. 
#태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.
#SASA 모형 1를 만들기 위해서는, 알파벳 S 모양의 블록 2개와 알파벳 A 모양의 블록 2개가 필요하다. 
#태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.
s, a = map(int,input().split())
c = s // 2
d = a // 2
if c > d :
    print(d)
else:
    print(c)

