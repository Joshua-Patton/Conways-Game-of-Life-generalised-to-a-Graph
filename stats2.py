import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Read the CSV file
with open("data.csv") as file:
    csv_data = file.read()

# Load the data into a pandas DataFrame
data = pd.read_csv(StringIO(csv_data))

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(data['steps_till_all_dead'], data['assortativity_coefficient'], color='blue', marker='o')
plt.xlabel("Number of Surviving Steps")
plt.ylabel("Assortativity Coefficient")
plt.title("Assortativity vs. Number of Surviving Steps")
plt.grid(True)
plt.ylim(bottom=0)  # Set the lower limit of y-axis to 0
plt.show()
