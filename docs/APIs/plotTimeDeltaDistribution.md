# Plot Time Delta Distribution

This function is designed to visualize the distribution of a timedelta column from a given dataset. The distribution can be represented in days, seconds, or months. Additionally, the function has the capability to filter out and visualize the effects of removing outliers.

## Usage
```python
plot_timedelta_distribution(df, time_delta_col, unit, n_bins, event_log, mark_outliers=False)

```

## Arguments
- `df` (pd.DataFrame): The input dataset containing the timedelta column.
- `time_delta_col` (str): Name of the column containing the timedelta values.
- `unit` (str): Time unit for plotting. Can be 'days', 'seconds', or 'months'.
- `n_bins` (int): Number of bins for the histogram.
- `event_log` (pd.DataFrame): Event log DataFrame, used when marking outliers.
- `mark_outliers` (bool, optional): Flag to determine if outliers should be marked in the original event log. Default is False.

## Return
If `mark_outliers` is True:

Returns a tuple containing:
1) DataFrame with removed outliers.
2) Case IDs of removed outliers.
3) Updated original event log with an outlier column.
If mark_outliers is False:

If `mark_outliers` is False:

Returns a tuple containing:
1) DataFrame with removed outliers.
2) Case IDs of removed outliers.
## Example
```
df_filtered, case_ids_removed, event_log_filtered = pm.plot_timedelta_distribution(df_duration,'time_delta', 'days', 10, event_log, True)
```

```
filtered_df, removed_ids = plot_timedelta_distribution(dataframe, 'time_column', 'days', 50, event_log_dataframe, mark_outliers=False)
```

## Output

<p align="center">
  <img src="./Pics/GetTraceDurationOutput.png" alt="Output of Plot Time Delta Distribution ">
</p>


Output Table


| case_id | event | timestamp | outlier |
| --- | --- | --- | --- |
| 111 | Event 1 | 2022-01-04 | yes |
| 111 | Event 2 | 2022-01-05 | yes |
| 111 | Event 3 | 2022-01-06 | yes |
| 222 | Event 1 | 2022-01-04 | no |
| 222 | Event 2 | 2022-01-20 | no |
| 222 | Event 3 | 2022-01-30 | no |

## Note

The case id are deemed outliers based on the total processing time of a case_id. Hence, it may be beneficial to remove unfinished cases before using this function. Also, this function assumes a normal distribution for the processing time. If the distribution of time accros all case id is binomial or something similar the distinction for outliers may not work as well. 