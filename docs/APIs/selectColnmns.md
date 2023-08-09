# Select columns from a Pandas DataFrame

The selectColumns functions selects the list columns needed for analysis from the dataset. It won’t change the original DataFrame, it will return the selected columns.

## Usage
``
selectColumns (DataFrame dataName, List colName)
``

## Arguments
- `dataName` is the name of Pandas DataFrame we want to manipulate.
- `ColName` is the list of the columns’ name we want to select.

## Return
Return a DataFrame including only the selected columns.

## Example
```
data=selectColumns (dataset, [‘event’,’Case.ID’,’Timestamp’]).
```

This will select only ‘event’, ‘Case.ID’,’TimeStamp’ columns to DataFrame. Table5. Represents the output dataframe after applying selectColumns () function to Table1. It’s only kept 3 columns.

Table1 Original DataFrame

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Product_Category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|


Table 2 DataFrame after applying the selectColumns () function to Table1. 

| Case.ID 	| TimeStamp           	| event                   	|
|---------	|---------------------	|-------------------------	|
| ...     	| ...                 	| ...                     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	|
| ...     	| ...                 	| ...                     	|