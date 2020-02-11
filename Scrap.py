import requests
from bs4 import BeautifulSoup
import re

# Using wildcards to get all the titles
rex = re.compile("Τίτλος Μαθήματος: *")

# Get all the html code
result = requests.get("https://www.iee.ihu.gr/udg_courses/")

# Get all the tds that contain the courses' title
c= result.content
soup = BeautifulSoup(c,features="html.parser")
samples = soup.find_all("td", title = rex)

# Insert the titles in a list
data =[]
for i in range(0,len(samples)):
    title = samples[i].string  # Keep just the title, scrap any html code
    data.insert(i, title)


# Write in the file the titles of the lessons of the 7th semester
with open("7th semester.txt", "w", encoding="utf-8") as f:
    for i in range(36, 47):
        f.write(data[i] + '\n')