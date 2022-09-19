# Server-cleaner
an automation project used to clean servers of unimportant disk consuming files. best used for old logs, cache etc...

the single folder cleaner branch was created to provide a solution for cases where just one specific folder needs to be cleaned.
in this branch the locations which will be cleaned are preplanned and embedded in the code to allow higher automation. for example multipale servers and directories can be specified and cleaned in one run and it can run in complete automation using task scheduler.
like in the main branch all files older then 21 days will be deleted from the location (the number of days could be changed if needed).

***obviously the server names in the file are in my own environment and will need to be changed as needed.

***requirements: install and import the following python libraries: os, datetime.
