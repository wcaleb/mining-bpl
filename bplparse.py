#! /usr/bin/env python
# -*- coding: utf-8 -*-
# bplscrape.py
# W. Caleb McDaniel / wcm1.web.rice.edu

# An ugly (but effective) method to take a list of item URLs in the
# BPL Antislavery Collection on the Internet Archive, find the URL to the
# item's full MARC XML record, and then parse that XML for desired metadata.
# For large, ongoing projects, it's recommended that you modify this script 
# to write all the XML records you need to local files.

# First, we'll parse the HTML of each item page to get HTTPS url root
# Append _marc.xml to each of these https URLs to get URL to MARC record.
# Then parse the MARC record to get desired data fields for the item.

# Function for dealing with empty datafields in the MARC record.
# http://stackoverflow.com/questions/3376666/
def getstring(tag):
	return "None" if tag is None else tag.subfield.string.encode('utf-8')

f = open('bplitemurls-chunk.txt','r')
for line in f:

	# remove new lines, save item name for later when forming url to MARC
	line = line.rstrip()	
	itemname = line.rsplit("/", 1)[1]

	# go to item page to get root for HTTPS url, needed for url to MARC
	itempage = urllib2.urlopen(line).read()
	htmlsoup = BeautifulSoup(itempage)
	https_string = htmlsoup.find(text="HTTPS")	
	xmlurl = https_string.find_parent("a")['href'] + "/" + itemname + "_marc.xml"

	# go to MARC record for item to get author, recipient(s), BPL call number
 	marcxml = urllib2.urlopen(xmlurl).read()
 	xmlsoup = BeautifulSoup(marcxml, "xml")
 	# bplcallno = getstring(xmlsoup.find(tag="099"))
	author = getstring(xmlsoup.find(tag="100"))
	recipient = getstring(xmlsoup.find(tag="700"))
	f = open('bplnetwork.txt','a')
	f.write(author + ';' + recipient + '\n')
	f.close

# CHECK IF I HAVE A LOCAL TRANSCRIPTION OF A GIVEN RECORD
# ----------------------------------------------------------

# The following code won't be generally useful. It's basically a method
# I devised to see if the notes I took at the BPL contain a transcription
# of an item that has been uploaded to the Internet Archive
# import os.path

# 	# strip out unneeded characters from bplcallno
# 	# E.g turn "Ms.A.9.2 vol. 16, p. 22" to "Ms.A.9.2.16.22"
# 	bplcallno = str(bplcallno).translate(None, ' voln,p')
# 
# 	if os.path.exists("/Users/wcm1/programming/bpltranscript/renamed/" + bplcallno):
# 		print bplcallno + " exists"
# 	else:
# 		print bplcallno + " does not exist"
# 
# # Strip out non-relevant characters using str.translate
# # str.translate(None, ' voln,p')
# 
# # The result is also the name of the file that has the transcription,
# # so combine the URL string with the text of this transcription file.
