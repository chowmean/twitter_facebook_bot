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
#import mysql.connector
#from mysql.connector import Error
#from connection import conn
#import config
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.common.proxy import *
namelist=['nameofuser']
usernamelist=['username']
passwordlist=['password']
mailer=['mailing domain']


def login(name,username,mail,password,ip,port):
    br = my_proxy()
    br.get('https://twitter.com/signup')
    if os.path.exists('cookies.pkl'):
        form = br.find_element_by_id('phx-signup-form')
        name_input = br.find_element_by_id('full-name')
	print "entering Name"
        email_input = br.find_element_by_id('email')
	print "entering mail"
	pass_input=br.find_element_by_id('password')
	print "entering password"	
	username_post=br.find_element_by_id('username')
	print "entering username"	
	name_input.send_keys(name)
        email_input.send_keys(mail)
	pass_input.send_keys(password)
	username_post.send_keys(username)     
	print "entered" 
  	time.sleep(10)
	form.submit()
	time.sleep(10)
	a=br.find_element_by_class_name('skip-link')
	insert(name,username,mail,password)
	print "Submiting form"	
        #pickle.dump( br.get_cookies() , open("cookies.pkl","wb"))
	print "cookies exist"
    else:
        try:
	   form = br.find_element_by_id('phx-signup-form')
           name_input = br.find_element_by_id('full-name')
           email_input = br.find_element_by_id('email')
	   pass_input=br.find_element_by_id('password')
	   username=br.find_element_by_id('username')
	   name_input.send_keys(name)
           email_input.send_keys(mail)
	   pass_input.send_keys(password)
	   username.send_keys(username)        
           br.implicitly_wait(10)
           time.sleep(10)	
	   form.submit()
	   time.sleep(15)
	   a=br.find_element_by_class_name('skip-link')
	   #insert(name,username,mail,password,ip,port)	
           br.implicitly_wait(10)
	   if os.path.exists('cookies.pkl'):
		print "logged in" 
        except Exception as e:
            print traceback.format_exc(e)



def my_proxy():
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.privatebrowsing.autostart", True)
	fp.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
        fp.update_preferences()
	#service = service.Service('/home/chowmean/Desktop/twitter_bot/chromedriver')
	#service.start()
	#capabilities = {'chrome.binary': '/path/to/custom/chrome'}
	#driver = webdriver.Remote(service.service_url, capabilities)
	return webdriver.Firefox(firefox_profile=fp)


def signing():
	name=  namelist[0]
	username=usernamelist[0]
	password=passwordlist[0]
	mail=usernamelist[0]+"@"+mailer[0]      
	login(name,username,mail,password,'0','0')
	time.sleep(2)
        br.close()
	

signing()
	
