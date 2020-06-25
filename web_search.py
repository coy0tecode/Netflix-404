# -*- coding: utf-8 -*-
"""

* Search movie names from file in google. Click netflix result on first page if
  found. Check if netflix result is 404.

"""

import csv
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import datetime

# Start value to measure program runtime
start = datetime.now()

# Open movie file and read all lines to file_lines variable
movie_file = open('C:/PythonStuff/Projects/netflix-404/movie_names.txt', 'r', encoding='utf-8')
file_lines = movie_file.readlines()

# Set paths for Firefox webdriver
executable_path = 'C:/WebDriver/bin/geckodriver.exe'

# Set the headless option for browser
no_head = webdriver.FirefoxOptions()
no_head.headless=True

# Create the browser
browser = webdriver.Firefox(
    executable_path=executable_path, options=no_head)

# Open/Create CSV file to write search results to
search_results = open('C:/PythonStuff/Projects/netflix-404/netflix_search.csv', 'w', encoding='utf-8')

# Create list for fieldnames
column_names = ['Movie', 'Netflix Result', '404', 'URL']

# Set up CSV file for writing from dictionary
movie_results = csv.DictWriter(search_results, fieldnames=column_names)
movie_results.writeheader()

# LOOP START

for line in file_lines:
    
    line = line.strip()
    line = line.replace(' ', '+')
    line = line.replace('&amp;', 'and')
    
    # Search google for the movie name + movie online
    browser.get('https://google.com/search?q=' + line + '+movie+online&start=0')

    # If a google result is found, click the link and check to see if the movie is
    # on Netflix or if the page has a 404 error
    try:
        match = browser.find_element_by_xpath('//a[starts-with(@href, "https://www.netflix.com")]')
    except:
        line = line.replace('+', ' ')
        movie_results.writerow(
            {'Movie' : line, 'Netflix Result' : 'Not Found', '404' : 'N/A', 'URL' : 'N/A'})
    else:
        try:
            WebDriverWait(browser, 90).until(EC.element_to_be_clickable((By.XPATH,
                        '//a[starts-with(@href, "https://www.netflix.com")]')))
        except:
            pass
        try:
            match.click()
        except:
            pass
        page = requests.get(browser.current_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        err_check = soup.find(class_='error-page not-found')
        line = line.replace('+', ' ')
        if err_check:
            current_page = browser.current_url
            movie_results.writerow(
                {'Movie' : line, 'Netflix Result' : 'Found', '404' : 'YES', 'URL' : str(current_page)})
        else:
            current_page = browser.current_url
            movie_results.writerow(
                {'Movie' : line, 'Netflix Result' : 'Found', '404' : 'NO', 'URL' : str(current_page)})
    sleep(randint(5, 10))
    
# LOOP END

# Close the files
movie_results.close()

# Close browser
browser.quit()

# Print the time now minus the time when program started to get runtime
print(datetime.now()-start)
