import urllib2
from BeautifulSoup import BeautifulSoup
from time import sleep

url = "http://www.londonelects.org.uk/im-voter/results-and-past-elections/live-results-2012?contest=23"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

while 1:
  updated = soup.find("p", {"class" : "updated"}).text
  print updated

  table = soup.find("table", {"class" : "candidates"})

  for row in table.tbody.findAll("tr"):
    name = row.find("td", {"class" : "candidate"}).contents[0]
    result = row.find("td", {"class" : "result"}).text
  
    print "%s : %s" % (name, result)
  
  print "\n"
  
  sleep(60)