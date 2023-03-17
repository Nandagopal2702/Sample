from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests():

    def test_validLogin(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        emailField.send_keys("test@gmail.com")

        passwordField = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        passwordField.send_keys("123456789")

        loginButton = driver.find_element(By.CSS_SELECTOR, "input[name='commit']")
        loginButton.click()