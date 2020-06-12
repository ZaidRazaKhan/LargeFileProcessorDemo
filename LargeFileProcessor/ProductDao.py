import mysql.connector
import config as database_config




def get_upsert_sql_statement():
    return"""INSERT INTO ProductTable (name, sku, description) 
    VALUES ( %(name)s, %(sku)s, %(description)s ) 
    ON DUPLICATE KEY UPDATE
    name = VALUES(name), 
    description = VALUES(description) ;"""


class ProductDao:
    def __init__(self, batch_size=10000, number_of_partitions=10):
        self.batch_size = batch_size
        self.number_of_partitions = number_of_partitions
        self.host=database_config.mysql["host"]
        self.database=database_config.mysql["db_name"]
        self.user=database_config.mysql["user"]
        self.password=database_config.mysql["password"]

    def get_connection(self):
        return mysql.connector.connect(host=self.host,
                                    database=self.database,
                                    user=self.user,
                                    password=self.password)

    def update_and_insert(self, spark_data_frame):
        """
        Method to perform update and insert operation on product db
        # """
        a = spark_data_frame.coalesce(self.number_of_partitions)
        print(a.rdd.getNumPartitions())
        a.show()
        a.foreachPartition(self.save_partition)

    def save_partition(self, partition):
        print(partition)
        connection = self.get_connection()
        cursor = connection.cursor()
        sql_statement = get_upsert_sql_statement()
        data_to_insert = []
        i = 0
        for row in partition:
            try:
                data_to_insert.append({'name': row.name, 'sku': row.sku, 'description': row.description})
                i = i + 1
                if i % self.batch_size == 0:
                    cursor.executemany(sql_statement, data_to_insert)
                    data_to_insert.clear()
            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
        if len(data_to_insert) > 0:
            cursor.executemany(sql_statement, data_to_insert)
        connection.commit()
        cursor.close()
        connection.close()
