import sqlite3
import json


class DB(object):
    def __init__(self):
        self.dbFile = "nfl.db"
        self.table_name_players = "PLAYERS"
        self.create_player_table()

    def create_player_table(self):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS " + self.table_name_players + ";")
        conn.commit()
        c.execute("CREATE TABLE " + self.table_name_players + " (PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                              "PLAYER text NOT NULL, TEAM text NOT NULL);")
                                                              # " FOREIGN KEY (player) REFERENCES ARTICLE (player));")
        conn.commit()
        conn.close()

# TODO: create tables for each position and team
    def create_qb_table(self):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS " + self.table_name_players + ";")
        conn.commit()
        c.execute("CREATE TABLE " + self.table_name_players + " (PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                              "RANK INTEGER NOT NULL, PLAYER text NOT NULL, "
                                                              "TEAM text NOT NULL, POS text NOT NULL, "
                                                              "COMP INTEGER NOT NULL, ATTEMPTS INTEGER NOT NULL, "
                                                              "PCT FLOAT NOT NULL, ATTPERGAME FLOAT NOT NULL, "
                                                              "YDS INTEGER NOT NULL, AVG FLOAT NOT NULL, "
                                                              "YARDSPERGAME FLOAT NOT NULL, TD INTEGER NOT NULL, "
                                                              "INTERCEPTION INTEGER NOT NULL, "
                                                              "FIRSTDOWN INTEGER NOT NULL, "
                                                              "FIRSTDOWNPERCENT FLOAT NOT NULL, LNG INTEGER NOT NULL, "
                                                              "TWENTYPLUS INTEGER NOT NULL, FORTYPLUS INTEGER NOT NULL,"
                                                              " SACK INTEGER NOT NULL, RATE FLOAT NOT NULL, "
                                                              " FOREIGN KEY (player) REFERENCES ARTICLE (player));")

        conn.commit()
        conn.close()

    def db_player_insert(self, player, team):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("INSERT INTO {tn} (PLAYER, TEAM) VALUES (?, ?)".format(tn=self.table_name_players), (player, team))
        conn.commit()
        conn.close()