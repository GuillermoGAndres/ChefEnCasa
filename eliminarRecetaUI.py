from tkinter import*
import integracion
from tkinter import messagebox;

import menuUI
#Eliminar el
class EliminarRecetaUI():

	def __init__(self):
		self.raiz = Tk()
		#self.raiz.configure(background="#e0e1e3")
		self.raiz.title("Chef en casa")
		self.raiz.geometry("500x600");
		#self.raiz.resizable(False, False);
		self.frame1 = Frame(self.raiz) .pack()
		self.eliminarRecetaL = Label(self.frame1, text = "Eliminar receta").pack()

		#Quiero agregar un botoncito de regresar pero quiero este en la esquina izquieda  de la ventana por eso puse plece
		imgButton = PhotoImage(file = "img/lineDark19_32.png")
		self.regresarBtton = Button(self.raiz, text = "Regresar", command = self.listenerRegresar, image = imgButton, relief = GROOVE).place(x = 5, y = 5)

		self.escribaRecetaL = Label(self.frame1, text = "Escriba el nombre de la receta: ").pack()
		self.nombreReceta = StringVar();
		self.escribaRecetaEntry = Entry(self.frame1, textvariable = self.nombreReceta).pack()
		self.eliminarButton = Button(self.frame1, text = "eliminar", command = self.listennerEliminar).pack()

		self.raiz.mainloop()
	pass

	def listennerEliminar(self):
		#print(self.nombreReceta.get())
		nombreRecetaUsuario = self.nombreReceta.get().replace(" ","") #quitamos los espacios
		#print(nombreRecetaUsuario)
		#Primero tenemos que verifacar si existe esa receta
		nombresRecetas = integracion.obtenerArchivoRecetario()
		#print(nombresRecetas)
		indice = busquedaLineal(nombresRecetas, len(nombresRecetas), nombreRecetaUsuario)
		if( indice == -1):
			#print("No se encontro la receta")
			#messagebox.showinfo("information","No se encontra la receta, favor de revisar si lo escribiste correctamente.")
			#messagebox.showerror("error","No se encontra la receta, favor de revisar si lo escribiste correctamente.")
			messagebox.showwarning("warning","No se encontra la receta, favor de revisar si lo escribiste correctamente.")  
		else:	
			#print(indice)
			#1)Se puede utilizar lista.pop() si utilizamos indices
			item = nombresRecetas.pop(indice)
			#print(item)
			#2)Podemos utilizar tambien lista.remove()
			#item = nombresRecetas.remove(nombreRecetaUsuario)
			#print(item)
			#Una vez eliminado la receta en la lista de recetas
			#tenemos ahora que eliminar la receta en la base de datos
			#Para que exista fuerte cohesion y separacion de tareas con respecto a la
			#base de datos, vamos a llamar la funcion de eliminar receta de la capa de
			#integracion que es el intermediario de la base de datos y aplicacion, es el
			#unico script que se puede conectar con la base de datos para mayor seguridad
			integracion.eliminarReceta(nombreRecetaUsuario)
			integracion.ajustarArchivoRecetario(nombresRecetas)
			messagebox.showinfo("information","Se ha eliminado correctamente")
			self.raiz.destroy()
			EliminarRecetaUI()
			#print(nombresRecetas)

	def listenerRegresar(self):
		self.raiz.destroy()
		menuUI.MenuUI()

def busquedaLineal(A, n, x):
	encontrado = -1;
	for k in range(n):
		if A[k] == x:
			encontrado = k;
			break;
	return encontrado;

#EliminarRecetaUI()