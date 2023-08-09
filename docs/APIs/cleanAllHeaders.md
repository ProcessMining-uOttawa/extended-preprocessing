# Clean all headers in DataFrame

The cleanOneHeader functions cleans all the columns from DataFrame. It only keeps lower case letters, numbers, and underscores. The special characters are replaced by ‘_’.

## Usage
``
cleanAllHeaders (DataFrame dataName)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to clean.

## Return
Return a dataframe with clean header names.

## Example
```
dataset=cleanAllHeaders(dataset)
```

Table1 Original DataFrame

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Product_Category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|

Table2 DataFrame after applying cleanAllHeaders() function to Table1.

| `case_id` 	| `timeStamp`          	| event                   	| `city`     	| `client`           	| `product_category` 	| `device`  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 122     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 121     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 123     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|