import math

def esnumero(valor: any) -> bool:
	"""Determina si un valor es un número real. """
	return isinstance(valor, int) or isinstance(valor, float)

def obtener_angulo(angulo: float, unidad: str = 'rad') -> float:
	"""
	Retorna el valor de un ángulo dado en radianes.
	
	Argumentos:
	-----------
		angulo: float
			El valor del ángulo a ser convertido.
		unidad: str = 'rad'
			La unidad en que se a el ángulo. 'rad' = radianes, 'deg' = grados decimales

	Lanza:
	------
		ValueError
			si la unidad es algo diferente a 'rad' o 'deg'
	"""	

	match str(unidad).lower():
		case 'rad':
			angulo = angulo
		case 'deg':
			angulo = math.radians(angulo)
		case _:
			raise ValueError(f"Unidad de ángulo '{unidad}' no definida. La función evsin() sólo admite 'rad' o 'deg'.")
	return angulo


if __name__ == "__main__":
	print("Ejecutando basic_functions.py del módulo udenarphys\n")