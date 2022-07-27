# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

word = input().lower()             
word_list = list(set(word))     # 받은 문자를 중복을 제거하여 리스트로 만든다.  

result = []                         
for i in word_list:             # 리스트의 각각의 값을 카운트하여 result에 갯수로서 집어넣는다.
    count_ = word.count(i)              
    result.append(count_)           

if result.count(max(result)) >=2:        # 리스트의 최댓값이 1개를 초과하면 ?를 출력한다.
    print('?')
else:
    print(word_list[(result.index(max(result)))].upper())       # 아니라면 max(result)의 result의 인덱스값을
                                                                #word_list에서 찾아 대문자로 출력





