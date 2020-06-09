from ProductRegistrar import ProductRegistrar
from ProductAggregator import ProductAggregator
from ProductDao import ProductDao


import config as database_config

def main():
    # connect(cfg.mysql["host"], cfg.mysql["user"], cfg.mysql["password"])
    product_registrar = ProductRegistrar()
    product_aggregator = ProductAggregator()
    data_frame = product_registrar.read_data_frame('./products.csv')
    print(data_frame.show(10))
    product_dao = ProductDao(database_config)
    try:
        product_dao.update({}, data_frame)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()