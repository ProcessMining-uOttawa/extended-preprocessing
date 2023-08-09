## Install all the required packages and run the required libraries
##-----------------------------------------------
import pandas as pd
import numpy as np
import warnings
from collections import defaultdict
from collections import Counter
import Levenshtein
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from sklearn.cluster import KMeans
from skimpy import clean_columns
from datetime import datetime as dt
import re
import gensim
from sklearn.cluster import DBSCAN
import seaborn as sns
from itertools import combinations
from tqdm import tqdm


## List of Functions
##-----------------------------------------------
#write to CSV file
#writeCSV(table DataSet, String file):The writeCSV function writes the dataframe to a CSV file.
#Arguments: DataSet is the name of dataframe to save, file is the name of the CSV output file.
#Returns a CSV file
def writeCSV(dataset,filename):
     dataset.to_csv(filename)

#read a CSV file
#readCSV(String file):The readCSV function reads the CSV file into workplace
#Arguments: file is the CSV file in the select work directory.
def readCSV(filename,case_id_col_name="id",event_col_name="event",timestamp_col_name="timestamp",format="%d/%m/%Y %H:%M"): #added by JT
    csv_data = pd.read_csv(filename)
    csv_data = cleanAllHeaders(csv_data,case_id_col_name,event_col_name,timestamp_col_name)
    csv_data = addNewTime(csv_data,cleanText(timestamp_col_name),format)
    return csv_data

def readExcel(filename,case_id_col_name="id",event_col_name="event",timestamp_col_name="timestamp",format="%d/%m/%Y %H:%M"): #added by JT
    xls_data = pd.read_excel(filename) 
    xls_data = cleanAllHeaders(xls_data,case_id_col_name,event_col_name,timestamp_col_name)
    xls_data=addNewTime(xls_data,cleanText(timestamp_col_name),format)
    return xls_data

def readPanda(panda,case_id_col_name="id",event_col_name="event",timestamp_col_name="timestamp",format="%d/%m/%Y %H:%M"): #added by JT
    pd_data = panda
    pd_data = cleanAllHeaders(pd_data,case_id_col_name,event_col_name,timestamp_col_name)
    pd_data=addNewTime(pd_data,cleanText(timestamp_col_name),format)
    return pd_data


# Added by Alexis
# function to use before transposeColumnsToEventLog if (time data does not match happens)
def convert_to_datetime(dataset, col_name,date_format="%Y-%m-%d %H:%M:%S.%f"):
    dataset_copy = dataset.copy()
    # convert expected format
    dataset_copy[col_name] = pd.to_datetime(dataset_copy[col_name], format=date_format, errors='coerce')
    # handle unexpected format
    mask = dataset_copy[col_name].isna()
    unexpected_dates = dataset_copy.loc[mask, col_name]
    if len(unexpected_dates) > 0:
        unexpected_dates = pd.to_datetime(unexpected_dates, infer_datetime_format=True, errors='coerce')
        dataset_copy.loc[mask, col_name] = unexpected_dates
    return dataset_copy



# Added by JT
# case_id: specifies what case id column to use
# time: specifies what timestamp column to use
# events: { event_name : timestampColumnToUse }
# used when there are single rows with multiple timestamp columns that
# can be broken down into multiple (distinct) events
def transposeColumnsToEventLog(dataset,events,case_id_col_name="id",format="%d/%m/%Y %H:%M",resourcecol=False):
    dataset = ArrangeRows(dataset,[case_id_col_name])
    event_log = []
    for index,row in dataset.iterrows():
        for key, value in events.items(): 
            if resourcecol != False:
                event_log.append({
                       'case_id'   : row[case_id_col_name],
                       'event'     : key,
                       'timestamp' : row[value],
                       'resource'  : row[resourcecol],
                        })    
            else:
                event_log.append({
                    'case_id' : row[case_id_col_name],
                      'event' : key,
                  'timestamp' : row[value],
                })

    return readPanda(pd.DataFrame(event_log),case_id_col_name,'event','timestamp',format)


def cleanText(colName):
    cleanedText=re.sub("[$&+,:;=?@#|'<>.^*()%!-]","_",colName).lower()
    return cleanedText

#select dataset columns for analysis
#selectColumns(table DataSet, string columnName, …): This function selects/keeps the list columns needed for analysis from the dataset. Only the
#list of selected columns/attributes are included in the dataset. 
#Arguments: DataSet is the name of the dataframe, columnName is the name of the column to keep in the dataset. Many can be listed, separated by commas.
#Returns a dataset including only the list of columns/attributes that are selected
def selectColumns(dataset,selectCol):
    return dataset[selectCol]


