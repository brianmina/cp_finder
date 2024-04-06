# This is a sample_html Python script.

import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

notification_gmail = "brian.mina17@gmail.com"
notification_gmail_password = ""

import smtplib, ssl
from email.message import EmailMessage

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = notification_gmail # Enter your address
receiver_email = notification_gmail  # Enter receiver address



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


def find_dan_class() -> str | None:
    for _ in range(8):
        try:
            found_class = driver.find_element(By.XPATH,
                                # '//section[div[contains(text(), "Dan")]]/div[button]/button/span[@data-component="ReserveCta"][contains(text(), "2")]')
                                '//section[div[contains(text(), "Corbin")] and div[button]/button/span[@data-component="ReserveCta"][contains(text(), "3")]]/div[@data-qa="ScheduleRow.date"]/time/span')
            return found_class.text
        # TODO: 1 credit class
        except NoSuchElementException as e:
            next_day_button = driver.find_element(By.XPATH, '//button[span[contains(text(), "See next day")]]')
            next_day_button.click()
    return None

class_time = find_dan_class()


def get_date(driver: WebDriver) -> str:
    found_date = driver.find_element(By.XPATH, "//div[@data-qa='DateBar.date']")
    return found_date.text


def send_class_info_email(class_time: str, class_date: str):
    msg = EmailMessage()
    msg.set_content(f"I found a class at {class_time} on {class_date}")
    msg['Subject'] = f"I found a class at {class_time} on {class_date}"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, notification_gmail_password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)



if class_time:
    class_date = get_date(driver)
    send_class_info_email(class_time, class_date)
else:
    print("Not found.")
# search_box.send_keys('ChromeDriver')

# search_box.submit()


driver.quit()

# TODO: add waits
# TODO: email notification with time and date
# TODO: automatic booking ?

