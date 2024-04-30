from modules.constants import *
import math

import numpy as np

# masses is in solar masses
# orbital_parameters:
#    - Period (years)
#    - Eccentricity (unitless)
#    - Semi-Major Axis (au)
def iekl_calculation(plt, masses, orbital_parameters, plot_options):
	# base conversions
	orbital_period = orbital_parameters["period"] * Conversion.YEARS_TO_SECONDS.value # seconds
	kilogram_masses = masses * Conversion.SOLAR_MASS_TO_KILOGRAMS.value # kilogram
	orbital_sm_axis = orbital_parameters["sm-axis"] * Conversion.AU_TO_METERS.value # meters
	orbital_eccentricity = orbital_parameters["eccentricity"]

	k = math.sqrt(Fundamental.GRAV_CONST.value)
	mass_sum = SgrAttributes.MASS.value + kilogram_masses
	mass_prod = SgrAttributes.MASS.value * kilogram_masses

	precession_top = 2 * Math.PI.value * Fundamental.SPEED_OF_LIGHT.value ** 2
	precession_bottom = 3 * k ** 3 * (mass_sum) ** (3/2)

	iekl_const = (4/3) * orbital_period * ((1 - orbital_eccentricity ** 2)**2) * np.power(mass_sum, 2) / (mass_prod) * orbital_sm_axis ** 2

	result_raw = np.power(iekl_const * precession_bottom / precession_top,  2/9)
	result = result_raw * Conversion.METERS_TO_AU.value
	print(result)

	plt.plot(masses, result, 
		label="$t_{iEKL} \\sim t_{GR}$ (%s)" % orbital_parameters["name"], 
		linestyle=plot_options["style"], 
		color=plot_options["color"]
	)