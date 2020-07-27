#Delete all archived messages from Messenger.com
#Date: 26/07/2020
#Developer: Alexandru Chiser
#Revision: 1

import time
import pynput

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from pynput.keyboard import Key, Controller

#xpaths for different interactable elements
xpath_email = '//*[@id="email"]'
xpath_password = '//*[@id="pass"]'
xpath_signin = '//*[@id="loginbutton"]'
xpath_settings = '//*[@id="settings"]'
xpath_3dots = '//*[@id="dots-3-horizontal"]'
xpath_delete = '//span[text()="Delete"]'

#credentials of your Facebook account
email = "insert email"
password = "insert password"

#types Y string in the X text box
def type_credentials (x, y):
    text_box = browser.find_element_by_xpath(x)
    text_box.click()
    text_box.send_keys(y)

#clicks on object X
def click_obj (x):
    obj = browser.find_element_by_xpath(x)
    obj.click()     
           
browser = webdriver.Chrome(r"insert path to chromedriver.exe")
url = "http://messenger.com"
browser.get(url)
time.sleep(2)

type_credentials(xpath_email, email)
type_credentials(xpath_password, password)

click_obj(xpath_signin)
time.sleep(2)

url = "https://www.messenger.com/archived/t/"
browser.get(url)
time.sleep(4)

#i is the number of deleted messages
i = 0

while(1):
    try:   
        click_obj(xpath_3dots)
        time.sleep(2)
    except ElementClickInterceptedException:
        break                     
    
    click_obj(xpath_delete)
    time.sleep(2)

    keyboard = Controller()

    #simulate TAB key press to switch to "Delete" button
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(2)

    #simulate ENTER key press to delete the message
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    i += 1

print("{}".format(i) + " messages deleted")

browser.quit()

