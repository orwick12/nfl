from requests import get
from bs4 import BeautifulSoup


class Scraper(object):
    def __init__(self, websites):
        self.websites = websites
        # self.db = db

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
            # for row in table:
            for tr in table.findAll(['tr']):
                line = ""
                line += tr.text
                # print(line)
                for td in table.findAll(['td']):
                    player = ""
                    player += td.text.strip()
                    print(player)
                    return player

