# Get basic statistics describing the event log

This function provides some general summary statistics about the event log. This includes the number of cases, events, event classes, starting events and end events. 

## Usage
``
getEventLogStats(DataFrame dataset)
``

## Arguments
- `dataset` is the name of pandas dataframe.

## Return
Returns a dataframe table showing the number of cases, events, event classes, starting events and end events.

## Example
```
data= getEventLogStats(dataset)
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
| 124     	| purchaseOrderDenied	| 12/15/2021 16:49   | Jill 	| 1625235763 |

Return:

| Cases | Events | Event Classes | Start events | End events |
| ----- | ------ | ------------- | ------------ | ---------- |
| 4 | 12 | 5 | 2 | 2 |