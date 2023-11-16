from modules.constants import *

import numpy as np

# masses is in solar masses
# orbital_parameters:
#    - Period (years)
#    - Eccentricity (unitless)
#    - Semi-Major Axis (au)
def iekl_calculation(plt, masses, orbital_parameters, plot_options):
	# base conversions
	orbit_period = orbital_parameters["period"] * Conversion.YEARS_TO_SECONDS.value

	# calculate the front constant of the expression.
	front_constant = (4/3) * orbit_period * (1 - (orbital_parameters["eccentricity"] ** 2) ** 2)
	print(front_constant)

	# calculate the mass terms associated
	summed_masses_squared = np.power(masses + SgrAttributes.MASS.value, 2)
	mass_terms = summed_masses_squared / (masses * SgrAttributes.MASS.value)
	print(mass_terms)

	

