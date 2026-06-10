'''
정보은닉 : 
    멤버변수의 외부 접근을 차단하고 클래스 내부에서만 
    접근하도록 설정하는 것을 말한다.
    파이썬 에서는 private와 같은 접근 지정자 대신 , 더블언더바( __ )를
    사용한다.
'''



class Computer:
    
    def __init__(self, name, passwd):
        # 외부 접근이 허용되는 멤버변수 (public)
        self.name = name
        # 외부 접근이 차단된 멤버변수(private)
        self.__password = passwd
    
    # 멤버함수 정의    
    def hitKeyboard(self):
        return f'{self.name}로 키보드 작업을 합니다.'
    def clickMouse(self):
        return (f'{self.name}에서 마우스로 클릭합니다.')
    # 정보 은닉된 멤버변수의 접근을 위해 getter/setter 정의
    def getPasswd(self):
        return self.__password
    def setPasswd(self,passwd):
        self.__passwd = passwd


# 인스턴스 생성    
myCom = Computer('LG Gram', 'qwer1234')
# 멤버함수 호출
print(myCom.hitKeyboard())
myCom.clickMouse()

# 외부 접근이 허용되므로 정상출력됨
print("컴퓨터 이름", myCom.name)

# private로 선언했으므로 접근할수 없어서 에러가 발생된다.
# AttributeError 발생됨.
# print("패스워드",myCom,__passwd)

# 접근이 되지 않으므로 getter를 통해 접근 후 출력해야 한다.
print("패스워드", myCom.getPasswd())


myCom.setPasswd('abcd9876')
print('패스워드 변경후 1',myCom.getPasswd())


'''
맹글링 규칙에 의해 정보은닉된 멤버변수는
내부적으로 이름이 변경된다.
따라서 아래와 같이 작성하면 값이 변경되지 않는다. 
또한 에러도 발생하지 않는다.'''

myCom.__passwd = "xxxxXXXX"
print('패스워드 변경후 2', myCom.getPasswd())

'''
정보은닉된 멤버변수는 아래와 같이 클래스명을 포함한 형태로
이름이 변경된다. 하지만 권장사항은 아니므로
사용하지 않는것이 좋다.'''

# 권장되지 않음
print("맹글링 규칙", myCom._Computer__passwd)