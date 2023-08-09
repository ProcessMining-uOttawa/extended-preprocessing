# Delete Consecutive Repeats of Events

The `deleteConsecutiveRepeats` function is designed to filter a DataFrame based on whether a list in a specific column has more than a specified number of consecutive repeated elements. This function can help in removing rows that exhibit excessive repetition patterns in the specified column. 

## Purpose

The main purpose of this function is to facilitate the removal of rows from a DataFrame that have lists in a specific column with an excessive number of consecutive repeated elements. This filtering process can aid in data cleaning and analysis by eliminating rows that do not meet certain repetition criteria. It is to note that using this function can improve the results of the clustering. Also, it takes the encoded activities as an input. Hence, the following function **getEncodedTraceLog()** should be run before this one. 


## Function Signature

```python
def deleteConsecutiveRepeats(df: pd.DataFrame, column_name: str, max_repeats: int) -> pd.DataFrame:
```

## Arguments
- `df` (pandas.DataFrame): The DataFrame to be filtered.
- `column_name` (str): The name of the column in which the lists are present.
- `max_repeats` (int): The maximum number of consecutive repeated elements to allow.

## Return
The function returns a filtered DataFrame, excluding rows that meet the specified repetition criteria.

## Example
```
filtered_data = deleteConsecutiveRepeats(input_data, 'list_column', max_repeats=3)
```
Before 

| case_id| encode_trace_log | trace count |
| --- | --- | --- |
| 111 | (1,2,4,3,5,6) | 20 | 
| 112 | (1,2,3,4) | 5 | 
| 113 | (1,2,2,2,2,3,4) | 1 | 
| 114 | (1,3,3,2,2,3,4) | 1 | 
| 115 |(1,3,3,3,4) | 1 | 

After

| case_id| encode_trace_log | trace count |
| --- | --- | --- |
| 111 | (1,2,4,3,5,6) | 20 | 
| 112 | (1,2,3,4) | 5 | 
| 114 | (1,3,3,2,2,3,4) | 1 | 
| 115 |(1,3,3,3,4) | 1 | 






