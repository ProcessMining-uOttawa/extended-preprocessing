<h1>Jacques Trottier</h1>
<img align='right' src="https://avatars.githubusercontent.com/u/4829121?v=4" width="150">
<p><em>Master, Digital Transformation and Innovation (2023) <a href="https://www2.uottawa.ca/en">University of Ottawa</a></br>Federal Public Servant and IT Manager at <a href="https://tc.canada.ca/en">Transport Canada</a> <img src="https://icons.iconarchive.com/icons/wikipedia/flags/512/CA-Canada-Flag-icon.png" width="30" style="margin-bottom: -10px;"> 
</em><br />For more info, visit my <a href="https://jacques.trottier.us/">personal website</a></p>

[![Linkedin: Jacques Trottier](https://img.shields.io/badge/-jjtrottier-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/jjtrottier/)](https://www.linkedin.com/in/jjtrottier/)
[![GitHub jjtrottier](https://img.shields.io/github/followers/jtrottier?label=follow&style=social)](https://github.com/jtrottier)


### Summary of Contributions  

New functions added:
- [anonymizeCaseIDs()](./APIs/anonymizeCaseIDs.md)</li>
- [deleteDuplicateEventRowsDelta()](./APIs/deleteDuplicateEventRowsDelta.md)
- [filterTracesWithinDateRange()](./APIs/filterTracesWithinDateRange.md)
- [getEventLogEndEvents()](./APIs/getEventLogEndEvents.md)
- [getEventLogStartEvents()](./APIs/getEventLogStartEvents.md)
- [getEventLogStats()](./APIs/getEventLogStats.md)
- [getTraceDurations()](./APIs/getTraceDurations.md)
- [readExcel()](./APIs/readExcel.md)
- [readPanda()](./APIs/readPanda.md)
- [renameEventNames()](./APIs/renameEventNames.md)
- [transposeColumnsToEventLog()](./APIs/transposeColumnsToEventLog.md)

Other enhancements:
- Refactored API functions to remove the need to explicity define case id, timestamp and event column names as parameters. Please make sure to start your journey with this API by invoking readCSV, readExcel or readPanda. These functions will ensure that your column names are reformatted to use subsequent functionality within the API. 
- Created an importable python .py file to import this API as a Python module (originally the API was in a notebook).
- Improved API documentation.

### Stay Tuned

A case study will be published showcasing the use of this API for process mining data from the Federal Public Service of Canada. References to be added here once publication has taken place.

---
