

from arbol import Arbol
from arbol import busqueda

#from nodo import Nodo
def main():
    #Creo mi arbol

    miArbol = Arbol()
    #Agrego los valores de mi arbol
    #El primer valor que agregue sera mi raiz de mi arbol
    miArbol.agregar(8)
    #Agregar hijos
    miArbol.agregar(3)
    miArbol.agregar(10)
    miArbol.agregar(1)
    miArbol.agregar(6)
    miArbol.agregar(14)
    miArbol.agregar(4)
    miArbol.agregar(7)
    miArbol.agregar(9)
    #Imprimir arbol en preorden
    miArbol.imprimirPreorden()
    #miArbol.imprimirInorden()
    #Busqueda de un valor especifico
    #Devolvera el nodo subyacente
    print("---------------------------")
    nodo = busqueda(miArbol.obtenerRaiz(), 14)
    print("Nodo con el valor que contiene: ",nodo.val)
#    print(miArbol.obtenerRaiz().val)
    pass



main()