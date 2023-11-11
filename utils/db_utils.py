import cx_Oracle
from conf.setting import con_config


class OracleDb:
    Host = ''
    Port = ''
    User = ''
    Password = ''
    Servername = ''
    Sid = ''
    cursor = ''
    uri = ''
    connection = ''

    def __init__(self, db_config):
        self.Host = db_config.get('HOST')
        self.Port = db_config.get('PORT')
        self.Password = db_config.get('PASSWORD')
        self.User = db_config.get('USERNAME')
        self.Servername = db_config.get('SERVER_NAME')
        self.Sid = db_config.get('SID')

        if self.Servername:
            self.uri = '{}/{}@{}:{}/{}'.format(self.User, self.Password, self.Host, self.Password, self.Servername)
        elif self.Sid:
            self.uri = '{}/{}@{}:{}/{}'.format(self.User, self.Password, self.Host, self.Password, self.Sid)
        else:
            assert self.Servername or self.Sid
        self._connection()

    def __del__(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def _connection(self):
        self.connection = cx_Oracle.connect(self.uri)

    def get_cursor(self):
        if not self.cursor:
            self.cursor = self.connection.cursor()

    def insert_data(self, sql):
        self.get_cursor()
        print('=' * 50)
        self.cursor.excute(sql)
        print("执行sql语句成功", sql)
        self.connection.commit()


oracle_db = OracleDb(con_config)
