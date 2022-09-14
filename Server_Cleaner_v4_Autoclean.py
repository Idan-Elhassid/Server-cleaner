import os
from datetime import *
import time

#the server we want to clean will be filled later using the list of servers we want.
chosen_server = ""
time_now = str(datetime.now())


def clean_folder():
    file = open("cleaner_log.txt", "a")
    #we want to delete only files older then 21 days so we will build a list of dates to check modified dates of files
    list_of_dates = []
    for number in range(0, 20):
        date_x = datetime.today() - timedelta(days=number)
        date_x_date = str(date_x.strftime("%Y-%m-%d"))
        list_of_dates.append(date_x_date)

    target_folder = chosen_server
    #a list of the folders in our desired location
    list_of_folders = os.listdir(target_folder)
    list_of_folder_links = []
    for item in list_of_folders:
        #if no folders in the desired location - do nothing
        if len(os.listdir(f"{target_folder}\{item}")) == 0:
            pass
        else:
            # we want to get a new location path\link of all the the folders in the desired location and create a list of those
            folder_link = f"{target_folder}\{item}"
            list_of_folder_links.append(folder_link)
            #for every file in the list we will test if the file's time-stamp-date is in the 21 day range
    for row in list_of_folder_links:
        new_file_list = os.listdir(row)
        for number in range(0, len(new_file_list)):
            file_to_test = f"{row}\{new_file_list[number]}"
            file_date_modified = os.path.getmtime(file_to_test)
            date_timestamped = str(datetime.fromtimestamp(file_date_modified))
            # if dates from the last 21 days appear in the file timestamp it will not delete it (pass)
            if any(date in date_timestamped for date in list_of_dates):
                pass
            else:
                file.write(time_now + file_to_test)
                os.remove(file_to_test)
    file.close()

#we will loop through this server list and clean each server
server_list = ["\\\\CT-Tech01\c$\CT-Tech\logs\LogFiles", "\\\\CT-Tech02\c$\CT-Tech\logs\LogFiles", "\\\\CT-Tech03\c$\CT-Tech\logs\LogFiles"]

for x in range (0, int(len(server_list))):
    chosen_server = server_list[x]
    clean_folder()
    time.sleep(300)
