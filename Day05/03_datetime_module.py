from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

print("Current Date and Time:", current_datetime)

# Print only the date
print("Date:", current_datetime.date())

# Print only the time
print("Time:", current_datetime.time())