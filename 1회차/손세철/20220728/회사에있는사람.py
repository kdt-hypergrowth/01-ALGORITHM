import sys
sys.stdin = open("_회사에있는사람.txt")

N = int(input())
logs = dict()
for i in range(N):
    # 공백으로 나눠진 두개의 단어 
    key, value = (input().split())
    logs[key] = value
logs = dict()
logs["Baha"] = "enter"
logs["Askar"] = "enter"
logs["baha"] = "leave"
logs["Artem"] = "enter"


#print(logs)
list_ = []
for key in logs:
    print(key)
    #value가 enter인 key를 찾아서 리스트에 저장
    if logs[key] == "enter":
        #리스트에 저장
        list_.appned(key)
print(list_)
list_.sort(reverse=True)
