# Anonymizes the original Case IDs in an event log

The anonymizeCaseIDs function renumbers case IDs in a sequential manner. This function can be useful for preserving privacy when you wish to remove original case IDs that could lead to personally identifying someone. 

>Note: This function relies on three standard column names: case_id, event, and timestamp. You should invoke this function after initializing the dataframe using one of [readCSV()](./APIs/readCSV.md), [readExcel()](./APIs/readExcel.md) or [readPanda()](./APIs/readPanda.md). 

## Usage
``
anonymizeCaseIDs (DataFrame dataset)
``

## Arguments
- `dataset` is the pandas dataframe we want to anonymize.


## Return
Return a dataframe with anonymized case IDs rows.

## Example

```
data=anonymizeCaseIDs(dataset).
```

This will sort the DataFrame dataset by TimeStamp and “product_category”. An example can be seen below.


Table1 Original DataFrame

| case_id 	| timestamp           	| event                   	| city     	| client           	| product_category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| 300342     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 300343     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 300344     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 300345     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|


Table2 DataFrame sort by Case.ID and TimeStamp

| case_id 	| timestamp           	| event                   	| city     	| client           	| product_category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| 1    	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 2     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 3     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 4     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|