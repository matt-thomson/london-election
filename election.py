import urllib2
from BeautifulSoup import BeautifulSoup
from time import sleep

url = "http://www.londonelects.org.uk/im-voter/results-and-past-elections/live-results-2012?contest=23"

prev_updated = ""

while 1:
  try:
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
  except:
    time.sleep(60)
    continue

  updated_elt = soup.find("p", {"class" : "updated"})
  
  if updated_elt:
    updated = updated_elt.text

  if updated != prev_updated:
    print updated
    print "        Name         | Vote"
    print "---------------------+-----"

    table = soup.find("table", {"class" : "candidates"})

    for row in table.tbody.findAll("tr"):
      name = row.find("td", {"class" : "candidate"}).contents[0]
      result = row.find("td", {"class" : "result"}).text

      print "%s | %s" % (name.ljust(20), result)

    print "\n"
    
  prev_updated = updated

  sleep(60)