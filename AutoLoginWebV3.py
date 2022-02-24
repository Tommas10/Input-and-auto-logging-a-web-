# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:38:19 2022

#To put input into a web page say for example auto-login to a website so the python program would open the web page and input the user and password automatically into the web page and press the login button automatically.
#Under Windows 10.
@author: tommas.huang
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = r'C:\Users\user\Desktop\PythonAutoLogin\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://tw.msn.com/')

username = driver.find_element_by_id("txtAccount")
password = driver.find_element_by_id("txtPwd")

username.send_keys("account")
password.send_keys("password")

driver.find_element_by_name("btnSubmit").click()