# Creates isRepeated Column

This function creates a new column called isRepeated. It indicates whether the event is repeated or not. Please note this function will automatically sort the rows by case_id and timestamp.
> Note: this function should run after ArrangeRows() function. For speed and efficiency, you can use this function to avoid duplicate sorts.

## Usage
``
eventIsRepeated (DataFrame dataset)
``

## Arguments
- `dataset` is the name of pandas dataframe we want to manipulate.

## Return
Return a dataframe containing a new column called isRepeated.

## Example
```
data= eventIsRepeated (dataset)
```