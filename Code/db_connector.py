import mariadb
#https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/

class DB:
    _user = '#TODO'
    _password = '#TODO'
    _host = '#TODO'
    _port = '#TODO'
    _database = '#TODO'

    @classmethod
    def request(cls, statement, values):
        try:
            with mariadb.connect(cls._user,
                                 cls._password,
                                 cls._host, cls._port,
                                 cls._database) as conn, conn.cursor() as cursor:
                cursor.execute(statement, values)
                return cursor
        except mariadb.Error as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    DB.request('Hallo Welt!', (1,))

