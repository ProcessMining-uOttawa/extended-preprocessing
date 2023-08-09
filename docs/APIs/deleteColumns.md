#  Delete columns from a DataFrame

The deleteColumns functions delete the list columns which is no needed for analysis from the dataset. It will change the original DataFrame, it will return the remaining columns after selected columns has deleted.

## Usage
``
deleteColumns (DataFrame dataName, List colName)
``

## Arguments
- `dataName` is the name of Pandas DataFrame we want to manipulate.
- `colName` is the list of the columns to drop from the dataset.


## Return
Return a dataframe except the columns that are selected to be dropped.

## Example
```
data=deleteColumns (dataset, [‘City’,’Client’,’Product_Category’,''Device]).
```
Table 1: Original DataFrame

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Product_Category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|

Table 2 DataFrame after applying the deleteColumns () function to Table1. 

| Case.ID 	| TimeStamp           	| event                   	|
|---------	|---------------------	|-------------------------	|
| ...     	| ...                 	| ...                     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	|
| ...     	| ...                 	| ...                     	|