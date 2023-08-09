# Filter traces within a specified start and end time

This function allows you to filter traces within a specified start and end time. The trace must fully start and finish within the time range specified for it to be included in the returned dataset.

>Note: This function relies on three standard column names: case_id, event, and timestamp. You should invoke this function after initializing the dataframe using one of [readCSV()](./APIs/readCSV.md), [readExcel()](./APIs/readExcel.md) or [readPanda()](./APIs/readPanda.md). 

## Usage
``
filterTracesWithinDateRange(Dataframe dataset,String start_date,String end_date,String format="%d/%m/%Y %H:%M")
``

## Arguments
- `dataset` is the source pandas dataframe.
- `start_date` is the start date we wish to use to include a trace.
- `end_date` is the end date we wish to use to include a trace. 
- `format` (optional) is the timestamp format used for the date comparison. The default format is: %d/%m/%Y %H:%M

## Return
Return a dataframe with only the traces that start and finish between the start_date and end_date.

## Example
```
filterTracesWithinDateRange(Dataframe dataset, '01/01/2021 00:00','31/12/2021 23:59')
```

Table 1: Source dataframe

| case_id 	| event           	    | timestamp  | purchaser | new_time |
| --------- | --------------------- | ---------- | --------- | -------- |
| 121     	| purchaseOrderCreated	| 31/12/2020 11:59   | Bob 	| 1625235606 |
| 121     	| purchaseOrderApproved	| 05/01/2021 13:53   | Bob 	| 1625235763 |
| 121     	| purchasePaid | 01/02/2021 14:55   | Bob 	| 1625236207 |
| 122     	| purchaseOrderCreated	| 05/01/2021 12:55   | Jane 	| 1625235606 |
| 122     	| purchaseOrderApproved	| 10/01/2021 09:30   | Jane 	|1625235763 |
| 122     	| purchasePaid | 28/01/2021 15:33   | Jane 	| 1625236207 |
| 123     	| purchaseOrderCreated	| 10/04/2021 23:59   | John 	| 1625235606 |
| 123     	| purchaseOrderApproved	| 24/04/2021 23:59   | John 	| 1625235763 |
| 123     	| purchasePaid | 04/05/2021 23:59   | John 	| 1625236207 |
| 124     	| purchaseOrderCreated	|  12/01/2021 15:22 | Jill 	| 1625235606 |
| 124     	| purchaseOrderApproved	| 12/15/2021 16:49   | Jill 	| 1625235763 |
| 124     	| purchasePaid | 05/01/2022 13:00   | Jill 	| 1625236207 |

Table 2: Returned dataframe with only the traces fully executed between the start and end dates

| case_id 	| event           	    | timestamp  | purchaser | new_time |
| --------- | --------------------- | ---------- | --------- | -------- |
| 122     	| purchaseOrderCreated	| 05/01/2021 12:55   | Jane 	| 1625235606 |
| 122     	| purchaseOrderApproved	| 10/01/2021 09:30   | Jane 	|1625235763 |
| 122     	| purchasePaid | 28/01/2021 15:33   | Jane 	| 1625236207 |
| 123     	| purchaseOrderCreated	| 10/04/2021 23:59   | John 	| 1625235606 |
| 123     	| purchaseOrderApproved	| 24/04/2021 23:59   | John 	| 1625235763 |
| 123     	| purchasePaid | 04/05/2021 23:59   | John 	| 1625236207 |
