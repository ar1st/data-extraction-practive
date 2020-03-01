import requests
from bs4 import BeautifulSoup
import re

#initialize variables
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
k = 10; #number of iterations
linksFromWiki = set()

def getLink(k):
    if ( k > 1):
        #seeds.txt contains the remaining links to be searched
        #constantly is filled with new links
        #get first line and then delete it
        with open('./seeds.txt','r') as f:
            first_line = f.readline().strip()
            data = f.read().splitlines(True)
        with open('seeds.txt', 'w') as fout:
            fout.writelines(data[1:])

        #get html code
        page = requests.get('https://en.wikipedia.org' + first_line, headers=header)
        soup = BeautifulSoup(page.content, 'html.parser')
        #get all the links
        allLinks = soup.find_all('a', href=True)

        for x in allLinks:
            ok = x['href'].split("/")
            if (len(ok) > 1):
                # get only the links that redirect inside wikipedia
                if (ok[1] == 'wiki'):
                    # get only links that redirect to other articles
                    # remove links like /wiki/Wikipedia:About and /wiki/Wikipedia:General_disclaimer
                    if (not (":" in ok[2])):
                        #check if link already exists
                        if ( not(x['href'] in linksFromWiki)):
                            #add link in set
                            linksFromWiki.add(x['href'])
                            #add link in links.txt
                            #contains all the unique links
                            with open('./links.txt', 'a',encoding="utf-8") as file:
                                file.write(x['href'] + '\n')
                            #add link in seeds.txt
                            with open('./seeds.txt', 'a',encoding="utf-8") as file:
                                file.write(x['href'] + '\n')
        #call the getLink method recursively
        getLink(k-1)
    return

#starting link
with open('./seeds.txt', 'w') as file:
    file.write('/wiki/Mia_Khalifa')
#delete everything on links.txt
open('links.txt', 'w').close()

#Start searching to get links
#using recursion
getLink(k)