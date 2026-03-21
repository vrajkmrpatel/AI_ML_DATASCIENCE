# from datetime import date, datetime

# # datetime class
# now = datetime.now()

# print(now)

# # print("Year: ",now.year)
# # print("Month: ",now.month)
# # print("Day: ",now.day)
# # print("Year: ",now.year)
# # print("Minute: ",now.minute)

# # specific_date_time = datetime(2023, 12, 25, 10, 30, 0)
# # print(specific_date_time)


import datetime

# date class
# today = datetime.date.today()
# print(today)

# sepcific_date = datetime.date(2026,12,25)
# print(sepcific_date)

# timedelta class
# Get the current date and time
now = datetime.datetime.now()

# Create a timedelta object representing 5 days
delta = datetime.timedelta(days=5)

# Add 5 days to the current date
new_date = now + delta
print("New date after adding 5 days:", new_date)

# strftime and strptime Methods

# Get the current date and time
now = datetime.datetime.now()

# Format it as a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)


# Convert a string to a datetime object
date_string = "2023-12-25 10:30:00"
date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Converted datetime object:", date_obj)

# timezone class
# Get the current time in UTC
now_utc = datetime.datetime.now(datetime.timezone.utc)
print("Current UTC time:", now_utc)
