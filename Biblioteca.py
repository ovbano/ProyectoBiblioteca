
'''
A continuación se mostrará un código que permitirá organizar los libros nuevos 
que se ingresen en una biblioteca mediante la programacion orientada a objetos.
Además de llevar un control en el prestamo de libros tomando en cuenta el tiempo
en que se va a realizar el préstamos. Para realizar eso se deberá importar la 
siguiente librería (calendar, que importa a c y a datetime), la cual permitira utilizar el formato real de la hora
actual. Finalmente el código será realizado por medio de lista (arrays) que 
contendran la información correspondiente a cada genero de libro. A continuación 
se evidencian las clases y los métodos correspondientes.

class catalogo:

    def __init__(self) -> None:
        Inicializadon de contador para llevar registro de nuevos datos
        y concatenarlos con los existentes.

        self.contador = [0, 0, 0, 0, 0, 0, 0]

    def aventura(self):
        Método que contendrá la información del género específico
        como el nombre, el autor y el editorial.

    def terror(self):
        Método que contendrá la información del género específico
        como el nombre, el autor y el editorial.

    def drama(self):
        Método que contendrá la información del género específico
        como el nombre, el autor y el editorial.

    def cienFiccion(self):
        Método que contendrá la información del género específico
        como el nombre, el autor y el editorial.

    def comedia(self):
        Método que contendrá la información del género específico
        como el nombre, el autor y el editorial.

    def romance(self):
        Método que contendrá la información del género específico
        como el nombre, el autor y el editorial.

    def infantil(self):
        Método que contendrá la información del género específico
        como el nombre, el autor y el editorial.

    def mostrarCatalogo(self):
        Método que permitirá ver el formato de visualización de 
        las listas de generos de libros dentro de la biblioteca.
'''

from calendar import c #Librería que define un calendario de módulo incorporado que maneja las operaciones relacionadas con el calendario.
import datetime #Importa el módulo de fecha y hora y muestre la fecha actual

print("|                     Bienvenido a la Biblioteca                        |")

