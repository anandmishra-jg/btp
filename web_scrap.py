import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import deque

# Make the request to the homepage of GeeksforGeeks
url = 'https://www.geeksforgeeks.org/array-data-structure/array-sorting/'
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

hyperlinks = []

for post in soup.findAll('a'):
    hyperlink = post['href']
    if hyperlink.startswith('https://www.geeksforgeeks.org'):
        hyperlinks.append(hyperlink)

# Scrape the content of the blog articles
visited = set()
# ids = []
titles = []
authors = []
contents = []
q = hyperlinks[:10]
i = -1
while len(titles) < 100 and i+1 < len(q):
    i+=1

    hyperlink = q[i]

    if hyperlink[0]!='h':
        continue
    if hyperlink in visited:
        continue

    visited.add(hyperlink)
    # if hyperlink.startswith('https'):

    # Make the request to the hyperlink
    # pass
    response = requests.get(hyperlink)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # # Extract the blog slug

    for title in soup.find_all('title'):
        titles.append(title)
    for content in soup.find_all('entry-content'):
        contents.append(content)


    # Find all the hyperlinks in the blog content
    for post in soup.find_all('a'):
        link = post.get('href')
        if link not in visited:
            q.append(link)



# Create a pandas DataFrame with the attributes
data = {'Title': titles,  'Hyperlink': hyperlinks[:len(titles)]}

df = pd.DataFrame(data)


# Print the DataFrame
print(df)
