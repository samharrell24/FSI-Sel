from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

# Home Page
driver.get("https://bagtag.flightsafety.com/Baggage")
consent_box = driver.find_element(By.NAME, "Consent")
consent_box.click()
continue_button = driver.find_element(By.NAME, "submit")
continue_button.click()

# Your Information Page
name = wait.until(EC.element_to_be_clickable((By.NAME, 'name')))
name.send_keys("Sam H")
job_title = driver.find_element(By.NAME, "position")
job_title.send_keys("Engineer")
company = driver.find_element(By.NAME, "company")
company.send_keys("Flight Safety")
aircraft = driver.find_element(By.NAME, "aircraft")
aircraft.send_keys("G550")
phone_number = driver.find_element(By.NAME, "phone")
phone_number.send_keys("123-345-6789")
time.sleep(8)
center_location = Select(driver.find_element(By.NAME, "CENTER"))
# center_location.select_by_value('1168')
center_location.select_by_visible_text('Columbus')

time.sleep(4)
submit_button = driver.find_element(By.NAME, "submit")
submit_button.click()

# Choose Manufacturer Page
gulfstream = driver.find_element(By.LINK_TEXT, "Gulfstream")
gulfstream.click()
time.sleep(4)

# Choose image for BagTag
g550 = driver.find_element(By.CSS_SELECTOR, "body > p > table > tbody > tr > td > ul > b > b > b > b > b > b > li > a > b")
g550.click()
first_g550_img = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img')))
first_g550_img.click()
time.sleep(6)

driver.close()
