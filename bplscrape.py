#! /usr/bin/env python
# -*- coding: utf-8 -*-
# bplscrape.py
# W. Caleb McDaniel / wcm1.web.rice.edu

# An ugly (but effective) method for getting all the item URLs from
# a given Internet Archive collection (in this case, I'm interested
# in a collection from the Boston Public Library called bplscas, but
# the method described here can be generalized to other collections.
# TODO: Figure out how to achieve same results using JSON API.

import urllib2
from bs4 import BeautifulSoup

# First, we'll get the HTML for each list of results from the IA collection.
# Then we will parse that HTML to find each item URL & append it to a text file.
# In this case I'm interested in the bplscas collection.

collectionname = 'bplscas'

# URLs for an Internet Archive search results page look like this:
# http://archive.org/search.php?query=collection%3Abplscas&page=1
# In this case I know there are 130 results pages.
# TODO: Automate the process of figuring out how many pages of results are in
# the search for a given collection

for resultsPage in range(1, 131):
 
 	url = "http://archive.org/search.php?query=collection%3A" + collectionname + "&page=" + str(resultsPage)
 	response = urllib2.urlopen(url).read()
 	soup = BeautifulSoup(response)
 	links = soup.find_all(class_="titleLink")
 	for link in links:
 		itemURL = link['href']
 		f = open('bplitemurls.txt','a')
 		f.write('http://archive.org' + itemURL + '\n')
 		f.close()

# Upon execution, the file `bplitemurls.txt` should contain a list of URLs.
# You can check to see that the number of URLs in the file matches the number
# listed in upper left hand corner of the collection's search results page
# on Internet Archive.
