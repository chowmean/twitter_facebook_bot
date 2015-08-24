from selenium import webdriver
import os
import requests
import pickle
import json
import time
import traceback
from selenium import webdriver
from bs4 import BeautifulSoup as BS4
from selenium.webdriver.common.keys import Keys

import config

def login():
    br.get('https://twitter.com')
    if os.path.exists('cookies.pkl'):
        form = br.find_element_by_class_name('signin')
        email_input = br.find_element_by_id('signin-email')
        pass_input = br.find_element_by_id('signin-password')
        email_input.send_keys("YOURUSERNAME")
	pass_input.send_keys("YOURPASWORD")
        pass_input.send_keys(Keys.RETURN)
        br.implicitly_wait(10)
        form.submit()
        br.implicitly_wait(10)
	print "Submiting form"	
        pickle.dump( br.get_cookies() , open("cookies.pkl","wb"))
	print "cookies exist"
    else:
        try:
	   print "cokkies doest not exist.trying logging in"
	   form = br.find_element_by_class_name('signin')		#name of login form ambigious	
           email_input = br.find_element_by_id('signin-email')
           pass_input = br.find_element_by_id('signin-password')
	   email_input.send_keys("YOURUSERNAME")
	   pass_input.send_keys("YOURPASWORD")	
	   pass_input.send_keys(Keys.RETURN)
           form.submit()
	   driver.implicitly_wait(10)
	   print "Submiting form"	
           pickle.dump( br.get_cookies() , open("cookies.pkl","wb"))
	   if os.path.exists('cookies.pkl'):
		print "logged in" 
        except Exception as e:
            print traceback.format_exc(e)
            
br = webdriver.Firefox()
login()

br.get("https://www.twitter.com")
r=br.find_elements_by_class_name("js-actionRetweet")
r[10].click()
r=br.find_element_by_class_name("retweet-action")
r.click()



