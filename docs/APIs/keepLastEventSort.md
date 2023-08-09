# Keep last event and drop repeated rows

This function removes the duplicated rows and keeps the last occurrence of an event. 
>Note: this function will automatically sort the rows by id and time.

## Usage

``
data= keepLastEventSort (dataset)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to manipulate.

## Return
Return a dataframe with only the last occurrence of an event name that is specified.

## Example
```
data= keepLastEventSort (dataset)
```