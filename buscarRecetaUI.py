from tkinter import*
from tkinter import messagebox;
#from recomendacionUI import RecomendacionUI
import recomendacionUI

import logica
from tkinter import messagebox;
import menuUI
#@author Guillermo Gerardo Andres Urbano 
class BuscarRecetaUI():
        def __init__(self):
            self.raiz = Tk()
            self.raiz.title("Chef en casa")
            self.raiz.geometry("500x600")
            self.raiz.resizable(0,0);
            self.frame1 = Frame(self.raiz)
            self.chefEnCasaL = Label(self.frame1, text="Chef en casa").pack();
            #Quiero agregar un botoncito de regresar pero quiero este en la esquina izquieda  de la ventana por eso puse plece
            imgButton = PhotoImage(file = "img/lineDark19_32.png")
            self.regresarBtton = Button(self.raiz, text = "Regresar", command = self.listenerRegresar, image = imgButton, relief = GROOVE).place(x = 5, y = 5)

            self.ingresarIngredientesL = Label(self.frame1, text="Cuantos ingredientes tienes").pack();
            self.numIngredientes = StringVar() #Objeto de tkinter
            self.ingresarIngredientesEtry = Entry(self.frame1,textvariable=self.numIngredientes).pack();
            self.ingresarBtton = Button(self.frame1, text="Ingresar", command = self.listennerIngresar);
            self.ingresarBtton.pack();
            self.frame1.pack()
            self.frame2 = Frame(self.frame1)
            self.valorCaja = []
            #self.sb = Scrollbar(self.frame1)
            #self.sb.pack(side=RIGHT, fill = Y)
            #self.sb.config(command
            self.confirmarBtton = None
            self.frame2.pack()
            self.raiz.mainloop()

        def listennerIngresar(self):
            if( not self.estaVacioIngredientes()):
                #Creare un arreglo el cual contendra los valores
                #de cada caja
                self.valorCaja = []
                for i in range(0, int(self.numIngredientes.get())):
                    self.valorCaja.append(StringVar())
                #Crear numIngredientes cajas para ingredientes
                for i in range(0,int(self.numIngredientes.get())):
                    ingredientesL = Label(self.frame2, text ="Escribir Ingrediente " + str(i+1)+ ":").pack()
                    cajasEtry = Entry(self.frame2, textvariable=self.valorCaja[i]).pack()
                self.ingresarBtton.config(state = "disable")
                self.confirmarBtton = Button(self.frame2, text = "Confirmar", command = self.listennerConfirmar).pack()
                self.frame2.pack()
            else:
                messagebox.showinfo("information","Favor de ingresar el numero de ingredientes")

        
        def listennerConfirmar(self):
            #print("Boton de confirmar")
            listaIngredientes = []
            for ingre in self.valorCaja:
                listaIngredientes.append(ingre.get().upper()) #Convertimos todo a mayuscula para sea nuestro estandar
            #print(listaIngredientes)
            #Me devolvera una lista con la recetas recomendas
            recetasRecomendadas = logica.algoritmoAMR(listaIngredientes)
            self.raiz.destroy()
            recomendacionUI.RecomendacionUI(recetasRecomendadas)


            pass
        def estaVacioIngredientes(self):
            '''Verifica que caja(Entry) no este vacia'''
            return self.numIngredientes.get() == "";


        def listenerRegresar(self):
            self.raiz.destroy()
            menuUI.MenuUI()
            pass
#Descomentar para probar esta parte de la aplicacion
#BuscarRecetaUI()
