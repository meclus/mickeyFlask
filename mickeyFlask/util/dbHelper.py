# -*- coding: utf-8 -*-
# dbHelper.py
"""
database util class
"""

import pymysql


class dbHelper(object):
    """db util helper class"""

    def __init__(self, conf):
        super(dbHelper, self).__init__()
        self.conf = conf

    def connect(self):
        '''
        create a db connect
        return: cursor
        '''
        conn = pymysql.connect(user=self.conf.username,
            password=self.conf.password,
            host=self.conf.host,
            port=self.conf.port,
            database=self.conf.database)
        cursor = conn.cursor()
        return dict(conn=conn, cursor=cursor)

    def close(self, connect):
        '''
        close db connect
        '''
        connect['cursor'].close()
        connect['conn'].close()

    def query(self, sql):
        '''
        execute sql script
        param sql: sql script
        return: tuple
        '''
        connect = self.connect()
        connect['cursor'].execute(sql)
        data = connect['cursor'].fetchall()
        self.close(connect)
        return data

    def exec(self, sql):
        '''
        execute sql script
        param sql: sql script
        return: tuple
        '''
        connect = self.connect()
        connect['cursor'].execute(sql)
        connect['conn'].commit()
        self.close(connect)

    def exec_sqls(self, sqls):
        connect = self.connect()
        for sql in sqls:
            connect['cursor'].execute(sql)
        connect['conn'].commit()
        self.close(connect)