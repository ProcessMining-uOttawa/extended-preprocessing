# Remove truncated traces

This function removes the traces that do not start with the provided eventName. 
>Note: this function should run after ArrangeRows() function. For speed and efficiency, you can use this function to avoid duplicate sorts.

## Usage
``
deleteTruncatedTracesStartSort (DataFrame dataset, String startEvent)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to manipulate.
- `startEvent` is the value of event’s name required to start with.

## Return
Return a dataframe containing only traces started with specified event.

## Example
```
data= deleteTruncatedTracesStartSort (dataset, “Home page”)
```
In this example, the function will remove all the traces that do not start with 
“Home page” event. It will help us filter incomplete traces whose beginning was not started with begin event.
