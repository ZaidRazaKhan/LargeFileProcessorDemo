from pyspark.sql import SparkSession
from ProductRegistrar import ProductRegistrar


class ProductDataIngestionManager:
    """
    This class is responsible for:
    1. Product Table ingestion
    2. Resilience such that if it fails in between it make sure that things remains consistent
    3. Aggregation Update
    """

    def __init__(self, product_registrar):
        self.spark_session = SparkSession.builder.appName("ProductRegistrar") \
            .getOrCreate()
            # .config("spark.some.config.option", "some-value") \
        self.product_registrar = product_registrar

    def ingest(self, file_path, file_format='csv', column_sep=',', line_delimiter='\r'):
        product_data_frame = self.spark_session.read \
            .load(file_path, format=file_format,
                  sep=column_sep, lineSep=line_delimiter,
                  engine='c', multiLine=True, header=True).withColumnRenamed('description\r', 'description')
        self.product_registrar.register_product_table(product_data_frame)

    def aggregation_update(self):
        pass
