from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def go_through_models(driver):
    models = driver.find_elements(By.TAG_NAME, "a")
    c = 0
    for i in models:
        if c == 26:
            break
        try:
            i.click()
            time.sleep(1)
        except:
            models = driver.find_elements(By.TAG_NAME, "a")
            models[c].click()
            time.sleep(1)
        driver.back()
        c+=1

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
actions = ActionChains(driver)

# Home Page
driver.get("https://flightsafety.com")

# Move to Business & Commercial
x = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[1]/a")
actions.move_to_element(x)
actions.click(x)
actions.perform()

business_and_commercial = driver.find_element(By.CLASS_NAME, "move-right")
p = business_and_commercial.find_elements(By.TAG_NAME, "a")

for i in p:
    i.click()
    driver.back()
    p = business_and_commercial.find_elements(By.TAG_NAME, "a")



time.sleep(4)
