from datetime import datetime, timedelta
#1
current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date five days ago:", new_date)

#2
today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime without microseconds:", current_datetime_without_microseconds)

#4
date1 = datetime(2024, 2, 20, 12, 0, 0)
date2 = datetime(2024, 2, 22, 12, 0, 0)

difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)


