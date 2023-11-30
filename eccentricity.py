import matplotlib.pyplot as plt
import numpy as np
import time

from modules.constants import *

# Define The Range Of Masses
separations = np.arange(1e-1, 1e4, 1)

# Define the plot itself.
plt.title("Constraints on Sgr A* Companion Eccentricity")
plt.xlabel("$a_c$ $[au]$")
plt.ylabel("$e$")
plt.axis([1e-1, 1e4, 0, 1.05])

# Make the axes log scale.
plt.semilogx()

# calculate
separation_ratio = (SgrAttributes.SCHWARZSCHILD_RADIUS.value * Conversion.METERS_TO_AU.value) / separations
eccentricities = (1 - separation_ratio) / (1 + separation_ratio)

plt.plot(separations, eccentricities, label="0.1 au")

separation_ratio_1 = (10 * SgrAttributes.SCHWARZSCHILD_RADIUS.value * Conversion.METERS_TO_AU.value) / separations
eccentricities_1 = (1 - separation_ratio_1) / (1 + separation_ratio_1)

plt.plot(separations, eccentricities_1, label="1 au")

plt.savefig("./output/eccentricities.png")