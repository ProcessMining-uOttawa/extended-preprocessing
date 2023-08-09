# getTimeframeCount (Count Occurence of event)

The `getTimeframeCount` function visualizes the frequency of occurrences of a specified event over different timeframes such as days, months, or years. By counting the number of times the event occurs within each period, this function offers a clear view of the event distribution over time.

## Usage
```python
getTimeframeCount(dataset, column_event, column_time, event_name, period_time)
```

## Arguments
- `dataset` (pd.DataFrame): The input dataset containing event information.
- `column_event` (str): The column name in the dataset that identifies events.
- `column_time` (str): The column name in the dataset that contains timestamps for each event.
- `event_name` (str): The specific event name for which occurrences are to be counted and visualized.
- `period_time` (str): The timeframe (e.g., 'year', 'month', 'day') over which the occurrences are to be grouped and counted.

## Return
Returns a plot showcasing the occurence of the specified event for the selected time period.

## Example
```
pm.get_timeframe_count(event_log,'event','timestamp','EventName','year')
```

