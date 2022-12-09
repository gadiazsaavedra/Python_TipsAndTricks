from datetime import datetime, date

time_now = datetime.now().strftime("%H:%M:%S")
print(f"Current Time = {time_now}")

today_date = date.today().strftime("%d/%m/%Y")
print(f"Today's date = {today_date}")
