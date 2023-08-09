# Get Optimal Clustering Function


## Purpose

The `getOptimalClustering` function is designed to assist in determining the optimal number of clusters for K-means clustering based on Levenshtein distances between unique trace logs. This function aids in choosing an appropriate number of clusters for further analysis. It also computes the Levensthein distance between encoded sequence of activities. 



## Usage

```python
def getOptimalClustering(df, encoded_column_name):
```

## Arguments
- `df`(pandas.DataFrame): A DataFrame containing the data to be used for calculating Levenshtein distances and determining optimal clusters.
- `encoded_column_name` (str): The name of the column containing the encoded trace logs.


## Return
- `distances_unique` (numpy.ndarray): A 2D array representing the Levenshtein distances between unique trace logs.
- `unique_trace_logs` (pandas.Series): A pandas Series containing the unique trace logs.

## Note
You may want to remove traces that have a lot of repeated number of events, or set a maximum threshold for the number of repeated events. This may cause the cluster to behave weirdly since there's no sequence of activities that are similar. You can use the function **deleteConsecutiveRepeats()** to remove repeated events. 

## Example
```
distances_unique, unique_trace_logs = getOptimalClustering(data_frame, 'encoded_trace_log')

```
## Output

The following is the output graph that helps choose the desired number of clusters in the following plot. Ideally, you want to pick a number of clusters that creates a sharp angle. You can refer [here](https://www.analyticsvidhya.com/blog/2021/05/k-mean-getting-the-optimal-number-of-clusters/) for more information.


<p align="center">
  <img src="./Pics/KMean_Elbow.png" alt="Kmean Elbow Plot ">
</p>

