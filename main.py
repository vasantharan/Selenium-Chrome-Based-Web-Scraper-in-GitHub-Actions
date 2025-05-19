from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://github.com/vasantharan')
time.sleep(4)

headers = driver.find_elements(By.TAG_NAME, "h3")

for h in headers:
    print("Header Text Content:", h.text)

driver.quit()