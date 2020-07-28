#Delete all archived messages from Messenger.com
#Date: 28/07/2020
#Developer: Alexandru Chiser
#Revision: 2

import time
import pynput

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from pynput.keyboard import Key, Controller

#xpaths for different interactable elements
XPATH_EMAIL = '//*[@id="email"]'
XPATH_PASSWORD = '//*[@id="pass"]'
XPATH_SIGNIN = '//*[@id="loginbutton"]'
XPATH_SETTINGS = '//*[@id="settings"]'
XPATH_3DOTS = '//*[@id="dots-3-horizontal"]'
XPATH_DELETE = '//span[text()="Delete"]'

#credentials of your Facebook account
email = "insert email or phone number"
password = "insert password"

#types a string in a desired text box
def type_credentials (xpath_elem, credentials):
    text_box = browser.find_element_by_xpath(xpath_elem)
    text_box.click()
    text_box.send_keys(credentials)

#clicks on object X
def click_obj (xpath_elem):
    obj = browser.find_element_by_xpath(xpath_elem)
    obj.click()
    
if __name__ == '__main__':           
    browser = webdriver.Chrome(r"insert path to chromedriver.exe")
    url = "http://messenger.com"
    browser.get(url)
    time.sleep(2)

    type_credentials(XPATH_EMAIL, email)
    type_credentials(XPATH_PASSWORD, password)

    click_obj(XPATH_SIGNIN)
    time.sleep(2)

    url = "https://www.messenger.com/archived/t/"
    browser.get(url)
    time.sleep(4)

    #i is the number of deleted messages
    i = 0

    while(1):
        try:   
            click_obj(XPATH_3DOTS)
            time.sleep(2)
        except ElementClickInterceptedException:
            break                     
        
        click_obj(XPATH_DELETE)
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

