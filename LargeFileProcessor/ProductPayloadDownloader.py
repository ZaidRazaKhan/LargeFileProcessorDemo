import gzip
import shutil
from google_drive_downloader import GoogleDriveDownloader as gdd
import sys

#File ID: '11ACp03VCQY5NElctMq7F5zn23jKrqTZI'


import config as database_config

class ProductPayloadDownloader:
    def __init__(self, data_id):
        self.data_id = data_id
    
    def extract(self, gz_file_path = './products.csv.gz', dest_file_path = './products.csv'):
        with gzip.open(gz_file_path, 'rb') as f_in:
            with open(dest_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return dest_file_path
    
    def fetch(self):
        gdd.download_file_from_google_drive(file_id=self.data_id, dest_path='./products.csv.gz')
        return self.extract()

