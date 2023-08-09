# Write a CSV file

The writeCSV functions writes the pandas DataFrame to a CSV file.

## Usage
``
writeCSV (DataFrame dataName, String fileName)
``

## Arguments
- `dataName` is the name of pandas dataframe we want to save.
- `fileName` is the name of the CSV output file name.

## Return
Return None or str (If path_or_buf is None, returning the resulting csv format as a string. Otherwise returns None).

## Example
```
writeCSV(dataset,’NewDataset.csv’)
```
This will write the Pandas DataFrame dataset to the NewDataset.csv file under the current path.
