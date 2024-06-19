import os
os.system("cls")


# Nombre del archivo
archivo = 'datosAlumnos.txt'

#pk primary key  
alumnos =   []

def leer_datos_archivo(archivo):
    # Lista para almacenar los datos
    lista_datos = []   

    # Abrimos el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
       
        for linea in file:
            # Eliminamos los espacios en blanco y los saltos de línea
            linea = linea.strip()
            # Dividimos la línea por comas
            datos = linea.split(',')
            # Creamos un diccionario con los datos
            lista_datos.append(datos[0])
            lista_datos.append(datos[1])
            lista_datos.append(int(datos[2]))

    return lista_datos

def buscar(rut):
    # Lista para almacenar los datos
    lista_datos = []   

    # Abrimos el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
       
        for linea in file:
            # Eliminamos los espacios en blanco y los saltos de línea
            linea = linea.strip()
            # Dividimos la línea por comas
            datos = linea.split(',')
            
            # Verificamos si el RUT coincide con el RUT buscado
            if datos[0] == rut:
                # Retornamos los datos como una lista
                return datos

    return -1

def eliminar(rut):
    # Lista para almacenar los datos actualizados
    lista_datos_actualizada = []
    
    existe=buscar(rut)
    
    if existe != -1:
        # Abrimos el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leemos cada línea del archivo
            for linea in file:
                # Eliminamos los espacios en blanco y los saltos de línea
                linea = linea.strip()
                # Dividimos la línea por comas
                datos = linea.split(',')
                # Verificamos si el RUT no coincide con el RUT a eliminar
                if datos[0] != rut:
                    # Si no coincide, añadimos el registro a la lista actualizada
                    lista_datos_actualizada.append(linea)
                #else:
                #    sw=0 #rut no existe
        
        # Abrimos el archivo en modo escritura para actualizar el contenido
        with open(archivo, 'w') as file:
            # Escribimos cada registro actualizado en el archivo
            for linea in lista_datos_actualizada:
                file.write(linea + '\n')
        return 1 #eliminado    
    else:
        return -1

def imprimir_datos(lista_datos):
    for i in range (0,len(lista_datos),3):
        print(f"{lista_datos[i]}, {lista_datos[i+1]}, {lista_datos[i+2]}")

def agregar_datos(rut, nombre, edad):
    # Abrimos el archivo en modo de agregar ('a')
    with open(archivo, 'a') as file:
        # Escribimos el nuevo registro en una nueva línea
        
        file.write(f"\n{rut},{nombre},{edad}")    

def modificar(rut_a_modificar, nuevo_nombre, nueva_edad):
    # Lista para almacenar los datos actualizados
    lista_datos_actualizada = []
    # Bandera para verificar si se encontró el RUT
    rut_encontrado = False
    
    # Abrimos el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
        for linea in file:
            # Eliminamos los espacios en blanco y los saltos de línea
            linea = linea.strip()
            # Dividimos la línea por comas
            datos = linea.split(',')
            # Verificamos si el RUT coincide con el RUT a modificar
            if datos[0] == rut_a_modificar:
                # Si coincide, modificamos el nombre y la edad
                datos[1] = nuevo_nombre
                datos[2] = str(nueva_edad)
                rut_encontrado = True
            # Añadimos el registro (modificado o no) a la lista actualizada
            lista_datos_actualizada.append(','.join(datos))
    
    # Si no se encontró el RUT, retornamos -1
    if not rut_encontrado:
        return -1
    
    # Abrimos el archivo en modo escritura para actualizar el contenido
    with open(archivo, 'w') as file:
        # Escribimos cada registro actualizado en el archivo
        for linea in lista_datos_actualizada:
            file.write(linea + '\n')
    
    # Retornamos 1 si se realizó la modificación
    return 1




# Leemos los datos del archivo
#alumnos = leer_datos_archivo(archivo)

#print(alumnos)
#os.system("pause")


rut=""
opcion=0
while opcion<=6:
    os.system("cls")
    print("Menù de Alumnos")
    print("1 Agregar")
    print("2 Buscar por rut")
    print("3 Eliminar por rut")
    print("4 ** Modificar **")
    print("5 Listar")
    print("6 Salir\n")
    opcion=int(input("Ingrese una opciòn [1-6]:  "))
    
    if opcion>=1 and opcion<=6:
        os.system("cls")
        match opcion:
            case 1: 
                print("\n Agregar Alumnos\n")
                #agregar
                print("Agregar datos a la Lista Alumnos \n")
                rut=input("Ingrese su rut:  ")
                nombre=input("Ingrese su nombre:  ")
                edad = int(input("Ingrese su edad:  "))
               
                agregar_datos(rut, nombre, edad)

            case 2: 
                rut=input("Ingrese un rut a buscar:  ")
                lista=buscar(rut)

                if lista !=-1:
                    print(lista)
                else:
                    print("Error, rut no existe")

            case 3: 
                
                rut=input("Ingrese un rut a eliminar:  ")
                lista=eliminar(rut)

                if lista !=-1:
                    print("rut eliminado")
                else:
                    print("Error, rut no existe")
                
                
            case 4: 
                print("\n Modificar\n")
                rut=input("Ingrese un rut a buscar:  ")
                
                lista=buscar(rut)

                if lista !=-1:                    
                    print("Rut encontrado")
                    print(lista[0]," ",lista[1]," ",lista[2])
                    print("\n")
                    nuevo_nombre=input("Ingrese el nuevo nombre: ")
                    nueva_edad  =int(input("Ingrese la nueva edad: "))
                    ret=modificar(rut, nuevo_nombre, nueva_edad)
                    print("\n Listo! datos modificados")                    
                else:
                    print("Error, rut no existe")

            case 5: 
               print("\n Listar Alumnos\n")

               alumnos=leer_datos_archivo(archivo)
               #print(alumnos)
               #os.system("pause")  
               imprimir_datos(alumnos)
               

        if opcion == 6:
            break
        os.system("pause")  
    else:
        print("Error, debe ingresar un valor entre 1 y 6")
        os.system("pause")     

print("Fin del menú")