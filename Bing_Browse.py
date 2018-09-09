from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url_to_sign_in = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1536194568&rver=6.7.6631.0&wp=MBI&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%2523%26sig%3d05F0C3C86BE867C000D4CFA96A84663E&lc=1033&id=264960&CSRFToken=140ddca9-e582-4821-8f5d-8b5bc7bdc8c2&aadredir=1'

def signIn():
	#sets the options for the browser
	browser_options = webdriver.FirefoxOptions()
	browser_options.set_headless(headless=False)

	#intializes them for the driver
	browser = webdriver.Firefox(firefox_options=browser_options)

	#takes in the url
	browser.get(url_to_sign_in)
	
	#finds the elements where I put in my username
	inputElement = browser.find_element_by_name("loginfmt")
	
	#enters my username
	inputElement.send_keys(#enter your username)
	
	#presses enter and takes you to the password page
	inputElement.send_keys(Keys.RETURN)
	
	time.sleep(5)
	
	#finds element where I put in my password
	inputElement = browser.find_element_by_name("passwd")
	
	#enters in my password
	inputElement.send_keys(#enter your password)
	
	inputElement.submit()
	
	return browser
	
	
	
def signOut(browser):


	#clicks on the profile so it can click signout
	inputElement = browser.find_element_by_id("id_n").click()
	
	time.sleep(2)
	
	#signs out of the account
	inputElement = browser.find_element_by_class_name("id_link_text").click()
	

def browse(url, browser):

	#takes in the url
	browser.get(url)
	