import time

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
driver.implicitly_wait(15)
# enter email
driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys("ndevaraj@msystechnologies.com")
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# loging in with keka password
driver.find_element(By.XPATH, "//div/form/button[2]").click()

# Entering the password and loging in
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Nandu@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# click on the org section
driver.find_element(By.XPATH, "//span[@class='ic-org sidebar-list-icon']").click()

# page title
# print(driver.find_element(By.XPATH, "//employee-org-directory/div/h1").text)

# dropdown of department section
driver.find_element(By.XPATH, "//xhr-async-data-filters/div/div/div[1]").click()
driver.find_element(By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li div input").click()
driver.find_element(By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li div input").send_keys("RMG")
driver.find_element(By.XPATH, "//span[@class='text-truncate-1 font-weight-bold']").click()

# clearing the text in Search input
driver.find_element(By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li div input").click()
driver.find_element(By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li div input").clear()

# Entering the new value in the search input and selecting the value in the dropdown
driver.find_element(By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li div input").click()
driver.find_element(By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li div input").send_keys("Amazon")
driver.find_element(By.XPATH, "//span[@class='text-truncate-1 font-weight-bold']").click()
driver.find_element(By.XPATH, "//xhr-async-data-filters/div/div/div[1]").click()

# Entering the value in the Search input
driver.find_element(By.XPATH, "//xhr-async-data-filters/div/div/div[3]").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search'][name='filter']").send_keys("vishnu")

# printing the value got form the search in pycharm
Name = driver.find_element(By.CSS_SELECTOR, "div h4[title='Vishnu Priya S']")
Department = driver.find_element(By.CSS_SELECTOR, "span:nth-child(1)")

print(f"You Searched for this person {Name.text} from this Department {Department.text}")


