phone = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

str_ = input()
sum_ = 0

for i in range(len(str_)):
    for j in range(len(phone)):
        if str_[i] in phone[j]:
            sum_ += phone.index(phone[j]) + 3

print(sum_)