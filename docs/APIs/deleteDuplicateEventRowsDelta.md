# Delete duplicate events within a specified time threshold

In some instances, duplicate events take place one after the other in quick succession. This could be due to a user clicking a button twice in a UI, causing multiple recordings of the same event. This function deletes duplicate events within the time threshold specified. You can also use different thresholds for different event types by including the event name in the last parameter of the function.

>Note: This function relies on three standard column names: case_id, event, and timestamp. You should invoke this function after initializing the dataframe using one of [readCSV()](./APIs/readCSV.md), [readExcel()](./APIs/readExcel.md) or [readPanda()](./APIs/readPanda.md). 

## Usage
``
deleteDuplicateEventRowsDelta(Dataframe dataset,Int delta,String event_name)
``

## Arguments
- `dataset` is the source pandas dataframe.
- `delta` is the threshold (in seconds) that we wish to use to delete duplicate events. The default is 120 seconds.
- `event_name` is the name of the event to apply this function to. Leaving this blank will delete duplicate events occurring for all event types. 

## Return
Return a dataframe with the duplicate events removed.

## Example
```
data= deleteDuplicateEventRowsDelta(dataset, 130,"purchasePaid")
```

Table 1: Source dataframe

| case_id 	| event           	    | timestamp  | purchaser | new_time |
| --------- | --------------------- | ---------- | --------- | -------- |
| 121     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | Bob 	| 1625235606 |
| 121     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | Bob 	| 1625235763 |
| 121     	| purchasePaid | 2022-12-25 23:59:00   | Bob 	| 1625236207 |
| 121     	| purchasePaid | 2022-12-25 23:59:30   | Bob 	| 1625236207 |
| 122     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | Jane 	| 1625235606 |
| 122     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | Jane 	|1625235763 |
| 122     	| purchaseOrderApproved	| 2022-12-15 23:59:01   | Jane 	|1625235763 |
| 122     	| purchasePaid | 2022-12-25 23:59:00   | Jane 	| 1625236207 |
| 122     	| purchasePaid | 2022-12-26 00:01:11   | Jane 	| 1625236207 |

Table 2: Returned dataframe with duplicate events for type purchasePaid deleted

| case_id 	| event           	    | timestamp  | purchaser | new_time |
| --------- | --------------------- | ---------- | --------- | -------- |
| 121     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | Bob 	| 1625235606 |
| 121     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | Bob 	| 1625235763 |
| 121     	| purchasePaid | 2022-12-25 23:59:00   | Bob 	| 1625236207 |
| 122     	| purchaseOrderCreated	| 2022-12-13 23:59:00   | Jane 	| 1625235606 |
| 122     	| purchaseOrderApproved	| 2022-12-15 23:59:00   | Jane 	|1625235763 |
| 122     	| purchaseOrderApproved	| 2022-12-15 23:59:01   | Jane 	|1625235763 |
| 122     	| purchasePaid | 2022-12-25 23:59:00   | Jane 	| 1625236207 |
| 122     	| purchasePaid | 2022-12-26 00:01:11   | Jane 	| 1625236207 |
