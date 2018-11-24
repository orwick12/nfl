import sqlite3
import json


class DB(object):
    def __init__(self):
        self.dbFile = "nfl.db"
        self.table_name_players = "PLAYERS"
        self.table_quarterbacks = "QUARTERBACKS"
        self.table_runningbacks = "RUNNINGBACKS"
        self.table_widereceivers = "WIDERECEIVERS"
        self.table_tightends = "TIGHTENDS"
        self.table_kickers = "KICKERS"
        self.create_player_tables()

    def create_player_tables(self):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS " + self.table_name_players + ";")
        c.execute("DROP TABLE IF EXISTS " + self.table_quarterbacks + ";")
        c.execute("DROP TABLE IF EXISTS " + self.table_runningbacks + ";")
        c.execute("DROP TABLE IF EXISTS " + self.table_widereceivers + ";")
        c.execute("DROP TABLE IF EXISTS " + self.table_tightends + ";")
        c.execute("DROP TABLE IF EXISTS " + self.table_kickers + ";")
        conn.commit()
        c.execute("CREATE TABLE " + self.table_name_players + " (PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                              "PLAYER text NOT NULL, TEAM text NOT NULL);")
        c.execute("CREATE TABLE " + self.table_quarterbacks + "(QB_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
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
                                                              " FOREIGN KEY (player) REFERENCES PLAYER (player));")
        c.execute("CREATE TABLE " + self.table_runningbacks + " (RB_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                              "RANK INTEGER NOT NULL, PLAYER text NOT NULL, "
                                                              "TEAM text NOT NULL, POS text NOT NULL, "
                                                              "ATT INTEGER NOT NULL, ATTPERGAME FLOAT NOT NULL, "
                                                              "YDS INTEGER NOT NULL, AVG FLOAT NOT NULL, "
                                                              "YARDSPERGAME FLOAT NOT NULL, TD INTEGER NOT NULL, "
                                                              "LNG INTEGER NOT NULL, FIRSTDOWN INTEGER NOT NULL, "
                                                              "FIRSTDOWNPERCENT FLOAT NOT NULL, "
                                                              "TWENTYPLUS INTEGER NOT NULL, FORTYPLUS INTEGER NOT NULL,"
                                                              "FUMBLE INTEGER NOT NULL,"
                                                              "FOREIGN KEY (player) REFERENCES PLAYER (player));")
        c.execute("CREATE TABLE " + self.table_widereceivers + " (WR_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                               "RANK INTEGER NOT NULL, PLAYER text NOT NULL, "
                                                               "TEAM text NOT NULL, POS text NOT NULL, "
                                                               "REC INTEGER NOT NULL, YDS INTEGER NOT NULL, "
                                                               "AVG FLOAT NOT NULL, YARDSPERGAME FLOAT NOT NULL,"
                                                               "LNG INTEGER NOT NULL, TD INTEGER NOT NULL, "
                                                               "TWENTYPLUS INTEGER NOT NULL, FORTYPLUS INTEGER NOT NULL,"
                                                               "FIRSTDOWN INTEGER NOT NULL, FIRSTDOWNPERCENT FLOAT NOT NULL,"
                                                               "FUMBLE INTEGER NOT NULL,"
                                                               "FOREIGN KEY (player) REFERENCES PLAYER (player));")
        c.execute("CREATE TABLE " + self.table_tightends + " (PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                           "RANK INTEGER NOT NULL, PLAYER text NOT NULL,"
                                                           "TEAM text NOT NULL, POS text NOT NULL, "
                                                           "REC INTEGER NOT NULL, YDS INTEGER NOT NULL, "
                                                           "AVG FLOAT NOT NULL, YARDSPERGAME FLOAT NOT NULL, "
                                                           "LNG INTEGER NOT NULL, TD INTEGER NOT NULL, "
                                                           "TWENTYPLUS INTEGER NOT NULL, FORTYPLUS INTEGER NOT NULL, "
                                                           "FIRSTDOWN INTEGER NOT NULL, FIRSTDOWNPERCENT FLOAT NOT NULL,"
                                                           "FUMBLE INTEGER NOT NULL,"
                                                           "FOREIGN KEY (player) REFERENCES PLAYER (player));")
        conn.commit()
        conn.close()

# TODO: create tables for each position and team
#     def create_qb_table(self):
#         conn = sqlite3.connect(self.dbFile)
#         c = conn.cursor()
#         c.execute("DROP TABLE IF EXISTS " + self.table_name_players + ";")
#         conn.commit()
#         c.execute("CREATE TABLE " + self.table_name_players + " (PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
#                                                               "RANK INTEGER NOT NULL, PLAYER text NOT NULL, "
#                                                               "TEAM text NOT NULL, POS text NOT NULL, "
#                                                               "COMP INTEGER NOT NULL, ATTEMPTS INTEGER NOT NULL, "
#                                                               "PCT FLOAT NOT NULL, ATTPERGAME FLOAT NOT NULL, "
#                                                               "YDS INTEGER NOT NULL, AVG FLOAT NOT NULL, "
#                                                               "YARDSPERGAME FLOAT NOT NULL, TD INTEGER NOT NULL, "
#                                                               "INTERCEPTION INTEGER NOT NULL, "
#                                                               "FIRSTDOWN INTEGER NOT NULL, "
#                                                               "FIRSTDOWNPERCENT FLOAT NOT NULL, LNG INTEGER NOT NULL, "
#                                                               "TWENTYPLUS INTEGER NOT NULL, FORTYPLUS INTEGER NOT NULL,"
#                                                               " SACK INTEGER NOT NULL, RATE FLOAT NOT NULL, "
#                                                               " FOREIGN KEY (player) REFERENCES ARTICLE (player));")
#         conn.commit()
#         conn.close()

    def db_player_insert(self, player, team):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("INSERT INTO {tn} (PLAYER, TEAM) VALUES (?, ?)".format(tn=self.table_name_players), (player, team))
        conn.commit()
        conn.close()

    def db_qb_insert(self, player, team):
        conn = sqlite3.connect(self.dbFile)
        c = conn.cursor()
        c.execute("INSERT INTO {tn} (PLAYER, TEAM) VALUES (?, ?)".format(tn=self.table_quarterbacks),
                  (player, team))
        conn.commit()
        conn.close()