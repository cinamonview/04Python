#산술연산자

x=2
y=4
z=8

print("x + y",x+y)
print("x - y",x-y)
print("x * y",x*y)
#나누기 연산. 결과는 실수(float)형으로 반환.
print("x / y",x/y)
# 몫을 구하기 위한 나누기 연산. 결과는 정수(int)형으로 반환. 몫만 나오기 때문에 정수가 된다.나머지는 무시
print("x // y",x//y)
# 거듭제곱을 연산해주는 연산자. x의 y승(제곱)의 결과를 반환.
print("x ** y",x**y)
# 파이썬에서 제공하는 기본함수로 거듭제곱의 결과 반환.
print("pow(x , y)",pow(x,y))
# x의 y승의 결과를 z로 나눈 나머지가 반환됨.
print("pow(x , y , z)",pow(x,y,z))
# x를 y로 나눈 몫과 나머지를 Tuple(튜플)로 반환.
print("divmod(x , y)",divmod(x,y))

# 블럭단위 주석 ''' ''' or """ """

''' 수학관련된 여러가지 함수를 가지고 있는 math모듈을 
현재 문서에 import한 후 에 팩토리얼 함수를 실행한다.'''
import math
print(" math,factorial(5)",math.factorial(5))
