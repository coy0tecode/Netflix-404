# -*- coding: utf-8 -*-
"""

* Scrapes all movie names listed on reelgood netflix filter and writes them
  to a text file

"""


import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import datetime

# Start value to measure program runtime
start = datetime.now()

names_file = open('C:/PythonStuff/Projects/netflix-404/movie_names.txt', 'w', encoding='utf-8')

offset = 0

# START OF OFFSET LOOP

for i in range(73):
    
    # Use sleep() to control crawl rate
    sleep(randint(3, 10))

    # Collect page of movies sorted alphabetically
    page = requests.get(f'https://reelgood.com/movies/source/netflix?filter-sort=4&offset={offset}')

    # Create BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    # Pull all text from css-1u7zfla e126mwsw1 (this is where the title is in the table)
    movie_list = soup.find_all(class_='css-1u7zfla e126mwsw1')

    # Add only the names of the movies (as strings) to list movie_names
    movie_names = [str(BeautifulSoup(item.text, 'html.parser')) for item in movie_list]
    
    for name in movie_names:
        names_file.write(name + '\n')
    
    offset += 50

# END OF OFFSET LOOP
    
names_file.close()

# Print the time now minus the time when program started to get runtime
print(datetime.now()-start)
