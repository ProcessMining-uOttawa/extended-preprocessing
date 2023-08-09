# Rename event classes/types in an event log

Often the names of events exported from a database are not user-friendly. Other times, we may wish to anonymize or obfuscate the event names to add a level of privacy. This function allows you to supply a dictionary of source event names and their replacements. 

>Note: This function relies on three standard column names: case_id, event, and timestamp. You should invoke this function after initializing the dataframe using one of [readCSV()](./APIs/readCSV.md), [readExcel()](./APIs/readExcel.md) or [readPanda()](./APIs/readPanda.md). 

## Usage
``
renameEventNames(DataFrame dataset,Dictionary replace_values)
``

## Arguments
- `dataset` is the pandas dataframe we want to anonymize.
- `replace_values` is the dictionary of source and replacement event names.


## Return
Return a dataframe with renamed event types.

## Example

```
replace_names = {
     'home.click' : 'Click Home Page',
       'cart.add' : 'Add to Cart',
     'order.conf' : 'Confirmation Order Page',
    'review.cart' : 'Review Shopping Cart'
}

data=renameEventNames(dataset,replace_names)
```


Table1 Original DataFrame

| case_id 	| timestamp           	| event                   	| city     	| client           	| product_category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| 1    | 08/01/2018 00/07/00 	| home.click        	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 2     	| 08/01/2018 00/07/03 	| cart.add            	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 3     	| 08/01/2018 00/07/02 	| order.conf 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 4     	| 08/01/2018 00/07/04 	| cart.review    	| Waterloo 	| Phone App        	| A                	| Apple   	|

Table2 DataFrame with replaced event names

| case_id 	| timestamp           	| event                   	| city     	| client           	| product_category 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| 1    | 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| A                	| Android 	|
| 2     	| 08/01/2018 00/07/03 	| Add to Cart             	| Ottawa   	| Computer Browser 	| N/A              	| Andriod 	|
| 3     	| 08/01/2018 00/07/02 	| Confirmation Order Page 	| Toronto  	| Phone App        	| B                	| Apple   	|
| 4     	| 08/01/2018 00/07/04 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| A                	| Apple   	|