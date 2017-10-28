import logging
import json

import pymysql
import arrow

from twitchRPG_core import config
from twitchRPG_core.notify import email

sqlquerylog = config.FS_LOGS + 'sql-queries.log'
logging.basicConfig(filename=sqlquerylog, level=logging.INFO)


class Model(object):
    """docstring for Model."""
    last_cursor = None
    conn = None

    def _create_conn(self):
        self.conn = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            db=config.DB_NAME,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def query_one(self, query="", params={}):
        self._create_conn()
        result = {}
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()
                self.last_cursor = cursor
        except pymysql.MySQLError as error:
            logging.error('MySqlError: ' + error)
            email.sendmail('[TwitchRPG] MySqlError', error)
        finally:
            self.conn.close()
        return result

    def query_all(self, query="", params={}):
        self._create_conn()
        result = []
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                self.last_cursor = cursor
        except pymysql.MySQLError as error:
            logging.error('MySqlError: ' + error)
            email.sendmail('[TwitchRPG] MySqlError', error)
        finally:
            self.conn.close()
        return result

    def save(self, query="", params={}):
        self._create_conn()
        response = False
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                if cursor.rowcount > 0:
                    response = True
                self.last_cursor = cursor
            self.conn.commit()
        finally:
            self.conn.close()
        return response


class Player(Model):
    """docstring for Player."""

    def __init__(self):
        super(Player, self).__init__()

    def get_players(self):
        return self.query_all("SELECT * FROM players LIMIT 100")


class Enemy(Model):
    """docstring for Enemy."""

    def __init__(self):
        super(Enemy, self).__init__()

    def get_enemies(self):
        return self.query_all("SELECT * FROM enemies LIMIT 100")
