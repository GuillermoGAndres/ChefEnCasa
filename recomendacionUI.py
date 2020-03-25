from tkinter import*
from recetaUI import RecetaUI
#Utilizaresmo el componenete de tkiniter llamado Treeview que se asemeja a una tabla
import tkinter.ttk as ttk 
import integracion
from tkinter import messagebox;

import buscarRecetaUI

class RecomendacionUI():

	def __init__(self, recetasRecomendadas):
		'''
		@param recetasRecomendadas es una lista de tuplas que continen
		(numeroCoincidencias, receta)

		'''
		self.raiz = Tk()
		self.raiz.title("Chef en casa")
		self.raiz.geometry("700x600");
		#self.raiz.resizable(False, False);
		self.frame1 = Frame(self.raiz).pack()
		self.menuL = Label(self.frame1, text = "Recetas recomendadas :").pack()

		#Quiero agregar un botoncito de regresar pero quiero este en la esquina izquieda  de la ventana por eso puse plece
		imgButton = PhotoImage(file = "img/lineDark19_32.png")
		self.regresarBtton = Button(self.raiz, text = "Regresar", command = self.listenerRegresar, image = imgButton, relief = GROOVE).place(x = 5, y = 5)

		#Estos son los encabezados que va llevar nuestra tabla, es decir, nuestras columnas
		lb_header = ['Receta', 'Coincidencias', 'Ingredientes que te faltan ']
		#Estas sera nusetra filas, es decir, nuestras recetas
		lb_list = [] #Tiene que tuplas
		#for tupla in recetasRecomendadas:
		#	print("-----------------")
		#	print("Coincidencia:",tupla[0])
		#	print("Receta:")
		#	print(tupla[1])
		#	print("------------------")


		for tupla in recetasRecomendadas:
			#orden es una variable auxliar que guardar una tupla que servira para mostrarlo en la
			#tablas de la interfaz, interpreta las columnas de la tabla
			orden = [] 
			#Obtenemos el nombre de la receta
			orden.append(tupla[1].getNombre())#Receta
			
			#Agregamos las coincidenias para mostrarlo en la tabla
			orden.append(tupla[0])

			#Asi obtenemos los numero de ingredientes que faltan para completar la receta
			# Total de ingredientesReceta - coincidencias que tiene con ella
			orden.append(len(tupla[1].obtenerIngredientes()) - tupla[0]) 
			
			lb_list.append(tuple(orden))
			#print(tuple(orden))

		self.tree = ttk.Treeview(columns = lb_header, show = "headings", selectmode = 'browse')
		#self.tree.grid(in_ = self.frame1)
		self.scroll = Scrollbar(self.raiz, orient = "vertical", command = self.tree.yview)
		self.scroll.pack(side = 'right', fill = Y) #
		self.tree.pack(side='top')
		self.tree.configure(yscrollcommand=self.scroll.set)
		for col in lb_header:
		    self.tree.heading(col, text = col)
		for item in lb_list:
		    #Debe de ser un tupla, un valor constante
		    self.tree.insert('','end', values = item)

		self.mostrarBtton = Button(self.frame1, text = "Mostrar", command = self.listennerMostrar).pack()
		self.raiz.mainloop()


	def listennerMostrar(self):
		if(not self.tree.focus() == ""):
			#Cualquier de los dos metodos funciona para poder obtener el id del seleccionado
			item = self.tree.focus()
			#item = self.tree.selection()[0]
			#muestra un diccionario con sus atributos del id seleccionado
			#print(self.tree.item(item))
			dic = self.tree.item(item)
			#print(dic['values']) #Muestra una lista[nombre, coincidencia]
			#print(dic['values'][0]) #Muestra solo la receta
			rutaReceta = "baseDatosRecetas/" + dic['values'][0].replace(" ","") + ".txt"
			receta = integracion.obtenerReceta(rutaReceta)
			#print(receta)
			self.raiz.destroy()
			RecetaUI(receta)
		else:
			messagebox.showinfo("information","Debes de seleccionar una receta")
			#print("Debes de seleccionar una receta")
		pass

	def listenerRegresar(self):
		self.raiz.destroy()
		buscarRecetaUI.BuscarRecetaUI()


#RecomendacionUI()