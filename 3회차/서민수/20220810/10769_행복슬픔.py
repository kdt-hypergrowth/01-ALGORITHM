# 승엽이는 자신의 감정을 표현하기 위해서 
# 종종 문자 메시지에 이모티콘을 넣어 보내곤 한다. 
# 승엽이가 보내는 이모티콘은 세 개의 문자가 붙어있는 구조로 이루어져 있으며, 
# 행복한 얼굴을 나타내는 :-) 와 슬픈 얼굴을 나타내는 :-( 가 있다.

# 혜성이는 승엽이의 이모티콘을 귀여운 척이라고 생각해 매우 싫어하므로, 
# 승엽이의 문자가 오면 전체적인 분위기만 판단해서 알려주는 프로그램을 작성하고 싶다.

a = input()
smile = a.count(":-)")
sad = a.count(":-(")
# print(smile,sad)

if smile == 0 and sad == 0:
    print('none')
    # print(smile,sad)
elif smile > sad:
    print('happy')
elif smile < sad:
    print("sad")
elif smile == sad:
    print("unsure")