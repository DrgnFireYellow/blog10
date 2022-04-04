import sqlite3
import os
import rich
def run():
    try:
        os.makedirs(f"{os.getcwd()}/build/")
    except FileExistsError:
        pass
    try:
        open(f'{os.getcwd()}/build/db.sqlite3')
    except FileNotFoundError:
        rich.print('[yellow]Building Database...[/yellow]')
        dbfile = open(f"{os.getcwd()}/build/db.sqlite3", mode='x')
        dbfile.write('')
        dbfile.close()
        con = sqlite3.connect(f'{os.getcwd()}/build/db.sqlite3')
        cur = con.cursor()
        cur.execute(f'''CREATE TABLE posts(id integer NOT NULL, date TIMESTAMP, name text)''')
        con.commit()
        con.close()
    return None