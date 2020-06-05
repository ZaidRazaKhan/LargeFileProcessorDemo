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
* [Zaid Khan](http://tooschoolforcool.xyz/) ([@ZaidRazaKhan](https://github.com/ZaidRazaKhan))
