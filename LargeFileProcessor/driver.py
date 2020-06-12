from ProductRegistrar import ProductRegistrar
from ProductDataIngestionManager import ProductDataIngestionManager
from ProductPayloadDownloader import ProductPayloadDownloader
import config as database_config
import sys
from ProductDao import ProductDao
from MySQLAccessor import MySQLAccessor
from DatabaseConfig import DatabaseConfig
from ProductIngestionOrchestrator import ProductIngestionOrchestrator 


def get_my_sql_accessor(data_base_conf):
    return MySQLAccessor(database_conf)

def get_product_dao(my_sql_accessor):
    return ProductDao(my_sql_accessor)


def get_product_registrar(product_dao):
    return ProductRegistrar(product_dao)

def get_product_data_ingestor(product_registrar):
    return ProductDataIngestionManager(product_registrar)

def main():

    data_base_conf = DatabaseConfig(database_config.mysql["host"], \
        database_config.mysql["user"], database_config.mysql["password"], \
            database_config.mysql["db_name"])

    # Please insert your input accordingly accrding to your run
    data_base_conf.host = "172.17.0.2" # <Please enter the output of "docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ProductDBServer">
    file_gdrive_id = "11ACp03VCQY5NElctMq7F5zn23jKrqTZI" # <insert gdrive id here.>


    product_data_ingestion_manager = ProductDataIngestionManager(ProductRegistrar(ProductDao(MySQLAccessor(data_base_conf))))
    ProductIngestionOrchestrator(ProductPayloadDownloader(), product_data_ingestion_manager).orchestrate_ingestion(file_gdrive_id)


if __name__ == "__main__":
    main()
