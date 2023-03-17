from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Program Files/pycharm/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://app.keka.com/")
driver.maximize_window()
