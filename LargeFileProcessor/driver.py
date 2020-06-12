from ProductRegistrar import ProductRegistrar
from pyspark.sql import SparkSession
from ProductDataIngestionManager import ProductDataIngestionManager
from ProductPayloadDownloader import ProductPayloadDownloader
import config as database_config
import sys

def main():
    print('Args received: '+ str(sys.argv))
    if len(sys.argv) != 3:
        raise Exception("Invalid arguments!!")
    print(sys.argv)
    data_base_ip = sys.argv[1]
    file_gdrive_id = sys.argv[2]
    database_config.mysql["host"] = data_base_ip
    file_path = ProductPayloadDownloader(file_gdrive_id).fetch()
    # # file_path = './products.csv'
    # product_data_ingestion_manager = ProductDataIngestionManager(file_path)
    # product_data_ingestion_manager.ingest()


if __name__ == "__main__":
    main()
