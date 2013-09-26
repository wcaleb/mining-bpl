#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import os.path
from bs4 import BeautifulSoup

# Get the HTML for each list of results from the BPL collection. URLs look
# like this: http://archive.org/search.php?query=collection%3Abplscas&page=1
# I know there are 103 pages.

# for resultsPage in range(1, 104):
# 
# 	url = "http://archive.org/search.php?query=collection%3Abplscas&page=" + str(resultsPage)
# 	response = urllib2.urlopen(url).read()
# 	soup = BeautifulSoup(response)
# 	links = soup.find_all(class_="titleLink")
# 	for link in links:
# 		itemURL = link['href']
# 		f = open('bplitemurls.txt','a')
# 		f.write('http://archive.org' + itemURL + '\n')
# 		f.close()

# Parse the HTML of each item page to get HTTPS url root
# Append _marc.xml to each of these https URLs.
# Get the HTML for the new url and parse for datafield tag=099 and
# subfield code=a 

bpldict = dict()
f = open('bplitemurls-short.txt','r')
for line in f:

	# remove new lines, save item name for later when forming url to MARC
	line = line.rstrip()	
	itemname = line.rsplit("/", 1)[1]

	# go to item page to get root for HTTPS url, needed for url to MARC
	itempage = urllib2.urlopen(line).read()
	htmlsoup = BeautifulSoup(itempage)
	https_string = htmlsoup.find(text="HTTPS")	
	xmlurl = https_string.find_parent("a")['href'] + "/" + itemname + "_marc.xml"

	# go to MARC record for item to get BPL call number
	marcxml = urllib2.urlopen(xmlurl).read()
	xmlsoup = BeautifulSoup(marcxml, "xml")
	xmlsoup = xmlsoup.find(tag="099")
	bplcallno = xmlsoup.subfield.string

	# strip out unneeded characters
	# E.g turn "Ms.A.9.2 vol. 16, p. 22" to "Ms.A.9.2.16.22"
	bplcallno = str(bplcallno).translate(None, ' voln,p')

	if os.path.exists("/Users/wcm1/programming/bpltranscript/renamed/" + bplcallno):
		print bplcallno + " exists"
	else:
		print bplcallno + " does not exist"

	


# Strip out non-relevant characters using str.translate
# str.translate(None, ' voln,p')

# The result is also the name of the file that has the transcription,
# so combine the URL string with the text of this transcription file.
