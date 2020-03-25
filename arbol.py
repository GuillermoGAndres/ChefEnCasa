
#from estructuraArbol.nodo import Nodo
from nodo import Nodo
import logica

#Este arbol sera nuestro arbol de recetas, un arbol solamente para nuestra applicacion de recetas
#Arbol de busqueda
class Arbol:
    
    def __init__(self):
        self.raiz = None
        self.listaCoincidencias = []
    
    def obtenerRaiz(self):
        return self.raiz

    def getListaCoincidencias(self):
        return self.listaCoincidencias

    def agregar(self, val):
        if(self.raiz == None):
            self.raiz = Nodo(val)
        else:
            self.agregarNodo(val, self.raiz)
    
    def agregarNodo(self, val, nodo):
        if(val < nodo.val):
            if(nodo.hijoIzq != None):
                #Significa que tiene ojo izquierde tiene que revisar para sea un arbol de busqueda
                self.agregarNodo(val, nodo.hijoIzq)
            else:
                nodo.hijoIzq = Nodo(val)
        else:
            if(nodo.hijoDer != None):
                self.agregarNodo(val, nodo.hijoDer)
            else:
                nodo.hijoDer = Nodo(val)

        pass

    def preorden(self, a):
        if a == None:
            return None
        else:
            print(str(a.val))
            self.preorden(a.hijoIzq)
            self.preorden(a.hijoDer)


    def inorden(self, receta, listaIngre):
        '''
        Vamos a sobreescribir este metodo para darle la funcionalidad de nuestra app
        En el recorrido, buscara el numero de coincidencia de cada receta que esta guardada en cada
        nodo, y guardara ese valor y la receta(indice/o referencia en donde se encuentra esa receta) se 
        almacenara en una tupla, dada esa tupla que contien el numero de coincidencia y la receta, la guardaremos
        en una lista, en esta lista contendremos cada numero Coincidencia de cada receta
        @retur regresara una lista de tuplas que contendran el numero de coincidencias de cada receta y la receta
        '''
        if receta == None:
            return None
        else:
            self.inorden(receta.hijoIzq, listaIngre)
            #print(str(a.val))
            #Aqui va todo el procesamiento de cada nodo
            #------------------------------------------------
            coincidencias = logica.buscarCoincidencias(receta.val, listaIngre)
            self.listaCoincidencias.append( (coincidencias, receta.val) )
            #Con este print verifico como se esta moviendo el arbol
            #print(str(receta.val))
            
            #----------------------------------------------
            self.inorden(receta.hijoDer, listaIngre)


    #def imprimirInorden(self):
    #    if(self.raiz != None):
    #        self.inorden(self.raiz)
    #    pass

    def imprimirPreorden(self):
        if(self.raiz != None):
            self.preorden(self.raiz)
        pass

    def imprimirInorden(self):
        if(self.raiz != None):
            self.recorridoInorden(self.raiz)
        pass
    def recorridoInorden(self, a):
        if a == None:
            return None
        else:
            self.recorridoInorden(a.hijoIzq)
            print(str(a.val))
            self.recorridoInorden(a.hijoDer)

    def mostrarCoincidencias(self):
        for item in self.listaCoincidencias:
            print(item)
        pass



def busqueda(nodo, llave):
    if(nodo == None or llave == nodo.val):
        return nodo
    if( llave < nodo.val):
        return busqueda(nodo.hijoIzq, llave)
    else:
        return busqueda(nodo.hijoDer, llave)


'''
    def inorden(self, a):
        if a == None:
            return None
        else:
            self.inorden(a.hijoIzq)
            print(str(a.val))
            self.inorden(a.hijoDer)
'''