# Group Similar Event Names

This function is designed to cluster similar event names within a given dataset. It employs Word2Vec embeddings and the DBSCAN clustering algorithm to group events based on their semantic similarities.

## Usage
``
getSimilarEvent(dataset, event_column_name, eps, min_samples)
``

## Arguments
- `dataset` (pd.DataFrame): The input dataset containing event information.
- `event_column_name` (str): The name of the column in the dataset that holds event descriptions.
- `eps` (float): The maximum distance between event vectors for them to be considered in the same cluster. Needs to be tuned 
- `min_samples` (int): The minimum number of events required to form a cluster.


## Return
Returns a DataFrame with clustered similar events.

## Example
```
clustered_events = getSimilarEvent(dataframe, 'event', eps=0.5, min_samples=3)
```

| cluster_0 | cluster_1 | cluster_2 |
| --- | --- | --- |
| Qpers Under Review | Goc Secret For Review | Adverse Qpers Letter Ready |
| Pv Qpers Under Review | Goc Secret For Approval | Adverse Qpers Letter Sent |
| Sibs Under Review | Police For Review | Adverse Qpers Letter To Edit |
