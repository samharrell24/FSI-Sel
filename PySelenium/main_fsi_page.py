from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

# Home Page
driver.get("https://flightsafety.com")
# career_top_menu = driver.find_element(By.CLASS_NAME, "header__secondary-nav")
# career_top_menu.click()

career_top_menu = driver.find_element(By.CLASS_NAME, "left")
# print(career_top_menu)
# print(len(career_top_menu))
p = career_top_menu.find_elements(By.TAG_NAME, "a")

p = career_top_menu.find_element(By.XPATH, "/html/body/header/div/nav/section/ul/li[1]/ul/li/div/div/div")
print(p)
pp = p.find_elements(By.XPATH, "/html/body/header/div/nav/section/ul/li[1]/ul/li/div/div/div/div[1]/ul")
print(pp)
# TODO: [6492:17032:0223/154347.010:ERROR:ssl_client_socket_impl.cc(974)] handshake failed; returned -1, SSL error code 1, net_error -101
# TODO: Fix ^^ from going to output in terminal by accepting cookies

# elem = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div/ul')
#     for each_ul in elem:
#         all_li = each_ul.find_elements_by_tag_name("li")
#         for li in all_li:
#             list_text.append(li.text)

for i in pp:
    print(i)
    # i.click()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)
    # p = career_top_menu.find_elements(By.TAG_NAME, "a")

# career_top_menu.click()

time.sleep(4)
# continue_button = driver.find_element(By.NAME, "submit")
# continue_button.click()