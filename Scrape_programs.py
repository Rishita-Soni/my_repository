import requests
import csv
import pandas as pd
from csv import writer
from bs4 import BeautifulSoup


url = 'https://knowthychoice.in/blog'

r = requests.get(url)
htmlcontent = r.content

programs = {}
soup = BeautifulSoup(htmlcontent,'html.parser')
program_links = []
internship = soup.find_all('div', attrs = {'class':'blog-post-content'})

for links in internship:
    download = links.find_all('a')
    for links in download:
        LinkText = (links['href'])
        program_links.append(LinkText)

for intern in program_links:
    htmlcont = requests.get(intern).content
    new = BeautifulSoup(htmlcont,'html.parser')
    name = new.title.string
    concepts_list = new.select('ul')
    for items in concepts_list[5:6]:
       concepts = items.text.split('\n')
       while "" in concepts:
        concepts.remove("")
       programs[name]=concepts
print(programs)
with open('Scrape_programs.csv','w') as testfile:
    writer = csv.writer(testfile)
    writer.writerow(programs.keys())
    writer.writerows(zip(*programs.values()))