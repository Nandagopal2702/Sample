from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Program Files\pycharm\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

driver.find_element(By.NAME, "enter-name").send_keys("Nandu")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
