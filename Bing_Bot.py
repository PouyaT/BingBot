import time
from selenium import webdriver
from Bing_Browse import signIn, browse, signOut
import random
import os
import linecache

def searching():
	baseURL = 'https://www.bing.com/search?q='

	#generates a random number
	randomNumber = random.randint(1,370099)
	
	#chooses a random word in the file
	randomWord = linecache.getline('Dictionary.txt',randomNumber)
	
	#concatinates the url and the random word
	search = baseURL + randomWord
	
	#signs in to the bing account
	browser = signIn()
	
	time.sleep(5)

	#searches using the random word
	browse(search, browser)
	
	time.sleep(5)
	
	#signouts of the account
	signOut(browser)
	
	time.sleep(5)
	
	#closes the browser
	browser.quit()

def main():
	while True:
		searching()

if __name__ == '__main__':
	main()		
	
	




