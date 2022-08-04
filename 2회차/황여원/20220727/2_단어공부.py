# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성.
# 단, 대문자와 소문자를 구분하지 않는다.

word = input().upper() # 가장 많이 사용된 알파벳을 대문자로 출력, Upper통해 대문자로 바꿈
word_list = list(set(word)) #중복제거 후 인덱싱이 가능하도록 리스트에 담기 ->  ['N', 'B', 'A']
# print(word_list)
cnt = []
# word를 반복하니까 똑같은 단어의 갯수를 여러번 찍어냄 -> 중복 제거해줘야겠다 
# 중복을 제거한 word_list를 만들고 반복 
for i in word_list :
    # count는 리스트안에 있는 i의 갯수를 알려주는 함수 
    num = word.count(i) 
    # print(num) # -> 3,1,2
    cnt.append(num) # cnt라는 빈 리스트를 만들고 count를 추가 
# cnt 리스트에서 가장 큰 수가 두개 이상이면 가장 많이 사용된 알파벳이 여러 개 존재하는 경우
# -> ? 출력 
if cnt.count(max(cnt)) >= 2 :
    print('?')

else : 
    print(word_list[(cnt.index(max(cnt)))])



