import urllib2
from BeautifulSoup import BeautifulSoup
from time import sleep

url = "http://www.londonelects.org.uk/im-voter/results-and-past-elections/live-results-2012?contest=23"

prev_updated = ""

while 1:
  page = urllib2.urlopen(url)
  soup = BeautifulSoup(page)

  updated = soup.find("p", {"class" : "updated"}).text

  if updated != prev_updated:
    print updated

    table = soup.find("table", {"class" : "candidates"})

    for row in table.tbody.findAll("tr"):
      name = row.find("td", {"class" : "candidate"}).contents[0]
      result = row.find("td", {"class" : "result"}).text

      print "%s : %s" % (name, result)

    print "\n"
    
  prev_updated = updated

  sleep(60)