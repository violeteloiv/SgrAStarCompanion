from modules.constants import *

import numpy as np

# masses is in solar masses
# orbital_parameters:
#    - Period (years)
#    - Eccentricity (unitless)
#    - Semi-Major Axis (au)
def iekl_calculation(plt, masses, orbital_parameters, plot_options):
	# calculate iEKL time scale parameters

	# base conversions
	orbit_period = orbital_parameters["period"] * Conversion.YEARS_TO_SECONDS.value
	proxy_masses = masses * Conversion.SOLAR_MASS_TO_KILOGRAMS.value
	orbital_sm_axis = orbital_parameters["sm-axis"] * Conversion.AU_TO_METERS.value

	# calculate the mass terms associated in the denominator
	denominator_mass_terms = np.power(SgrAttributes.MASS.value + proxy_masses, 2) / (SgrAttributes.MASS.value * proxy_masses)

	# calculate the denominator result
	denominator = (8/3) * Math.PI.value * orbit_period * (1 - orbital_parameters["eccentricity"] ** 2) * denominator_mass_terms * (orbital_sm_axis ** 2)
	print("iEKL", denominator)
	
	# calculate the numerator result
	companion_eccentricity = 0.8 # this is sketchy !
	numerator = (6 * Math.PI.value * (Fundamental.GRAV_CONST.value ** 2) * np.power(proxy_masses, 2)) / ((Fundamental.SPEED_OF_LIGHT.value ** 2) * (1 - companion_eccentricity ** 2))
	print("iEKL", numerator)

	# calculate the final value of semi-major axis in terms of companion masses
	proxy_axis = np.power(numerator / denominator, 2)
	result = proxy_axis * Conversion.METERS_TO_AU.value
	print("a_c", result)

	plt.plot(masses, result, 
		label="$t_{iEKL} \sim t_{GR}$", 
		linestyle=plot_options["style"], 
		color=plot_options["color"]
	)