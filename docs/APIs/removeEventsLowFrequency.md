# Remove events with low frequency from dataset

The removeEventsLowFrequency functions removes the events from DataFrame whose frequency is lower than the frequency provided.

## Usage
``
removeEventsLowFrequency (DataFrame dataName, Int frequency, List/String exceptions)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to manipulate.
- `frequency` is the threshold value that is used to filter out rows whose count is less than threshold.
- `exceptions` (optional) is a string or list of events that you do not want to be removed (even if they are below the threshold specified in the frequency parameter).

## Return
Return a dataframe containing only events whose frequency is larger than threshold.

## Example
```
data=removeEventsLowFrequency(dataset,20).
```

This will remove all the events are not met the minimum frequency.