ID = str(input("아이디를 입력하세요 : "))

user_info = ['sung','kim','hong','park','lee']


'''
선생님 정답

퀴즈2] 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 패스워드를 입력받아 일치하는지 확인하는 프로그램을 작성하시오. 여기서 패스워드는 1234로 가정합니다. 
'''
'''
정답]
user_info = ['sung', 'kim', 'hong', 'park', 'lee']
match_flag = False
my_id = input('아이디를 입력하세요:')

if my_id in user_info:
    match_flag = True
    my_pass = input('패스워드를 입력하세요:')
    if my_pass == '1234':
        print('아이디와 패스워드 일치')
    else:
        print('패스워드 틀림')
            
if match_flag == False:
    print('일치하는 아이디가 없습니다.')




'''