#Creación de super clase
class catalogo:
    #Atributo constructor del programa 
    def __init__(self) -> None:
        #Contador que permitirá concatenar nuevos datos con los datos ya existentes.
        self.contador = [0, 0, 0, 0, 0, 0, 0]

    #Metodos del la super clase 
    def asignacion(self):
        #Asignando funciones, para poder utilizar varibles
        cata.aventura()
        cata.terror()
        cata.drama()
        cata.infantil()
        cata.cienFiccion()
        cata.romance()
        cata.comedia()

    '''
    En esta parte se crearon los métodos para la super clases cuales constaran 
    de una dunción que contendra unas lista con la información respectiva de 
    cada género del catalogo de la biblioteca. Las Funciones constan de un numbre
    autor, editorial...
    '''

    def aventura(self):
        self.nomAventura = ["La isla del tesoro", "Robinson Crusoe", "Moby-Dick", "Viaje al centro de la Tierra",
                            "El corsario negro"]
        self.autorAventura = ["Robert Louis Stevenson", "Daniel Defoe", "Herman Melville", "Julio Verne",
                              "Emilio Salgari"]
        self.editAventura = ["Fontana", "W.Taylor", "Richard Bentley", "Hetzel", "Verbum"]
        self.contador[0] = len(self.nomAventura)

    def terror(self):
        self.nomTerror = ["It", "Drácula", "El resplandor", "Apartamento 16", "Dejame entrar"]
        self.autorTerror = ["Stephen King", "Bram Stoker", "Stephen King", "Adam L. G. Nevill", "John Ajvide Lindqvist"]
        self.editTerror = ["debolsillo", "Porrúa", "Doubleday", "Planeta Editorial", "Espasa "]
        self.contador[1] = len(self.nomTerror)

    def drama(self):
        self.nomDrama = ["Las dos esfinges", "La sombra de tu memoria", "Sueños de papel", "Khalil",
                         "El perro del hortelano"]
        self.autorDrama = ["L. Sancho", "Noelia Amarillo", "María Amorós", "Susana López Pérez", "Lope de Vega"]
        self.editDrama = ["Casa del Libro", "Noelia Amarillo", "Casa del Libro", "Alianza Editorial", "CATEDRA"]
        self.contador[2] = len(self.nomDrama)

    def cienFiccion(self):
        self.nomCCFF = ["Dune", "Fahrenheit 451", "El problema de los tres cuerpos", "El juego de Ender",
                        "Un mundo feliz"]
        self.autorCCFF = ["Frank Herbert", "Ray Bradbury", "Liu Cixin", "Orson Scott Card", "Aldous Huxley"]
        self.editCCFF = ["Chilton Books", "Minotauro", "NOVA", "Tor Books", "DEBOS"]
        self.contador[3] = len(self.nomCCFF)

    def comedia(self):
        self.nomComedia = ["La conjura de los necios", "Ha vuelto", "El proyecto esposa", "Maldito karma",
                           "Cuentos sin plumas"]
        self.autorComedia = ["John Kennedy", "Timur Vermes", "Graeme Simsion", "David Safier", "Woody Allen"]
        self.editComedia = ["Louisiana State University Press", "Casa del Libro", "Salamandra", "Rowohlt Verlag GmbH",
                            "Tusquets"]
        self.contador[4] = len(self.nomComedia)

    def romance(self):
        self.nomRomance = ["Cumbres borrascosas", "Jane Eyre", "Un cuento perfecto", "Bajo la misma estrella",
                           "Eleanor & Park"]
        self.autorRomance = ["Emily Brontë", "Charlotte Brontë", "Elísabet Benavent", "John Green", "Rainbow Rowell"]
        self.editRomance = ["Alma", "Smith, Elder & Company", "SUMA", "Dutton Books", "St. Martin's Press"]
        self.contador[5] = len(cata.nomRomance)

    def infantil(self):
        self.nomInfantil = ["El principito", "El monstruo de colores", "El pollo Pepe", "A qué sabe la luna?",
                            "La historia interminable"]
        self.autorInfantil = ["Antoine de Saint-Exupéry", "Anna Llenas", "Nick Denchfield", "Michael Grejniec",
                              "Michael Ende"]
        self.editInfantil = ["Reynal & Hitchcock", "Flamboyant", "EDICIONES SM", "Kalandraka", "Thienemanns Verlag"]
        self.contador[6] = len(cata.nomInfantil)

    """
    La siguiente función muestra el catalogo completo antes y despues de asignar cualquierr
    otro libro a la lista. De tal manera que los muestra mediante el formato establecido 
    Nombre-Autor-Editorial. Para lograr eso se necesitó utilizar una estructura repetitiva for.
    """
    def mostrarCatalogo(self):
        print(
            "______________________________________________\n CATALOGO\n ______________________________________________")
        print("Formato de visualizacion: Nombre-Autor-Editorial")
        print(
            "______________________________________________\nLibros de Aventura\n")
        for x in range(cata.contador[0]):
            print(cata.nomAventura[x], "-", cata.autorAventura[x], "-", cata.editAventura[x])
        print("______________________________________________")

        print("Libros de Terror\n")
        for x in range(cata.contador[1]):
            print(cata.nomTerror[x], "-", cata.autorTerror[x], "-", cata.editTerror[x])
        print("______________________________________________")

        print("Libros de Drama\n")
        for x in range(cata.contador[2]):
            print(cata.nomDrama[x], "-", cata.autorDrama[x], "-", cata.editDrama[x])
        print("______________________________________________")

        print("Libros de Ciencia Ficción\n")
        for x in range(cata.contador[3]):
            print(cata.nomCCFF[x], "-", cata.autorCCFF[x], "-", cata.editCCFF[x])
        print("______________________________________________")

        print("Libros de Comedia\n")
        for x in range(cata.contador[4]):
            print(cata.nomComedia[x], "-", cata.autorComedia[x], "-", cata.editComedia[x])
        print("______________________________________________")

        print("Libros de Romance\n")
        for x in range(cata.contador[5]):
            print(cata.nomRomance[x], "-", cata.autorRomance[x], "-", cata.editRomance[x])
        print("______________________________________________")

        print("Libros Infantiles\n")
        for x in range(cata.contador[6]):
            print(cata.nomInfantil[x], "-", cata.autorInfantil[x], "-", cata.editInfantil[x])
        print("______________________________________________")

