#program to insert the details of an a03 work into a csv

import sys
import csv
import requests
from bs4 import BeautifulSoup
import os.path 

if len(sys.argv) < 3:
    print("Please add the url and the path to the csv as arguments.")
    exit()

url = sys.argv[1] #get the url from the command line
output_path = sys.argv[2] #get the csv path from the command line

#go to the ao3 url and scrape the information wanted
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

fandom_tags = soup.find_all("dd", class_="fandom tags")
for tag in fandom_tags:
    t = tag.find_all("a", class_="tag")
    if t != None:
        break

fandoms = [] 
for element in t:
    fandoms.append(element.text)

relationship_tags = soup.find_all("dd", class_="relationship tags")
for tag in relationship_tags:
    t = tag.find_all("a", class_="tag")
    if t != None:
        break

relationships = [] 
for element in t:
    relationships.append(element.text)

freeform_tags = soup.find_all("dd", class_="freeform tags")
for tag in freeform_tags:
    t = tag.find_all("a", class_="tag")
    if t != None:
        break

tags = []
for element in t:
    tags.append(element.text)

title_element = soup.find("h2", class_="title heading") 
title = title_element.text.strip()

authors = []
author_element = soup.find("h3", class_="byline heading") 
authors_list = author_element.find_all("a")

for element in authors_list:
    authors.append(element.text)

stats = soup.find("dl", class_="stats") 
words = stats.find("dd", class_= "words")
wordcount = words.text
 
summary = ""
summary_element = soup.find("div", class_="summary module" )
summary_list = summary_element.find_all("p")
for p in summary_list:
    summary = summary + p.text.strip()

#write the information to a csv 
exists = False

if os.path.isfile(output_path) == True:
    exists = True

with open(output_path, 'a', newline='') as outfile:
    writer = csv.writer(outfile)

    if exists == False:
        writer.writerow(["Title", "Author", "URL", "Fandom", "Relationship",  "Wordcount", "Tags", "Summary"])

    writer.writerow([title, ", ".join(authors), url, ", ".join(fandoms), ", ".join(relationships), wordcount, ", ".join(tags), summary])

print("All done!")