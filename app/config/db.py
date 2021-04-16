import os
from collections import namedtuple

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import NamedTupleCursor

load_dotenv(override=True)

Connection = namedtuple('Connection', ['cursor', 'named_cursor'])


class DB:
    def __enter__(self):
        self.conn = psycopg2.connect(
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            dbname=os.getenv('DATABASE'),
            port=os.getenv('PORT'),
            host=os.getenv('HOST')
        )
        self.cursor = self.conn.cursor()
        self.named_cursor = self.conn.cursor(
            cursor_factory=NamedTupleCursor
        )

        return Connection(
            cursor=self.cursor,
            named_cursor=self.named_cursor
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.named_cursor.close()
        self.conn.close()
