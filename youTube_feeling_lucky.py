# I'm feeling lucky search from terminal for YouTube
# usage: youTube_feeling_lucky.py <enter search term here>

import sys
from selenium import webdriver

PATH = '/users/rorycockle/documents/python/chromedriver'
searchTerm = '+'.join(sys.argv[1:])

browser = webdriver.Chrome(PATH)
browser.get('https://youtube.com/results?search_query=' + searchTerm)
thumbnailElem = browser.find_element_by_id('thumbnail')
thumbnailElem.click()