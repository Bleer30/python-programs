
def add_time(start, duration, day=''):
    # Split the input time
    parts = start.split()
    time = parts[0]
    period = parts[1]

    start_hour, start_minute = map(int, time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert 12-hour format to 24-hour format
    if period == "PM":
        start_hour += 12 if start_hour != 12 else 0
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Add the time
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    total_minutes %= 60  # Keep minutes within 0-59

    # Determine new AM/PM and 12-hour format
    new_period = "AM" if total_hours % 24 < 12 else "PM"
    new_hour = total_hours % 12
    new_hour = 12 if new_hour == 0 else new_hour  # 12-hour format fix

    # Count days later
    days_later = total_hours // 24

    # Convert minutes to two-digit format
    new_minutes = f"{total_minutes:02}"

    # Format the new time
    new_time = f"{new_hour}:{new_minutes} {new_period}"

    # Handle day of the week if provided
    if day:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = weekdays.index(day.capitalize())
        new_day = weekdays[(day_index + days_later) % 7]
        new_time += f", {new_day}"

    # Append days later notation
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Example test
print(add_time("3:00 PM", "3:10"))  # Expected: "6:10 PM"
print(add_time("11:55 AM", "3:12"))  # Expected: "3:07 PM"
print(add_time("9:15 PM", "5:30"))  # Expected: "2:45 AM (next day)"
print(add_time("11:40 AM", "0:25"))  # Expected: "12:05 PM"
print(add_time("2:59 AM", "24:00", "Monday"))  # Expected: "2:59 AM, Tuesday (next day)"
