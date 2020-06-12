import mysql.connector
import config as database_config

class ProductDao:
    def __init__(self, my_sql_accessor, batch_size=10000, number_of_partitions=10):
        self.my_sql_accessor = my_sql_accessor
        self.batch_size = batch_size
        self.number_of_partitions = number_of_partitions

    def get_upsert_sql_statement(self):
        return"""INSERT INTO ProductTable (name, sku, description) 
        VALUES ( %(name)s, %(sku)s, %(description)s ) 
        ON DUPLICATE KEY UPDATE
        name = VALUES(name), 
        description = VALUES(description) ;"""

    def update_and_insert(self, spark_data_frame):
        """
        Method to perform update and insert operation on product db
        # """
        spark_data_frame.coalesce(self.number_of_partitions).foreachPartition(self.save_partition)

    def save_partition(self, partition):
        connection = self.my_sql_accessor.get_connection()
        cursor = connection.cursor()
        sql_statement = self.get_upsert_sql_statement()
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
