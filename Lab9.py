# Programming in Science - Lab 9
# Written in Python
# Create 3 functions

import numpy as np

# Function 1: Read values from a file into an array
# This function reads numerical values from a text file and stores them in a NumPy array.
# Example file content:
# 1.5
# 2.5
# 3.5
def read_values_from_file(filename):
    return np.array([])


# Function 2: Read Oscillatory Wave Data and Compute Statistics
# This function reads a CSV file containing wave data with length and amplitude values.
# It returns:
#   - A NumPy 2D array of the data
#   - The mean amplitude
#   - The maximum amplitude
# Example file content:
# 1,2
# 3,4
# 5,6
def read_oscillatory_wave_data(filename):
    return np.array([]), 0, 0


# Function 3: Read Standing Wave Data and Compute Wave Speed
# This function reads a CSV file containing standing wave data with length and tension values.
# It returns:
#   - A NumPy 2D array of the data
#   - A NumPy array of computed wave speeds using v = sqrt(T / μ)
# Example file content:
# 1,4
# 2,9
# 3,16
def read_standing_wave_data(filename):
    return np.array([]), np.array([])
