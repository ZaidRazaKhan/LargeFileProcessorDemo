#!/usr/bin/env python
import preprocessing

mysql = {
    "jdbc_url" : "jdbc:mysql://localhost:3306/ProductDatabase",
    "jdbc_driver" : "com.mysql.cj.jdbc.Driver",
    "host": "localhost",
    "user": "zaid",
    "passwd": "algorithm",
    "db_name": "ProductDatabase",
}
# preprocessing_queue = [
#     preprocessing.scale_and_center,
#     preprocessing.dot_reduction,
#     preprocessing.connect_lines,
# ]
use_anonymous = True