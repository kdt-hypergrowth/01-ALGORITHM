# 🎞 후기
- 하루는 벽을 느끼고, 다시 다음날이 되면 조금 성장해감을 느끼는 것 같다.
- 부족한 것은 문법이 아니라 **문제를 바라보는 시각을 바탕으로한 알고리즘적 이해**임을 오늘도 깨닫는다!
- 조금씩 method와 함수 사용을 이어나가고 있다. 직관적이고 빠른 프로그래밍이 가능하지만 시간 복잡도 고려를 잊어서는 안됨! ([method 난사하다가 시간초과 난 케이스](./BOJ_1157.py))
- 코드리뷰를 할 때 마다 느끼는 것은, `작성한건 난데 왜 설명이 잘 안되는거지?` ... 더 많은 이해가 필요한듯하다.

## 💎 가장 강렬했던 문제
- 오늘 가장 큰 쾌감을 주었던 대망의 [버섯 처먹는 마리오 문제](./BOJ_2851.py)
- 작성한 코드의 양도 많아서 임팩트가 있었지만 이를 풀이하는 과정에서 카타르시스를 느낄 수 있었다.
- 주어진 문제에만 매몰되어 **무조건의 input**으로 data를 다루지 않고 받는 data를 가공해가며 문제에 접근할 수 있었다.
```python
def abs_val(n):  # 절댓값 내장함수도 있더라...?
    if n > 0:
        return n
    else:
        return -n

result = []
total_point = []
add_point = 0

for i in range(10):
    point = int(input())  # 원래 input
    add_point += point
    total_point.append(add_point)  # input으로 받은 data를 가지고 새로운 data를 정의

for i in range(len(total_point)):
    result.append(abs_val(100 - total_point[i]))  # 새로운 data (2)
```
- 문제를 바라보는 시야가 아주 조금씩 넓혀져가고 있다, 아직 많이 멀었지만 이렇게 꾸준하게 한다면 분명 큰 성취 이루리!