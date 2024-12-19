
from selenium import webdriver
import  time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive = "C:\\chrome driver\\chromedriver.exe"
service = Service(chrome_drive)

driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/events/")

python_event = driver.find_elements(By.CSS_SELECTOR, '.list-recent-events time')
event_name = driver.find_elements(By.CSS_SELECTOR, '.list-recent-events li a')

events = {name.text:time.text for name, time in zip(event_name, python_event)}
print(events)


driver.quit()