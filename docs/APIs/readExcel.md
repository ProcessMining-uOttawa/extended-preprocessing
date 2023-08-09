# Read an Excel file

The readExcel functions reads the xls(x) file into a Pandas DataFrame. And for subsequent use of the time filtering functions, we need to introduce the new_time column name in advance and transform it. This function reads the xls(x) file, standardizes the columns for case id, timestamp and event, and creates a new Column called ‘new _time’. For consistency, all column names are transformed to lowercase and special characters are removed.

>Note: all other supporting functions require you start by invoking [readCSV()](./APIs/readCSV.md), [readExcel()](./APIs/readExcel.md) or [readPanda()](./APIs/readPanda.md). This is so that the column names for case_id, event and timestamp are kept consistent throughout.

## Usage
``
readExcel (String filename, String case_id_col_name,String event_col_name,String timestamp_col_name,String format)
``

## Arguments
- `filename` is the name of the XLS(x) file we want to import.
- `case_id_col_name` is the name of the time column in the source XLS(x) file.
- `event_col_name` is the name of the event column in the source XLS(x) file.
- `timestamp_col_name` is the name of the timestamp column in the source XLS(x) file.
- `format` is the timestamp format used in the source XLS(x) file. If left blank, the default value is %d/%m/%Y %H:%M.

## Return
Returns a Pandas DataFrame. The case id, event and timestamp column names from the source file will be renamed and standardized to the following column names (respectively): case_id,event,timestamp

## Example
```
data=pm.readExcel('eventlog.csv','Case.ID','eventaction','Datetime',"%Y-%m-%d %H:%M:%S")
```
This will read the XLS(x) file under the current path to the Pandas dataframe which has been created called data. Table1 (below) is an example of a source dataset file. Table2 gives an example of the output from the readExcel function.

Table 1: An example of source dataset

| Case.ID 	| Datetime           	| eventaction             	| City     	| Client           	| Product_Category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 2022-12-13 23:59:00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 122     	| 2022-12-13 23:59:00 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 123     	| 2022-12-13 23:59:00 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 124     	| 2022-12-13 23:59:00 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|

Table 2: Pandas DataFrame after using readExcel () function

| case_id 	| timestamp           	| event                   	| city     	| client           	| product_category 	| device  	| new_time 	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|----------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	| ...      	|
| 121     	| 2022-12-13 23:59:00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	| 420      	|
| 122     	| 2022-12-13 23:59:00 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	| 422      	|
| 123     	| 2022-12-13 23:59:00 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	| 423      	|
| 124     	| 2022-12-13 23:59:00 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	| 424      	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|          	|