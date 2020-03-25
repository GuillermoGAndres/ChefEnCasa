from tkinter import*
#from buscarRecetaUI import BuscarRecetaUI
import buscarRecetaUI

#from agregarRecetaUI import AgregarRecetaUI #*****
import agregarRecetaUI #***

#from eliminarRecetaUI  import EliminarRecetaUI
import eliminarRecetaUI

#from consultaUI import ConsultaUI
import consultaUI
#@author Guillermo Gerardo Andres Urbano 
class MenuUI():

    def __init__(self):
        self.raiz = Tk()
        #self.raiz.configure(background="#e0e1e3")
        self.raiz.title("Chef en casa")
        self.raiz.geometry("500x630");
        #self.raiz.resizable(False, False);
        self.frame1 = Frame(self.raiz) .pack()
        logo = PhotoImage(file = "img/logo340.png") #, width = 300, height = 300
        self.logoL = Label(self.frame1, image = logo).pack();
        self.asistenteL = Label(self.frame1, text = '''
        Hola soy spunk tu asistente para ayudarte a eligir la
        receta ideal para ti, tendremos cuatro opciones:
        1) La primera es para escoger tu receta ideal con los ingrendientes
        que tienes.
        2) Y la otra para poder ayudar a la comunidad registrando tus recetas
        y poder crecer este gran aplicacion.
        3) Puedes eliminar una receta para actualizarla si hubo un error.
        4) Y la cuarta es que puedes tambien consultar todo nuestro recetario
         que tenemos.
        Elige la opcion que mas guste''',
        font = "Helvetica 10 italic",
        pady = 30).pack()

        self.buscarRecetaBtton = Button(self.frame1, text = "Buscar receta ideal para mi",
                                 command = self.listennerBuscarReceta, pady = 3,
                                bg = "#0099de",
                                activebackground = 'gray',
                                font = 'Verdana 10 bold italic', bd = 2 ).pack();

        self.agregarRecetaBtton = Button(self.frame1, text = "Agregar nueva receta", 
                                command = self.listennerAgregarReceta,
                                font = 'Verdana 10 bold italic',
                                bg = '#00b05c').pack();

        self.eliminarRecetaBtton = Button(self.frame1, text = "Eliminar receta",
                                   command = self.listennerEliminarReceta,
                                   font = 'Verdana 10 bold italic',
                                   bg = '#e03626').pack()
        
        self.consultarRecetarioBtton = Button(self.frame1, text = "Consultar recetario",
                                       command = self.listennerConsultarRecetario,
                                       font = 'Verdana 10 bold italic',
                                       bg = '#ff7f0d').pack()
        self.raiz.mainloop()


    def listennerBuscarReceta(self):
        self.raiz.destroy()
        buscarRecetaUI.BuscarRecetaUI()
        pass

    def listennerAgregarReceta(self):
        self.raiz.destroy()
        #print(dir(agregarRecetaUI))
        agregarRecetaUI.AgregarRecetaUI()
        #AgregarRecetaUI()
        pass

    def listennerEliminarReceta(self):
        self.raiz.destroy()
        eliminarRecetaUI.EliminarRecetaUI()
        pass

    def listennerConsultarRecetario(self):
        #print("Click")
        self.raiz.destroy()
        consultaUI.ConsultaUI()
        pass



def main():
    MenuUI()
    pass

if __name__ == "__main__":
    main()
