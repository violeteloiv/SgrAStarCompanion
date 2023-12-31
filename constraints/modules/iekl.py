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
	orbit_period = orbital_parameters["period"] * Conversion.YEARS_TO_SECONDS.value # seconds
	kilogram_masses = masses * Conversion.SOLAR_MASS_TO_KILOGRAMS.value # kilogram
	orbital_sm_axis = orbital_parameters["sm-axis"] * Conversion.AU_TO_METERS.value # meters
	orbital_eccentricity = orbital_parameters["eccentricity"]

	# important constant values
	mass_constant_eta = (SgrAttributes.MASS.value - kilogram_masses) / (SgrAttributes.MASS.value + kilogram_masses)
	gravitational_radius = Fundamental.GRAV_CONST.value * (SgrAttributes.MASS.value + kilogram_masses) / (Fundamental.SPEED_OF_LIGHT.value**2)

	# computational constants
	print(4/mass_constant_eta)
	constant_1 = np.power(4/mass_constant_eta, 2/9)
	print(constant_1)

	constant_2 = gravitational_radius * np.power(orbital_sm_axis/gravitational_radius, 7/9)
	print(constant_2)

	# setting the companion_eccentricity to 0.5 as test
	constant_3 = ((1 - orbital_eccentricity**2)**2 / (1 - SgrAttributes.COMPANION_ECCENTRICITY.value**2))**(2/9)
	print(constant_3)

	result = constant_1 * constant_2 * constant_3 * Conversion.METERS_TO_AU.value

	plt.plot(masses, result, 
		label="$t_{iEKL} \sim t_{GR}$", 
		linestyle=plot_options["style"], 
		color=plot_options["color"]
	)