# Delete traces with insufficient duration

This function removes the traces that do not record for a duration time. 
> Note: this function will automatically sort the rows by id and timestamp.

## Usage
``
deleteTracesWithTimeLessSort (DataFrame dataset, Int time)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to save.
- `time` is the threshold of time duration between start event and end event, in seconds.

## Return
Return a dataframe containing only traces have a total duration greater than or equal to t.

## Example
```
data= deleteTracesWithTimeLessSort(dataset,300)
```

In this example, this function will drop all traces that were running with total duration less than 300 seconds.
