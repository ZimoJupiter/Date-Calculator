import tkinter as tk
import tkinter.ttk as ttk
import datetime
import calendar


def calculate():
    day1 = int(day1_cb.get())
    month1 = int(month1_cb.get())
    year1 = int(year1_cb.get())
    
    day2 = int(day2_cb.get())
    month2 = int(month2_cb.get())
    year2 = int(year2_cb.get())
    
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    date3 = datetime.date.today()
    
    delta = date2 - date1
    delta2 = date3 - date1
    days = delta.days
    started = delta2.days
    percentage = format((date3 - date1)/delta*100, '.2f')
    
    label9.config(text="Number of days between end date and start date：" + str(days))
    label10.config(text="Number of days between today and start date：" + str(started))
    label11.config(text="Percentage of days between today and start date：" + percentage + '%')
    percentage = float(percentage)
    if percentage >= 100:
        progressbar = '*'*50
    elif percentage <= 0:
        progressbar = '-'*50
    else:
        progressbar = '*'*int((0.5*percentage)) + '-'*int((0.5*(100-percentage)))
    label12.config(text = progressbar)


def update_day1(event):
    global day1_cb
    day1 = int(day1_cb.get())
    month1 = int(month1_cb.get())
    year1 = int(year1_cb.get())
    max_day1 = calendar.monthrange(year1, month1)[1]
    day1_cb['values'] = list(range(1, max_day1 + 1))
    if day1 > max_day1:
        day1_cb.set(max_day1)
    else:
        day1_cb.set(day1)


def update_month1(event):
    global month1_cb
    month1 = int(month1_cb.get())
    year1 = int(year1_cb.get())
    max_day1 = calendar.monthrange(year1, month1)[1]
    day1_cb['values'] = list(range(1, max_day1 + 1))


def update_day2(event):
    global day2_cb
    day2 = int(day2_cb.get())
    month2 = int(month2_cb.get())
    year2 = int(year2_cb.get())
    max_day2 = calendar.monthrange(year2, month2)[1]
    day2_cb['values'] = list(range(1, max_day2 + 1))
    if day2 > max_day2:
        day2_cb.set(max_day2)
    else:
        day2_cb.set(day2)


def update_month2(event):
    global month2_cb
    month2 = int(month2_cb.get())
    year2 = int(year2_cb.get())
    max_day2 = calendar.monthrange(year2, month2)[1]
    day2_cb['values'] = list(range(1, max_day2 + 1))


window = tk.Tk()

window.title("Date Calculator")

window.geometry("800x600")

frame = tk.Frame(window)

frame.pack()

label0 = tk.Label(frame, text="Please select start date and end date：")
label0.grid(row=0, columnspan=3, padx=10, pady=10)

label1 = tk.Label(frame, text="Star Date：")
label1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

label2 = tk.Label(frame, text="Year：")
label3 = tk.Label(frame, text="Month：")
label4 = tk.Label(frame, text="Day：")

label2.grid(row=2, column=0, padx=10, pady=10)
label3.grid(row=2, column=1, padx=10, pady=10)
label4.grid(row=2, column=2, padx=10, pady=10)

# create three string variables for storing the selected values of date1
selected_day1 = tk.StringVar()
selected_month1 = tk.StringVar()
selected_year1 = tk.StringVar()

# create three combobox widgets for displaying the dropdown menus of date1
day1_cb = ttk.Combobox(frame, textvariable=selected_day1)
month1_cb = ttk.Combobox(frame, textvariable=selected_month1)
year1_cb = ttk.Combobox(frame, textvariable=selected_year1)

# set the values for each combobox of date1
day1_cb['values'] = list(range(1, 32))
month1_cb['values'] = list(range(1, 13))
year1_cb['values'] = list(range(1, 5000))

# prevent typing a custom value
day1_cb['state'] = 'readonly'
month1_cb['state'] = 'readonly'
year1_cb['state'] = 'readonly'

# default select the first value
today = datetime.date.today()
day1_cb.set(today.day)
month1_cb.set(today.month)
year1_cb.set(today.year)

# place the widgets
day1_cb.grid(row=3, column=2, padx=10, pady=10)
month1_cb.grid(row=3, column=1, padx=10, pady=10)
year1_cb.grid(row=3, column=0, padx=10, pady=10)

# bind the selected value changes
day1_cb.bind('<<ComboboxSelected>>', update_day1)
month1_cb.bind('<<ComboboxSelected>>', update_month1)
year1_cb.bind('<<ComboboxSelected>>', update_day1)

label5 = tk.Label(frame, text="End Date：")
label5.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

label6 = tk.Label(frame, text="Year：")
label7 = tk.Label(frame, text="Month：")
label8 = tk.Label(frame, text="Day：")

label6.grid(row=5, column=0, padx=10, pady=10)
label7.grid(row=5, column=1, padx=10, pady=10)
label8.grid(row=5, column=2, padx=10, pady=10)

# create three string variables for storing the selected values of date2
selected_day2 = tk.StringVar()
selected_month2 = tk.StringVar()
selected_year2 = tk.StringVar()

# create three combobox widgets for displaying the dropdown menus of date2
day2_cb = ttk.Combobox(frame, textvariable=selected_day2)
month2_cb = ttk.Combobox(frame, textvariable=selected_month2)
year2_cb = ttk.Combobox(frame, textvariable=selected_year2)

# set the values for each combobox of date2
day2_cb['values'] = list(range(1, 32))
month2_cb['values'] = list(range(1, 13))
year2_cb['values'] = list(range(1, 5000))

# prevent typing a custom value
day2_cb['state'] = 'readonly'
month2_cb['state'] = 'readonly'
year2_cb['state'] = 'readonly'

# default select the first value
day2_cb.set(today.day)
month2_cb.set(today.month)
year2_cb.set(today.year)

# place the widgets
day2_cb.grid(row=6, column=2, padx=10, pady=10)
month2_cb.grid(row=6, column=1, padx=10, pady=10)
year2_cb.grid(row=6, column=0, padx=10, pady=10)

# bind the selected value changes
day2_cb.bind('<<ComboboxSelected>>', update_day2)
month2_cb.bind('<<ComboboxSelected>>', update_month2)
year2_cb.bind('<<ComboboxSelected>>', update_day2)


button = tk.Button(frame, text="计算", command=calculate)

button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)


label9 = tk.Label(frame, text="")
label10 = tk.Label(frame, text="")
label11 = tk.Label(frame, text="")
label12 = tk.Label(frame, text="")

label9.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
label10.grid(row=9, column=0, columnspan=3, padx=10, pady=10)
label11.grid(row=10, column=0, columnspan=3, padx=10, pady=10)
label12.grid(row=11, column=0, columnspan=3, padx=10, pady=10)


window.mainloop()


# pyinstaller --onefile --icon=favicon.ico dateCal.py