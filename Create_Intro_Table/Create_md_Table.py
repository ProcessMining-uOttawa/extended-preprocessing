# Step 1: Define Columns and Rows
columns = ["", "Row", "Column", "Trace", "Other"]
rows = ["Add", "Remove", "Modify", "Other"]

# Step 2: Create Data Structure

# Initialize the table with empty strings
table_data = {row: {col: "" for col in columns} for row in rows}

# Define a function to append data to a specific cell
def append_data(row, col, data):
    if row in table_data and col in table_data[row]:
        if table_data[row][col]:
            table_data[row][col] += " " + data
        else:
            table_data[row][col] = data
    else:
        print(f"Error: Invalid row '{row}' or column '{col}'")

# Inserting data
append_data("Add", "Column", "[concatenateColumns()](./APIs/concatenateColumns.md)")
append_data("Add", "Column", "[concatenateColumns()](./APIs/concatenateColumns.md)")
append_data("Add", "Column", "[eventIsRepeated()](./APIs/eventIsRepeated.md)")
append_data("Add", "Column", "[eventIsRepeatedSort()](./APIs/eventIsRepeatedSort.md)")
append_data("Add", "Column", "[addNewTime()](./APIs/addNewTime.md)")



append_data("Add", "Trace", "[deleteTraceLengthLessThan()](./APIs/deleteTraceLengthLessThan.md)")
append_data("Add", "Trace", "[deleteTruncatedTracesStart()](./APIs/deleteTruncatedTracesStart.md)")
append_data("Add", "Trace", "[deleteTruncatedTracesEndSort()](./APIs/deleteTruncatedTracesEndSort.md)")
append_data("Add", "Trace", "[deleteTruncatedTracesEnd()](./APIs/deleteTruncatedTracesEnd.md)")
append_data("Add", "Trace", "[deleteTruncatedTracesEndSort()](./APIs/deleteTruncatedTracesEndSort.md)")
append_data("Add", "Trace", "[deleteTruncatedTracesEnd()](./APIs/deleteTruncatedTracesEnd.md)")
append_data("Add", "Trace", "[deleteTruncatedTracesEndSort()](./APIs/deleteTruncatedTracesEndSort.md)")
append_data("Add", "Trace", "[deleteTracesWithTimeLess()](./APIs/deleteTracesWithTimeLess.md)")
append_data("Add", "Trace", "[deleteTracesWithTimeLessSort()](./APIs/deleteTracesWithTimeLessSort.md)")

append_data("Remove", "Row", "[keepFirstEvent()](./APIs/keepFirstEvent.md)")
append_data("Remove", "Row", "[keepLastEvent()](./APIs/keepLastEvent.md)")
append_data("Remove", "Row", "[removeEventsLowFrequency()](./APIs/removeEventsLowFrequency.md)")
append_data("Remove", "Row", "[filterRows()](./APIs/filterRows.md)")
append_data("Remove", "Row", "[deleteAllEvents()](./APIs/deleteAllEvents.md)")
append_data("Remove", "Row", "[deleteDuplicateEventRowDelta()](./APIs/deleteDuplicateEventRowsDelta.md)")
append_data("Remove", "Row", "[filterTracesWithinDateRange()](./APIs/filterTracesWithinDateRange.md)")
append_data("Remove", "Row", "[keepFirstEventSort()](./APIs/keepFirstEventSort.md)")
append_data("Remove", "Row", "[deleteConsecutiveRepeats()](./APIs/deleteConsecutiveRepeats.md)")

append_data("Remove", "Column", "[deleteColumns()](./APIs/deleteColumns.md)")

append_data("Modify", "Row", "[cleanOneHeader()](./APIs/cleanOneHeader.md)")
append_data("Modify", "Row", "[cleanAllHeaders()](./APIs/cleanAllHeaders.md)")
append_data("Modify", "Row", "[arrangeRows()](./APIs/sortRows.md)")
append_data("Modify", "Row", "[MergeSameEventRows()](./APIs/MergeSameEventRows.md)")

append_data("Modify", "Column", "[anonymizeCaseIDs()](./APIs/anonymizeCaseIDs.md)")
append_data("Modify", "Column", "[renameEventNames()](./APIs/renameEventNames.md)") 

append_data("Modify", "Other", "[cleanText()](./APIs/cleanText.md)") 

append_data("Other", "Column", "[selectColumns()](./APIs/selectColnmns.md)")

append_data("Other", "Other", "[readCSV()](./APIs/readCSV.md)")
append_data("Other", "Other", "[readExcel()](./APIs/readExcel.md)")
append_data("Other", "Other", "[readPanda()](./APIs/readPanda.md)")
append_data("Other", "Other", "[transposeColumnsToEventLog()](./APIs/transposeColumnsToEventLog.md)")
append_data("Other", "Other", "[writeCSV()](./APIs/writeCSV.md)")
append_data("Other", "Other", "[getCluster()](./APIs/getCluster.md)")
append_data("Other", "Other", "[getEventLogEndEvents()](./APIs/getEventLogEndEvents.md)")
append_data("Other", "Other", "[getEventLogStartEvents()](./APIs/getEventLogStartEvents.md)")
append_data("Other", "Other", "[getEventLogStats()](./APIs/getEventLogStats.md)")
append_data("Other", "Other", "[getOptimalClustering()](./APIs/getOptimalClustering.md)")
append_data("Other", "Other", "[getSimilarEvent()](./APIs/getSimilarEvent.md)")
append_data("Other", "Other", "[getTimeFrameCount()](./APIs/getTimeFrameCount.md)")
append_data("Other", "Other", "[getToEventLog()](./APIs/getToEventLog.md)")
append_data("Other", "Other", "[getTraceDurations()](./APIs/getTraceDurations.md)")
append_data("Other", "Other", "[getEncodedTraceLog()](./APIs/getEncodedTraceLog.md)") 

# Step 3: Print Markdown Table to Terminal

def write_table_to_file(filename):
    with open(filename, 'w') as f:
        # Write the headers
        f.write("| " + " | ".join(columns) + " |\n")
        f.write("| " + " | ".join(["---"] * len(columns)) + " |\n")

        # Write the data
        for row in rows:
            f.write("| " + " | ".join([row] + [table_data[row][col] for col in columns[1:]]) + " |\n")  # Adjusted here


write_table_to_file("table.md")
