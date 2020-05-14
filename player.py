from bs4 import BeautifulSoup
import requests
import re

# The underscore represents % (ie. fg_ = field goal percentage)
class perGame(object):
    __slots__ =  'age', 'team', 'league', 'pos', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_', 'p3', 'pa3', 'p3_', 'p2', 'pa2', 'p2_', 'efg_','ft', 'fta', 'ft_', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts'


def parsePerGame(stats):
    avgs = perGame()
    avgs.age = stats[1]
    avgs.team = stats[2]
    avgs.league = stats[3]
    avgs.pos = stats[4]
    avgs.g = stats[5]
    avgs.gs = stats[6]
    avgs.mp = stats[7]
    avgs.fg = stats[8]
    avgs.fga = stats[9]
    avgs.fg_ = stats[10]
    avgs.p3 = stats[11]
    avgs.pa3 = stats[12]
    avgs.p3_ = stats[13]
    avgs.p2 = stats[14]
    avgs.pa2 = stats[15]
    avgs.p2_ = stats[16]
    avgs.efg_ = stats[17]
    avgs.ft = stats[18]
    avgs.fta = stats[19]
    avgs.ft_ = stats[20]
    avgs.orb = stats[21]
    avgs.drb = stats[22]
    avgs.trb = stats[23]
    avgs.ast = stats[24]
    avgs.stl = stats[25]
    avgs.blk = stats[26]
    avgs.tov = stats[27]
    avgs.pf = stats[28]
    avgs.pts = stats[29]
    return avgs

#Given a player's name, getURL returns the URL of the player's page on basketball-reference.com
def getURL(firstName, lastName):
    firstName = firstName.lower() #URL is case sensitive
    lastName = lastName.lower()
    url = "https://www.basketball-reference.com/players/" + lastName[0] + "/" + lastName[:5] + firstName[:2] + "01.html"
    return url;

#getCareerAvg takes in a soup object as its parameter and returns a dict object containing a player's season averages for every season that player has played
def getCareerAvg(soup):
    seasonTable = soup.findAll('tr', attrs = {'class':'full_table'})
    for szn in seasonTable:
        statList = szn.getText(separator = ' ').split(' ')
        year = statList[1]
        parsePerGame( statList )

def getSznTotals(soup):
    #seasonTable = soup.findAll('tr', attrs = {'class':'full_table'})
    seasonTable = soup.findAll('tr', id = re.compile('^per'))
    for one in seasonTable:
        print(one.prettify())
        print('\n------------------------\n')

#getPlayerData takes in a URL as a string and returns the player's data
def getPlayerData(url):
    if()
    page = requests.get(url)
    if page:
        print("Success")
    else:
        print("Failure")
        return
    soup = BeautifulSoup(page.content)
    #getCareerAvg(soup)
    print('SEASON TOTALS\n')
    #print(soup.prettify())
    getSznTotals(soup)
    return;

getPlayerData(getURL("klay", "thompson"))
