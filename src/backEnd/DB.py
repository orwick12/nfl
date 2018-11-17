import sqlite3
import json


class DB(object):
    def __init__(self):
        self.dbFile = "nfl.db"
        self.table_name_players = "PLAYERS"
        self.table_name_metadata = "METADATA"

    def create_table(self):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS " + self.table_name_players + ";")
        c.execute("DROP TABLE IF EXISTS " + self.table_name_metadata + ";")
        conn.commit()
        c.execute("CREATE TABLE " + self.table_name_players + " (ARTICLE_ID INTEGER PRIMARY KEY AUTOINCREMENT, URL text NOT NULL, AUTHOR text NOT NULL, PUBLISH_DATE text NOT NULL, CONTENT text NOT NULL, FOREIGN KEY (ARTICLE_ID) REFERENCES ARTICLE (ARTICLE_ID));")
        c.execute("CREATE TABLE " + self.table_name_metadata + " (METADATA_ID INTEGER PRIMARY KEY AUTOINCREMENT, ARTICLE_ID_1 INTEGER NOT NULL, ARTICLE_ID_2 INTEGER NOT NULL, PERCENT_MATCH REAL NOT NULL, FOREIGN KEY (ARTICLE_ID_1) REFERENCES ARTICLE (ARTICLE_ID_1), FOREIGN KEY (ARTICLE_ID_2) REFERENCES ARTICLE (ARTICLE_ID_2));")
        conn.commit()
        conn.close()