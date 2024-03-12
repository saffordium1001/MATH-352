import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(-2, 2, 400)

# Define the functions
y1 = np.exp(x) - 2
y2 = np.cos(np.exp(x) - 2)

# Plotting the graphs
plt.plot(x, y1, label='y = e^x - 2')
plt.plot(x, y2, label='y = cos(e^x - 2)')

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of y = e^x - 2 and y = cos(e^x - 2)')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
