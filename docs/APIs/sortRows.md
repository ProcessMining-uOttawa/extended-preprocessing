# Delete traces with low number of events

The ArrangeRows function sorts the rows by conditions. It could be multiple conditions.

## Usage
``
ArrangeRows (DataFrame dataset, List conditions)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to sort.
- `conditions` are lists of column names we want to sort by.


## Return
Return a dataframe with sorted rows.

## Example

```
data=ArrangeRows (dataset, [“case_id”,”TimeStamp”]).
```

This will sort the DataFrame dataset by TimeStamp and “product_category”. An example can be seen below.


Table1 Original DataFrame

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Product_Category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|

Table2 DataFrame sort by Case.ID and TimeStamp

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Product_Category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| `121`    	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| `121`     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|