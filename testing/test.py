from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import random

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.quit()
driver.maximize_window()
time.sleep(5)


username = driver.find_element(By.XPATH, "//input[@name = 'username']")
username.send_keys("Admin")

password = driver.find_element(By.XPATH, "//input[@name = 'password']")
# password.click()
password.send_keys("admin123")

loginBtn = driver.find_element(By.XPATH, "//button[text() = ' Login ']")
loginBtn.click()
time.sleep(3)

recruitment = driver.find_element(By.XPATH, "//span[text() = 'Recruitment']")
recruitment.click()

time.sleep(5)
dropDown = driver.find_elements(By.XPATH, "//div[text() = '-- Select --']")

for field in dropDown:
    field.click()
    options = driver.find_elements(By.XPATH, "//div[@role = 'option']")
    # random.choice(options).click()    //Can also select 0th index  which contains 'Select'
    count= random.randint(1,len(options)-1)
    
    options[count].click()


candidate_name = driver.find_element(By.XPATH,"//input[@placeholder = 'Type for hints...']")
candidate_name.send_keys("John  Doe")


date_of_application_from = driver.find_element(By.XPATH,"//input[@placeholder = 'From']")
date_of_application_from.send_keys("2024-08-14")

date_of_application_to = driver.find_element(By.XPATH,"//input[@placeholder = 'To']")
date_of_application_to.send_keys("2024-08-20")

search_button = driver.find_element(By.XPATH,"//button[text() = ' Search ']")
search_button.click()



# select = driver.find_element(By.XPATH, "//*[text() = 'Account Assistant']")
# select.click()


time.sleep(5)
