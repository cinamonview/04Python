




# 모듈 임포트
import time
from datetime import date, datetime,timedelta

# 오늘 날짜와 년, 월, 일 출력
today = date.today()
print('오늘날짜', today, today.year, today.month, today.day)

print(f"{'구분선':-^50}")

# 현재 시각을 알아보는 함수 datetime 현재시각 년월일 시분초마이크로세컨즈
dtime = datetime.now()
print('현재시각', dtime)
print('년/월/일', dtime.year,dtime.month,dtime.day)
print('시/분/초/밀리세컨즈', dtime.hour,dtime.minute,dtime.second,dtime.microsecond)

print(f"{'구분선':-^50}")

# 날짜계산 1
# 하루를 얻어와서 변수에 저장 => 1 day, 0:00:00 형식으로 반환
one_day = timedelta(days=1)
# 오늘 날짜에서 하루를 더하거나 빼서 날짜를 계산할 수 있다.
yesterday = today - one_day
tommorow = today + one_day
print("어제와 오늘", yesterday, tommorow)

# 날짜계산 2
# 오늘에서 어제를 빼면 '하루' 의 결과가 나옴.
date_diff = today - yesterday
print("날짜차이", date_diff)   #결과 : 1 day, 0:00:00

# 날짜형식
# 날짜 형식 지정
date_str = today.strftime('%Y-%m-%d')
print("형식지정", date_str)

# 크리스마스까지 남은 날짜 계싼
# 날짜계산3
x_mas_str = f'{today.year}-12-25'
# str -> datetime 타입으로 형식 변환
x_mas_datetime = datetime.strptime(x_mas_str, '%Y-%m-%d')
# datetime -> date 타입으로 형식변환
x_mas_date = datetime.date(x_mas_datetime)
# 각 변수의 값과 타입 확인
print(x_mas_str,x_mas_datetime,x_mas_date)
print(type(x_mas_str),type(x_mas_datetime),type(x_mas_date))
# 크리스마스에서 오늘을 빼면 남은 날짜를 계산할 수 있다.
date_diff = x_mas_date - today

print("크리스마스까지 1", date_diff)
print("크리스마스까지 2", date_diff.days)
