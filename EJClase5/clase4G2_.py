import re # Librería que permite compilar información para hacer operaciones más eficientes
class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema1(): # Separé los sistemas para que al usar un objeto tipo sistema dentro de una función no generara conflicto
    def __init__(self):
      self.__lista_pacientes = [] #Decidí cambiar nuevamente a lista para facilitar el recorrido de la información
      self.__numero_pacientes = len(self.__lista_pacientes)

class Sistema2():      
    def ingresarPaciente(self):
        # 1- solicito los datos por teclado
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))    
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")
        # 2- creo el objeto Paciente y le asigno los datos
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)        
        # 3- guardo el Paciente en  la lista        
        self.__lista_pacientes.append(p)
        # 4- actualizo la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        sis = Sistema1
        return sis.self.__numero_pacientes
    
    def verificarPac(self,cedula):
            encontrado = False
            for p in self.__lista_pacientes:
                if cedula == p.verCedula():
                    encontrado = True
                    break
            return encontrado
    
    def verLista(self):
        return self.__lista_pacientes
    
    def verDatosPaciente():
        sis = Sistema1()
        while True:
            try:
                TipoBusqueda = input("\nIngrese para:\n0. Busqueda por cédula o parte de ella \n1. Nombre o parte de él\n 2.Salir de la búsqueda>> ")
                if TipoBusqueda == 2:
                    break
                while True:
                  
                    try:
                     if TipoBusqueda == 0:
                        cedulav = input("Ingrese la cedula o parte de ella: ")
                        patron = re.complie(f".*{cedulav}.*")
                        c = 0
                        listadispobible = sis.verLista()
                        for p in listadispobible:
                                if patron.match(p.verCedula()):
                                    c += 1
                                    print("Nombre: " + p.verNombre())
                                    print("Cedula: " + str(p.verCedula()))
                                    print("Genero: " + p.verGenero())
                                    print("Servicio: " + p.verServicio())
                        if c == 0: 
                                print("No se tiene coincidencias.")
                     if TipoBusqueda == 1:
                            nombre = input("Ingrese el nombre o parte de él: ")

                            patron = re.complie(f".*{nombre}.*")
                            c = 0
                            listadispobible = sis.verLista()
                            for p in listadispobible:
                                if patron.match(p.verNombre()):
                                    c += 1
                                    print("Nombre: " + p.verNombre())
                                    print("Cedula: " + str(p.verCedula()))
                                    print("Genero: " + p.verGenero())
                                    print("Servicio: " + p.verServicio())
                                if c == 0: 
                                    print("No se tiene coincidencias.")
                    except:
                        ValueError, TypeError
                        print("Ingrese un número válido")
                        continue
                
            except:
                ValueError, TypeError
                print("Ingrese un número válido")
                continue
