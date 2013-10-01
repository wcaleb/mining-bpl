I'm an historian of American antislavery. One of the largest and most useful collections of antislavery correspondence in the United States is the [Anti-Slavery Collection](http://www.bpl.org/distinction/featured-collections/anti-slavery/) at the Boston Public Library in Copley Square. That collection is now being gradually digitized and uploaded to the [Internet Archive](http://archive.org/details/bplscas/).

This repository contains two scripts I wrote to interact with the digital items in the collection, of which there are now over 6400.

- The script `bplscrape.py` was written to get a list of all the URLs to individual items in the collection. So that you don't have to run it again, I've also included the results (as of September 30, 2013) in the file `bplitemurls.txt`, and I will attempt to update this list as new items are uploaded to the collection.
- The script `bplparse.py` figures out the URL for each item's full MARCXML record and then parses the XML for particular metadata such as the creator and recipient of a letter. This can be useful for creating tables like the one in `bplnetwork.txt`, which contains (what I believe to be) the author and recipient for each letter in the collection, separated by a semicolon.

Please use these scripts with care so that the Internet Archive doesn't get hammered by requests. If you plan to interact at length with the XML metadata, for instance, you should probably modify one of the scripts so that you download copies of all the MARC records to your computer for local parsing.

For more explanation of how I'm using the stuff in this repository, see my blog post on [Mining the BPL Antislavery Collection on the Internet Archive](http://wcm1.web.rice.edu/mining-bpl-antislavery.html).
