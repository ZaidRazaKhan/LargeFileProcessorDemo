from ProductRegistrar import ProductRegistrar
from ProductDataIngestionManager import ProductDataIngestionManager
from ProductPayloadDownloader import ProductPayloadDownloader
import config as database_config
import sys
from ProductDao import ProductDao
from MySQLAccessor import MySQLAccessor
from DatabaseConfig import DatabaseConfig

class ProductIngestionOrchestrator:
    def __init__(self, product_payload_downloader, product_data_ingestion_manager):
        self.product_data_ingestion_manager = product_data_ingestion_manager
        self.product_payload_downloader = product_payload_downloader

    def orchestrate_ingestion(self, file_gdrive_id):
        file_path = self.product_payload_downloader.fetch(file_gdrive_id)
        self.product_data_ingestion_manager.ingest(file_path)

