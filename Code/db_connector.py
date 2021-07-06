import mariadb
import configparser


class config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("barbara.conf")
        self.user = config["server"]["user"]
        self.password = config["server"]["password"]
        self.host = config["server"]["host"]
        self.port = config["server"]["port"]
        self.database = config["server"]["database"]

    # def test(self):
    #     for i in ["user", "password", "host", "port", "database"]:
    #         if not config["server"][i]:
    #             # print("% not set", i)
    #             print("Config item is not set:", i)


class DB:
    _user = config.config.user
    _password = config.config.password
    _host = config.config.host
    _port = config.config.port
    _database = config.config.database

    @classmethod
    def request(cls, statement, values):
        try:
            with mariadb.connect(
                    cls._user,
                    cls._password,
                    cls._host, cls._port,
                    cls._database
            ) as conn, conn.cursor() as cursor:
                cursor.execute(statement, values)
                return cursor
        except mariadb.Error as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    DB.request('Hallo Welt!', (1,))


#https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/
