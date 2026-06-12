from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.ikosmo.co.kr/main'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a').click()
time.sleep(2)

driver.find_element(By.NAME, 'id').send_keys('sepiablur')
time.sleep(2)

driver.find_element(By.NAME, 'password').send_keys('**********')
time.sleep(15)

driver.find_element(By.XPATH, '//*[@id="subConts"]/div/div/div/div/section/section/form/fieldset/div[2]/ul/li/a').click()
time.sleep(40)

driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div/div[1]/div/a/span').click()
time.sleep(40)