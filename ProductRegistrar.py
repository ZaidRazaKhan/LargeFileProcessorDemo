from pyspark.sql import SparkSession


class ProductRegistrar():
    def __init__(self):
        self.spark = SparkSession.builder.appName("ProductRegistrar") \
            .config("spark.some.config.option", "some-value") \
                .getOrCreate()
        print("Product Registrar is created")


    def read_data_frame(self, file_path, file_format = 'csv', column_seperator = ',', line_delimeter = '\r'):
        '''
        Takes file_path and return a dataframe
        '''
        product_dataframe = self.spark.read \
            .load(file_path, format=file_format, \
                sep = column_seperator, lineSep = line_delimeter, \
                    engine = 'c', multiLine = True, header = True)
        return product_dataframe
