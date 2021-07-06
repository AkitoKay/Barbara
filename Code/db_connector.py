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

    @classmethod
    def get_tes(cls):
        data = [('1', 'Harry Potter and the Half-Blood Prince (Harry Potter  #6)',
                 'J.K. Rowling-Mary GrandPré', 'Harding Alvin W.', '2011-10-23', '1'),
                ('13', "The Ultimate Hitchhiker's Guide (Hitchhiker's Guide to the Galaxy #1-5)",
                 'Douglas Adams', 'Kline Abraham W.', '1995-07-27', '1'),
                ('14', 'A Short History of Nearly Everything', 'Bill Bryson-William Roberts', 'Mason Ian C.',
                 '1978-02-04', '1')]
        return data


if __name__ == '__main__':
    DB.request('Hallo Welt!', (1,))

