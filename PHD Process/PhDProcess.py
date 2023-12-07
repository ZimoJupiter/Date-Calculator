import tkinter as tk
from datetime import date

def calculate_days():
    today = date.today()
    target_date1 = date(2023, 9, 4)
    target_date2 = date(2027, 5, 31)
    
    days_passed = (today - target_date1).days
    days_remaining = (target_date2 - today).days
    total_days = (target_date2 - target_date1).days
    
    ratio = days_passed / total_days
    
    result_label1.config(text=f"It has been {days_passed} days\n")
    result_label2.config(text=f"{days_remaining} days left\n")
    result_label3.config(text=f"{ratio:.2%} of the process has been completed")
    progressbar = '*'*int((50*ratio)) + '-'*int((50*(1-ratio)))
    result_label4.config(text = progressbar)

window = tk.Tk()
window.title("PhD Process")
window.geometry("400x300")

result_label1 = tk.Label(window, font=("Arial", 12), pady=10)
result_label1.pack()
result_label2 = tk.Label(window, font=("Arial", 12), pady=10)
result_label2.pack()
result_label3 = tk.Label(window, font=("Arial", 12), pady=10)
result_label3.pack()
result_label4 = tk.Label(window, font=("Arial", 12), pady=10)
result_label4.pack()

calculate_button = tk.Button(window, text="RUN", command=calculate_days)
calculate_button.pack()

window.mainloop()

# pyinstaller --onefile --icon=favicon.ico PhDProcess.py