import numpy as np
import matplotlib.pyplot as plt

frequency = [5.190, 5.495, 6.881, 7.407, 8.197] #frecventa
U0 = [780.63, 898.56,  1256.5, 1387.7, 1261.6] #valorile tensiunii de stopare

coefficients = np.polyfit(frequency, U0, 1)
U0_fit = np.polyval(coefficients, frequency)

plt.figure(figsize=(8, 6))
plt.plot(frequency, U0, 'o', label='Data points U0 average', markersize=8)
plt.plot(frequency, U0_fit, '-r', label=f'U0(v) = {coefficients[0]:.2f} * ν + {coefficients[1]:.2f}')  # Ecuatia dreptei

# Label the axes
plt.xlabel('ν · 10^14 (Hz)')
plt.ylabel('U0 (mV)')
plt.title('Linear Regression of U0')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
