import logging
import pytest

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

def configure_loggers():
    logging.getLogger('py4j').setLevel(logging.INFO)
    logging.getLogger('pyspark').setLevel(logging.INFO)


@pytest.fixture(scope='session')
def sc(request):
    '''Retrieve the spark context'''
    conf = SparkConf() \
        .set("spark.driver.host", "localhost")\
        .setMaster("local[2]") \
        .setAppName("end-to-end-local-testing") \
        .set("spark.executorEnv.PYTHONHASHSEED", 0)

    sc = SparkContext(conf=conf)
    request.addfinalizer(lambda: sc.stop())
    configure_loggers()
    yield sc


@pytest.mark.usefixtures('sc')
@pytest.fixture(scope='session')
def spark(sc):
    yield SQLContext(sparkContext=sc)
