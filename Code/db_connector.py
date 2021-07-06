import mariadb
# import mysql.connector
import configparser


class params:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("barbara.conf")

    def user(self):
        self.user = self.config["server"]["user"]

    def password(self):
        self.password = self.config["server"]["password"]

    def host(self):
        self.host = self.config["server"]["host"]

    def port(self):
        self.port = self.config["server"]["port"]

    def database(self):
        self.database = self.config["server"]["database"]

    # def test(self):
    #     for i in ["user", "password", "host", "port", "database"]:
    #         if not config["server"][i]:
    #             # print("% not set", i)
    #             print("Config item is not set:", i)


class DB:

    _user = params.user
    _password = params.password
    _host = params.host
    _port = params.port
    _database = params.database

    @classmethod
    def request(cls, statement, values):
        try:
            with mariadb.connect(
                    cls._user,
                    cls._password,
                    cls._host,
                    cls._port,
                    cls._database
            ) as conn, conn.cursor() as cursor:
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


if __name__ == "__main__":
    # test_connection()
    # DB.request('Hallo Welt!', (1,))
    DB.request("SELECT * FROM literature", (1,))
