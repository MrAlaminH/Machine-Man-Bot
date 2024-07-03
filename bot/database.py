import sqlite3
from config import DATABASE_NAME

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            chat_id INTEGER,
            chat_type TEXT DEFAULT 'private'
        )
        ''')
        self.conn.commit()

    def add_user_or_group(self, username, chat_id, chat_type=None):
        self.cursor.execute(
            'INSERT OR IGNORE INTO users (username, chat_id, chat_type) VALUES (?, ?, ?)',
            (username, chat_id, chat_type if chat_type else 'private')
        )
        self.conn.commit()

    def get_all_chat_ids(self):
        self.cursor.execute('SELECT chat_id FROM users')
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.conn.close()