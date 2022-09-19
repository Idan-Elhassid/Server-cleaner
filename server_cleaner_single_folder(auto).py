import os
from datetime import *

time_now = str(datetime.now())


def clean_folder():
    file = open("single_folder_autoclean_log.txt", "a")
    # list of dates to check modified dates of files
    list_of_dates = []
    for number in range(0, 20):
        date_x = datetime.today() - timedelta(days=number)
        date_x_date = str(date_x.strftime("%Y-%m-%d"))
        list_of_dates.append(date_x_date)

    target_folder = ["\\\\CT-Tech01\c$\CT-Tech\logs\LogFiles", "\\\\CT-Tech02\c$\CT-Tech\logs\LogFiles"]
    for item in target_folder:
        new_file_list = os.listdir(item)
        for number in range(0, len(new_file_list)):
            file_to_test = f"{item}\{new_file_list[number]}"
            file_date_modified = os.path.getmtime(file_to_test)
            date_timestamped = str(datetime.fromtimestamp(file_date_modified))
            if any(date in date_timestamped for date in list_of_dates):
                pass
            else:
                file.write(time_now + file_to_test)
                os.remove(file_to_test)
    file.close()


clean_folder()
