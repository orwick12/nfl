from requests import get
from bs4 import BeautifulSoup


class Scraper(object):
    def __init__(self, websites, db):
        self.websites = websites
        self.db = db

    def generate_stats(self):
        for site in self.websites:
            soup = self.scrape(site)
            self.parse(soup)

    def scrape(self, website):
        response = get(website)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def parse(self, soup):
        for table in soup.findAll('table'):
            for row in table.findAll(['tr']):
                player = []
                for column in row.findAll(['td']):
                    playerData = column.text.strip()
                    player.append(playerData)
                if player:
                    self.db.db_player_insert(player=player[1], team=player[2])
                    if player[3] == "QB":
                        self.db.db_qb_insert(player=player[1], team=player[2], pos=player[3], comp=player[4], att=player[5], pct=player[6], attpergame=player[7], yds=player[8], avg=player[9], yardspergame=player[10], td=player[11], interception=player[12], firstdown=player[13], firstdownpct=player[14], lng=player[15], twentyplus=player[16], fortyplus=player[17], sack=player[18], rate=player[19])
                    elif player[3] == "RB":
                        self.db.db_rb_insert(player=player[1], team=player[2],pos=player[3], att=player[4], attpergame=player[5], yds=player[6], average=player[7], yardspergame=player[8], td=player[9], lng=player[10], firstdown=player[11], firstdownpct=player[12], twentyplus=player[13], fortyplus=player[14], fumble=player[15])
                    elif player[3] == "WR":
                        self.db.db_wr_insert(player=player[1], team=player[2], pos=player[3], rec=player[4], yds=player[5], average=player[6], yardspergame=player[7], lng=player[8], td=player[9], twentyplus=player[10], fortyplus=player[11], firstdown=player[12], firstdownpct=player[13], fumble=player[14])
                    elif player[3] == "TE":
                        self.db.db_te_insert(player=player[1], team=player[2], pos=player[3], rec=player[4], yds=player[5], average=player[6], yardspergame=player[7], lng=player[8], td=player[9], twentyplus=player[10], fortyplus=player[11], firstdown=player[12], firstdownpct=player[13], fumble=player[14])
