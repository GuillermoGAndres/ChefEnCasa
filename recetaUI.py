from tkinter import*
from tkinter import font
import menuUI

class RecetaUI():

	def __init__(self, receta):
		self.raiz = Tk()
		self.raiz.title("Chef en casa")
		self.raiz.geometry("1050x600");

		#Quiero agregar un botoncito de regresar pero quiero este en la esquina izquieda  de la ventana por eso puse plece
		imgButton = PhotoImage(file = "img/home.png")
		self.regresarBtton = Button(self.raiz, text = "Regresar", command = self.listenerRegresar, image = imgButton, relief = GROOVE).place(x = 5, y = 5)
		
		#self.raiz.resizable(False, False);
		self.frame1 = Frame(self.raiz).pack(side = LEFT)
		#self.recetaL = Label(self.frame1, text = str(receta)).pack();
		#fontTitulo = font.Font( family = "/fonts/droid-serif/DroidSerif-Italic.ttf", size = 30)
		
		self.tituloL = Label(self.frame1, text = receta.getNombre(), font = "Times 40", pady=27).pack()
		
		self.ingredienteL = Label(self.frame1, text = "Ingredientes", font = "Helvetica 20 italic").pack()
		#self.ingredientesL = Label(self.frame1, text = )
		
		#print(receta.obtenerIngredientes())
		listaIngre = ""
		for ingre in receta.obtenerIngredientes():
			listaIngre += "*" + ingre + "\n"
		
		self.listaIngreL = Label(self.frame1, text = listaIngre, font = "Courier 15").pack()

		self.preparacionLabel = Label(self.frame1, text = "Preparacion", font = "Helvetica 20 italic").pack()

		self.preparacionL = Label(self.frame1, text = receta.obtenerPreparacion(), font = "Courier 15").pack()
		
		self.raiz.mainloop()		
		pass

	def listenerRegresar(self):
		self.raiz.destroy()
		menuUI.MenuUI()