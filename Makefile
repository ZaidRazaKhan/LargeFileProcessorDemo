build:
	docker pull mysql:latest
	ls
	cd ./LargeFileProcessor
	pwd
	docker build -t large-file-processor-image:1 ./LargeFileProcessor

clean:
	docker stop ProductDBServer
	docker rm ProductDBServer
	echo "Waiting for the DB server to be killed."
	sleep 30

setup:
	docker run --name=ProductDBServer --env="MYSQL_ROOT_PASSWORD=algorithm1" -p 33061:3306 -d mysql:latest
	echo "Please wait while the db server starts"
	sleep 30
	docker exec -it ProductDBServer mysql -uroot -palgorithm1 -e "CREATE USER 'zaid'@'%' IDENTIFIED BY 'algorithm';"
	docker exec -it ProductDBServer mysql -uroot -palgorithm1 -e "GRANT ALL PRIVILEGES ON *.* TO 'zaid'@'%';"
	docker exec -it ProductDBServer mysql -uroot -palgorithm1 -e "CREATE DATABASE ProductDatabase;"
	docker exec -it ProductDBServer mysql -uroot -palgorithm1 -e "CREATE TABLE IF NOT EXISTS ProductDatabase.ProductTable(name VARCHAR(255) NOT NULL, sku VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, PRIMARY KEY(sku));"
	docker exec -it ProductDBServer mysql -uroot -palgorithm1 -e "CREATE OR REPLACE VIEW ProductDatabase.ProductAggregate as select name, count(name) from ProductDatabase.ProductTable GROUP BY name;"

test:
	docker run -it  large-file-processor-image:1
	docker exec -it ProductDBServer mysql -uroot -palgorithm1 -e "select * from ProductDatabase.ProductTable;"
	docker exec -it ProductDBServer mysql -uroot -palgorithm1 -e "select * from ProductDatabase.ProductAggregate;"


