import math
from funciones_basicas import *
# from icecream import ic

# Clase

class EValue:

	"""
	EValue: una clase para representar valores experimentales con su\
	incrtidumbre. Permite realizar operaciones aritméticas básicas entre\
	objetos de esta clase con operadores "infix".

	Parámetros:
	-----------
		mesurando: Mesurando del valor exerimental.
		incertidumbre: Incertidumbre del valor experimental.
	"""

	def __init__(self, mesurando=0, incertidumbre=0):
		if not(esnumero(mesurando)) or not(esnumero(incertidumbre)):
			raise ValueError("El mesurando y la incertidumbre deben ser números reales.")

		self.mesurando = mesurando
		self.incertidumbre = abs(incertidumbre)

	def __repr__(self):
		return f'EValue({self.mesurando!r} \u00B1 {self.incertidumbre!r})'

	# Adición

	def __add__(self, other):
		if esnumero(other):
			other = EValue(other)

		mesurando = self.mesurando + other.mesurando
		incertidumbre = math.sqrt(self.incertidumbre**2 + other.incertidumbre**2)
		return EValue(mesurando, incertidumbre)

	def __radd__(self, other):
		return self + other

	# Sustracción

	def __sub__(self, other):
		if esnumero(other):
			other = EValue(other)

		mesurando = self.mesurando - other.mesurando
		incertidumbre = math.sqrt(self.incertidumbre**2 + other.incertidumbre**2)
		return EValue(mesurando, incertidumbre)

	def __rsub__(self, other):
		if esnumero(other):
			other = EValue(other)

		mesurando = other.mesurando - self.mesurando
		incertidumbre = math.sqrt(self.incertidumbre**2 + other.incertidumbre**2)
		return EValue(mesurando, incertidumbre)

	# Multiplicación

	def __mul__(self, other):
		if esnumero(other):
			mesurando = self.mesurando * other
			incertidumbre = abs(other) * self.incertidumbre
		else:
			mesurando = self.mesurando * other.mesurando
			incertidumbre = abs(mesurando) * math.sqrt((self.incertidumbre/self.mesurando)**2 + (other.incertidumbre/other.mesurando)**2)

		return EValue(mesurando, incertidumbre)

	def __rmul__(self, other):
		return self * other

	# División

	def __truediv__(self, other):
		if esnumero(other):
			other = EValue(other)

		mesurando = self.mesurando / other.mesurando
		incertidumbre = abs(mesurando) * math.sqrt((self.incertidumbre / self.mesurando)**2 + (other.incertidumbre / other.mesurando)**2)
		return EValue(mesurando, incertidumbre)

	def __rtruediv__(self, other):
		if esnumero(other):
			other = EValue(other)

		mesurando = other.mesurando/self.mesurando
		incertidumbre = abs(mesurando) * math.sqrt((self.incertidumbre / self.mesurando)**2 + (other.incertidumbre / other.mesurando)**2)
		return EValue(mesurando, incertidumbre)


	# Potencia

	def __pow__(self, exponente):
		if not(esnumero(exponente)):
			raise TypeError("El exponente debe ser un número real.")
		mesurando = self.mesurando ** exponente
		incertidumbre = abs(mesurando) * exponente * self.incertidumbre / self.mesurando
		return EValue(mesurando, incertidumbre)


# Funciones trigonométricas para la clase EValue

def evsin(valor: EValue, unidad: str = 'rad') -> EValue:
	"""
	Retorna el seno de un EValue.
	
	Argumentos:
	----------
		valor : EValue
			El valor cuyo seno se va a calcular.
		unidad: str = 'rad'
			Unidad del ángulo que se introdujo. Puede ser 'rad'(radianes) o 'deg'(grados decimales).
	"""

	angulo = obtener_angulo(valor.mesurando, unidad)
	incert = obtener_angulo(valor.incertidumbre, unidad)

	mesurando = math.sin(angulo)		
	incertidumbre = abs(math.cos(angulo))*incert
	return EValue(mesurando, incertidumbre)

def evcos(valor: EValue, unidad: str = 'rad'):
	"""
	Retorna el coseno de un EValue.
	
	Argumentos:
	----------
		valor : EValue
			El valor cuyo coseno se va a calcular.
		unidad: str = 'rad'
			Unidad del ángulo que se introdujo. Puede ser 'rad'(radianes) o 'deg'(grados decimales).
	"""

	angulo = obtener_angulo(valor.mesurando, unidad)
	incert = obtener_angulo(valor.incertidumbre, unidad)

	mesurando = math.cos(angulo)		
	incertidumbre = abs(math.sin(angulo))*incert
	return EValue(mesurando, incertidumbre)

