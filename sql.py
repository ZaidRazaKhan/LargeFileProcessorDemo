import mysql.connector
from mysql.connector import Error
from pyspark.sql import SparkSession
from pyspark import SparkContext
# import MySQLdb

spark = SparkSession.builder.appName("ProductRegistrar") \
            .config("spark.some.config.option", "some-value") \
                .getOrCreate()
# spark_context = SparkContext()

# try:
#     connection = mysql.connector.connect(host='localhost',
#                              database='ProductDatabase',
#                              user='zaid',
#                              password='algorithm', connection_timeout= 180)
    
#     if connection.is_connected():
#        db_Info = connection.get_server_info()
#        print("Connected to MySQL database... MySQL Server version on ",db_Info)

#        cursor = connection.cursor()
#        cursor.execute("SHOW TABLES;")
#        cursor.
#        for table in cursor:
#            print(table)
#     #    #global conneection timeout arguments
#     #    global_connect_timeout = 180
#     #    global_wait_timeout = 180
#     #    global_interactive_timeout = 180 

#     #    cursor.execute(global_connect_timeout)
#     #    cursor.execute(global_wait_timeout)
#     #    cursor.execute(global_interactive_timeout)
       
#        connection.commit()

# except Error as e :
#     print ("Error while connecting to MySQL", e)
# finally:
#     #closing database connection.
#     if(connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

def save_batch(batch):
    batch.foreach
def save_partition(partition):
    # connection_properties = broadcast_connection_parameter.value
    connection = mysql.connector.connect(host='localhost',\
        database='ProductDatabase', \
            user='zaid', \
                password='algorithm')
    # , connection_timeout= 180
    # , autocommit = True
    cursor = connection.cursor()
    db_batch_size = 10000
    sql_statement = """INSERT INTO ProductTable (name, sku, description) 
    VALUES ( %(name)s, %(sku)s, %(description)s ) 
    ON DUPLICATE KEY UPDATE
    name = VALUES(name), 
    description = VALUES(description) ;"""
    # sql_statement = """INSERT INTO ProductTable (name, sku, description) 
    # VALUES ( %(name)s, %(sku)s, %(description)s ) 
    # ON DUPLICATE KEY UPDATE
    # name = %(name)s, 
    # description = %(description)s ;"""
    data_to_insert = []
    i = 0
    for row in partition:
        try:
            data_to_insert.append({'name':row.name, 'sku' : row.sku, 'description' : row.description})
            # cursor.execute(sql_statement, (row.name, row.sku, row.description, row.name, row.description))
            # cursor.execute(sql_statement, {'name':row.name, 'sku' : row.sku, 'description' : row.description})
            i = i+1
            if i % db_batch_size == 0:
               cursor.executemany(sql_statement, data_to_insert)  
               data_to_insert.clear()
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
        # finally:
        #     print("kuch bhi")
        #     # data_to_insert.clear()
    if len(data_to_insert) > 0:
        cursor.executemany(sql_statement, data_to_insert)
    connection.commit()
    cursor.close()
    connection.close()


def update():
    spark_dataframe = spark.read.load("./products.csv", \
        format="csv",sep=",",lineSep="\r", engine="c", multiLine=True, \
             header = True)
    user = 'zaid'
    password = 'algorithm'
    jdbc_url = 'jdbc:mysql://localhost:3306/ProductDatabase'
    jdbc_driver = 'com.mysql.cj.jdbc.Driver'
    db_name = "ProductDatabase"
    # connection_properties = {"user": user, "password": password, \
    #     "jdbcUrl": jdbc_url, "jdbcDriver": jdbc_driver, "dbname": db_name}
    # broadcast_connection_parameter = spark_context.broadcast(connection_properties)
    spark_dataframe.coalesce(10).foreachPartition(save_partition)


update()


# jdbc_dataframe = spark.read.format('jdbc').option("url", "jdbc:mysql://localhost:3306/ProductDatabase").option("dbtable", "ProductTable").option("user", "zaid").option("password", "algorithm").load()
# print(jdbc_dataframe.groupBy("name").count().show(20))