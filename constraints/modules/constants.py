from enum import Enum

class Math(Enum):
	# dimensionless
	PI = 3.1415926535 # Pi up to 10 digits

class Conversion(Enum):
	AU_TO_METERS = 1.498e11 # 1 au = x meters
	METERS_TO_AU = 1/AU_TO_METERS # 1 meter = x au

	YEARS_TO_SECONDS = 365.25 * 24 * 60 * 60 # 1 year = x seconds
	SECONDS_TO_YEARS = 1/YEARS_TO_SECONDS # 1 second = x years

	SOLAR_MASS_TO_KILOGRAMS = 1.98847e30 # kilograms
	KILOGRAMS_TO_SOLAR_MASS = 1/SOLAR_MASS_TO_KILOGRAMS # solar masses

	MEGAYEARS_TO_YEARS = 1e6 # years
	YEARS_TO_MEGAYEARS = 1/MEGAYEARS_TO_YEARS # megayears

class Fundamental(Enum):
	GRAV_CONST = 6.6743e-11 # newton meters squared per kilogram squared
	SPEED_OF_LIGHT = 299792458 # meters per second

class SgrAttributes(Enum):
	MASS = 4.297e6 * Conversion.SOLAR_MASS_TO_KILOGRAMS.value # kilograms
	SCHWARZSCHILD_RADIUS = 0.1 * Conversion.AU_TO_METERS.value # meters 

