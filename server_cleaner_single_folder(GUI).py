import os
from datetime import *
from tkinter import *


def clean_folder():
    #we want to delete only files older then 21 days so we will build a list of dates to check modified dates of files
    list_of_dates = []
    for number in range(0, 20):
        date_x = datetime.today() - timedelta(days=number)
        # notice the date format mentioned below, it needs to be the same as modified dates in windows folders.
        date_x_date = str(date_x.strftime("%Y-%m-%d"))
        list_of_dates.append(date_x_date)

    target_folder = path_entry.get()
    new_file_list = os.listdir(target_folder)
    for number in range(0, len(new_file_list)):
        file_to_test = f"{target_folder}\{new_file_list[number]}"
        file_date_modified = os.path.getmtime(file_to_test)
        date_timestamped = str(datetime.fromtimestamp(file_date_modified))
        # if dates from the last 21 days appear in the file timestamp it will not delete it (pass)
        if any(date in date_timestamped for date in list_of_dates):
            pass
        else:
            os.remove(file_to_test)
    finished_label.config(text="the folder is clean, thank you and come again")

# this section is only for the Tkinter GUI
window = Tk()
window.title("Folder Cleaner")
window.config(padx=100, pady=50)

canvas = Canvas(width=800, height=600, highlightthickness=0)
cleaner_image = PhotoImage(file="cleaner-image.PNG")
canvas_image = canvas.create_image(400, 300, image=cleaner_image)
canvas.grid(column=0, row=1)

welcome_label = Label(text="File Path: ", font=("david", 16), padx=20, pady=50)
welcome_label.grid(column=0, row=2)

path_entry = Entry(width=50, font=("david", 16))
path_entry.insert(END, string="")
path_entry.grid(column=0, row=3)

space_label = Label(text="", font=("david", 16), padx=10, pady=10)
space_label.grid(column=0, row=4)

clean_button = Button(text="Clean", highlightthickness=0, command=clean_folder, padx=10, pady=10)
clean_button.grid(column=0, row=5)

finished_label = Label(text="", font=("david", 16), padx=20, pady=50)
finished_label.grid(column=0, row=6)


window.mainloop()
