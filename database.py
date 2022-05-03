import psycopg2


class PgsqlConnect:
    """数据库操作"""

    def __init__(self, dbname, user, passwd, host, port):

        self.dbname = dbname
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.passwd, host=self.host,
                                     port=self.port)

        self.cursor = self.conn.cursor()

    def pgsql_execute(self, sql):

        self.cursor.execute(sql)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

