# Aggregate/merge duplicated rows

This is the most import and complex function aggregates duplicated rows into one row. This function works by splitting data into groups. The groups have different case_id. People can specify the merge rules, such as keep first occurrence, calculate the mean, min, max from duplicated rows. This function is needed because we can merge duplicated rows according to our merge rules. <br>
The aggregation operations that can be applied on the different columns are:

- mean: computes the mean of the aggregated values.
- median: computes the median of the aggregated values.
- first: keeps the first occurrence value.
- last: keeps the last occurrence value.
- max: keeps the maximum value among the aggregated values.
- min: keeps the minimum value among the aggregated values.
- sum: calculates the sum of the aggregated values.
- any: logical function where any of the values is true.
- all: logical function where all the values are true.


## Usage
``
MergeSameEventRows (DataFrame dataset, Object conditions)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to manipulate.
- `conditions` is an object{key:value}. and it includes the merge rules.

## Return
Return a dataframe without duplicated rows.

## Example
```
data=MergeSameRows (data, {“City”: ”first”, “Time_duration”: “sum”, “Device: ”last”})
```

Table 1 Original Dataframe

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Time_duration 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| Ottawa   	| Computer Browser 	| 2                	| Android 	|
| 121     	| 08/01/2018 00/07/02 	| Click Home Page         	| Ottawa   	| Computer Browser 	| 2                	| Android 	|
| 121     	| 08/01/2018 00/07/02 	| Click Home Page         	| Ottawa   	| Computer Browser 	| 3                	| Android 	|
| 121     	| 08/01/2018 00/07/05 	| Click Home Page         	| Toronto 	| Computer Browser 	| 1                	| Apple 	|
| 122     	| 08/01/2018 00/07/06 	| Confirmation Order Page 	| Toronto  	| Phone App        	| 3                	| Apple   	|
| 121     	| 08/01/2018 00/07/09 	| Add to Cart             	| Ottawa   	| Computer Browser 	| 1              	| Andriod 	|
| 123     	| 08/01/2018 00/07/10 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| 2                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|

Table 2 Dataframe after applying MergeSameRows on 
Table 1.

| Case.ID 	| TimeStamp           	| event                   	| City     	| Client           	| Time_duration 	| Device  	|
|---------	|---------------------	|-------------------------	|----------	|------------------	|------------------	|---------	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
| 121     	| 08/01/2018 00/07/00 	| Click Home Page         	| `Ottawa`   	| Computer Browser 	| `8`                	| `Apple` 	|
| 122     	| 08/01/2018 00/07/06 	| Confirmation Order Page 	| Toronto  	| Phone App        	| 3                	| Apple   	|
| 121     	| 08/01/2018 00/07/09 	| Add to Cart             	| Ottawa   	| Computer Browser 	| 1              	| Andriod 	|
| 123     	| 08/01/2018 00/07/10 	| Review Shopping Cart    	| Waterloo 	| Phone App        	| 2                	| Apple   	|
| ...     	| ...                 	| ...                     	| ...      	| ...              	| ...              	| ...     	|
