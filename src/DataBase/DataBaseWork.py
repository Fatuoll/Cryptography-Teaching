import sqlite3

from datetime import datetime

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from src.Algorithms.AES.AesPractical import AesLibrary


class DataBaseWork:
    def __init__(self):
        self.dbname = 'src/DataBase/database.db'
        self.userid = None
        self.attempts = {}

    def signin(self, user, password):
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        id_user = cur.execute("SELECT id FROM Users WHERE user = ?", (user,)).fetchone()[0]
        if id_user:
            real_password = cur.execute("SELECT password FROM Users WHERE id = ?", (id_user,)).fetchone()[0]
            try:
                ph = PasswordHasher()
                password_hash = ph.hash(password)
                ph.verify(real_password, password_hash)

                self.userid = id_user
                con.close()
                return True, ''
            except VerifyMismatchError:
                self.attempts[id_user] = self.attempts[id_user] + 1 if id_user in self.attempts else 1
                max_attempt = cur.execute("SELECT attempts FROM Users WHERE id = ?", (id_user,)).fetchone()[0]
                if self.attempts[id_user] >= max_attempt:
                    cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("DELETE FROM Users WHERE id = ?", (id_user,))
                    con.commit()
                    con.close()
                    return False, 'User was deleted!'
                if self.attempts[id_user] == max_attempt - 1:
                    con.close()
                    return False, 'Only one attempt remaining.'
                con.close()
                return False, 'Wrong password.'
            except Exception as er:
                self.attempts[id_user] = self.attempts[id_user] + 1 if id_user in self.attempts else 1
                max_attempt = cur.execute("SELECT attempts FROM Users WHERE id = ?", (id_user,)).fetchone()[0]
                if self.attempts[id_user] >= max_attempt:
                    cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("DELETE FROM Users WHERE id = ?", (id_user,))
                    con.commit()
                    con.close()
                    return False, 'User was deleted!'
                if self.attempts[id_user] == max_attempt - 1:
                    con.close()
                    return False, f'Only one attempt remaining! Unknown error: {er}.'
                con.close()
                return False, f'Unknown error: {er}'
        else:
            con.close()
            return False, 'This username does not exist.'

    def signup(self, user, password, max_attempt):
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        id_user = cur.execute("SELECT id FROM Users WHERE user = ?", (user,)).fetchone()[0]
        if not id_user:
            ph = PasswordHasher()
            hash_password = ph.hash(password)

            cur.execute("INSERT INTO Users (user, password, attempts) VALUES (?, ?, ?)", (user, hash_password, max_attempt))
            con.commit()
            self.userid = cur.execute("SELECT id FROM Users WHERE user = ?", (user,)).fetchone()[0]
            con.close()
            return True, ''
        else:
            con.close()
            return False, 'This username is already taken.'

    def addkey(self, algorithm, ktype, attempts, title, key, password, technical):
        con = sqlite3.connect(self.dbname)
        key = AesLibrary.encrypt(key=password, mes=key, enc='UTF-8', dec='Hex')
        current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        cur = con.cursor()
        titles = cur.execute("SELECT title FROM Keys").fetchall()
        if title in titles:
            con.close()
            return False, 'This title is already exists.'

        cur.execute("INSERT INTO Keys (user_id, algorithm, type, create_time, attempts, title, key, technical) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (self.userid, algorithm, ktype,
                                                        current_time, attempts, title, key, technical))
        con.close()
        return True, ''

    def set_settings(self, theme):
        con = sqlite3.connect(self.dbname)
        current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        cur = con.cursor()
        cur.execute("UPDATE Settings SET theme = ?, last_usage = ?", (theme, current_time))
        con.close()


class GetFromDataBase(DataBaseWork):
    def __init__(self):
        super().__init__()
        self.attempts = {}

    def get_key(self, title, password):
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        key = cur.execute("SELECT key FROM Keys WHERE user_id = ?, title = ?", (self.userid, title,)).fetchone()[0]
        if not key:
            con.close()
            return False, f'The key "{title}" does not exist.'

        key, istag = AesLibrary.decrypt(password, key)
        if not istag:
            self.attempts[title] = self.attempts[title] + 1 if title in self.attempts else 1
            max_attempts = cur.execute("SELECT attempts FROM Keys WHERE user_id = ?, title = ?", (self.userid, title)).fetchone()[0]
            if self.attempts[title] >= max_attempts:
                cur.execute("DELETE FROM Keys WHERE user_id = ?, title = ?", (self.userid, title))
                con.commit()
                con.close()
                return False, 'Key was deleted!'
            con.close()
            return False, key
        con.close()
        return True, key

    def get_theme(self):
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        theme = cur.execute("SELECT theme FROM Settings").fetchone()[0]
        con.close()
        return theme

    def get_last_usage(self):
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        last_usage = cur.execute("SELECT last_usage FROM Settings").fetchone()[0]
        con.close()
        return last_usage


db = DataBaseWork()
gdb = GetFromDataBase()