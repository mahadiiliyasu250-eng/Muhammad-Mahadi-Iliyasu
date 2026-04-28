# Lab 2 & 5: Temperature Converter (PEP 8 Compliant)

# --- CELSIUS TO FAHRENHEIT ---
celsius_input_string = input("Enter temperature in Celsius: ")
celsius_float_value = float(celsius_input_string)

# Formula: (C * 9/5) + 32
fahrenheit_converted_result = (celsius_float_value * 9/5) + 32

print(f"{celsius_float_value:.1f} degrees Celsius is equal to {fahrenheit_converted_result:.1f} degrees Fahrenheit.")

print("-" * 30) # Visual separator for the user

# --- FAHRENHEIT TO CELSIUS ---
fahrenheit_input_string = input("Enter temperature in Fahrenheit: ")
fahrenheit_float_value = float(fahrenheit_input_string)

# Formula: (F - 32) * 5/9
celsius_converted_result = (fahrenheit_float_value - 32) * 5/9

print(f"{fahrenheit_float_value:.1f} degrees Fahrenheit is equal to {celsius_converted_result:.1f} degrees Celsius.")
