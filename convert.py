def convert_seconds(seconds):
    hours = seconds
    minutes = (seconds - hours * 3600)
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)