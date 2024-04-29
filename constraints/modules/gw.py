import numpy as np

from modules.constants import *

# starting assumption is that the binary has existed since the early universe.
# masses = au
# time = years
# plots a graph on the solar mass vs. au plot.
# 
# returns the semi-major axis array
def gravitational_wave_calculations(plt, masses, time, plot_options):
	# convert masses into kilograms for calculations.
	proxy_masses = masses * Conversion.SOLAR_MASS_TO_KILOGRAMS.value

	# compute the constant term in this equation.
	constant = (5/256) * ((Fundamental.SPEED_OF_LIGHT.value**5)/(Fundamental.GRAV_CONST.value**3))
	# convert the time to seconds for the calculation.
	time_over_constant = time * Conversion.YEARS_TO_SECONDS.value / constant

	# calculate the mass term in this equation:
	masses_squared = np.power(proxy_masses, 2)
	mass_terms = (SgrAttributes.MASS.value**2) * proxy_masses + masses_squared * (SgrAttributes.MASS.value)

	# finally computer the separations and convert it to AUs.
	separations = np.power(mass_terms * time_over_constant, 1/4)  * Conversion.METERS_TO_AU.value

	# plt.fill(masses, separations, facecolor="black", alpha=0.5)

	plt.plot(masses, separations, 
		label="$t_{GW}$="+str(time * Conversion.YEARS_TO_MEGAYEARS.value)+"Myrs", 
		linestyle=plot_options["style"], 
		color=plot_options["color"]
	)

	return separations # in au