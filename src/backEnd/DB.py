import sqlite3
import json


class DB(object):
    def __init__(self):
        self.dbFile = "nfl.db"
        self.table_name_players = "PLAYERS"
        # self.table_name_metadata = "METADATA"
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS " + self.table_name_players + ";")
        # c.execute("DROP TABLE IF EXISTS " + self.table_name_metadata + ";")
        conn.commit()
        c.execute("CREATE TABLE " + self.table_name_players + " (PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                              "RANK INTEGER NOT NULL, PLAYER text NOT NULL, "
                                                              "TEAM text NOT NULL, POS text NOT NULL, "
                                                              "COMP INTEGER NOT NULL, ATTEMPTS INTEGER NOT NULL, "
                                                              "PCT FLOAT NOT NULL, ATTPERGAME FLOAT NOT NULL, "
                                                              "YDS INTEGER NOT NULL, AVG FLOAT NOT NULL, "
                                                              "YARDSPERGAME FLOAT NOT NULL, TD INTEGER NOT NULL, "
                                                              "INT INTEGER NOT NULL, FIRSTDOWN INTEGER NOT NULL, "
                                                              "FIRSTDOWNPERCENT FLOAT NOT NULL, LNG INTEGER NOT NULL, "
                                                              "TWENTYPLUS INTEGER NOT NULL, FORTYPLUS INTEGER NOT NULL,"
                                                              " SACK INTEGER NOT NULL, RATE FLOAT NOT NULL, "
                                                              " FOREIGN KEY (player) REFERENCES ARTICLE (player));")
        # c.execute("CREATE TABLE " + self.table_name_metadata + " (METADATA_ID INTEGER PRIMARY KEY AUTOINCREMENT, ARTICLE_ID_1 INTEGER NOT NULL, ARTICLE_ID_2 INTEGER NOT NULL, PERCENT_MATCH REAL NOT NULL, FOREIGN KEY (ARTICLE_ID_1) REFERENCES ARTICLE (ARTICLE_ID_1), FOREIGN KEY (ARTICLE_ID_2) REFERENCES ARTICLE (ARTICLE_ID_2));")
        conn.commit()
        conn.close()

    def db_insert(self):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()