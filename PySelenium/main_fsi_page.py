from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# https://stackoverflow.com/questions/37883759/errorssl-client-socket-openssl-cc1158-handshake-failed-with-chromedriver-chr
# [20624:19784:0229/153538.135:ERROR:ssl_client_socket_impl.cc(970)] handshake failed; returned -1, SSL error code 1, net_error -101 ^^^

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
actions = ActionChains(driver)

# Home Page
driver.get("https://flightsafety.com")

bc = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[1]/a")
sp = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[3]/a")
abt = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[4]/a")

# Get left and right UL of dropdown
left = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[1]/ul/li/div/div/div/div[1]/ul")
right = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[1]/ul/li/div/div/div/div[2]/ul")

# Get all <a href>'s under the left and right <ul> inside of Business and Commercial dropdown. 
b = left.find_elements(By.TAG_NAME, "a") # left side of business and commercial dropdown
b2 = right.find_elements(By.TAG_NAME, "a") # right side of business and commercial dropdown
b.extend([x for x in b2])

for i in range(0,len(b)):
    actions.move_to_element(bc)
    actions.click(bc)
    actions.perform()
    b[i].click()
    driver.back()

# Government & Military
defense = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[2]/a")
defense.click()
driver.back()

# Simulation Products
sim_products = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[3]/ul/li/div")
s = sim_products.find_elements(By.TAG_NAME, "a")
# print(len(s))

# Go through all items in Simulation Products drop down
for i in range(0,len(s)):
    actions.move_to_element(sp)
    actions.click(sp)
    actions.perform()
    s[i].click()
    driver.back()

# About Dropdown
about = driver.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[4]/ul/li/div")
a = about.find_elements(By.TAG_NAME, "a")
# print(len(a))

# Go through all items in About drop down
for i in range(0,len(a)):
    actions.move_to_element(abt)
    actions.click(abt)
    actions.perform()
    a[i].click()
    driver.back()

# myFlightSafety
myfsi = driver.find_element(By.XPATH, "/html/body/header/section/nav/ul/li[1]/a[2]")
myfsi.click()

# Enter in login information
username = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input28"]')))
username.send_keys("")
next = driver.find_element(By.XPATH, '//*[@id="form20"]/div[2]/input')
next.click()
username = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input62"]')))
username.send_keys("")
verify = driver.find_element(By.XPATH, '//*[@id="form54"]/div[2]/input')
verify.click()

time.sleep(4)