#delete columns from the dataset
def deleteColumns(dataset,deleteCol):
    return dataset.drop(columns=deleteCol)

def cleanOneHeader(dataset,col_name):
    cleaned=cleanText(col_name)
    dataset=dataset.rename(columns={col_name:cleaned})
    return dataset


#clean column headers
#cleanHeaders(table DataSet)
#This function cleans the headers of the columns from spaces and other special characters.
#It only keeps lower case letters, numbers, and underscores (_). The spaces are replaced by ‘_’ and the special characters are removed. 
#Returns a dataframe with clean header names
def cleanAllHeaders(dataset,case_id_col_name,event_col_name,timestamp_col_name):
    dataset=dataset.rename(columns={case_id_col_name:'case_id',event_col_name:'event',timestamp_col_name:'timestamp'})
    col_list=dataset.columns.tolist()
    for i in col_list:
        cleaned=cleanText(i)
        dataset=dataset.rename(columns={i:cleaned})
    return dataset


#filter rows
#The filter function keeps records/rows based on the conditions specified. 
#Only the rows where the condition is TRUE are kept in the DataSet. 
#The filter function supports multiple functions, for example: ==, >, <, >=, <=, &, | , ! . 
def filterRows(dataset,conditions):
    return dataset.query(conditions)


##remove rows with low frequency
#Column represents the column you want to filter
# freq the threshold value that is used to filter out rows whose count is less than freq.
def removeEventsLowFrequency(dataset,freq,exceptions=None):
    if exceptions is None:
        return dataset[dataset.groupby('event')['event'].transform('count').gt(freq)]
    
    if type(exceptions) is str:
        dataset_e = dataset[dataset['event'] == exceptions]
        if dataset_e['event'].value_counts()[0] > freq:
            warnings.warn("Warning: Your exception event(s) occurs more often than your cut off. This will lead to duplicate occurences of your exceptions in the event log.")

        dataset_f = dataset[dataset.groupby('event')['event'].transform('count').gt(freq)]
        dataset = pd.concat([dataset_e,dataset_f])
        return ArrangeRows(dataset,['case_id','timestamp'])

    if type(exceptions) is list:
        dataset_e = dataset[dataset['event'].isin(exceptions)]        
        dataset_f = dataset_f = dataset[dataset.groupby('event')['event'].transform('count').gt(freq)]
        dataset = pd.concat(dataset_e,dataset_f)
        return ArrangeRows(dataset,['case_id','timestamp'])

    return False


#delete traces with number of events less than a specific number (num)
def deleteTraceLengthLessThan(dataset,num):
    return dataset.groupby('case_id').filter(lambda x : len(x)>=num)


# delete traces that do not start with one of many start events
# Not Sort 
def deleteTruncatedTracesStart(dataset,start_events):
    return dataset.groupby('case_id').filter(lambda oneCompanyData: oneCompanyData.iloc[0]['event'] in start_events)

## multiple conditions, values


# delete traces that do not start with one of many start events
# Need to Sort 
def deleteTruncatedTracesStartSort(dataset,start_events):
    dataset.sort_values(by=['case_id','new_time'])
    return dataset.groupby('case_id').filter(lambda oneCompanyData: oneCompanyData.iloc[0]['event'] in start_events)


#delete traces that do not end with one of many end events
# Need to sort

def deleteTruncatedTracesEndSort(dataset,end_events):
    dataset.sort_values(by=['case_id','new_time'])
    return deleteTruncatedTracesEnd(dataset,'case_id','event',end_events)
# multiple conditions, values


# delete traces that do not end with a specific end event
# No need to sort
def deleteTruncatedTracesEnd(dataset,end_events):
    return dataset.groupby('case_id').filter(lambda oneCompanyData: oneCompanyData.iloc[-1]['event'] in end_events)


#delete traces with total duration less than t
def deleteTracesWithTimeLessSort(dataset,t):
    dataset=dataset.sort_values(by=['case_id','new_time'])
    result=dataset.groupby('case_id').filter(lambda oneCompanyData: (oneCompanyData.iloc[-1].new_time - oneCompanyData.iloc[0].new_time) > t)
    return result

## format condition


#delete traces with total duration less than t
# Without sorting
def deleteTracesWithTimeLessSort(dataset,t):
    result=dataset.groupby('case_id').filter(lambda oneCompanyData: (oneCompanyData.iloc[-1].new_time - oneCompanyData.iloc[0].new_time) > t)
    return result


