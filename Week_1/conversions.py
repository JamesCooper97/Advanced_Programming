def feet_inches_to_meters(feet, inches):
    if feet < 0 or inches < 0 or inches >= 12:
        raise ValueError("Feet must be >= 0, and inches must be between 0 and 11")
    meters = feet * 0.3048 + inches * 0.0254
    return meters

def meters_to_feet_inches(meters):
    if meters < 0:
        raise ValueError("Meters must be >= 0")
    total_inches = meters / 0.0254
    feet = int(total_inches // 12)
    inches = total_inches % 12
    return feet, inches

def pounds_to_kilograms(pounds):
    if pounds < 0:
        raise ValueError("Pounds must be >= 0")
    kilograms = pounds * 0.453592
    return kilograms

def kilograms_to_pounds(kilograms):
    if kilograms < 0:
        raise ValueError("Kilograms must be >= 0")
    pounds = kilograms / 0.453592
    return pounds

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin cannot be below 0")
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    if kelvin < 0:
        raise ValueError("Celsius is too low, resulting in negative Kelvin.")
    return kelvin

def hours_minutes_to_seconds(hours, minutes):
    if hours < 0 or minutes < 0 or minutes >= 60:
        raise ValueError("Hours must be >= 0, and minutes must be between 0 and 59.")
    seconds = (hours * 3600) + (minutes * 60)
    return seconds

def seconds_to_hours_minutes(seconds):
    if seconds < 0:
        raise ValueError("Seconds must be >= 0.")
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes
