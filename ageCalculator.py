import tkinter as tk
from datetime import datetime
import pytz

# Get current date in New Zealand
now_utc = datetime.utcnow()
utc_timezone = pytz.timezone('UTC')
now_utc = utc_timezone.localize(now_utc)
nz_timezone = pytz.timezone('Pacific/Auckland')
now_nz = now_utc.astimezone(nz_timezone)
today = now_nz.date()

# Create GUI window
window = tk.Tk()
window.title("Age Calculater v0.1")
window.geometry("310x300")

# Functions
# Main Function
def get_user_age():
  day=inputDay.get()
  month=inputMonth.get()
  year=inputYear.get() 
  
  if validate_input(year, 0, today.year, 'year') is True:
    if validate_input(month, 1, 12, 'month') is True:
      if validate_input(day, 1, 31, 'day') is True:
        day = int(day)
        month = int(month)
        year = int(year)
        if feb_check(year,day) is True:
          if compare_date_with_today(year,month,day) is True:
            print("validation done")

            age = today.year - year - 1
            print(age)
            ageCalculation = calculateAge(day, month, year)
            display_calculated_age(ageCalculation)
        else:
          print("compare validation failed")
      else:
        print("day validation failed")
    else:
      print("month validation failed")
  else:
    print("year validation failed")

# calculates years between todays date and input
def calculateAge(day, month, year):
    age = today.year-year-((today.month, today.day)<(month,day))
    return age

# display age input on outpu GUI
def display_calculated_age(age):
  ageOuput.config(state='normal')
  ageOuput.delete('1.0', tk.END)
  ageOuput.insert(tk.END,age)
  ageOuput.config(state='disabled')

# validates if input is an integer
def is_integer(input, input_value):
  try:
      int(input)
      return True
  except ValueError:
    if input_value == 'year':
      error_label_year.config(text="Please enter a year (eg. 2011).")
      inputYear.delete(0 ,'end')
    elif input_value == 'month':
      error_label_month.config(text="Please enter a valid month as a number (eg. January is 1).")
      inputMonth.delete(0 ,'end')
    elif input_value == 'day':
      error_label_day.config(text="Please enter a valid day as a number (eg. 4).")
      inputDay.delete(0 ,'end')

# validates if input is within assigned range based on what it is
def validate_input(input, min_value, max_value, input_value):
  if input_value == 'year':
    if is_integer(input, input_value) is True:
      if min_value <= int(input) <= max_value:
          error_label_year.config(text="")
          print(f"{input_value} validation passed")
          return True
      else:
          error_label_year.config(text="Please enter a valid year.")
          inputYear.delete(0 ,'end')
          print(f"{input_value} validation failed")
    else:
      return False
  if input_value == 'month':
    if is_integer(input, input_value) is True:
      if min_value <= int(input) <= max_value:
        error_label_year.config(text="")
        print(f"{input_value} validation passed")
        return True
        
      else:
        error_label_month.config(text="Please enter a valid month as a number (eg. January is 1).")
        inputMonth.delete(0 ,'end')
        print(f"{input_value} validation failed")
    else:
      return False
  if input_value == 'day':
    if is_integer(input, input_value) is True:
      if min_value <= int(input) <= max_value:
        error_label_year.config(text="")
        print(f"{input_value} validation passed")
        return True
      else:
        error_label_day.config(text="Please enter a day value between 1 and 31.")
        inputDay.delete(0 ,'end')
        print(f"{input_value} validation failed")
    else:
      return False

# checks if input year is a leap year
def leap_year_check(year):
  return year % 4 == 0

# checks if the user can enter 29th of Feb depending on year
def feb_check(year,day):
  if leap_year_check(year) is True and day > 29:
    error_feb.config(text="Please enter a day value between 1 and 29.")
    inputDay.delete(0 ,'end')
  elif leap_year_check(year) is False and day > 28:
    error_feb.config(text="Please enter a day value between 1 and 28.")
    inputDay.delete(0 ,'end')
  else:
    return True

# validates that the date entered is not in the future
def compare_date_with_today(input_year, input_month, input_day):
  input_date = datetime(int(input_year), int(input_month), int(input_day))
  today_date = datetime.combine(today, datetime.min.time())
  
  input_days_since_1970 = (input_date - datetime(1970, 1, 1)).days
  today_days_since_1970 = (today_date - datetime(1970, 1, 1)).days
  
  if input_days_since_1970 > today_days_since_1970:
    error_label_date.config(text="Please enter a date that is not in the future.")
    inputYear.delete(0 ,'end')
    inputMonth.delete(0 ,'end')
    inputDay.delete(0 ,'end')
    
  else:
    error_label_date.config(text="")
    return True

# Interface Setup
instructionText = tk.Label(text="Enter Your Birthday:")
instructionText.pack()

dateLabel = tk.Label(window, text="Date:",)
dateLabel.pack()

monthLabel = tk.Label(window, text="Month:")
monthLabel.pack()

yearLabel = tk.Label(window, text="Year:")
yearLabel.pack()

inputDay = tk.Entry(window, width=5)
inputDay.pack()

inputMonth = tk.Entry(window, width=5)
inputMonth.pack()

inputYear = tk.Entry(window, width=5)
inputYear.pack()

buttonCalculate = tk.Button(window, text="Calculate", command=get_user_age)
buttonCalculate.pack()

ageLabel = tk.Label(window, text="Your calculated age is:")
ageLabel.pack()

ageOuput = tk.Text(window, width=5, height=0, state='disabled')
ageOuput.pack()

error_label_year = tk.Label(window, text="")
error_label_year.pack()

error_label_month = tk.Label(window, text="")
error_label_month.pack()

error_label_day = tk.Label(window, text="")
error_label_day.pack()

error_label_date = tk.Label(window, text="")
error_label_date.pack()

error_feb = tk.Label(window, text="")
error_feb.pack()

buttonExit = tk.Button(window, text="Exit", command=exit)
buttonExit.pack()

# Positions
instructionText.place(x=70, y=5)
dateLabel.place(x=90, y=25)
monthLabel.place(x=90, y=50)
yearLabel.place(x=90, y=75)
inputDay.place(x=140, y=25)
inputMonth.place(x=140, y=50)
inputYear.place(x=140, y=75)
buttonCalculate.place(x=100, y=100)
ageLabel.place(x=85, y=130)
ageOuput.place(x=125, y=150)
error_label_year.place(x=10, y=170)
error_label_month.place(x=10, y=190)
error_label_day.place(x=10, y=210)
error_label_date.place(x=10, y=230)
error_feb.place(x=10, y=250)
buttonExit.place(x=125, y=270)



tk.mainloop()

