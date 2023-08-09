# Transpose Columns to Event Log

Sometimes multiple events are recorded in one database row across multiple columns. The transposeColumnsToEventLog function transposes columns into separate rows suitable for an event log.

This function reads accepts a dataframe as input and a dictionary specifying event names with their source event columns.

## Usage
``
transposeColumnsToEventLog(Dataframe dataset,Dictionary events,String case_id_col_name,String format="%d/%m/%Y %H:%M",String resourcecol)
``

## Arguments
- `dataset` is the pandas dataframe you wish to import.
- `events` is the dictionary that specifies event names from the source columns.
- `case_id_col_name` is the name of the case id column from the source dataframe.
- `format` is the format of timestamps from your source dataframe.
- `resourcecol` is an optional parameter. If your input dataframe has a column that specifies a resource responsible for an event, you can preserve this data by specifying the column name from your source dataframe. A null value will ignore this.

## Return
Returns a Pandas DataFrame. The case id, event and timestamp column names from the source dataframe will be renamed and standardized to the following column names (respectively): case_id,event,timestamp. A new_time column is added for subsequent use of time filtering functions.

## Example
```

event_columns_dict = {
    'purchaseOrderCreated'  : 'pocreated',
    'purchaseOrderApproved' : 'poapproved',
    'purchasePaid' : 'popaid'
}

data=pm.transposeColumnsToEventLog(pd,event_columns_dict,'Case.ID',"%Y-%m-%d %H:%M:%S",'purchaser')
```
This will read the Pandas dataframe. Table1 (below) is an example of a source dataset. Table2 gives an example of the output from the readPanda function.

Table 1: An example of source dataframe


| Case.ID | pocreated | poapproved | popaid | Purchaser |
| ------- | --------- | ----------- | -------- | ------- |
| 121 | 2022-12-13 23:59:00 | 2022-12-15 23:59:00 | 2022-12-25 23:59:00 | Bob |
| 122     	| 2022-12-13 23:59:00 	| 2022-12-15 23:59:00   | 2022-12-25 23:59:00    	| Jane 	|
| 123     	| 2022-12-13 23:59:00 	| 2022-12-15 23:59:00   | 2022-12-25 23:59:00    	| John 	|
| 124     	| 2022-12-13 23:59:00 	| 2022-12-15 23:59:00   | 2022-12-25 23:59:00    	| Jill 	|

Table2: Output dataframe after using the transposeColumnsToEventLog() function

| case_id 	| event           	    | timestamp  | purchaser | new_time |
| --------- | --------------------- | ---------- | --------- | -------- |
| 121     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | Bob 	| 1625235606 |
| 121     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | Bob 	| 1625235763 |
| 121     	| purchasePaid | 2022-12-25 23:59:00   | Bob 	| 1625236207 |
| 122     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | Jane 	| 1625235606 |
| 122     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | Jane 	|1625235763 |
| 122     	| purchasePaid | 2022-12-25 23:59:00   | Jane 	| 1625236207 |
| 123     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | John 	| 1625235606 |
| 123     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | John 	| 1625235763 |
| 123     	| purchasePaid | 2022-12-25 23:59:00   | John 	| 1625236207 |
| 124     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | Jill 	| 1625235606 |
| 124     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | Jill 	| 1625235763 |
| 124     	| purchasePaid | 2022-12-25 23:59:00   | Jill 	| 1625236207 |