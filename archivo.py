from src.metodos import (establecer_esperar_iteraciones,
                         obtener_modo_de_manejo, cambiar_modo_de_manejo,
                         nave_incrementar_potencia, nave_decrementar_potencia,
                         nave_rotar, nave_coordenada_x, nave_coordenada_y,
                         nave_largo, nave_alto, asteroide_coordenada_x,
                         asteroide_coordenada_y, asteroide_largo,
                         asteroide_alto)

#print("1 - Modo automatico")
#print("2 - Modo manual")

#if n == 1:
#print(obtener_modo_de_manejo())
def solucion():
  # Escribir su solucion dentro de esta funcion
  nave_incrementar_potencia()
  
  
  
  if obtener_modo_de_manejo()=="manual":
    print("-     MENU    -")
    print("1 - Continuar trayectoria por N interaciones")
    print("2 - Incrementar potencia")
    print("3 - Descrementar potencia")
    print("4 - Rotar")
    print("5 - Cambiar modo de manejo")
    print("0 - Salir")
  
    num = 0
    num = int(input("Ingrese un numero "))
  
    if num == 1:
        print("Has elegido continuar trayectoria por N interaciones")
        cantidad_iteraciones=int(input("Cantidad de iteraciones: "))
        establecer_esperar_iteraciones(cantidad_iteraciones) 
    elif num == 2:
        print("Has elegido Incrementar potencia")
        nave_incrementar_potencia()
    elif num  == 3: 
        print("Has elegido Decrementar potencia")
        nave_decrementar_potencia()
    elif num == 4:
        print("Has elegido Rotar")
        eje_y=input("arriba o abajo: ")
        eje_x=input("izquierda o derecha: ")
        nave_rotar(eje_x, eje_y)
    elif num == 5:
        print("Has elegido Cambiar modo de manejo")
       
        cambiar_modo_de_manejo()
    
    elif num == 0:
        print("Salir")
        exit()
    else:
        print("Ingrese una opcion correcta")

    
  if obtener_modo_de_manejo()=="auto":

    
    eje_x = asteroide_coordenada_x()-nave_coordenada_x()
    eje_y = asteroide_coordenada_y()-nave_coordenada_y()
   
    
    if eje_x > 0 and eje_y > 0:
      nave_rotar("derecha", "abajo")
    elif eje_x < 0 and eje_y < 0:
      nave_rotar("izquierda", "arriba")
    elif eje_x > 0 and eje_y < 0:
      nave_rotar("derecha", "arriba")
    elif eje_x < 0 and eje_y > 0:
      nave_rotar("izquierda", "abajo")
    elif eje_x == 0 and eje_y > 0:
      nave_rotar("", "abajo")
    elif eje_x == 0 and eje_y < 0:
      nave_rotar("", "arriba")
    elif eje_x > 0 and eje_y == 0:
      nave_rotar("derecha", "")
    else:
      nave_rotar("izquierda", "")
    
    pass
