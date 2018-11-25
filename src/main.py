from frontEnd.Web import Web
from backEnd.Scraper import Scraper
from backEnd.DB import DB

websites = [
    'http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=QUARTERBACK&season=2018&seasonType=REG',
    'http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=RUNNING_BACK&season=2018&seasonType=REG',]
    # 'http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=WIDE_RECEIVER&season=2018&seasonType=REG',
    # 'http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=TIGHT_END&season=2018&seasonType=REG',
    # 'http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=FIELD_GOAL_KICKER&season=2018&seasonType=REG']


class Main(object):

    def __init__(self):
        self.db = DB()
        self.scraper = Scraper(websites, self.db)
        self.web = Web(self.scraper)
