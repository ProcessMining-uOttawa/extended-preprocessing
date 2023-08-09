# Get To Event Log

The `getToEventLog` function is designed to merge two DataFrames, adding a 'cluster' column to the original event log table based on matching case IDs of the results obtained from clustering. This function aids in enriching the event log data with cluster information for subsequent analysis or visualization.


## Purpose

The primary purpose of this function is to combine two DataFrames, adding a 'cluster' column from a secondary table to the original event log table. By matching case IDs, the function enables the incorporation of cluster information into the event log, providing a more comprehensive dataset for further analysis.


## Function Signature

```python
def getToEventLog(table1, table2):
```

## Arguments
- `table1` (pandas.DataFrame): The first DataFrame to be merged. It should include a column named 'case_id'. This table should be the event log table you have in which you want a cluster column appended.
- `table2` (pandas.DataFrame): The second DataFrame to be merged. It should include a column named 'case_id' and a column named 'cluster'. This table is the result after running **getCluster()**

## Return
The function returns a merged DataFrame, representing the original event log table enriched with the 'cluster' column.

## Example
```
event_log_export = get_to_event_log(event_log,df_cluster_results)

```

Output 

| case_id | event | timestamp | Cluster |
| --- | --- | --- | --- |
| 111 | Event 1 | 2022-01-04 | 0 |
| 111 | Event 2 | 2022-01-05 | 0 |
| 111 | Event 3 | 2022-01-06 | 0 |
| 222 | Event 1 | 2022-01-04 | 1 |
| 222 | Event 2 | 2022-01-20 | 1 |
| 222 | Event 3 | 2022-01-30 | 1 |






