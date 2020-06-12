import mysql.connector


class MySQLAccessor:
    def __init__(self, database_config):
        self.database_config = database_config

    
    def get_connection(self):
        return mysql.connector.connect(host=self.database_config.host,
                                    database=self.database_config.db_name,
                                    user=self.database_config.user,
                                    password=self.database_config.passoword)
