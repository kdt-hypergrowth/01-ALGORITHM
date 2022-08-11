#  숭실대학교의 참여도, 고려대학교의 참여도, 한양대학교의 참여도를 의미하는 
#  세 자연수 S, K, H가 공백으로 구분되어 주어진다
S, K, H = map(int,input().split())

if S + K + H >= 100  : 
    print('OK')

elif S + K + H < 100 :
    if min(S,K,H) == S : 
        print('Soongsil')
    if min(S,K,H) == K : 
        print('Korea')
    if min(S,K,H) == H : 
        print('Hanyang')