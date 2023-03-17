from selenium import webdriver
import time
import pytest
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:\Program Files\pycharm\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
