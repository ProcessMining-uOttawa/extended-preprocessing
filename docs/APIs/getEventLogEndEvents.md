# List the unique end event types from all traces

This function identifies all of the unique event types at the end of all traces in the dataset.

## Usage
``
getEventLogEndEvents(DataFrame dataset)
``

## Arguments
- `dataset` is the name of pandas dataframe.

## Return
Returns a unique list of the event types at the end of all traces in the dataset.

## Example
```
data= getEventLogEndEvents(dataset)
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
| 124     	| purchaseOrderDenied	| 12/15/2021 16:49   | Jill 	| 1625235763 |

Return:

['purchasePaid','purchaseOrderDenied']