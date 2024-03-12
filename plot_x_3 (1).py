import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 - 2*x**2 - 4*x + 2

# Generate x values
x = np.linspace(-5, 5, 400)

# Generate y values
y = f(x)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$f(x) = x^3 - 2x^2 - 4x + 2$')
plt.title('Plot of $f(x) = x^3 - 2x^2 - 4x + 2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
