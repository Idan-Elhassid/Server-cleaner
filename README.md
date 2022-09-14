# Server-cleaner
an automation project used to clean servers of unimportant disk consuming files. best used for old logs, cache etc...

this branch was created to provide a complete multi server automated solution (does not include a GUI)
in this branch the locations which will be cleaned are preplanned and embedded in the code to allow higher automation. for example multipale servers and directories can be specified and cleaned in one run and it can run in complete automation using task scheduler.  
like in the main branch all files older then 21 days will be deleted from the location (the number of days could be changed if needed).

***obviously the server names in the file are in my own environment and will need to be changed as needed.

***requirements: install and import the following python libraries: os, datetime, time.
