import math
# from icecream import ic

# Auxiliar functions primarily used by the class ExperimentalValue

def numtoExpVal(number):
	return ExperimentalValue(number, 0)

def isnumber(number):
	return isinstance(number, int) or isinstance(number, float)


# Functions for the class ExperimenalValue

def evsin(value, unit='rad'):
	"""
	Returns the sine of an ExperimentalValue object as an ExperimentalValue.
	
	Arguments:
	----------
		value : ExperimentalValue
			The value whose sine is to be computed
		unit='rad' : String
			The unit to be used. It can be 'rad'(radians) or 'deg'(decimal degrees)
	"""

	match unit:
		case 'rad':
			angle = value.measurand
		case 'deg':
			angle = math.radians(value.measurand)
		case _:
			raise ValueError(f"Unidad de ángulo '{unit}' no definida. La función evsin() sólo admite 'rad' o 'deg'.")

	measurand = math.sin(angle)		
	uncertainty = abs(math.cos(value.measurand))*value.uncertainty
	return ExperimentalValue(measurand, uncertainty)

def evcos(value, unit='rad'):
	"""
	Returns the cosine of an ExperimentalValue object as an ExperimentalValue.
	
	Arguments:
	----------
		value : ExperimentalValue
			The value whose cosine is to be computed
		unit='rad' : String
			The unit to be used. It can be 'rad'(radians) or 'deg'(decimal degrees)
	"""

	match unit:
		case 'rad':
			angle = value.measurand
		case 'deg':
			angle = math.radians(value.measurand)
		case _:
			raise ValueError(f"Unidad de ángulo '{unit}' no definida. La función evsin() sólo admite 'rad' o 'deg'.")

	measurand = math.cos(angle)		
	uncertainty = abs(math.sin(value.measurand))*value.uncertainty
	return ExperimentalValue(measurand, uncertainty)


# Classes

class ExperimentalValue:

	def __init__(self, measurand=0, uncertainty=0):
		self.measurand = measurand
		self.uncertainty = abs(uncertainty)

	def __repr__(self):
		return f'ExperimentalValue({self.measurand!r} \u00B1 {self.uncertainty!r})'

	# Addition

	def __add__(self, other):
		if isnumber(other):
			other = numtoExpVal(other)

		measurand = self.measurand + other.measurand
		uncertainty = math.sqrt(self.uncertainty**2 + other.uncertainty**2)
		return ExperimentalValue(measurand, uncertainty)

	def __radd__(self, other):
		return self + other

	# Subtraction

	def __sub__(self, other):
		if isnumber(other):
			other = numtoExpVal(other)

		measurand = self.measurand - other.measurand
		uncertainty = math.sqrt(self.uncertainty**2 + other.uncertainty**2)
		return ExperimentalValue(measurand, uncertainty)

	def __rsub__(self, other):
		return self - other

	# Multiplication

	def __mul__(self, other):
		if isnumber(other):
			other = numtoExpVal(other)

		measurand = self.measurand * other.measurand
		uncertainty = abs(measurand) * math.sqrt((self.uncertainty/self.measurand)**2 + (other.uncertainty/other.measurand)**2)
		return ExperimentalValue(measurand, uncertainty)

	def __rmul__(self, other):
		return self * other

	# Division

	def __truediv__(self, other):
		if isnumber(other):
			other = numtoExpVal(other)

		measurand = self.measurand / other.measurand
		uncertainty = abs(measurand) * math.sqrt((self.uncertainty / self.measurand)**2 + (other.uncertainty / other.measurand)**2)
		return ExperimentalValue(measurand, uncertainty)

	def __rtruediv__(self, other):
		if isnumber(other):
			other = numtoExpVal(other)

		measurand = other.measurand/self.measurand
		uncertainty = abs(measurand) * math.sqrt((self.uncertainty / self.measurand)**2 + (other.uncertainty / other.measurand)**2)
		return ExperimentalValue(measurand, uncertainty)


	# Power

	def __pow__(self, power):
		if not(isnumber(power)):
			raise TypeError("El exponente debe ser un número real.")
		measurand = self.measurand ** power
		uncertainty = abs(measurand) * power * self.uncertainty / self.measurand
		return ExperimentalValue(measurand, uncertainty)

if __name__ == "__main__":
	print("Ejecutando udenarphysutils.py \n")
