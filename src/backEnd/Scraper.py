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



