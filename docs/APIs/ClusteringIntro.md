# Event Sequence Clustering

The functions in the groups involves grouping similar event sequences together to identify patterns, trends, and insights from your data. Clustering can help you uncover hidden relationships in the order of activities performed within various processes. 

## Purpose

The primary purpose of event sequence clustering is to discover meaningful clusters of activities within event logs. By identifying these clusters, you can gain insights into different process variants, detect anomalies, and understand how activities are commonly organized.

## Sequential Execution of Functions

To achieve effective event sequence clustering, a series of functions need to be executed in a specific sequence. Each function contributes to different aspects of the clustering process, ultimately leading to meaningful results.

1. **`getEncodedTraceLog`**: This function encodes the event log data, preparing it for the clustering process. It can display tables, encode the data, and show the encoder details if needed.

2. **`get_optimal_clustering`**: After encoding the trace log, this function determines the optimal number of clusters for your data. It analyzes the encoded data to identify the most suitable number of clusters.

3. **`get_cluster`**: Once the optimal number of clusters is determined, this function performs the actual clustering using the chosen number of clusters. It uses distances and encoded data to group similar event sequences together.

4. **`get_to_event_log`**: After clustering, this function can help you visualize and interpret the results. It provides a way to transform the clustered data back into an understandable event log format.

These functions are discussed in further details in the files underneath.

Remember that executing these functions in the specified sequence is crucial to obtaining accurate and insightful results from your event sequence clustering process.
