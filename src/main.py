from frontEnd.Web import Web
from backEnd.Scraper import Scraper
from backEnd.DB import DB

websites = [
    'http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=QUARTERBACK&season=2018&seasonType=REG']


class Main(object):

    def __init__(self):
        self.db = DB()
        self.scraper = Scraper(websites)
        self.web = Web(self.scraper)
