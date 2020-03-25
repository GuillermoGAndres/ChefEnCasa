#Algoritmo de la mejor receta (AMR)
from receta import Receta
import integracion

#Este script tendra toda la logica del programa, hara la funcionalidad
#Sera el modelo de nuestro patron de diseño, aqui programara toda la logica
#Es decir, aqui obtenendremos las mejor receta de las que existen

#Iteramos nuestra lista de ingredientes
#for ingrediente in listaIngredientes:

def algoritmoAMR(listaClienteIngre):
	'''
	@return recetasRecomendadas regresara una lista con las recetas mejor
	encontradas en nuestra base de datos, segun las coincidencias con sus
	ingredientes que el cliente tiene 
	'''
	#print(listaClienteIngre)
	arbolRecetario = integracion.obtenerRecetario()
	#1.-Una vez obtenido todo nuestro recetario en un arbol de tenemos
	#ahora que recorrer(Inorden) en cada nodo una tupla (coincidencias, receta)
	#que sera una lista que sera guardada como atributo de arbolRecetatio
	arbolRecetario.inorden(arbolRecetario.obtenerRaiz(), listaClienteIngre)
	#2.- Una vez obtenido nuestras tuplas, buscaremos en la lista, el mayor
	#numero de coincidencia de las recetas, si es igual con otra receta, esa 
	#receta la vamos a necesitar como una recomendacio que tambien le puede servir
	#al cliente, asi que guardaremos esas recetas que tambien coinciden en una 
	#lista de recomendaciones[]
	recetasRecomendadas = []
	#Buscar la mayor coincidencia
	maxCoincidencia = arbolRecetario.getListaCoincidencias()[0] #sera una tupla
	for tupla in arbolRecetario.getListaCoincidencias():
		if(tupla[0] > maxCoincidencia[0]):
			maxCoincidencia = tupla

	#Primero se debe encontrar el de mayor Coincidencia, una vez encontrada
	#tenemos que buscar tambien si existen mas recetas que cotienen el mismo numero
	#de coincidencias que el maxCoincidencia
	#busqueda lineal
	for tupla in arbolRecetario.getListaCoincidencias():
		if(tupla[0] == maxCoincidencia[0]):
			recetasRecomendadas.append(tupla)
	#Por lo tanto en recetas recomendas, ya viene incluida maxCoincidencia
	#como primer elemento
	return recetasRecomendadas
	#No solamente va a ser una, podrian ser muchas mas qeu el coincidan
	#con sus ingredientes por esos va hacer una lista de recetas con sus
	#respectivas coincidencias
	#return Receta();
	pass

def buscarCoincidencias(receta, listaIngredientes):
	'''
	@listaIngredientes: numero de ingrediente que contiene el usuario
	@receta: receta con la cual buscaremos el numero de ingredientes de coincidencia
	Utilizaremos busqueda binaria ya que el atributo de receta.ingredientes contendra
	un arreglo ya ordena, asi el tiempo de respues sera rapido
	Tambien puede ser lineal
	Devolvera el numero de coincidencias
	'''
	coincidencias = 0
	for ingrediente in listaIngredientes:
		valor = busquedaLinealMejorada(receta.obtenerIngredientes(), len(receta.obtenerIngredientes()), ingrediente)
		if valor != -1:
			coincidencias += 1
	return coincidencias;


def busquedaLinealMejorada(A, n, x):
	encontrado = -1;
	for k in range(n):
		if(A[k] == x):
			encontrado = k;
			break;
	return encontrado;


def busquedaBinariaRecursiva(A, x, izquierda, derecha):
	if(izquierda > derecha):
		return -1;
	medio = math.floor((izquierda + derecha)/2);
	#print(medio);
	if(A[medio] == x):
		return medio;
	elif(A[medio] < x):
		return busquedaBinariaRecursiva(A, x, medio + 1, derecha);
	else:
		return busquedaBinariaRecursiva(A, x, izquierda, medio - 1);

'''
receta = Receta("Tostadas a la veracruzana")
#receta.setNombre("Tostadas a la veracruzana")
receta.agregarIngrediente("Ajo") #[0]
receta.agregarIngrediente("aguacate") #[1]
receta.agregarIngrediente("tomate") #[2]
receta.agregarIngrediente("LEChuga") #[3]
receta.agregarPreparacion("Cocer 20min a fuego lento")
print(receta)

coincidencias =  buscarCoincidencias(receta, ['Ajo'.upper(), 'lechuga'.upper()])
coincidenciasMaxima = coincidencias

print(coincidencias)
'''