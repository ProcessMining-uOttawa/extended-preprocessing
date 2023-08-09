#  Transform time format

The addNewTime function will transform time column and create a new column called new_time to better manage time for the event logs. 
>In general, one does not need to call this function explicitly as it is already called in the readCSV, readExcel and readPanda functions.

## Usage
``
addNewTime (DataFrame dataName, String timeColName, String formats)
``

## Arguments
- `dataName` is the name of Pandas DataFrame we want to manipulate.
- `timeColName` is the name of the time column in the CSV file.
- `formats` is the format of time stamp. The default one is “%d/%m/%Y %H:%M”. The user can modify it according to the datasets.

## Return
Return a new DataFrame with new column ‘new_time’.

## Example
```
data=addNewTime (dataset, "time","%d/%m/%Y %H:%M")
```
