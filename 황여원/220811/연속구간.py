# 정수 세개를 입력받는다 
for _ in range(3):
    num = int(input())
    # 연속해서 나오는 구간 중 가장 긴 것의 길이를 저장할 변수 
    # 연속하여 같은 숫자가 나오는 것이 없으므로 1을 출력하므로 1로 초기화 
    max_num = 1 

    #현재 연속중인 숫자를 저장하는 변수 선언
    cur_num = num[0] 

    #현재 연속중인 숫자를 저장하는 변수 선언
    cur_num_cnt = 1 

    # 여덟 자리 정수 
    for i in range(1,8) :
        # 현재 숫자와 뒤의 숫자가 같다면 
        if num[i] == num[i-1] :
            # 현재 연속중인 숫자의 구간 길이에 + 1 
            cur_num_cnt += 1

            # 현재 연속중인 숫자의 연속구간 길이의 값이 이전까지 가장 긴 구간 값보다 크다면 
            if cur_num_cnt > max_num : 
                max_num = cur_num_cnt
            # 현재숫자와 뒤의 숫자 다르면 
            else : 
                # 현재 연속중인 숫자 변수에 현재 숫자를 넣어주고 
                cur_num = num[i]
                # 구간의 길이를 1 로 초기화 
                cur_num_cnt = 1 
    print(max_num)