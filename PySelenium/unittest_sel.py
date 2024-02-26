import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

class TestBagTagApplication(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_bag_tag_application(self):
        driver = self.driver
        wait = self.wait

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

        center_location = Select(driver.find_element(By.NAME, "CENTER"))
        center_location.select_by_visible_text('Columbus')

        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()

        # Choose Manufacturer Page
        gulfstream = driver.find_element(By.LINK_TEXT, "Gulfstream")
        gulfstream.click()

        # Choose image for BagTag
        g550 = driver.find_element(By.CSS_SELECTOR, "body > p > table > tbody > tr > td > ul > b > b > b > b > b > b > li > a > b")
        g550.click()
        first_g550_img = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a/img')))
        first_g550_img.click()

if __name__ == "__main__":
    unittest.main()
