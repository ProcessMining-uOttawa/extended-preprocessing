# Encode Trace Logs

This function, `getEncodedTraceLog`, is designed to perform event sequence clustering. It will encode each event names and will output a table containing the case ID and the sequence of each event. 

## Purpose

The purpose of this function is to facilitate event sequence clustering and analysis by generating encoded trace logs for each case ID, clustering events based on case ID, and calculating the frequency of unique event traces.

## Function Signature

```python
def getEncodedTraceLog(dataset, show_tables=False, number_rows_display=10, display_encoder=False, Title_size=14):
```

## Arguments
- `dataset` (pandas.DataFrame): A DataFrame containing the event log data with columns "case_id" and "event".
- `show_tables` (bool): A boolean value indicating whether to display the results as tables.
- `number_rows_display` (int): The number of rows to display in the output tables.
- `display_encoder` (bool): A boolean value indicating whether to display the encoder values.
- `Title_size` (int): The font size of the table captions.

## Return
This function returns two pandas DataFrames:

`df_group_traces`: A DataFrame containing the frequency of unique event traces.

`df_cluster_results`: A DataFrame containing the count of case IDs for each unique trace.

## Example
```
df_group_traces, df_cluster_results = getEncodedTraceLog(event_log_data, show_tables=True, number_rows_display=10, display_encoder=False, Title_size=16)

```
Total Count by Trace Log

| trace_log | trace_count |
| --- | --- |
| (1,2,4,3,5,6) | 20 | 
| (1,4,2,3,6,4) | 13 | 
| (1,2,3,4) | 5 | 

Total Count Case Id Trace Log Occures

| case_id | encoded_trace_log | trace_count |
| --- | --- | --- |
| 1234 | (1,4,2,3,6,4) | 13 |
| 1235 | (1,2,4,3,5,6) | 20 |
| 1236 | (1,2,3,4) | 5 |