'''
La clase catálogo correspondrá a la super clases que heredará sus atributos
y métodos a una sub clase denominada libNuevo(catalogo): la cual contendrá
los atributos y métodos caracteristicos para agrega un libro nuevo a la lista
ya existente en la super clase catalogo. Esta clase se la declararía de la 
siguiente manera:

class libNuevo(catalogo):
    
    def __init__(self, a):
        Aquí aparecen los atributos de la sub clase que usaremos para llenar 
        datos de los libros nuevos que valla a ingresar a la lista de libros
        existentes.

        self.nombre = []
        self.editorial = []
        self.fechas = []
        self.autor = []
        self.datoLib=[""]
        self.a=0

    def agregarLib(self):
        Dentro de este método existe una serie de campos que el usuario deberá 
        llenar para que se pueda agregar a la lista existente, aplicando una 
        condición para ir validando cada método que ya existe dentro de nuestra 
        super clase catalogo.

    def menu (self):
        Esta función va a presentar

    def registro (self):
        Esta fución

'''

class libNuevo(catalogo):
    #Atributo constructor de la sub clase
    def __init__(self,a ):
        #Para esta sub clase se tienen los siguientes atributos los cuales 
        #también son una lista a manera de arrays.
        super().__init__()
        self.nombre = []
        self.editorial = []
        self.fechas = []
        self.autor = []
        self.datoLib=[""]
        self.a=0 #Contador
    #Menú principal del programa
    def menu(self):

        opcion = 0
        
        while opcion != 5:
            print("________________")
            print("Menu Principal")
            print("1- Visualizar Catalogo")
            print("2- Agregar libros")
            print("3- Visualizar registros")
            print("4- Solicitar prestamo de libros")
            print("5- Salir")
            print("________________")
            opcion = int(input("Ingrese su opcion:"))
            if opcion == 1:
                cata.mostrarCatalogo()
            elif opcion == 2:
                nuevo.agregarLib()
            elif opcion == 3:
                nuevo.subMenu()
            elif opcion == 4:
                pres.prestarLib()
                pres.b=pres.b+1
            elif opcion == 5:
                "Salir"
    
    def subMenu(self):
        op_regis=0
        while op_regis != 3:
                    print("________________")
                    print("Registros")
                    print("1- Registro de Libros ingresados")
                    print("2- Registro de prestamos")
                    print("3- Salir")
                    print("________________")
                    op_regis = int(input("Ingrese su opcion:"))
                    if op_regis == 1:
                        nuevo.registroLib()
                        nuevo.a = nuevo.a + 1
                    elif op_regis == 2:
                        pres.registroprestamo()
                    elif op_regis == 3:
                        print("Salir")

    """
    Para este método se van a realizan una serie de condiciones que validen 
    el ingreso de los géneros ya establecidos, pues que antes de registrar 
    un libro primeramente deberá digitar el número de libros que desea registrar
    también el género al que pertenece... 
    """

    def agregarLib(self):

        print("Ha seleccionado la opcion para agregar libros nuevos a la biblioteca")
        print(
            "Los generos disponibles para agregar libros son: \n -Aventura \n -Terror \n -Drama \n -Ciencia Ficción \n -Comedia \n -Romance \n -Infantil")
        genero = input("Ingrese el genero del/los libro/s que desea agregar a la biblioteca: ")
        minusGen = genero.lower() #Función que permite transformar una cadena de caracte a minúscula
        #Validación del ingreso de datos.
        while not (
                minusGen == "aventura" or minusGen == "terror" or minusGen == "drama" or minusGen == "ciencia ficcion" or minusGen == "comedia" or minusGen == "romance" or minusGen == "infantil"):
            print("El genero que ingreso no se encuentra en la biblioteca \n Por favor ingrese un genero disponible")
            genero = input("")
            minusGen = genero.lower()

        if minusGen == "aventura":
            cantidad = int(input("Cuantos libros nuevos desea agregar al genero de Aventura?: "))

            for x in range(cantidad):
                print("Ingrese el nombre del libro", x + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", x + 1)
                self.autor.append(input())

                print("Ingrese el editorial", x + 1)
                self.editorial.append(input())

            """
            Las siguientes funcines permiten que se agresen o permite que se concatenen
            los nuevos rigistros con los existentes ubicandolos al final de la lista 
            declarada.
            """
            cata.nomAventura.extend(self.nombre)
            cata.autorAventura.extend(self.autor)
            cata.editAventura.extend(self.editorial)
            cata.contador[0] = cata.contador[0] + cantidad

        elif minusGen == "terror":
            cantidad = int(input("Cuantos libros nuevos desea agregar al genero de Terror?: "))
            x = 0
            for x in range(cantidad):
                print("Ingrese el nombre del libro", x + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", x + 1)
                self.autor.append(input())

                print("Ingrese el editorial", x + 1)
                self.editorial.append(input())

            """
            Las siguientes funcines permiten que se agresen o permite que se concatenen
            los nuevos rigistros con los existentes ubicandolos al final de la lista 
            declarada.
            """
            cata.nomTerror.extend(self.nombre)
            cata.autorTerror.extend(self.autor)
            cata.editTerror.extend(self.editorial)
            cata.contador[1] = cata.contador[1] + cantidad

        elif minusGen == "drama":
            cantidad = int(input("Cuantos libros nuevos desea agregar al genero de Drama?: "))
            x = 0
            for x in range(cantidad):
                print("Ingrese el nombre del libro", x + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", x + 1)
                self.autor.append(input())

                print("Ingrese el editorial", x + 1)
                self.editorial.append(input())

            """
            Las siguientes funcines permiten que se agresen o permite que se concatenen
            los nuevos rigistros con los existentes ubicandolos al final de la lista 
            declarada.
            """
            cata.nomDrama.extend(self.nombre)
            cata.autorDrama.extend(self.autor)
            cata.editDrama.extend(self.editorial)
            cata.contador[2] = cata.contador[2] + cantidad

        elif minusGen == "ciencia ficcion":
            cantidad = int(input("Cuantos libros nuevos desea agregar al genero de Ciencia Ficción?: "))
            x = 0
            for x in range(cantidad):
                print("Ingrese el nombre del libro", x + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", x + 1)
                self.autor.append(input())

                print("Ingrese el editorial", x + 1)
                self.editorial.append(input())

            """
            Las siguientes funcines permiten que se agresen o permite que se concatenen
            los nuevos rigistros con los existentes ubicandolos al final de la lista 
            declarada.
            """
            cata.nomCCFF.extend(self.nombre)
            cata.autorCCFF.extend(self.autor)
            cata.editCCFF.extend(self.editorial)
            cata.contador[3] = cata.contador[3] + cantidad

        elif minusGen == "comedia":
            cantidad = int(input("Cuantos libros nuevos desea agregar al genero de Comedia?: "))
            x = 0
            for x in range(cantidad):
                print("Ingrese el nombre del libro", x + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", x + 1)
                self.autor.append(input())

                print("Ingrese el editorial", x + 1)
                self.editorial.append(input())

            """
            Las siguientes funcines permiten que se agresen o permite que se concatenen
            los nuevos rigistros con los existentes ubicandolos al final de la lista 
            declarada.
            """
            cata.nomComedia.extend(self.nombre)
            cata.autorComedia.extend(self.autor)
            cata.editComedia.extend(self.editorial)
            cata.contador[4] = cata.contador[4] + cantidad

        elif minusGen == "romance":
            cantidad = int(input("Cuantos libros nuevos desea agregar al genero de Romance?: "))
            x = 0
            for x in range(cantidad):
                print("Ingrese el nombre del libro", x + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", x + 1)
                self.autor.append(input())

                print("Ingrese el editorial", x + 1)
                self.editorial.append(input())

            """
            Las siguientes funcines permiten que se agresen o permite que se concatenen
            los nuevos rigistros con los existentes ubicandolos al final de la lista 
            declarada.
            """
            cata.nomRomance.extend(self.nombre)
            cata.autorRomance.extend(self.autor)
            cata.editRomance.extend(self.editorial)
            cata.contador[5] = cata.contador[5] + cantidad

        elif minusGen == "infantil":
            cantidad = int(input("Cuantos libros nuevos desea agregar al genero Infantil?: "))
            x = 0
            for x in range(cantidad):
                print("Ingrese el nombre del libro", x + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", x + 1)
                self.autor.append(input())

                print("Ingrese el editorial", x + 1)
                self.editorial.append(input())

            """
            Las siguientes funcines permiten que se agresen o permite que se concatenen
            los nuevos rigistros con los existentes ubicandolos al final de la lista 
            declarada.
            """
            cata.nomInfantil.extend(self.nombre)
            cata.autorInfantil.extend(self.autor)
            cata.editInfantil.extend(self.editorial)
            cata.contador[6] = cata.contador[6] + cantidad

        fecha = datetime.datetime.now()
        fechaa = datetime.datetime.strftime(fecha, '%d, %B %Y')
        self.fechas.append(fechaa)
        for x in range(len(self.nombre)):
            self.datoLib[self.a] += self.nombre[x] + ", "
        print("El/Los libro/s:", self.nombre, "\n Se agregaron correctamente al catalogo en el genero de", genero)
        print("En la fecha ", fechaa)
        for x in range(len(self.nombre)):
            self.nombre.pop()
            self.autor.pop()
            self.editorial.pop()

    def registroLib(self):

        print("Registro de libros ingresados a la biblioteca")
        print("_______________")
        for x in range(len(self.datoLib)):
            print("El/Los libro/s:", self.datoLib[x], "\n fueron ingresados al catalogo")
            print("En la fecha ", self.fechas[x])
            print("_______________")

"""
La siguiente clase fué creada para llevar el registro de los prestamos de libros
dentro de la biblioteca, la clase consta de los atributos y metodos correspondientes
para su correcto funcionamiento. Acontinuación se declaran la clase prestamo:

class prestamo:

    def __init__(self):
        Contiene el costructor que permite llamar a las funciones asi mismas
        En esta parte se ubican las variables en asignación a listas.

    def prestarLib(self):
        Dentro de esta función habrán los campos correspondientes par que el
        usuario lo llenes, dichos datos proporcionan información sobre el prestamo
        de los libros, asi como los nombres del cliente que presta los libros
        y la fecha en la que se deberá entregar el libro.

    def registroprestamo(self):
        Con esta función lo que se esta imprimientdo son los datos ingresados
        por el cliente en la funición anterior, la cual atraves de la biblioteca
        determinará la fecha exacta a la que deberá regresar el libro.

"""

class prestamo:
    #Atributos con el Costructor de la clase
    def __init__(self):
        self.nomCliente = []
        self.apelliCliente=[]
        self.id=[]
        self.nomLibro = []
        self.tiemPrestamo = [""]
        self.fechaPress =[]
        self.dia=0
        self.b=0
    #Métodos de la clase
    def prestarLib(self):
        #Compos que proporcionan información sobre los prestamosde libros correspondientemente
        #al género que valla a señalar el usuario.
        print("A solicitado prestar un libro a la biblioteca\nIngrese algunos datos y condiciones para realizar este proceso")
        self.nomCliente.append(input("Ingrese su nombre: "))
        self.apelliCliente.append(input("Ingrese su apellido: "))
        self.id.append(input("Ingrese su numero de identificacion/cedula: "))
        genero = input("Ingrese el genero del libro que desea prestar: ")
        minusGen = genero.lower()
        while not (minusGen == "aventura" or minusGen == "terror" or minusGen == "drama" or minusGen == "ciencia ficcion" or minusGen == "comedia" or minusGen == "romance" or minusGen == "infantil"):
            print("El genero que ingreso no se encuentra en la biblioteca \n Por favor ingrese un genero disponible")
            genero = input("")
            minusGen = genero.lower()

        if minusGen == "aventura":
            nom=input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(cata.nomAventura,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            if busquedaLib(cata.nomAventura,nom) == True:
                self.nomLibro.append(nom)

        elif minusGen == "terror":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(cata.nomTerror,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            if busquedaLib(cata.nomTerror,nom) == True:
                self.nomLibro.append(nom)

        elif minusGen == "drama":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(cata.nomDrama,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            if busquedaLib(cata.nomDrama,nom) == True:
                self.nomLibro.append(nom)

        elif minusGen == "ciencia ficcion":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(cata.nomCCFF,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            if busquedaLib(cata.nomCCFF,nom) == True:
                self.nomLibro.append(nom)

        elif minusGen == "comedia":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(cata.nomComedia,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            if busquedaLib(cata.nomComedia,nom) == True:
                self.nomLibro.append(nom)

        elif minusGen == "romance":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(cata.nomRomance,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            if busquedaLib(cata.nomRomance,nom) == True:
                self.nomLibro.append(nom)

        elif minusGen == "infantil":
            nom = input("Ingrese el nombre del libro de que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(cata.nomInfantil,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            if busquedaLib(cata.nomInfantil,nom) == True:
                self.nomLibro.append(nom)
        #Tiempo que el usuario valla aprestar los libros
        print("Puede solicitar el prestamo por un tiempo limitado de 3 meses\nIngrese en numeros los mes y dias, que dispodra del libro")
        mes=int(input("Meses: "))
        while mes<1 or mes>3:
            mes=int(input("El numero que ingreso esta fuera de rango, con respecto al tiempo de prestamo segun el mes\nIntente nuevamente: "))
        #Validación de presamos de libros
        if mes == 3:
            self.dia=0
        elif mes == 2:
            self.dia = int(input("Debido a que a ingresado para 2 meses el prestamo, podra ingresar como maximo 30 dias: "))
            while self.dia < 0 or self.dia > 30:
                self.dia = int(input("Ingreso mal los dias\nIntente nuevamente: "))
        elif mes == 1:
            self.dia = int(input("Puede ingresar como maximo 60 dias"))
            while self.dia < 0 or self.dia > 60:
                self.dia = int(input("Ingreso mal los dias\nIntente nuevamente: "))
        #Cálculos para determinar el dia exacto en el que se debe devlver los libros.
        self.tiemPrestamo[self.b]=str(mes)+" meses con "+str(self.dia)+" dias"
        fecha = datetime.datetime.now()
        fechaa = datetime.datetime.strftime(fecha, '%d, %B %Y')
        self.fechaPress.append(fechaa)
        print("Felicidades!, a realizado el proceso de prestamo con exito\nDisfrute del libro")
    #Enseñar los datos a usuario.
    def registroprestamo(self):
        print("Registro de Prestamo realizados")
        print("_______________")
        for x in range(len(self.nomCliente)):
            print("El/La Señor/a:", self.nomCliente[x], self.apelliCliente[x],"con ID:",self.id[x])
            print("Solicito prestar el libro: ", self.nomLibro[x],"con tiempo de",self.tiemPrestamo[x])
            print("En la fecha", self.fechaPress[x])
            print("_______________")

#Algoritmo de busque binaria
"""
Este algoritmo de busqueda se cumple siempre y cuando el usuario ingrese el mismo nombre
que se declaró en la parte de arriba de la lista, de ser el caso contrario quedará atrapado 
en un bucle hasta que vuelva a ingresar correctamente el nombre.
"""
def busquedaLib(lista,valor):
    primero=0
    ultimo=len(lista)-1
    encontrado=False

    while primero <= ultimo and not encontrado:
        mitad=(primero+ultimo)//2

        if lista[mitad]==valor:
            encontrado=True
        else:
            if valor<lista[mitad]:
                ultimo=mitad-1
            else:
                primero=mitad+1

    return encontrado
#Instanciar objetos de clases y subclases.
cata = catalogo()
nuevo = libNuevo(catalogo)
pres=prestamo()
#Llamar a los métodos de cada clase correspondiente mente.
cata.asignacion()
nuevo.menu()