# Example using plt.pause for live updates
import matplotlib.pyplot as plt
import numpy as np

# Initialize plot
plt.ion() # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')

ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Live Graph Simulation")

# Generate data (replace with your actual data source)
x_data = []
y_data = []

# Loop to update the graph
for i in range(100):
    x_data.append(i / 10.0)
    y_data.append(np.sin(i / 10.0)) # Example data

    line.set_xdata(x_data)
    line.set_ydata(y_data)

    # Redraw the figure
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.1) # Pause to allow the plot to update

plt.ioff() # Turn off interactive mode
plt.show()