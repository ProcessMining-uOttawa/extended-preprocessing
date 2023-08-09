# Get Cluster

The `getCluster` function performs K-means clustering on encoded trace logs, assigning cluster labels to each trace. The resulting cluster information is added as a new column in the DataFrame. This function is designed to enhance your event sequence data by clustering similar traces together for further analysis or visualization.

## Purpose

The primary purpose of this function is to apply K-means clustering to encoded trace logs, creating clusters of similar sequences of activities. The assigned cluster labels can later be used to filter and analyze data in Process Mining tools or other analysis environments.


## Function Signature

```python
def getCluster(df_cluster, distances_unique, unique_trace_logs, column_name, k_cluster):
```

## Arguments
-`df_cluster` (pandas.DataFrame): The DataFrame containing event sequence data to be clustered.
-`distances_unique` (numpy.ndarray): A 2D array of Levenshtein distances between unique trace logs.
-`unique_trace_logs` (pandas.Series): A pandas Series containing unique trace logs.
-`column_name` (str): The name of the column containing the encoded trace logs.
-`k_cluster` (int): The number of clusters to create.

## Return
The function returns a DataFrame with an additional cluster column containing cluster labels assigned to each trace.

## Example
```
clustered_data = getCluster(data_frame, distances_unique, unique_trace_logs, 'encoded_trace_log', k_cluster=3)

```
Output

| case_id| encode_trace_log | trace count | cluster |
| --- | --- | --- | --- |
| 111 | (1,2,4,3,5,6) | 20 | 0 |
| 112 | (1,2,3,4) | 5 | 1 |
| 113 | (1,2,2,2,2,3,4) | 1 | 2 | 
| 114 | (1,3,3,2,2,3,4) | 1 | 2 |
| 115 |(1,3,3,3,4) | 1 | 2 |





