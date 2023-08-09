# Delete traces with insufficient duration

This function removes the traces that do not record for a duration time. 
>Please be noticed this function will automatically sort the rows by id and time.

## Usage
``
concatenateColumns (DataFrame dataset, String newColName, …String colName, String separator)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to save.
- `newColName` is the new column name which is for concatenation of the columns.
- `...colName` is the multiple column names we want to merge.
- `Separaor` is the delimiter between two columns.

## Return
Return a new dataframe with new concatenated column added.

## Example
```
data= concatenateColumns(dataset,”event_city”,”event”,”City”,”-”)
```

In this example, this function will merge “City”, “event” columns to a new colnmn called “event_City”. 

Table 1: Original DataFrame

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Product_Category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|

Table 2: DataFrame after applying example script on Table 1

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Product_Category 	| Device  	| `event_City`             |
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	| ---------------------  |
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	| ...                    |
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	| Click Home Page-Ottawa |
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	| Confirmation Order Page-Toronto|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	| Add to Cart            |
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	| Review Shopping Cart-Waterloo |
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	| ...                    |