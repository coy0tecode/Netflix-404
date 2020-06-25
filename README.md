# Netflix-404
Repository for my Netflix-404 Project
I was searching on google for a movie to watch one night, and on the first page of the results was a Netflix result for the movie. But when I clicked it, I got a 404 page. I searched on Netflix itself for the movie and got no results.

This is my first project, a small one where we scrape the names of all the movies available on Netflix according to reelgood.com's filter, search the first page of google using the movie names plus 'movie online', click the first Netflix link if found, and check to see if the movie's available or if there's a 404 error.

Next, we take the results of the search and write them to a csv file. We then use that file to sort movies that produced no result in the search and movies that returned a 404 error, and write these to respective csv files. Finally, we make a pie chart showing the search results and save it to a PDF.

There's lots of room for improvement with this project. For example, web_search.py instruction to wait until element is clickable will stop trying after 90 seconds, and won't always return the correct result, requiring manual correction of the csv file (I tried some additional waits and Javascript execution, but did not find a way to resolve this issue without further errors).

Additional considerations:

    Movie results that returned a 404 error may be available on Netflix as a DVD rental. Another script could search https://dvd.netflix.com/ for these movies
    The offset on reelgood's movie listings may increase if more movies are added and none are removed. Currently reelgood_scrape.py is hard-coded to reach a maximum offset of 3650, which could leave out new movies added.
