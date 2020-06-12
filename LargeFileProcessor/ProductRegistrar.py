from ProductDao import ProductDao


class ProductRegistrar:
    def __init__(self, product_dao):
        self.product_table_dao = product_dao

    def register_product_table(self, spark_data_frame):
        self.product_table_dao.update_and_insert(spark_data_frame)


