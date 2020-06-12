from ProductDataIngestionManager import ProductDataIngestionManager


def main():
    file_path = './products.csv'
    product_data_ingestion_manager = ProductDataIngestionManager(file_path)
    product_data_ingestion_manager.ingest()


if __name__ == "__main__":
    main()
