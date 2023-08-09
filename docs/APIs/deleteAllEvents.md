# Delete all events with specified name

This function removes the traces with specified event.

## Usage
``
eventIsRepeatedSort (DataFrame dataset, String idName, List/String eventName)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to manipulate.
- `eventName` is the name of event that we want to delete.

## Return
Return a dataframe without the specified event.

## Example
```
data= deleteAllEvents (dataset, “Home page”)
```

In this example, all the traces named with “Home page” event will be removed.