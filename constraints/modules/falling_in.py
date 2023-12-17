from modules.constants import *

def falling_in_calculation(plt, masses, eccentricity, plot_options):
	minor_axis = SgrAttributes.SCHWARZSCHILD_RADIUS.value * (1 + eccentricity) / (1 - eccentricity)
	
	plt.plot(masses, [minor_axis * Conversion.METERS_TO_AU.value] * masses.size,
		label="e={0}".format(eccentricity),
		linestyle=plot_options["style"], 
		color=plot_options["color"]
	) 