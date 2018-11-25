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
                        self.db.db_rb_insert()
                    elif player[3] == "WR":
                        self.db.db_wr_insert()
                    elif player[3] == "TE":
                        self.db.db_te_insert()
