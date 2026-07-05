import numpy as np

#Numpy array to store th celsius temperatures

celcius_temps = np.array([29, 26, 37, 39, 32, 35, 30])  # Celsius temperatures

#Calculating Fahrenheit temperatures using the formula: F = (C * 9/5) + 32
fahrenheit_temps = (celcius_temps * 9/5) + 32  # Convert to Fahrenheit

# Print both arrays side by side with clear labels.
for i, (c_temp, f_temp) in enumerate(zip(celcius_temps, fahrenheit_temps), start=1):
    print(f"Day-{i} : Celcius: {c_temp}'C, Fahrenheit: {f_temp:.2f}'F")