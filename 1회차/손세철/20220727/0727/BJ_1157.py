# Mississipi
# M=1, i=4, s=4, p=1

# ord() # 문자 => 숫자
# chr() # 숫자 => 문자

word = input().upper()

check = [0] * 26

for i in word:
    check[ord(i) - 65] += 1

mx = max(check)
cnt = check.count(mx)
if cnt > 1:
    print("?")
else:
    print(chr(check.index(mx) + 65))



########################################
word = input().upper()

alphabet = [0] * 26

for i in word:
    alphabet[ord(i) - 65] += 1

if alphabet.count(max(alphabet)) >1 :
    print("?")

else:
    print(chr(alphabet.index(max)+65))

