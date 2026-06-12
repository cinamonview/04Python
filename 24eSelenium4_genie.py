# 판다스 셀레니움 뷰티불숲 임폴트

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 크롬 웹드라이버 로드 및 페이지 접속
driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

# 데이터 저장을 위한 리스트 생성
song_data = []
rank = 1

# 1~4페이지까지 반복하는 for문
for page in range(1,5):
    # 페이지 정보 출력 및 2초간 묵시적 대기
    print("페이지", page)
    driver.implicitly_wait(5)
    
    # 파싱을 위해 페이지 소스를 얻어온 후 Soup 객체로 변환
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    # tbody>tr 태그를 이용해서 
    # 각 페이지의 챠트 테이블의 <tr>부분을 선택한 후 반복
    songs = soup.select('tbody>tr')
    
    # //*[@id="body-content"]/div[6]/div/table/tbody/tr[1]/td[5]/a[1]     1위곡 제목 xpath딴것
    
    for song in songs:
        
        '''
        copy>selector로 땄음
        
        #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
        '''
        #노래제목
        title = song.select('a.title')[0].text.strip()
        # 가수
        singer = song.select('a.artist')[0].text
        # 파싱한 정보를 리스트에 추가
        song_data.append(['Genie', rank, title, singer])
        rank += 1
        
    '''
    페이지 하단의 다음페이지로 가기위한 버튼을 클릭한다.
    각 버튼의 XPath의 패턴은 a[1]~[4]와 같이 되어있다.
    '''
        
    if page < 4:
        driver.find_element(By.XPATH,f'//*[@id="body-content"]/div[7]/a[{page+1}]').click()
    # 다음페이지로 이동하면 5초간 묵시적 대기    
    
    
    driver.implicitly_wait(5)
    
    # 리스트를 데이터프레임으로 변환 및 컬럼 추가
    columns = ['서비스', '순위','타이틀','가수']
    pd_data = pd.DataFrame(song_data, columns=columns)
    # 데이터 프레임의 최상위 5개 데이터 확인
    print(pd_data.head())
    # 엑셀저장
    pd_data.to_excel('./saveFiles/genie_chart.xlsx',index=False)