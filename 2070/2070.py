"""
입력
3
3 8 
7 7 
369 123

출력
#1 <
#2 =
#3 >
"""
T = int(input())
for i in range(1, T + 1):
    input_number = list(input().split(' '))
    output_equal = ''
    if int(input_number[0]) > int(input_number[1]):
        output_equal = '>'
    elif int(input_number[0]) < int(input_number[1]):
        output_equal = '<'
    else:
        output_equal = '='
    print(f'#{i} {output_equal}')