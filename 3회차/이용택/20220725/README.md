# 🎞 후기

- 자신이 작성한 코드에 대해 한 줄 한 줄 설명을 하고 납득이 가는지를 확인하며 문제를 풀 수 있었음
- 평소 습관처럼 당연하게 작성하던 코드에 대해서도 뜯어보며 이해를 하는 방향으로 과제를 진행함
    - `map()` `input().split()` 등의 함수 또는 method의 작동원리를 계속해서 시뮬레이션
- `programmers`를 통한 알고리즘 문제 풀이를 시작할 수 있게됨 ! 기존의 온라인 저지와는 사뭇 다른 환경이었지만 어렵지 않게 적응할 수 있었음
    - 특히나 해당 플랫폼으로의 코딩테스트가 많이 치뤄지는 만큼 해당 온라인 저지를 많이 이용해야겠음!
-
## 💎 가장 강렬했던 문제

- 문제 : `2_두개뽑아서더하기.py (programmers)`
- 문제를 보자마자 직관적으로 떠올린 풀이가 계속해서 오답을 내어 당황하였음. 
1. i 번째에서 선택한 요소에 대하여 j번째에서 하나씩 전개하가며 더하면 답이 나올 줄 알고 작성하였는데 더한 횟수가 많은 것을 확인
=> 두번째 for loop에서 j의 시작값이 i 였음.
이로인해 i와 j가 같을 때에도 연산이 동작하여 더한 횟수가 더 많았음. **j + 1** 로 고쳐 오류 해결!
```python
 # 수정 전
for i in range(len(numbers) - 1):
    for j in range(i, len(numbers)):
    
# 수정 후
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
```

2. set() 및 sort()를 활용하여 자료구조를 output에 부합하게 바꿨다고 생각했는데 작동하지 않음
=> return value는 answer이었는데 내가 작성했던 코드는 아래와 같음
```python    
list(set(answer)).sort()
return answer
```
sort()가 동작한 객체는 answer이 아닌 전혀 다른 `list(set(answer))` 객체였음.
```python
answer = list(set(answer))
answer.sort()
return answer
```
과 같이 객체의 이름을 명시적으로 초기화하여 동일한 객체에 대한 method 적용! 
