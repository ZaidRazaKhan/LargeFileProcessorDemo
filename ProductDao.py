#!/usr/bin/env python
from pyspark.sql import SparkSession
from pyspark import SparkContext


import config as database_config

# connect(cfg.mysql["host"], cfg.mysql["user"], cfg.mysql["password"])
class ProductDao():
    def __init__(self, config):
        print('DataManupilotor object is created')
        self.spark = SparkSession.builder.appName("ProductRegistrar") \
            .config("spark.some.config.option", "some-value") \
                .getOrCreate()
        self.config = config
        self.jdbc_dataframe = self.spark.read.format('jdbc') \
            .option("url", "jdbc:mysql://localhost:3306/ProductDatabase") \
                .option("dbtable", "ProductDatabase.ProductTable") \
                    .option("user", "zaid") \
                        .option("password", "algorithm")
        
    

    def update(self, config, spark_dataframe , partition_size = 10, batch_size = 100):
        '''
        Method to perform upsert operation
        '''
        raise Exception("Yet to be implemented!!")
        spark_dataframe = self.spark.read.load("./products.csv", \
        format="csv",sep=",",lineSep="\r", engine="c", multiLine=True, \
             header = True)
        user = 'zaid'
        password = 'algorithm'
        jdbc_url = 'jdbc:mysql://localhost:3306/ProductDatabase'
        jdbc_driver = 'com.mysql.cj.jdbc.Driver'
        db_name = "ProductDatabase"
        spark_context = SparkContext()
        connection_properties = {"user": user, "password": password, \
            "jdbcUrl": jdbc_url, "jdbcDriver": jdbc_driver, "dbname": db_name}
        broadcast_connection_parameter = spark_context.broadcast(connection_properties)
        
        