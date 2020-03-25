
#@author Guillermo Gerardo Andres Urbano 
class Receta():

	def __init__(self, nombreReceta = None):
		self.nombre = nombreReceta
		self.ingredientes = list()
		self.preparacion = ""

	def agregarIngrediente(self, ingredient):
		if(type(ingredient) is type("")):
			self.ingredientes.append(ingredient.upper())
		pass

	def agregarPreparacion(self, preparation):
		if(type(preparation) is type("")):
			self.preparacion = preparation.upper()

	def obtenerIngredientes(self):
		return self.ingredientes

	def obtenerPreparacion(self):
		return self.preparacion

	def ordenarIngredientes(self):
		self._quicksort(self.obtenerIngredientes(), 0, len(self.obtenerIngredientes()) - 1)
		pass

	def getNombre(self):
		return self.nombre

	def setNombre(self, nombre):
		self.nombre = nombre

	def __str__(self):
		receta = ""
		nombre = self.getNombre() + "\n"
		ingredient = "Ingredientes\n"
		procedimiento = "Procedimiento\n"
		for item in self.obtenerIngredientes():
			ingredient += item + "\n"
		receta += nombre + ingredient + procedimiento + self.obtenerPreparacion() + "\n";
		return receta;

	#Ahora vamos a darle al objeto una manera de poder hacer comparacion entre recetas segun nuestro criterio
	#Nuestro criterio de comparacion sera los nombres de las recetas, el que inicie con "A" sera < "Z" ya que 
	#ya que "A" es menor por su correspodiente ASQUI 65 y sera sera 90, ademas de que A inicia primero y despues Z 
	#en el abecedario
	#Esto nos ayudara a poder hacer comparaciones entre objetos, para eso tenemos que sobreescribir los metodos:
	#Esto es como si implementaras comparteTo de Java
	#Python ya identifica que si es mayor entonces ya sabre que es menor
	def __gt__(self, otro):
		return self.getNombre().replace(" ","").upper() > otro.getNombre().replace(" ","").upper()

	def __ge__(self, otro):
		return self.getNombre().replace(" ","").upper() >= otro.getNombre().replace(" ","").upper()
	def __eq__(self, otro):
		return self.getNombre().replace(" ","").upper() == otro.getNombre().replace(" ","").upper()






	#Guion bajo indican que son metodos privados en python
	def _intercambiar(self,A, x, y):
		tmp = A[x];
		A[x] = A[y];
		A[y] = tmp;


	def _particionar(self,lista, p, r):
		i = p - 1;
		x = lista[r];
		for j in range(p, r):
			if(lista[j] <= x):
				i = i + 1;
				self._intercambiar(lista, i, j);
		self._intercambiar(lista, i + 1, r);
		return i + 1;


	def _quicksort(self,lista , p, r):
		if(p < r):
			q = self._particionar(lista, p, r);
			self._quicksort(lista, p, q -1);
			self._quicksort(lista, q+1, r);

'''
lista = ["tomate", "ZANAHORIA", "lechuga", "ajo", "berenjena"]
procedimiento = '''
'''Freir la lechuga y despues cocerla 10min
a fuego lento, sofreirla constantemente'''
'''
myRecipe = Receta();
for item in lista:
	myRecipe.agregarIngrediente(item)


myRecipe.agregarPreparacion(procedimiento)
print(myRecipe)
myRecipe.ordenarIngredientes()
print(myRecipe)
'''
'''receta = Receta()
receta.setNombre("Tostadas a la veracruzana")
receta.agregarIngrediente("Ajo")
receta.agregarPreparacion("Cocer 20min a fuego lento")
print(receta)'''

'''
receta1 = Receta("Arroz con leche")

receta2 = Receta("Atun")


if(receta1 < receta2):
	print("es menor")
'''