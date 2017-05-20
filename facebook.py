# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from gmailsend import mailerror, mailsend


url = "http://www.facebook.com"
birthday = '/events/birthdays'
day = 24 * 60 * 60 # in seconds
wish = "Happy Birthday"

def Login(driver, username, password):
    driver.get(url)
    
    assert "Facebook" in driver.title
    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys(username)
    elem = driver.find_element_by_name("pass")
    elem.clear()
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

def WishHappyBirthday(driver):
    assert "Events" in driver.title
    birthdays = driver.find_elements_by_class_name("mentionsTextarea")
    for elem in birthdays:
        elem.clear()
        elem.send_keys(wish)
        elem.send_keys(Keys.RETURN)
    return len(birthdays)

def loginAndPost(username, password):
    driver = webdriver.Firefox(executable_path='/Users/terrencedrumm/Desktop/FacebookBirthday/geckodriver') # Path to your geckodriver
    # driver = webdriver.PhantomJS()
    # driver.set_window_size(1080, 720)
    try:
        Login(driver, username, password)
        assert "Page Not found" not in driver.page_source
        time.sleep(10)
        driver.get(url + birthday)
        time.sleep(10)
        c = str(WishHappyBirthday(driver))
        time.sleep(30)
        mailsend(username, c)
    except Exception as e:
        print(str(repr(e)))
        mailerror(username, e)
    finally:
        driver.quit()
