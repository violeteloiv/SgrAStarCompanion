import matplotlib.pyplot as plt
import numpy as np
import time

from modules.iekl import *
from modules.gw import *
from modules.falling_in import *

from modules.constants import *

# Define The Range Of Masses
masses = np.arange(1e-2, 1e8, 1e1)

# Define the plot itself.
plt.title("Constraints on Sgr A* Companion")
plt.xlabel("$m_c$ $[M_\odot]$")
plt.ylabel("$a_c$ [au]")
plt.axis([1e-2, 1e8, 1e-1, 1e5])

# Make the axes log scale.
plt.semilogx()
plt.semilogy()

# Plot Constraints
start = time.time()

# -- Gravitational Wave Constraints 2.5-5.8 Myr -- #

gravitational_wave_calculations(plt, masses, 5.8 * Conversion.MEGAYEARS_TO_YEARS.value,
{
	"style": 'solid',
	'color': '#000000'
})

seps_in_au_gw = gravitational_wave_calculations(plt, masses, 2.5 * Conversion.MEGAYEARS_TO_YEARS.value,
{
	"style": 'dashdot',
	"color": "#444444"
})

# calculate minimum eccentricity given constraints

minimum = seps_in_au_gw[0]
separation_ratio = 0.1 / minimum
maximum_eccentricity = (1 - separation_ratio) / (1 + separation_ratio)

# -- Constraints on Falling Into Sgr A* -- #

falling_in_calculation(plt, masses, maximum_eccentricity,
{
	"style": 'solid',
	"color": "#7bc9ea"
})

falling_in_calculation(plt, masses, 0.8,
{
	"style": 'solid',
	"color": '#000000'
})

falling_in_calculation(plt, masses, 0.4,
{
	"style": 'solid',
	"color": '#000000'
})

# -- Inverse Eccentric Kozai-Loidav Mechanism Constraints -- #

observing_objects = [
	{
		"parameters": {
			"name": "S0-2",
			"period": 16.0158, # years
			"eccentricity": 0.88466,
			"sm-axis": 970, # au
		},
		
		"styling": {
			"style": 'solid',
			"color": '#FF0000'
		}
	}
]

for obj in observing_objects:
	iekl_calculation(plt, masses, obj["parameters"], obj["styling"])

end = time.time()
comp_time = end - start
print("Computations Took:", comp_time, "seconds")

# Save the plot to the output folder.
start = time.time()
plt.legend()
plt.savefig("./output/constraints.png")
end = time.time()
plot_time = end - start
print("Plotting Time:", plot_time, "seconds")
print("Total Time:", comp_time + plot_time, "seconds")