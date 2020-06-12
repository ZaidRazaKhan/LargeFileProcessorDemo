from ProductRegistrar import ProductRegistrar
from pyspark.sql import SparkSession
from ProductDataIngestionManager import ProductDataIngestionManager


def main():
    # spark_session = SparkSession.builder.appName("ProductRegistrar") \
    #     .config("spark.some.config.option", "some-value") \
    #         .getOrCreate()
    file_path = './products.csv'
    product_data_ingestion_manager = ProductDataIngestionManager(file_path)
    product_data_ingestion_manager.ingest()
    # product_registrar = ProductRegistrar(spark_session)
    # product_registrar.read_data_frame('./products.csv')
    # data_frame = product_registrar.get_data_frame()
    #
    # print(data_frame.show(10))


if __name__ == "__main__":
    main()
