# This is a sample_html Python script.

import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://classpass.com/login")
# driver.quit()
# driver = webdriver.Chrome('/home/brianmina17/Downloads/chrome_drivers/chrome-linux64')  # Optional argument, if not specified will search path.

# driver.get('http://www.google.com/');

# time.sleep(5) # Let the user actually see something!

email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')

email.send_keys("brian.mina17@gmail.com")
password.send_keys("")

submit = driver.find_element(By.XPATH, '//button[span[contains(text(),"Log in")]]')
submit.click()
time.sleep(5) # Let the user actually see something!

driver.get("https://classpass.com/studios/yoga-home-pompano-beach-wwpg")


def find_dan_class():
    for _ in range(8):
        try:
            found_class = driver.find_element(By.XPATH,
                                # '//section[div[contains(text(), "Dan")]]/div[button]/button/span[@data-component="ReserveCta"][contains(text(), "2")]')
                                '//section[div[contains(text(), "Corbin")]]/div[button]/button/span[@data-component="ReserveCta"][contains(text(), "3")]')
            return found_class
        # TODO: 1 credit class
        except NoSuchElementException as e:
            next_day_button = driver.find_element(By.XPATH, '//button[span[contains(text(), "See next day")]]')
            next_day_button.click()
    return None

class_found = find_dan_class()

# search_box.send_keys('ChromeDriver')

# search_box.submit()


driver.quit()

# TODO: add waits
# TODO: email notification with time and date
# TODO: automatic booking ?

