import sqlite3
from config import config


def connector(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(config.dbase)
        conn.execute('''PRAGMA foreign_keys = on''')
        try:
            res = func(conn, *args, **kwargs)
        except KeyboardInterrupt:
            conn.rollback()
        else:
            conn.commit()
            return res
        finally:
            conn.close()
    return wrapper


@connector
def create_db(conn):
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS USERS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME            TEXT,
        EMAIL           TEXT UNIQUE,
        PASSWORD        TEXT);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS THEMES
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER            INTEGER,
        NAME            TEXT,
        FOREIGN KEY (USER) REFERENCES USERS(ID));''')

    cur.execute('''CREATE TABLE IF NOT EXISTS RESOURCES
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TYPE           TEXT    NOT NULL,
        PATH           TEXT    NOT NULL,
        DESCRIPTION    TEXT,
        THEME          INTEGER,
        SOURCE         TEXT,
        DATE           TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (THEME) REFERENCES THEMES(ID));''')
         
    cur.execute('''CREATE TABLE IF NOT EXISTS TAGS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME            TEXT);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS RECORDS
        (RESOURCE INTEGER,
        TAG       INTEGER,
        FOREIGN KEY (RESOURCE) REFERENCES RESOURCES(ID) ON DELETE CASCADE,
        FOREIGN KEY (TAG) REFERENCES TAGS(ID));''')

    cur.execute('''CREATE TABLE IF NOT EXISTS ACTIVE_USER
        (id INTEGER PRIMARY KEY CHECK (id = 1),
        USER INTEGER,
        FOREIGN KEY (USER) REFERENCES USERS(ID));''')

    cur.execute('''INSERT OR IGNORE INTO USERS (ID, NAME, EMAIL, PASSWORD) VALUES (0, NULL, NULL, NULL)''')

    cur.execute('''INSERT OR IGNORE INTO ACTIVE_USER (id, USER) VALUES (1, 0)''')


@connector
def get_active_user(conn):
    cur = conn.cursor()
    cur.execute('''SELECT USER FROM ACTIVE_USER''')
    user = cur.fetchone()
    return user[0]


@connector
def set_active_user(conn, user):
    cur = conn.cursor()
    cur.execute(f'''UPDATE ACTIVE_USER SET USER = {user} WHERE id = 1''')


@connector
def match_user(conn, email, password):
    cur = conn.cursor()
    cur.execute('''SELECT ID FROM USERS WHERE EMAIL = ? and PASSWORD = ?''', (email, password))
    user = cur.fetchone()
    if not user:
        return 0
    return user[0]


@connector
def add_user(conn, name, email, password):
    cur = conn.cursor()
    cur.execute('''INSERT INTO USERS (NAME, EMAIL, PASSWORD) VALUES (?, ?, ?)''', (name, email, password))
    cur.execute('''SELECT seq FROM sqlite_sequence WHERE name = "USERS"''')
    last = cur.fetchone()
    cur.execute('''INSERT OR IGNORE INTO THEMES (USER, NAME) VALUES (?, ?)''', (last[0], "Без темы"))
    return last[0]


@connector
def add_resource(conn, tpe, path, description, theme, source = 0):
    cur = conn.cursor()
    cur.execute('''INSERT INTO RESOURCES (TYPE, PATH, DESCRIPTION, THEME, SOURCE) VALUES (?, ?, ?, ?, ?)''', (tpe, path, description, theme, source))
    cur.execute('''SELECT seq FROM sqlite_sequence WHERE name = "RESOURCES"''')
    last = cur.fetchone()
    return last[0]


@connector
def add_theme(conn, user, name):
    cur = conn.cursor()
    cur.execute('''INSERT INTO THEMES (USER, NAME) VALUES (?)''', (user, name))
    cur.execute('''SELECT seq FROM sqlite_sequence WHERE name = "THEMES"''')
    last = cur.fetchone()
    return last[0]


@connector
def add_tag(conn, name):
    cur = conn.cursor()
    cur.execute('''INSERT INTO TAGS (NAME) VALUES (?)''', (name, ))
    cur.execute('''SELECT seq FROM sqlite_sequence WHERE name = "TAGS"''')
    last = cur.fetchone()
    return last[0]


@connector
def add_record(conn, tpe, path, description, theme, source = 0, tags = None):
    if tags is None:
        tags = []
    resource_id = add_resource(tpe, path, description, theme, source)
    cur = conn.cursor()
    for tag in tags:
        tag_id = cur.execute('''SELECT ID FROM TAGS WHERE NAME = (?)''', (tag, )).fetchone()
        if tag_id is None:
            tag_id = add_tag(tag)
        else:
            tag_id = tag_id[0]
        cur.execute('''INSERT INTO RECORDS (RESOURCE, TAG) VALUES (?, ?)''', (resource_id, tag_id))
        conn.commit()


@connector
def delete_record(conn, table, row_id):
    cur = conn.cursor()
    cur.execute(f'''DELETE FROM {table} WHERE ID = {row_id}''')


@connector
def load_table(conn, table):
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM {table}''')
    rows = cur.fetchall()
    return rows

@connector
def load_row(conn, res_id):
    cur = conn.cursor()
    cur.execute(f'''SELECT S.TYPE, S.PATH, S.DESCRIPTION, T.NAME, S.SOURCE, S.DATE FROM RESOURCES S 
        JOIN THEMES T ON S.THEME = T.ID WHERE S.ID = {res_id}''')
    row = cur.fetchall()
    return row[0]


@connector
def load_user_records(conn, user):
    cur = conn.cursor()
    rows = load_user_themes(user)
    if not rows:
        return []
    themes = tuple(theme[0] for theme in rows)
    if len(rows) == 1:
        cur.execute(f'''SELECT ID FROM RESOURCES WHERE THEME = {themes[0]}''')
    else:
        cur.execute(f'''SELECT ID FROM RESOURCES WHERE THEME IN {themes}''')
    records = cur.fetchall()
    return records

@connector
def load_user_themes(conn, user):
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM THEMES WHERE USER = {user}''')
    themes = cur.fetchall()
    return themes

@connector
def load_tags(conn, res_id):
    cur = conn.cursor()
    cur.execute(f'''SELECT C.TAG, T.NAME FROM RECORDS C JOIN TAGS T ON C.TAG = T.ID WHERE C.RESOURCE = {res_id}''')
    tags = cur.fetchall()
    return tags


#config.set_user(1)
create_db()
#add_record("link2", "path2", "description2", 0, "source2", ["c", "python", "sql"])
