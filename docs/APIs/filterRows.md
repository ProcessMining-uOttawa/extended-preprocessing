# Clean Text

The filterRows functions keep rows based on the condition we provided. Only the rows where the condition is TRUE will be kept in the DataFrame. We can specify multiple conditions, for example: ==, >, <, >=, <=, &, ||,!

## Usage
``
filterRows (DataFrame dataName, String condition)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to manipulate.
- `condition` is the logical conditions and that’s what we want to keep in the DataFrame.

## Return
Return a dataframe where the conditions are true.

## Example
```
filterRows (data, ‘device==”Apple” | new_time>422’).
```