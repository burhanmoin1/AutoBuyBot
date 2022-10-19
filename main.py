from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


df = pd.io.parsers.read_csv('script - Sheet1.csv', dtype={'Zipcode': 'str'})

url = 'https://www.mediaworld.it/it/myaccount/auth/login?redirectURL=%2Fcheckout%2Flogin'


driver = webdriver.Chrome('D:\pythonProject2\chromedriver')
driver.implicitly_wait(10)

driver.get(url)

wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pwa-consent-layer-accept-all-button"]')))
driver.find_element("xpath", '//*[@id="pwa-consent-layer-accept-all-button"]').click()
driver.find_element("id", 'email').send_keys(df['Username'][0])
driver.find_element("id", "password").send_keys(df['Password'][0])
driver.find_element("id", "mms-login-form__login-button").click()

print("logged in successfully")
sleep(1)

driver.get('https://www.mediaworld.it/it/product/_sony-ps5-cuffie-pul3d-midbla-cuffie-gaming-163436.html')
driver.find_element('xpath', '//*[@id="pdp-add-to-cart-button"]').click()
driver.find_element('xpath', '//*[@id="main-content"]/div[5]/div[2]/div[3]/div[2]/button').click()
driver.find_element('xpath', '//*[@id="main-content"]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div/div/div[1]').click()
driver.find_element('xpath', '//*[@id="mms-styled-modal-desktop-wrapper"]/div/div/div/div/div[2]/div/div[1]/input').send_keys(df['Zipcode'][0])
driver.find_element('xpath', '//*[@id="mms-styled-modal-desktop-wrapper"]/div/div/div/div/div[2]/div/div[2]/button').click()
driver.find_element('xpath', '//*[@id="mms-styled-modal-desktop-wrapper"]/div/div/div/div[2]/div[2]/button').click()

driver.find_element('xpath', '//*[@id="continueButtonWrapper"]/div/button').click()
driver.find_element('xpath', '//*[@id="continueButtonWrapper"]/div/button').click()
driver.find_element('xpath', '//*[@id="main-content"]/div[2]/div[1]/div/div[2]/form/div/div[11]/div/button').click()
