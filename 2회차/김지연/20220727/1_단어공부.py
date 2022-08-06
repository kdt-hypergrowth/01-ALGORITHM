import sys  

sys.stdin = open("1_단어공부.txt")

words = input().upper()
list_ = list(set(words))
cnt = []

for i in range(len(list_)):
    cnt.append(words.count(list_[i]))

max_ = max(cnt)

if cnt.count(max_) != 1:
    print('?')
else:
    print(list_[cnt.index(max_)])