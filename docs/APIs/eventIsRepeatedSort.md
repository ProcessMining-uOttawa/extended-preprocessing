# Creates isRepeated Column

This function creates a new column called isRepeated. It indicates whether the event is repeated or not. Please note this function will automatically sort the rows by id and time.
> Note: this function will automatically sort the rows by case_id and timestamp.

## Usage
``
eventIsRepeatedSort (DataFrame dataset)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to manipulate.

## Return
Return a dataframe containing a new column called isRepeated.

## Example
```
data= eventIsRepeatedSort (dataset)
```