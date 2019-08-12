import sqlite3
import os

class FileLite:

    sql = '''\
        create table files (
        fileid integer primary key autoincrement,
        path text unique not null
        );
        '''

    def __init__(self, dbpath=None):
        if dbpath is None:
            self.conn = sqlite3.connect(":memory:")
        else:
            self.conn = sqlite3.connect(dbpath)
        self.conn.execute(self.sql)

    def max_id(self):
        _id, *_ = self.conn.execute('select max(fileid) from files').fetchone()
        if _id is None:
            _id = 0
        return _id

    def insert(self, path):
        cursor = self.conn.cursor()
        _id = self.max_id()
        fileid = _id + 1
        c = cursor.execute('insert into files (fileid, path) values (?,?)', (fileid, path))
        cursor.close()
        return c.arraysize

    def insertmany(self, files):
        cursor = self.conn.cursor()
        _id = self.max_id()
        data = []
        for index, file in enumerate(files, start=1):
            data.append((_id+index, file))
        c = cursor.executemany('insert into files (fileid, path) values (?,?)', data)
        cursor.close()
        return c.arraysize

def test():
    fl = FileLite()
    path = []
    for p, _, files in os.walk('F:'):
        for file in files:
            path.append(os.path.join(p, file))
    fl.insertmany(path)
    return fl
        
