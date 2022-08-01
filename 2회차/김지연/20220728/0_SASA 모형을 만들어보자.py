# N, M = map(int, input().split())
# cnt = 0

# if N < M:
#     for i in range(N):
#         if N > 0:
#             N -= 2
#             M -= 2
#             cnt += 1
#         else:
#             break

# elif N == M:
#     while True:
#         if N > 0 and M > 0:
#             N -= 2
#             M -= 2
#             cnt += 1
#         elif N <= 0 or M <= 0:
#             break

# elif N > M:
#     for i in range(M):
#         if M > 0:
#             N -= 2
#             M -= 2
#             cnt += 1
#         else:
#             break

# print(cnt)

print(min(map(int, input().split())) // 2)