# https://www.acmicpc.net/problem/3046

R1, S = map(int, input().split())

# S = (R1 + R2) / 2
# R2 = 2S - R1

R2 = S * 2 - R1

print(R2)