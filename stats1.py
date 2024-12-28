import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from io import StringIO

# Read the CSV file
with open("data.csv") as file:
    csv_data = file.read()

# Load the data into a pandas DataFrame
data = pd.read_csv(StringIO(csv_data))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Initial value for n
initial_n = 0

# Function to plot based on the selected n value
def plot_filtered_data(n):
    # Clear the current plot
    ax.clear()

    # Filter the data to only include rows where steps_till_all_dead > n
    filtered_data = data[data['steps_till_all_dead'] > n]

    # Plot edos_renyi_p vs poss_of_initial_dead for models that lasted more than n steps
    ax.scatter(filtered_data['edos_renyi_p'], filtered_data['poss_of_initial_dead'], color='blue', marker='o')
    ax.set_xlabel("Erdős–Rényi p")
    ax.set_ylabel("Possibility of Initial Dead")
    ax.set_title(f"Models Lasting More Than {n} Steps")
    ax.set_xlim(0, 1)  # Assuming p values are between 0 and 1
    ax.set_ylim(0, data['poss_of_initial_dead'].max())  # Adjust y-axis as necessary
    ax.grid(True)
    plt.draw()

# Initial plot
plot_filtered_data(initial_n)

# Create a slider for n with increment of 1
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])  # [left, bottom, width, height]
n_slider = Slider(ax_slider, 'Minimum Steps', 0, data['steps_till_all_dead'].max(), valinit=initial_n, valstep=1)

# Update the plot when the slider value changes
def update(val):
    n = n_slider.val
    plot_filtered_data(int(n))

n_slider.on_changed(update)

# Show the plot
plt.show()
