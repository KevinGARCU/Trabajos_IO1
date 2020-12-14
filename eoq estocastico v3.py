
import numpy as np

def CantidadPedidosS(d,k,h):
    q=int(np.sqrt((2*d*k)/(h)))
    return q  #define la cantidad optima de pedidos

def CantidadOrdenQ(d,k,h,p):
    q=int(np.sqrt((2*d*k)/(h))*(np.sqrt((p+h)/(p))))
    return q  #Eleccion de la catidad de orden Q estocastico continua
    
def PuntoReordenR(u,K1,l,o):
    r=int(u+K1-l*o)
    return r  #Eleccion del punto de reorden R estocastico continua

def InventarioSeguridad1(Is1,r,u):
    Is1=int(r-u)
    return Is  #Inventario de Seguridad 1

def InventarioSeguridad2(Is2,K1,l,o):
    Is2=int(K1-l*o)
    return Is2  #Inventario de seguridad 2     

def menu():  #Menu de opciones
    opc = 50
    if (faltante=='No'): 
        CF = CanOpPedidosSF(d,k,h)
        n = NumeroPedidos (d,CF)
        t = TiempoEntrePedidos (CF,d)   #Si el problema es sin faltates ejecuta los respectivos procesos definidos anteriormente
    else: 
        CCF = CanOpPedidosCF(d,k,h,p)
        n = NumeroPedidos (d,qCF)
        t = TiempoEntrePedidos (CCF,d)
        defi = int(np.sqrt((2*d*k)/(h))*(np.sqrt((p+h)/(p))))  #Si el problema es con faltante recibe los parametros que se necesitan
    while (opc!=0):
      
        print ("\nMENU DE OPCIONES")
        print ("1. Cantidad optima de unidades por pedido.")
        print ("2. Número esperado de pedidos.")
        print ("3. Punto de reorden.")
        print ("0. SALIR.")
        opc = int (input("¿Que se desea conocer?\n"))   #El usuario escoge la variable que quiere conocer
        if (opc==1): 
            if (faltante=='No'):
                
                print ("La cantidad optima de pedidos es:")
                print ("Q = "+str(CCF)+" Unidades")  # contidad optima de pedidos sin faltantes
            else:
                
                print ("La cantidad optima de pedidos es:")
                print ("Q = "+str(CF)+" Unidades")   # Icontidad optima de pedidos con faltantes
        elif (opc==2):
           
            print ("El número esperado de pedidos es:")
            print ("N = "+str(N)+" Pedidos")   # Imprime el número esperado de pedidos
        elif (opc==3):
            
            print ("El tiempo entre pedidos es:")
            print ("t = "+str(t))    # Imprime el tiempo entre pedidos
        elif (opc==4):
            
            L = int (input("Ingrese el lead time:\n"))
            r = PuntodeReorden (dias,L,d)
            print ("El punto de reorden es:")
            print ("R = "+str(r))   # Pide el lead time y los dias trabajados del problema para calcular e imprimir el punto de reorden



print("MODELO EOQ Estocastico") 
d=float(input("Ingrese la demanda promedio: \n")) 
k=float(input("Ingrese el costo de preparación: \n"))
h=float(input("Ingrese el costo de mantener: \n"))
faltante=input("¿El modelo tiene faltantes? (Si/No) \n")
if faltante=='No':
    menu()                                                    #valores iniciales del problema
else:
    p=float(input("Ingrese el costo de faltantes : "))
    menu()


