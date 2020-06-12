How to run
go to the Main directory
run : 
    make build; 
    make clean; 
    make setup; 
        You will have to change the ip and gdrive id in the test of the Driver.py file line #14-#15
        You can get it by running below command in the terminal :
        docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ProductDBServer
Now run :
    docker run -it  large-file-processor-image:1 ; 
    make test;


Over all structure
Note : This just gives a rough representation of my thought process and will be helpful in understanding the overall thing. However it will map broadly with the code but may not map exactly.

Current Architecture and Implementation
System level Components
A. There is a mysql DB server backed by docker which hosts the ProductDatabase, having a mysql table ProductTable and a mysql view ProductAggregation which is an aggregation over ProductTable on the Names column.
B. There is another component, LargeFileProcessor which is currently vended as a docker which spins up every time we have a product data file to be ingested.
C. There is a MakeFile demo script which has targets to :
1. Spin up mysql db docker.
2. Create the users, grant permissions, create Product data base , ProductTable inside it and a ProductAggregation view on top of it.
3. Spin up LargeFileProcessor, which takes the Product csv file as an input and processes it.
4. Prints the state of the ProductTable and ProductAggregation for testing.

Actors
LargeFileProcessor can have 3 components :
1. Product data registrar : takes a spark data frame and processes it into the
2. Product Data ingestion manager : reads the file into spark data frame, provides decoupling for registrar so that it can be used with any source without any change in it.
2. Product data aggregator and its manager : is vestigial as of now because the mysql view is already handling it in this implementation.
3. Driver : An orchestrator wrapping these. Gets the call, downloads the csv file and initialized the components and orchestrates the ingestion flows.

Use cases
1. Files can be parallelly ingested.
2. LargeFileProcessor is only dependednt on the ip of the DBServer, so it is totally decoupled with the DB implementaton, for scaling master slave can be done on DB Server without any changes on the LargeFileProcessor.
3. LargeFileProcessor takes ulr of the zipped csv file.

Flow
1. Driver receives the data base ip and uses it to ini`
1. Driver initializes the DB accessing, Product Registrar, Product Data ingestion manager etc.
2. Calls the

Future use cases / Improvements
1. Handling fault tolerance where the LargeFileProcessor goes down in between the ingestion, introduce idempotence and retry mechanism to handle it.
2. Running LargeFileProcessor backed by swarm or Kubernetes having an upper cap as DB will be a bottle neck.
3. ProductAggregate is backed by mysql, but with data increasing, we will have to move it to big data or other solutions.
4. Purging the Product table and respective update of the Aggregation table.
5. Handling partial failures of Product Ingestion flow, Product Aggregation Flow etc.
6. Exhaustive validation and checks.

PS : Due to the time constraints it did not made much sense to implement the above mentioned ones into the MVP, however I do have the full solution for the above mentioned points.





<!-- ### Please ignore below




# LargeFileProcessor
A system which would be able to handle long-running processes in a distributed fashion

# Problem Statement
We need to be able to import products from a CSV file and into a database. There are half a million products to be imported into the database. You can find the CSV file [here](https://drive.google.com/drive/folders/1X3qomdbjWU1oOTbBvxchTzjLMAwYBWFT) in a compressed format Large File processing - Assignment. 
Sample rows
| Name  | Sku | Description |
| ------------- | ------------- | ------------- |
| Bryce Jones  | lay-raise-best-end  | Art community floor adult your single type  |
| John Robinson  | cup-return-guess  | Produce successful hot tree past action young  |

After importing the data, we would like to run an aggregate query to give us no. of products with the same name.

## Points to achieve
* The code should follow concept of OOPS
* Support for regular non-blocking parallel ingestion of the given file into a table. Consider thinking about the scale of what should happen if the file is to be processed in 2 mins.
* Support for updating existing products in the table based on `sku` as the primary key. 
* All 500k rows to be inserted into a single table
* An aggregated table on above rows with `name` and `no. of products` as the columns


## Notes
* You can choose programming language and framework of your choice
* You can choose a database of your preference
* You can use any design pattern you prefer to solve the above problems

## Getting Started

### Introduction 

### Steps to run code
Will be updated later!!

### Schemas and details for table generation
Will be updated later!!

### Points achieved
* None

### Future Improvements
Implementation of the above problem statement


### Installation
* Clone this repository
```bash
git clone https://github.com/ZaidRazaKhan/LargeFileProcessor.git
cd LargeFileProcessor
```
* Install the requirements (not checked)
```bash
Language dependent
```
### Download data csv
```bash
python download_dummy_csv_data.py
```

## Conclusion
Project Just got initiated!!

## Author
* [Zaid Khan](http://tooschoolforcool.xyz/) ([@ZaidRazaKhan](https://github.com/ZaidRazaKhan)) -->