# Change the format of time
def addNewTime(dataset,time,formats="%d/%m/%Y %H:%M"):
    dates=pd.to_datetime(dataset[time],format=formats)
    dataset['new_time']=(dates - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
    return dataset


#concatenate two columns
def concatenateColumns(dataset,newCol,separator,*cols):
    dataset[newCol]=""
    for col in cols:
        dataset[newCol]=dataset[newCol]+separator+dataset[col].astype(str)
    return  dataset


# In this example, the keep parameter is set to False, so that only Unique values are taken and the duplicate values are removed from data.
# Determines which duplicates (if any) to mark.
# first : Mark duplicates as True except for the first occurrence.
# last : Mark duplicates as True except for the last occurrence.
# False : Mark all duplicates as True.
## Group by id
def eventIsRepeated(dataset):
    res = pd.DataFrame([])
    grouped = dataset.groupby('case_id')
    for name, group in grouped:
        group['match1'] = group.event.eq(group.event.shift()) 
        group['match2'] = group.event.eq(group.event.shift(-1)) 
        group["isRepeated"] = group.apply(lambda x: x['match1'] or x['match2'], axis = 1)
        group = group.drop(["match1", "match2"], axis = 1)
        res = pd.concat([res, group])
    return res


# In this example, the keep parameter is set to False, so that only Unique values are taken and the duplicate values are removed from data.
# Determines which duplicates (if any) to mark.
# first : Mark duplicates as True except for the first occurrence.
# last : Mark duplicates as True except for the last occurrence.
# False : Mark all duplicates as True.
## Group by id
def eventIsRepeatedSort(dataset):
    dataset.sort_values(by=['case_id','new_time'])
    res = pd.DataFrame([])
    grouped = dataset.groupby('case_id')
    for name, group in grouped:
        group['match1'] = group.event.eq(group.event.shift()) 
        group['match2'] = group.event.eq(group.event.shift(-1)) 
        group["isRepeated"] = group.apply(lambda x: x['match1'] or x['match2'], axis = 1)
        group = group.drop(["match1", "match2"], axis = 1)
        res = pd.concat([res, group])
    return res


# keep first event in each sequence of consecutive events in each trace of logs
def keepFirstEventSort(dataset):
    dataset=dataset.sort_values(by=['case_id','new_time'])
    res = pd.DataFrame([])
    grouped2 = dataset.groupby('case_id')
    for name, group in grouped2:
        test = group.loc[group['event'].ne(group['event'].shift())]
        res = pd.concat([res, test])
    return res


# keep first event in each sequence of consecutive events in each trace of logs
def keepFirstEvent(dataset):
    res = pd.DataFrame([])
    grouped2 = dataset.groupby('case_id')
    for name, group in grouped2:
        test = group.loc[group['event'].ne(group['event'].shift())]
        res = pd.concat([res, test])
    return res


# keep last event in each sequence of consecutive events in each trace of logs
def keepLastEventSort(dataset):
    dataset=dataset.sort_values(by=['case_id','new_time'],ascending=False)
    res = pd.DataFrame([])
    grouped2 = dataset.groupby('case_id')
    for name, group in grouped2:
        test = group.loc[group['event'].ne(group['event'].shift())]
        res = pd.concat([res, test])
    return res.sort_values(by=['case_id','new_time'])


# keep last event in each sequence of consecutive events in each trace of logs
def keepLastEvent(dataset,time):
    res = pd.DataFrame([])
    grouped2 = dataset.groupby('case_id')
    for name, group in grouped2:
        test = group.loc[group['event'].ne(group['event'].shift())]
        res = pd.concat([res, test])
    return res.sort_values(by=['case_id',time])


#delete all events
def deleteAllEvents(dataset,eventNames):
  if type(eventNames) is list:
    for eventName in eventNames:
        dataset = dataset.groupby('case_id').filter(lambda g: (g.event != eventName).all())
    return dataset
  
  return dataset.groupby('case_id').filter(lambda g: (g.event != eventNames).all())


#Merge rows no sort
def MergeSameEventRows(dataset,conditions):
    res = pd.DataFrame([])
    grouped = dataset.groupby('case_id')
    for name, group in grouped:
        group['sup'] = group.event.eq(group.event.shift()).map(lambda x: 0 if x == True else 1 ).cumsum()
        res = pd.concat([res, group])
    
    lists = dataset.columns.to_list()
    ignore = ['case_id']
    for column in lists:
        if column not in ignore and column not in conditions:
            conditions[column] = "first"
    test = res.groupby(['case_id', 'sup']).agg(conditions).reset_index().drop(['sup'], axis=1)
    return test
    

#Merge rows sort
def MergeSameEventRowsSort(dataset,conditions):
    dataset.sort_values(by=['case_id','new_time'])
    res = pd.DataFrame([])
    grouped = dataset.groupby('case_id')
    for name, group in grouped:
        group['sup'] = group.event.eq(group.event.shift()).map(lambda x: 0 if x == True else 1 ).cumsum()
        res = pd.concat([res, group])
    
    lists = dataset.columns.to_list()
    ignore = ['case_id']
    for column in lists:
        if column not in ignore and column not in conditions:
            conditions[column] = "first"
    result = res.groupby(['case_id', 'sup']).agg(conditions).reset_index().drop(['sup'], axis=1)
    return result
    

#Modified by JT
def ArrangeRows(dataset,condition,ascending=True):
    return dataset.sort_values(by=condition,ascending=ascending) # added by JT

# Added by JT
# This function deletes duplicate events that occur within a very close time of eachother
# You can specify the time threshold (delta) in seconds for when to delete duplicate events
# This function keeps the first (earliest) instance of an event when two occur close together
def deleteDuplicateEventRowsDelta(dataset,delta=120,event_name=None): 
    dataset = ArrangeRows(dataset,['case_id','new_time','event'])
    grouped = dataset.groupby('case_id')
    res = pd.DataFrame([])
    for case_id, group in grouped:
        group['match1'] = group.event.eq(group.event.shift()) 
        group['match2'] = group.event.eq(group.event.shift(-1)) 
        group['isRepeated'] = group.apply(lambda x: x['match1'] or x['match2'], axis = 1)
        group['delta'] = group['new_time'].diff()
        if event_name is None:
            group = group.drop(group[(group.isRepeated == True) & (group.match1 == True) & (group.delta < delta)].index)
        else:
            group = group.drop(group[(group.isRepeated == True) & (group.match1 == True) & (group.delta < delta) & (group.event == event_name)].index)
        res = pd.concat([res, group])
    res = res.reset_index(drop=True)
    return res

# Added by JT
# To anonymize event names a dataset, you can feed a map of
# search and replace values
def renameEventNames(dataset,replace_values):
    return dataset.replace({'event': replace_values})
    
# Added by JT
# To anonymize case IDs in a dataset to remove the risk of
# identifying someone based on the original case id
# This idea was inspired by Disco PM software's method
def anonymizeCaseIDs(dataset):
    dataset = ArrangeRows(dataset,['case_id','new_time'])
    grouped = dataset.groupby('case_id')
    res = pd.DataFrame([])
    c = 1
    for case_id, group in grouped:
        group = group.replace({'case_id': { case_id : c }})
        res = pd.concat([res,group])
        c += 1
    return res

# Added by JT
def getEventLogStartEvents(dataset):
    dataset = ArrangeRows(dataset,['case_id','timestamp'])
    start_events = []
    case_id = 0

    for index,row in dataset.iterrows():
        # check if we're at the start of a new case
        # if the case_id doesn't match the previous row, we have a new start event
        if case_id != row['case_id']:
             if row['event'] not in start_events:
                start_events.append(row['event'])
        case_id = row['case_id']
    start_events.sort(key=str.lower)
    return start_events

def getEventLogEndEvents(dataset):
    dataset = ArrangeRows(dataset,['case_id','timestamp'],False)
    end_events = []
    case_id = 0

    for index,row in dataset.iterrows():
        # check if we're at the start of a new case
        # if the case_id doesn't match the previous row, we have a new start event
        if case_id != row['case_id']:
             if row['event'] not in end_events:
                end_events.append(row['event'])
        case_id = row['case_id']
    end_events.sort(key=str.lower)
    return end_events

def getEventLogStats(dataset):
    total_cases = dataset['case_id'].nunique()
    total_events = dataset.shape[0]
    start_events = len(getEventLogStartEvents(dataset))
    end_events = len(getEventLogEndEvents(dataset))
    total_event_classes=dataset['event'].nunique()
    
    data = [{'Cases':total_cases,'Events':total_events,"Event Classes":total_event_classes,"Start events":start_events,"End events":end_events}]
    res = pd.DataFrame(data)
    return res


def getTraceDurations(dataset):
    dataset = ArrangeRows(dataset,['case_id','timestamp'])
    case_id = 0
    traces = []
    start_time = ""

    for index,row in dataset.iterrows():
        if case_id != row['case_id'] and case_id !=0:
            # we have a new start timestamp
            traces.append({
                'case_id' : case_id,
                'start' : start_time,
                'end'  : end_time
            })
            start_time = row['timestamp']
        
        if case_id == 0:
            start_time = row['timestamp']

        case_id = row['case_id']
        end_time = row['timestamp']

    res = pd.DataFrame(traces)
    res['start'] = pd.to_datetime(res['start'])
    res['end'] = pd.to_datetime(res['end'])
    res['time_delta'] = (res.end - res.start)
    res = ArrangeRows(res,['time_delta'],False)     
    return res


def filterTracesWithinDateRange(dataset,start_date,end_date,format="%d/%m/%Y %H:%M"):
    dataset = ArrangeRows(dataset,['case_id','timestamp'])
    case_id = 0
    start_date = dt.strptime(start_date,format)
    end_date = dt.strptime(end_date,format)

    for index,row in dataset.iterrows():
        # check if we're at the start of a new case
        # if the case_id doesn't match the previous row, we have a new start event
        if case_id != row['case_id'] and case_id !=0:
            if start_time < start_date or end_time > end_date:
                dataset = dataset[dataset.case_id != case_id]

            if type(row['timestamp']) == str:
                start_time = dt.strptime(row['timestamp'],format)
            else:
                start_time = row['timestamp']
            
        if case_id == 0: 
            if type(row['timestamp']) == str:
                start_time = dt.strptime(row['timestamp'],format)
            else:
                start_time = row['timestamp']

        case_id = row['case_id']

        if type(row['timestamp']) == str:
            end_time = dt.strptime(row['timestamp'],format)
        else:
            end_time = row['timestamp']

    return dataset



# Added by Alexis.B
def getEncodedTraceLog(dataset, show_tables=False, number_rows_display = 10,display_encoder = False,Title_size = 14):

    """
    Purpose: Create a trace log for each case id, then cluster events by case ID and calculate the frequency of unique event traces in the event log. 
    Optionally display the results as tables.

    Args:
        dataset (pandas.DataFrame): A DataFrame containing the event log data with columns "case_id" and "event".  
        show_tables (bool): A boolean value indicating whether to display the results as tables. 
        number_rows_display (int): An integer value indicating the number of rows to display in the output tables.                         
        display_encoder (bool): A boolean value indicating whether to display the encoder values.
        Title_size (int): An integer value indicating the font size of the table captions. 

    Returns:
        df_group_traces (pandas.DataFrame): A pandas DataFrame containing the frequency of unique event traces.
        df_cluster_results (pandas.DataFrame): A pandas DataFrame containing the count of case IDs for each unique trace.
    """
    
    # New table to cluster case id (the events are already sorted by case id and timestamp)
    df_cluster = dataset.copy()

    # Creates a column with encoded values for the events
    index = df_cluster.columns.get_loc("event") + 1
    df_cluster.insert(2,'event_encoded',df_cluster['event'].factorize()[0])
    encoder = {value: i for i, value in enumerate(df_cluster['event'].factorize()[1])}

    # Create a dict that maps case id with encoded trace log
    trace_log = df_cluster.groupby('case_id')['event_encoded'].apply(list).to_dict() 
    total_trace = len(trace_log)

    # Create a defaultdict to store the frequency of each trace
    trace_counts = defaultdict(int)

    # Loop over the dictionary and update the frequency of each trace
    for trace in trace_log.values():
        trace_counts[tuple(trace)] += 1

    # Create a set of unique traces
    unique_traces = set(trace_counts.keys())

    # Count the number of unique traces
    num_unique_traces = len(unique_traces)

    # Create a table that has case_id as column and the encode trace log as the other one
    df_cluster_results = pd.DataFrame({'case_id': list(trace_log.keys()), 'encoded_trace_log': list(trace_log.values())})
    df_cluster_results['trace count'] = df_cluster_results['encoded_trace_log'].apply(lambda x: trace_counts[tuple(x)])

    # Create a table to showcase (trace log -> encoded trace order, trace appearance count -> how many time it appears)
    df_group_traces = pd.DataFrame({'trace_log': list(trace_counts.keys()), 'trace count':list(trace_counts.values())})
    df_group_traces = df_group_traces.sort_values(by=['trace count'],ascending=False)

    # Show encoder values:
    if display_encoder == True:
        print(encoder)
    
    # Display both tables
    if show_tables:
        with pd.option_context('display.max_colwidth', None):
            table1 = df_group_traces.head(20).style.set_caption("Total Count by Trace Log")
            table1.set_table_styles([{'selector': 'caption', 'props': [('text-align', 'center'), ('font-size', str(Title_size)+'pt'), ('color','black')]}])
            display(table1)

            table2 = df_cluster_results.head(20).style.set_caption("Total Count Case Id Trace Log Occures")
            table2.set_table_styles([{'selector': 'caption', 'props': [('text-align', 'center'), ('font-size', str(Title_size)+'pt'),('color','black')]}])
            display(table2)

        pd.options.display.max_colwidth = 20

    return df_group_traces, df_cluster_results


## ------------------------- Machine Learning ------------------------- ##

#Added by Alexis 

def getSimilarEvent(dataset,event_column_name,eps,min_samples):

    """
    Clusters similar events in a given dataset using Word2Vec embeddings and DBSCAN clustering.

    Args:
        dataset (pd.DataFrame): The dataset containing events.
        event_column_name (str): The name of the column containing event descriptions.
        eps (float): The maximum distance between samples for one to be considered as in the neighborhood of the other.
        min_samples (int): The number of samples in a neighborhood for a point to be considered as a core point.

    Returns:
        pd.DataFrame: A DataFrame containing clustered similar events.
    """


    unique_events = dataset[event_column_name].unique().tolist()
    
    # Tokenize each event into a list of words
    unique_events_tokenized = [event.split() for event in unique_events]

    # Train Word2Vec model
    model = gensim.models.Word2Vec(unique_events_tokenized, min_count=1)

    # Convert activities into vectors by averaging the vectors of each word in the activity
    vectors = [np.mean([model.wv[word] for word in event], axis=0) for event in unique_events_tokenized]

    # Cluster the vectors using DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)  # you may need to tune these parameters depending on your data
    dbscan.fit(vectors)

    # Create a DataFrame for the clusters
    cluster_df = pd.DataFrame()

    for cluster_id in set(dbscan.labels_):
        if cluster_id != -1:  # -1 is noise in DBSCAN
            cluster_activities = [unique_events[i] for i, label in enumerate(dbscan.labels_) if label == cluster_id]
            cluster_df[f'cluster_{cluster_id}'] = pd.Series(cluster_activities)

    # Fill NaN values with an empty string
    cluster_df = cluster_df.fillna('')
    
    return cluster_df


#Added by Alexis
def getTimeframeCount(dataset,column_event,column_time,event_name,period_time):
    # select rows where event is appSignedDate and create a copy
    signed_dates = dataset[dataset[column_event] == event_name].copy()

    # convert timestamp to datetime
    signed_dates[column_time] = pd.to_datetime(signed_dates[column_time])

    # extract period from timestamp column and assign to new column specified by period_time variable
    signed_dates[period_time] = getattr(signed_dates[column_time].dt, period_time)

    # create bar chart of number of occurrences by period
    sns.countplot(data=signed_dates, x=period_time)

    # display list of period count values
    print(signed_dates[period_time].value_counts().sort_index(ascending=False).to_string())


# Added by Alexis
def deleteOutliers(dataset, feature, iqr_multiplier=3,show_summary = False):
  '''
  Description: Removes outliers from a given feature column of a pandas
  dataframe using the interquartile range (IQR) and an IQR multiplier.
  
  Args:
      dataset (pandas Dataframe): table you want to remove outliers
      feature (string): name of the feature column to remove outliers from (colunmn needs to be numerical)
      iqr_multiplier (int or float): numerical multiplier of the IQR range
  
  Returns:
      clean_df (pandas Dataframe): the original dataframe with the identified outliers removed
  '''

  # Create a copy of the input dataframe
  clean_df = dataset.copy()
  clean_df = clean_df.reset_index(drop=True)

  outlier_upper_id = [] 
  outlier_lower_id = []
  a = clean_df[feature].describe()
  iqr = a["75%"] - a["25%"]   
   
  # Calcualte Outer Fence
  upper_outer_fence = a["75%"] + iqr_multiplier * iqr
  lower_outer_fence = a["25%"] - iqr_multiplier * iqr
  


  # Remove outliers from the clean dataframe
  for index, time in enumerate(clean_df[feature]):    
      # Upper limit 
      if time > upper_outer_fence:          
          outlier_upper_id.append(clean_df.loc[index, 'case_id'])
          clean_df.drop(index, inplace=True)
    
      # Lower limit
      elif time < lower_outer_fence:
          outlier_lower_id.append(clean_df.loc[index, 'case_id'])
          clean_df.drop(index, inplace=True)
          
  outlier_upper_id = tuple(outlier_upper_id)
  outlier_lower_id = tuple(outlier_lower_id)
 
  if show_summary:
      print(f'The threshold used for the upper fence is {upper_outer_fence}\n')
      print(f'The threshold used for the lower fence is {lower_outer_fence}\n')
      print(f"The following are outliers that had higher process time: \n\n{outlier_upper_id}\n")
      print(f"The following are outliers that had lower process time than usual: \n\n{outlier_lower_id}\n")
    
  return clean_df, outlier_upper_id, outlier_lower_id


## ----------------------------------- Outlier Analysis ----------------------- ##


def add_outlier(event_log, outlier_case_ids):
    """
    Adds a new column to the event_log DataFrame indicating whether a case ID is an outlier.

    Parameters:
        event_log (pd.DataFrame): DataFrame containing the event log with columns case_id and event.
        outlier_case_ids (set): Set of case IDs identified as outliers.

    Returns:
        pd.DataFrame: Updated event_log DataFrame with the new column added.
        
        
    """
    
    event_log_copy = event_log.copy()
    event_log_copy['outlier'] = 'no'
    
    
    for idx, row in event_log.iterrows():
        case_id = row['case_id']
        if case_id in outlier_case_ids:            
            event_log_copy.loc[idx, 'outlier'] = 'yes'
          
            
    return event_log_copy
    

def plotTimeDeltaDistribution(df, time_delta_col, unit, n_bins, event_log, mark_outliers=False):
    """
    Plots the distribution of a timedelta column in days, seconds, or months.

    Parameters:
        df (pd.DataFrame): DataFrame containing the timedelta column.
        time_delta_col (str): Name of the column containing the timedelta values.
        unit (str): Time unit to use for plotting. Possible values are 'days', 'seconds', or 'months'.
        n_bins (int): Number of bins to use for the histogram.
        mark_outliers (bool): Flag indicating whether to mark outliers in the original table.

    Returns:
        Tuple: DataFrame with removed outliers, case IDs of removed outliers, and updated original DataFrame with outlier column
    """

    # Make a copy of the dataframe
    df_copy = df.copy()

    # convert the timedelta column to the specified unit
    if unit == 'days':
        time_delta_col_unit = time_delta_col + '_days'
        df_copy[time_delta_col_unit] = df_copy[time_delta_col] / pd.Timedelta(days=1)
        unit_name = 'days'
    elif unit == 'seconds':
        time_delta_col_unit = time_delta_col + '_seconds'
        df_copy[time_delta_col_unit] = df_copy[time_delta_col].dt.total_seconds()
        unit_name = 'seconds'
    elif unit == 'months':
        time_delta_col_unit = time_delta_col + '_months'
        df_copy[time_delta_col_unit] = df_copy[time_delta_col].dt.days / 30.4375
        unit_name = 'months'

    # Create figure with 2 subplots
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

    # Plot with outliers
    sns.histplot(data=df_copy, x=time_delta_col_unit, bins=n_bins, ax=axs[0])
    axs[0].set_title('Events with outliers')
    axs[0].set_xlabel(f'Total {unit_name}')
    axs[0].set_ylabel('Frequency')

    # calculate the lower and upper bounds of the data
    q1 = df_copy[time_delta_col_unit].quantile(0.25)
    q3 = df_copy[time_delta_col_unit].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 3 * iqr
    upper_bound = q3 + 3 * iqr

    # filter the data by the lower and upper bounds
    df_filtered = df_copy[(df_copy[time_delta_col_unit] >= lower_bound) & (df_copy[time_delta_col_unit] <= upper_bound)]

    # get the case IDs that are removed
    case_ids_removed = set(df_copy['case_id']) - set(df_filtered['case_id'])
    print(f"Number of event logs removed: {len(case_ids_removed)}")

    if mark_outliers:       
        event_log_filtered = add_outlier(event_log, case_ids_removed)

    # Plot without outliers
    sns.histplot(data=df_filtered, x=time_delta_col_unit, bins=n_bins, ax=axs[1])
    axs[1].set_title('Events without outliers')
    axs[1].set_xlabel(f'Total {unit_name}')
    axs[1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.show()

    if mark_outliers:
        return df_filtered, case_ids_removed, event_log_filtered
    else:
        return df_filtered, case_ids_removed


def add_time_threshold_events(df, threshold, time_unit, exclude_events=[]):
    # create a copy of the dataframe to not alter the original
    df = df.copy()

    # calculate the time difference for each group
    df['time_difference'] = df.groupby('case_id')['timestamp'].diff()

    # fillna to ensure the first record for each case_id doesn't have a null difference
    df['time_difference'] = df['time_difference'].fillna(pd.Timedelta(**{time_unit: threshold}))

    # create the new column based on the threshold
    df[f'minimum {threshold} {time_unit}(s) between events'] = np.where(
        (df['time_difference'] < pd.Timedelta(**{time_unit: threshold})) &
        (~df['event'].isin(exclude_events)),
        'yes',
        ''
    )

    # drop the time_difference column
    df = df.drop(columns=['time_difference'])

    return df



def deleteConsecutiveRepeats(df: pd.DataFrame, column_name: str, max_repeats: int) -> pd.DataFrame:
    """
    Filter the table based on whether a list in a specific column has more than max_repeats consecutive numbers.
    :param df: The DataFrame to filter.
    :param column_name: The name of the column that contains the lists.
    :param max_repeats: The maximum number of consecutive repeated elements to allow.
    :return: The filtered DataFrame.
    """
    def has_excessive_repeats(lst):
        """
        Return True if the list has more than max_repeats consecutive repeated elements, else False.
        """
        count = 1
        for i in range(1, len(lst)):
            if lst[i] == lst[i-1]:
                count += 1
                if count > max_repeats:
                    return True
            else:
                count = 1
        return False

    # Create a boolean mask
    mask = df[column_name].apply(has_excessive_repeats)

    # Filter the DataFrame using the mask
    filtered_df = df[~mask]
    
    return filtered_df


def getOptimalClustering(df,encoded_column_name):
    
    # Find unique logs:

    # Convert lists to tuples
    df[encoded_column_name] = df[encoded_column_name].apply(tuple)

    # Find unique tuples
    unique_trace_logs = pd.Series(list(set(df[encoded_column_name])))

    # If you need to convert it back to a list
    unique_trace_logs = unique_trace_logs.apply(list)


    # Initialize unique distance
    n_unique = len(unique_trace_logs)
    distances_unique = np.zeros((n_unique, n_unique))
    
    
    # Calculate Levenshtein distance and update time
    for i, j in tqdm(combinations(range(n_unique), 2), total=(n_unique*(n_unique-1)//2)):
        dist = Levenshtein.distance(unique_trace_logs[i], unique_trace_logs[j])
        distances_unique[i, j] = dist
        distances_unique[j, i] = dist

    wcss = [] # within-cluster sum of squares
    K = range(1,15)
    for k in tqdm(K, desc='Fitting KMeans'):
        km = KMeans(n_clusters=k, n_init=20)
        km = km.fit(distances_unique)
        wcss.append(km.inertia_)

    plt.plot(K, wcss, 'bx-')
    plt.xlabel('k')
    plt.ylabel('SSE') # Sum of squared error
    plt.title('K-means Elbow Graph Sum of squared distances')

       

    return distances_unique, unique_trace_logs


def getCluster(df_cluster, distances_unique,unique_trace_logs, column_name, k_cluster):
    
    # Create a dataframe with unique trace logs
    df_unique_trace_logs = pd.DataFrame(unique_trace_logs, columns=[column_name])

    # Perform KMeans clustering on the traces
    kmeans = KMeans(n_clusters=k_cluster, n_init=20) # Rerun Kmean with optimal number of clusters
    clusters = kmeans.fit_predict(distances_unique) 

    # Assign the clusters to this dataframe
    df_unique_trace_logs['cluster'] = clusters
    
    
    # Convert lists to tuples for the mapping operation
    df_cluster['encoded_trace_log_tuple'] = df_cluster[column_name].apply(tuple)
    df_unique_trace_logs['encoded_trace_log_tuple'] = df_unique_trace_logs[column_name].apply(tuple)

    # Perform the mapping operation
    df_cluster['cluster'] = df_cluster['encoded_trace_log_tuple'].map(df_unique_trace_logs.set_index('encoded_trace_log_tuple')['cluster'])

    # convert tuples back to lists
    df_cluster[column_name] = df_cluster['encoded_trace_log_tuple'].apply(list)
    df_unique_trace_logs[column_name] = df_unique_trace_logs['encoded_trace_log_tuple'].apply(list)

    # Drop the temporary tuple columns
    df_cluster = df_cluster.drop(columns='encoded_trace_log_tuple')
    
    return df_cluster
    

def getToEventLog(table1, table2):
    
    '''
    Description: Add a cluster column to the original table based on case id
    Args:
        
    table1 (pandas dataframe):Represents the first table to be merged. It should include a column named 'case_id'.
    table2:(pandas dataframe): Represents the second table to be merged. It should include a column named 'case_id' and a column named 'cluster'.
    
    '''
        
    merged_table = pd.merge(table1, table2[['case_id', 'cluster']], on='case_id', how='left')
    columns = list(merged_table.columns)
    columns = columns[:-1] + [columns[-1]]
    merged_table = merged_table[columns]
    return merged_table
    
