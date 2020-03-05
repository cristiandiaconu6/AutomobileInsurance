from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:/Users/cristian.diaconu/PycharmProjects/AutomobileInsurance/Drivers/chromedriver.exe")
driver.get("http://sampleapp.tricentis.com/101")
driver.implicitly_wait(10)
driver.maximize_window()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "nav_automobile"))).click()
WebDriverWait.until()

