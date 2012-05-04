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
    sleep(60)
    continue

  updated_elt = soup.find("p", {"class" : "updated"})
  
  if updated_elt:
    updated = updated_elt.text

    if updated != prev_updated:
      print updated
      print "        Name         |             Party                  | Vote "
      print "---------------------+------------------------------------+------"

      table = soup.find("table", {"class" : "candidates"})

      for row in table.tbody.findAll("tr"):
        candidate = row.find("td", {"class" : "candidate"})
        name = candidate.contents[0]

        party = candidate.find("span", {"class" : "party"}).contents
        if len(party):
          party = party[0]
        else:
          party = 'Independent'

        result = row.find("td", {"class" : "result"}).text

        print "%s | %s | %s" % (name.ljust(20), party.ljust(34), result.rjust(4))

      print "\n"
    
    prev_updated = updated

  sleep(60)
