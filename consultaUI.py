from tkinter import*
#from recetaUI import RecetaUI
import recetaUI
import tkinter.ttk as ttk 
import integracion
from tkinter import messagebox;

import menuUI

class ConsultaUI():

	def __init__(self):
	    self.raiz = Tk()
	    self.raiz.title("Chef en casa")
	    self.raiz.geometry("500x600")
	    #self.raiz.resizable(0,0)
	    self.frame1 = Frame(self.raiz).pack()
	    self.recetarioL = Label(self.frame1, text = "Recetario").pack()
	    
	    #Quiero agregar un botoncito de regresar pero quiero este en la esquina izquieda  de la ventana por eso puse plece
	    imgButton = PhotoImage(file = "img/lineDark19_32.png")
	    self.regresarBtton = Button(self.raiz, text = "Regresar", command = self.listenerRegresar, image = imgButton, relief = GROOVE).place(x = 2, y = 0)


		#Estos son los encabezados que va llevar nuestra tabla, es decir, nuestras columnas
	    lb_header = ['Recetario',""]
	    #Estas sera nusetra filas, es decir, nuestras recetas
	    lb_list = []
	    arbolRecetario = integracion.obtenerRecetario()
	    #print(arbolRecetario)
	    #Utlizamos un inorden porque asi tambien mostrar nuestro recetario
	    #de forma ordenada segun el nombre de la receta
	    lb_list = self.inorden(arbolRecetario.obtenerRaiz(), lb_list)
	    aux2 = []
	    for x in lb_list:
	    	aux = []
	    	#Primero crearemos una lista de dos elementos ["cadena","lo que sea"]
	    	#Esto es porque cuando conviertes una cadena a una tuple de descompone la
	    	#cadene por caracter, y lo que nosotros necesitasmo es que sea un tupla de una
	    	#cadena, y la unica manera es teniendo un lista de dos elemento la cual la primera 
	    	#posicion estara nuestra cadana, que queremos que se muestre y como segunda un valor cualquiera
	    	aux.append(x)
	    	aux.append("")
	    	aux2.append(tuple(aux))
	    lb_list = aux2

	    self.tree = ttk.Treeview(columns = lb_header, show = "headings", selectmode = 'browse')
	    self.scroll = Scrollbar(self.raiz, orient = "vertical", command = self.tree.yview)
	    self.scroll.pack(side = 'right', fill = Y)
	    self.tree.pack(side='top')
	    self.tree.configure(yscrollcommand=self.scroll.set)
	    for col in lb_header:
	    	self.tree.heading(col, text = col)
	    for item in lb_list:
	    	#Debe de ser un tupla, un valor constante
	    	self.tree.insert('','end', values = item)

	    self.mostrarBtton = Button(self.frame1, text = "Mostrar receta", command = self.listennerMostrar).pack()
	    self.raiz.mainloop()

	def listennerMostrar(self):
		#Primero tenemos que verificar que seleccione algo
		if(not self.tree.focus() == ""):

			#Cualquier de los dos metodos funciona para poder obtener el id del seleccionado
			item = self.tree.focus()
			#print(type(item))
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
			recetaUI.RecetaUI(receta)
		else:
			messagebox.showinfo("information","Debes de seleccionar una receta")
			#print("Debes de seleccionar una receta")
		pass

	def listenerRegresar(self):
		self.raiz.destroy()
		menuUI.MenuUI()

	def inorden(self, a, lb_list):
		'''
		Ulizaremos el recorrido inorden para consultar nuestras recetas y guardar los nombres
		en nuestra variable lb_list que sera las filas de la tabla
		@return lb_list Devolcera una lista de tupla que contendra los nombres de cada receta
		por que tupla porque en nuestro tabla deber ser de ese tipo
		'''
		if a == None:
			return None
		else:
			self.inorden(a.hijoIzq, lb_list)
			#print(str(a.val))
			lb_list.append((a.val.getNombre()))
			self.inorden(a.hijoDer, lb_list)
		return lb_list

#ConsultaUI()