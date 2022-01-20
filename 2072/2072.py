"""
입력
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   

출력
#1 200
#2 208
#3 121
"""
T = int(input()) #몇 개의 케이스인지 입력받고
for i in range(1, T + 1): #각 케이스 별로
    input_list = input() #10개의 수를 입력받아서
    sum_list = list(input_list.split(' ')) #리스트에 넣습니다
    listsum = 0 #결과값 초기화
    for j in sum_list: #리스트 목록 하나하나
        if int(j) % 2 == 1: #정수형으로 바꾸고 홀수인지 확인해봅니다
            listsum += int(j) #맞으면 더함
    print(f'#{i} {listsum}') #결과 한 줄씩 출력