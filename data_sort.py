# -*- coding: utf-8 -*-
"""

* Sort data into CSV files, output pie plot showing results of web_search.py

"""


import pandas as pd
import gc

df = pd.read_csv('C:/PythonStuff/Projects/netflix-404/netflix_search.csv')

# Get info from df
df.info()

# Check column names
print(df.columns)

# Assign variables for each column
movie_name = df['Movie']
netflix = df['Netflix Result']
err = df['404']
link = df['URL']


# Replace the null values in 'err' and 'url'
err.fillna('N/A', inplace=True)
link.fillna('N/A', inplace=True)

# Variable to store number of '404' negatives
available = sum(df['404'] == 'NO')
print(f'Available = {available}')

# Variable to store number of '404' positives
missing = sum(df['404'] == 'YES')
print(f'Missing = {missing}')

# Variable to store number of 'not found' results
not_found = sum(df['Netflix Result'] == 'Not Found')
print(f'Not Found = {not_found}')

# Variable to store total number of movies
total_movies = sum(df['Movie'] != '')
print(f'Total Number of Movies = {total_movies}')

# Variable to store number of movies found
movies_found = total_movies - not_found
print(f'Total number of movies found = {movies_found}')

# Get info again
df.info()

# Variable to store rows of '404' positive movies
missing_data = df[df['404'] == 'YES']

# Variable to store rows of 'Not Found' movies
absent_data = df[df['Netflix Result'] == 'Not Found']

# Create data frame for pie plot
pie_df = pd.DataFrame({'totals': [available, not_found, missing]},
                      index=['Available', 'Not Found', 'Missing'])

# Function for adding totals and % to pie plot
def numbers(totals):
    def my_autopct(value):
        total = total_movies
        num = int(round(value*total/100))
        return '{v:.2f}% ({n:d})'.format(v=value, n=num)
    return my_autopct

# Make the pie plot
pie_plot = pie_df.plot.pie(y='totals', figsize=(7, 7), autopct=numbers('totals'))

# Calculate % of movies found
found_per = (movies_found / total_movies) * 100
found_per = str(round(found_per, 2))

# Calculate % of movies available
avail_per = (available / total_movies) * 100
avail_per = str(round(avail_per, 2))

# Calculate % of movies not found
not_found_per = (not_found / total_movies) * 100
not_found_per = str(round(not_found_per, 2))

# Calculate % of movies missing (404)
missing_per = (missing / total_movies) * 100
missing_per = str(round(missing_per, 2))


# Write the missing and absent data to respective csv files
missing_data.to_csv('C:/PythonStuff/Projects/netflix-404/404_Error.csv')
absent_data.to_csv('C:/PythonStuff/Projects/netflix-404/Not_Found.csv')

# Write a summary of the results to a text file
with open('C:/PythonStuff/Projects/netflix-404/results_summary.txt',
          'w', encoding='utf-8') as rs:
    rs.write(f'Summary of Search Results\n\n')
    rs.write(f'Total number of titles searched: {total_movies}\n')
    rs.write(f'Movies found: {movies_found}\n')
    rs.write(f'Movies available: {available}\n')
    rs.write(f'Movies not found: {not_found}\n')
    rs.write(f'404 errors encountered: {missing}\n')
    rs.write(f'Percentage of movies found: {found_per}\n')
    rs.write(f'Percentage of movies available: {avail_per}\n')
    rs.write(f'Percentage of movies not found: {not_found_per}\n')
    rs.write(f'Percentage of movies missing (404 errors): {missing_per}\n')
    

# Save the pie plot to a file
fig = pie_plot.get_figure()
fig.savefig('C:/PythonStuff/Projects/netflix-404/movie_pie.pdf')
    

# Collect and release memory used by DataFrames
# Commenting out for now while I research more/better ways to do this

gc.collect()
df = pd.DataFrame()
pie_df = pd.DataFrame()