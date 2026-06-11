
# 셀레니움 으로부터 크롬을 띄우기 위해서 웹 드라이버라는 친구를 데리고 온다.
# 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
# 크롬 로드 . 이때 웹브라우저가 실행된다.
driver = webdriver.Chrome()


'''
셀레니움은 크롬 브라우저를 이용해서 크롤링할 페이지를 띄운 후
데이터를 얻어온다. 이때 비동기 통신을 통해 데이터를 로드하는 
경우 조금 늦게 로딩되는 경우가 있으므로 셀레니움에서는 '암묵적대기'
가 필요한 경우가 있다.
이런 경우 5초까지는 대기하겠다는 선언이다.
'''

driver.implicitly_wait(5)

'''
time 모듈을 사용하는 경우에는 로딩과 상관없이 무조건 5초를 대기한다.
따라서 반드시 필요한 경우에만 사용하는 것이 좋다.
'''

# import time
# time.sleep(5)


#  멜론챠트 페이지 크롤링을 위한 URL 설정
url = 'https://www.melon.com/chart/index.htm'
# 셀레니움을 통해 페이지의 데이터(HTML 원본소스)를 얻어온다.
driver.get(url)
html = driver.page_source

# 뷰티플숲을 임포트 한 후 얻어온 데이터를 Soup객체로 변환
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보(순위, 곡 등)를 저장할 리스트 생성
song_data = []
rank = 1

# 셀렉터를 이용해서 반복되는 엘리먼츠 <tr>을 얻어온다.
songs = soup.select('tbody > tr')
# 갯수만큼 반복
for song in songs:
    #노래제목
    title = song.select('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')[0].text
    # 가수
    singer = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')[0].text
    # 좋아요 갯수
    favo = song.select('td:nth-child(8) > div > button > span.cnt')[0].text
    # 파싱한 내용을 콘솔에 출력해서 확인
    print(title,singer,favo,sep="|")
    #리스트에 데이터를 추가
    song_data.append(['Melon', rank,title,singer,favo])
    rank += 1
    
# 판다스 모듈 임포트
import pandas as pd
# 컬럼명 추가를 위해 리스트 생성
columns = ['서비스', '순위','타이틀','가수','좋아요']
# 데이터 프레임으로 변환시 앞에서 작성한 컬럼을 사용.
pd_data = pd.DataFrame(song_data, columns=columns)
#데이터 프레임의 상위 5개 행을 출력해서 확인
print(pd_data.head())
# 엑셀로 저장
pd_data.to_excel('./saveFiles/melon_chart.xlsx', index=False)   