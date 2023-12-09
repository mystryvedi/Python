# Date and Time Operations

from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_datetime}")

# Function to calculate the future date after a given number of days
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days} days: {formatted_future_date}")

# Display the current date and time
display_current_datetime()
