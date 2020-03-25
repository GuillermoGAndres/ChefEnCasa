from tkinter import*
from tkinter import messagebox;
from receta import Receta

#from menuUI import MenuUI #****
import menuUI #****
import pickle #Libreria para serializar objetos

#@author Guillermo Gerardo Andres Urbano 
class AgregarRecetaUI():

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Chef en casa")
        self.raiz.geometry("600x700")
        #self.raiz.resizable(0,0)
        self.frame1 = Frame(self.raiz)
        self.agregarRecetaL = Label(self.frame1,text="Agregar Receta").pack()
        #Quiero agregar un botoncito de regresar pero quiero este en la esquina izquieda  de la ventana por eso puse plece
        imgButton = PhotoImage(file = "img/lineDark19_32.png")
        self.regresarBtton = Button(self.raiz, text = "Regresar", command = self.listenerRegresar, image = imgButton, relief = GROOVE).place(x = 5, y = 5)

        self.numeroIngreL = Label(self.frame1, text="Numero de ingredientes: ").pack()
        self.numIngre = StringVar()
        self.numIngreEtry = Entry(self.frame1, textvariable = self.numIngre)
        self.numIngreEtry.pack()
        self.ingresarButton = Button(self.frame1, text = "Ingresar", command = self.listennerIngresar)
        self.ingresarButton.pack()
        self.nombreRecetaL = None
        self.nombreReceta = StringVar()
        self.nombreRecetaEtry = None
        self.valorCaja = []
        self.cajaTexto = None
        self.listoButton = None
        self.frame2 = Frame(self.frame1);
        self.frame1.pack()
        self.raiz.mainloop()
        pass

    def listennerIngresar(self):
        if(not self.estaVacioIngresar()):
            self.nombreRecetaL = Label(self.frame2, text = "Nombre de la receta").pack()
            self.nombreRecetaEtry = Entry(self.frame2, textvariable = self.nombreReceta).pack()
            self.valorCaja = []
            for i in range(0, int(self.numIngre.get())):
                self.valorCaja.append(StringVar())
            for i in range(0, int(self.numIngre.get())):
                ingredientesL = Label(self.frame2, text ="Escribir Ingrediente " + str(i+1)+ ":").pack()
                caja = Entry(self.frame2, textvariable = self.valorCaja[i]).pack()
            self.ingresarButton.config(state="disable")
            self.numIngreEtry.config(state = "disable")
            escribirRecetaL = Label(self.frame2, text = "Escribir procediento de la receta: ").pack()
            self.sb = Scrollbar(self.frame2)  
            self.sb.pack(side = RIGHT, fill = Y)
            self.cajaTexto = Text(self.frame2, height = 10, width = 50, yscrollcommand = self.sb.set )
            self.cajaTexto.config(padx = .2, pady = .2)
            self.sb.config( command = self.cajaTexto.yview )
            #self.cajaTexto.insert(INSERT, "@")  
            self.cajaTexto.pack()
            self.listoButton = Button(self.frame2, text = "Listo", command = self.listennerListo)
            self.listoButton.pack()
            self.frame2.pack()
        else:
            messagebox.showinfo("information","Favor de ingresar un numero")
        pass

    def listennerListo(self):
        #Primero tenemos que verificar que llene todos los campos

        #Aqui es donde crearemos nuestro objeto Receta
        nuevaReceta = Receta(self.nombreReceta.get())
        for ingre in self.valorCaja:
            nuevaReceta.agregarIngrediente(ingre.get())
        process = self.cajaTexto.get(1.0, 100.0)
        #1.0 a 5.0 es el tañano del Caja de Text para que el usuario escriba la receta
        #if process == "@":
        #    print("Esta vacio")
        #else:
        #    print(process)
        nuevaReceta.agregarPreparacion(process)
        try:
            self._agregarBaseDatosReceta(nuevaReceta)
        except:
            print("No se agrego correctamen vuelva a intentar")
        
        messagebox.showinfo("information","Se ha agregado correctamente al recetario")
        self.raiz.destroy()
        AgregarRecetaUI()
        #print(nuevaReceta)
        pass

    def listenerRegresar(self):
        #print("regreso")
        self.raiz.destroy()
        menuUI.MenuUI()


    def _agregarBaseDatosReceta(self, receta):
        #Con esto serializamos la receta
        with open('baseDatosRecetas/' + receta.getNombre().replace(" ", "") + ".txt", "wb") as file:
            #replace para no haya espacion en blanco en el nombre del archivo
            pickle.dump(receta, file)
            file.close()

        #Con esto lo guardadomos en el recetario.txt para despues poder extraerlos
        with open('baseDatosRecetas/recetario.txt', 'a') as recetario:
            recetario.write(receta.getNombre().replace(" ", "") + "\n")
            recetario.close()
        pass

    def estaVacioIngresar(self):
        return self.numIngre.get() == "";
        pass

    def estaVacioCampoIngre(self):
        #Tenemos que iterar cada campo para verificar su contenido
        for ingrediente in self.cajaTexto:
            if(ingrediente.get() == ""):
                return True
        return False

    def estaVacioCampoPrepare(self):
        #Verificamos el campo
        pass

#Preguntar si funcion es correcto colocarla como metodo de la clase o mejor afuera
#como una funcion externa
#def eliminarEspacion(cadena):
    #pass

#*** Significa que tengo que investigarn el por que debe ser asi la importacion de los modulos
#tiene que ver acerca de los modulos el lenguaje python, hay una interferencia cuando dos modulos se importan
#de manera from module import class cuando cada modulo se necesita de unos mismo cada script
#necesita de cada uno 
#RESPUESTA:
#Ya se porque, es porque cuando importas el script el scripy tambien esta importando cosas y entre esas cosas
#se importanto asi mismo con sus mismo componentes
#Aqui en python existe dos maneras:
#Si al importar un script y en el script se importando al script que lo esta importando
#Puede ver dos maneras de verlos si:
#si se esta importando de esta fomra
#from modulo import classs
#Marcara error
#en cambio si se importa de esta forma:
#import modulo
#No lo hara a pesar que se importando asi mismos
#Como conclusion puedes importarte a si mismo de otro script si se importa
#de esta manera.

#Descomentar para probar esta parte de la aplicacion
#AgregarRecetaUI()
