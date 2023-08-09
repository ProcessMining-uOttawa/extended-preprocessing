# Get the duration of all traces in the event log

This function calculates the duration of each trace in the event log and returns a table sorted from the longest trace to the shortest.

## Usage
``
getTraceDurations(DataFrame dataset)
``

## Arguments
- `dataset` is the name of pandas dataframe.

## Return
Returns a dataframe table showing the case_id, trace start and stop date and duration, sorted from longest running trace to shortest.

## Example
```
data= getTraceDurations(dataset)
```

Table 1: Source dataframe

| case_id 	| event           	    | timestamp  | purchaser | new_time |
| --------- | --------------------- | ---------- | --------- | -------- |
| 121     	| purchaseOrderCreated	| 31/12/2020 11:59   | Bob 	| 1625235606 |
| 121     	| purchaseOrderApproved	| 05/01/2021 13:53   | Bob 	| 1625235763 |
| 121     	| purchasePaid | 01/02/2021 14:55   | Bob 	| 1625236207 |
| 122     	| purchaseOrderDraft	| 05/01/2021 12:54   | Jane 	| 1625235606 |
| 122     	| purchaseOrderCreated	| 05/01/2021 12:55   | Jane 	| 1625235606 |
| 122     	| purchaseOrderApproved	| 10/01/2021 09:30   | Jane 	|1625235763 |
| 122     	| purchasePaid | 28/01/2021 15:33   | Jane 	| 1625236207 |
| 123     	| purchaseOrderCreated	| 10/04/2021 23:59   | John 	| 1625235606 |
| 123     	| purchaseOrderApproved	| 24/04/2021 23:59   | John 	| 1625235763 |
| 123     	| purchasePaid | 04/05/2021 23:59   | John 	| 1625236207 |
| 124     	| purchaseOrderCreated	|  12/01/2021 15:22 | Jill 	| 1625235606 |
| 124     	| purchaseOrderDenied	| 15/01/2021 16:49   | Jill 	| 1625235763 |

Return:

| case_id | start | end | time_delta |
| ----- | ------ | ------------- | ------------ |
| 121 | 31/12/2020 11:59 | 01/02/2021 14:55 | 32 days 02:56:0 |
| 123 | 10/04/2021 23:59 | 04/05/2021 23:59 | 24 days |
| 122 | 05/01/2021 12:54 | 28/01/2021 15:33 | 23 days 02:39:0 |
| 124 | 12/01/2021 15:22 | 15/01/2021 16:49 | 3 days 1:27:0 |