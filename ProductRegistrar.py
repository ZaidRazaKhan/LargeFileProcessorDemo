from ProductDao import ProductDao


class ProductRegistrar:
    def __init__(self, spark_data_frame):
        self.spark_data_frame = spark_data_frame
        self.product_table_dao = ProductDao()

    def register_product_table(self):
        self.product_table_dao.update_and_insert(self.spark_data_frame)


