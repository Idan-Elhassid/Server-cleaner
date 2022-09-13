import os
from datetime import *
from tkinter import *
from tkinter import messagebox


chosen_server = ""
time_now = str(datetime.now())


def clean_folder():
    #safety check to avoid miss-clicks
    are_you_sure = messagebox.askokcancel(title="are you sure?", message="are you sure you want to clean this folder?")
    if are_you_sure:
        # this file will log all of our actions in this program
        file = open("cleaner_log.txt", "a")
        # list of dates to check modified dates of files, at the end of the loop you get a list of 21 last days dates
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
                #for every file in the list we will test if the file time-stamp-date is in the 21 day range or else it will be deleted
        for row in list_of_folder_links:
            new_file_list = os.listdir(row)
            for number in range(0, len(new_file_list)):
                file_to_test = f"{row}\{new_file_list[number]}"
                file_date_modified = os.path.getmtime(file_to_test)
                date_timestamped = str(datetime.fromtimestamp(file_date_modified))
                if any(date in date_timestamped for date in list_of_dates):
                    pass
                else:
                    file.write(time_now + file_to_test)
                    os.remove(file_to_test)
        finished_label.config(text="the server is clean, thank you and come again")
        file.close()
    else:
        finished_label.config(text="operation cancelled")


# this section is the code for the GUI (tkinter)

def clean_ct_tech01():
    global chosen_server
    chosen_server = "\\\\CT-Tech01\c$\CT-Tech\logs\LogFiles"
    clean_folder()


def clean_ct_tech02():
    global chosen_server
    chosen_server = "\\\\CT-Tech02\c$\CT-Tech\logs\LogFiles"
    clean_folder()


def clean_ct_tech03():
    global chosen_server
    chosen_server = "\\\\CT-Tech03\c$\CT-Tech\logs\LogFiles"
    clean_folder()



window = Tk()
window.title("Server Cleaner")
window.config(padx=100, pady=50)

canvas = Canvas(width=300, height=200, highlightthickness=0)
cleaner_image = PhotoImage(file="cleaning.PNG")
canvas_image = canvas.create_image(150, 100, image=cleaner_image)
canvas.grid(column=1, row=1)

welcome_label = Label(text="which server would you like to clean? ", font=("david", 16), padx=20, pady=50)
welcome_label.grid(column=1, row=2)

clean_ct_tech01_button = Button(text="CT-Tech01", highlightthickness=0, command=clean_ct_tech01, padx=10, pady=10)
clean_ct_tech01_button.grid(column=0, row=3)

clean_ct_tech02_button = Button(text="CT-Tech02", highlightthickness=0, command=clean_ct_tech02, padx=10, pady=10)
clean_ct_tech02_button.grid(column=1, row=3)

clean_ct_tech03_button = Button(text="CT-Tech03", highlightthickness=0, command=clean_ct_tech03, padx=10, pady=10)
clean_ct_tech03_button.grid(column=2, row=3)

finished_label = Label(text="", font=("david", 16), padx=20, pady=50)
finished_label.grid(column=1, row=12)


window.mainloop()
