S, A = map(int,input().split())

# SASA 네개가 한쌍 -> s,a 합을 4로 나눈 몫이 sasa 한쌍의 갯수..?

# sum_ = S + A 
# print((S + A) // 4)

# 두개가 필요하니까 ..
SA = min(S,A)
print(SA//2)