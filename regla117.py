'''
El Erids
'''

import sys
def imprime_resultado(cadena):
	resultado_formato = '_'
	for caracter in cadena:
		if caracter == '1':
			resultado_formato = resultado_formato + '@'
		else:
			resultado_formato = resultado_formato + ' '
	print(resultado_formato + '_')
	
'''	#Regla 165
def procesa_ventana(ventana):
	if ventana[0]==ventana[2]:
		resultado = '1'
	else:
		resultado = '0'
	return resultado
'''
	#Regla 117
def procesa_ventana(ventana):
	if (ventana[0]==ventana[2]):
		resultado = '1'
		if (ventana[0]=='1' and ventana[1]=='1' and ventana[2]=='1'):
			resultado = '0'
	else:
		if (ventana[0]=='1' and ventana[2]=='0'):
			resultado = '1'
		else:
			resultado = '0'
		
	return resultado
	
def recorrer_cadena(cadena):
	nueva_cadena = ''
	
	for i in range(0, len(cadena)):
		n = len(cadena)
		ventana = cadena[(i+(n-1))%n] + cadena[i] + cadena[(i+1)%n]
		nueva_cadena = nueva_cadena + procesa_ventana(ventana)
	
	return nueva_cadena
	
cadena1 = "0000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000"
cadena_actual = cadena1
iteraciones = sys.argv[1]

for i in range(0, int(iteraciones)):
	imprime_resultado(cadena_actual)
	nueva_cadena = recorrer_cadena(cadena_actual)
	cadena_actual = nueva_cadena
