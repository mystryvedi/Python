# Date and Time Operations

from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_datetime}")
