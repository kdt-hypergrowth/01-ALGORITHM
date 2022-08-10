a, b = map(int, input().split())        # 두 자연수
x = abs(((a-1) // 4) - ((b-1) // 4))    # x좌표 거리(4로 나눈 몫)
y = abs(((a-1) % 4) - ((b-1) % 4))      # y좌표 거리(4로 나눈 나머지)
print(x + y)                            # 직각거리는 x + y