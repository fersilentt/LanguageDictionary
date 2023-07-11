# IMPORTANDO MODULOS


# Importamos la biblioteca de Tkinter que permite diseñar
# toda la interfaz

# ttk = biblioteca de Tkinter que permite diseñar toda la interfaz
from tkinter import ttk


# Importamos todo el modulo de Tkinter

# tkinter = permite crear interfaces de Escritorio con Python
from tkinter import *


# Importamos el modulo de Message Box

# messagebox = este modulo permite mostrar mensajes de dialogo, lo
#              vamos a usar para eliminar los datos
from tkinter import messagebox


# Importamos el modulo de Tkinter nuevamente, para poder
# agregat el scroll a treeview
import tkinter as tk



# Importamos este modulo para obtener una ruta absoluta de
# nuestro proyecto, para poder importar las imagenes para 
# nuestros botones
import os



# Importamos este modulo para poder ejecutar scripts de Python
import subprocess




# Importamos este modulo para poder abrir el archivo de base de datos
# y el directorio donde se va a crear la base de datos
from tkinter import filedialog



# Importamos ñps tipos de letra de Tkinter, para despues mostrarlos
# en un Listbox
from tkinter import font







# Importamos este modulo para poder inertar el path, de donde se encuentran 
# los archivos del CRUD, de esta manera podremos importar nuestros archivos
# independientemmente de cualquier carpeta de donde se encuentren
import sys

# os.path.abspath("src") = obtenemos la ruta absoluta del proyecto para desepues importar
#                          los archivos
file = os.path.abspath("src")

# Agregamoso la ruta absoluta de nuestro proyeto, para que reconozca la ruta de importacion
# de los archivos que realizan el CRUD
sys.path.insert(0, file)































class Ventana:


    # Creamos una funcion, para crear un constructor de la clase "Ventana"

    # self = es una referencia al instancia actual de la clase, y se utiliza para acceder
    #        a las variables que pertenecen a la clase, podemos llámarlo como queramos, pero
    #        tiene que ser el primer parámetro de cualquier función en la clase

    # window = parametro que espera recibir el constructor de la clase y que tendra la
    #          iniciacion del metodo que va a arrancar la ventana
    def __init__(self, window):



        # Abrimos los archivos que contienen la configuracion de la interfaz de la aplicacion 
        
        # Abrimos el archivo .txt que contiene el tipo de letra de los componentes del formulario
        f_font_type = open('src/settings/font-type.txt', 'r')
        self.file_font_type = f_font_type.read()
        f_font_type.close()


        # Abrimos el archivo .txt que contiene el tamaño de letra de los componentes del formulario
        f_font_size = open('src/settings/font-size.txt', 'r')
        self.file_font_size = f_font_size.read()
        f_font_size.close()


        # Abrimos el archivo .txt que contiene el tamaño de los componentes del formulario
        f_size_components = open('src/settings/size-components.txt', 'r')
        self.file_size_components = f_size_components.read()
        f_size_components.close()


        # Abrimos el archivo .txt que contiene el tamaño de las cabeceras del Grid
        f_size_components_grid = open('src/settings/size-components-grid.txt', 'r')
        self.file_size_components_grid = f_size_components_grid.read()
        f_size_components_grid.close()





        # Almacenamos el parametro "window" que recibe el constructor en un propiedad llamada
        # "self.wind"

        # self. = primer parametro del contructor y hace referencia a la instancia actual
        #         de la clase

        # .wind = propiedad donde se va almacenar lo que reciba el parametro "window", puede
        #         tener cualquier nombre
        self.wind = window



        # Añadimos un titulo a la ventana
        self.wind.title('Dictionary English')






        # Damos una resolucion a nuestra venta con la finalidad de que todos los campos que vamos 
        # agregando a nuestra lista entren y la ventana no se muestre en cualquier parte de la ventana,
        # si no en el centro este metodo lo hemos usado para centrar en la pantalla
        w = self.wind.winfo_reqwidth()
        h = self.wind.winfo_reqheight()


        ws = self.wind.winfo_screenwidth()
        hs = self.wind.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.wind.geometry('+%d+%d' % (x, y))




       
        


        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario

        # self.wind = aqui indicamos donde va a estar posicionado el Frame, aqui le estamos
        #             indicando que va a estar dentro de la ventana "window"

        # text = '' = aqui le estoy indicando el titulo que va a tener
        #             el Frame, aqui no va a tener titulo
        frame = LabelFrame(self.wind, text = '')


        # Creamos un frame que va a contener los botones de las opciones de nuestra aplicacion
        frame01 = LabelFrame(self.wind, text = '')









        

        # Ahora posicionamoe el Frame de los botones del CRUD

        # frame = variable que almacena el Frame que anteriormente hemos creado

        # grid = metodo que nos permite indicar en que posicion de la ventana va a estar nuestro boton
        #        o entrada de texto, esto es una grilla invisible, que nos ayudara a colocar  nuestros
        #        elementos de acuerdo a la posicion que queramos

        # row=0 = esto indica que este elemento va a estar en la fila 0 de nuestra grilla, el valor
        #         se lo indica en pixeles

        # column=0 = esto indica que este elemento va a estar en la columna 0 de nuestra grilla

        # columnspan=3 = esto indica cuantas columnas de nuestra grilla va abarcar nuestra ventana
        #                es decir va a ser columnas vacias sin nada de contenido, es decir con esto vamos
        #                a centrar el frame

        # pady=20= esto es un padding, indica un espaciado ineterno de cada elemento, para que los elementos no
        #          se vean tan juntos, aqui le indicamos en pixeles el espaciado de arriba y abajo
        frame.grid(row=1, column=0, columnspan=3, pady=5, sticky = W)

        # Ahora posicionamos el Frame de las opciones de nuestra aplicacion
        frame01.grid(row=0, column=0, columnspan=3, sticky = W)

        









        # Importamos las imagenes de nuestro proyecto para usarlas  como iconos en nuestros botones

        # Imagenes de las opciones de nuestra aplicacion
        self.img_open_database = PhotoImage(file=os.path.abspath("src/static/open-database.png"))
        self.img_create_database = PhotoImage(file=os.path.abspath("src/static/create-database.png"))
        self.img_update_application = PhotoImage(file=os.path.abspath("src/static/update-application.png"))
        self.img_settings = PhotoImage(file=os.path.abspath("src/static/settings.png"))


        # Imagenes del CRUD de nuestra aplicacion

        # PhotoImage = esta funcion permite importar imagenes
        # file = esto permite dar la ruta de donde se encuentra la imagen
        # os.path.abspath("src/static/add.png") = obtenemos la ruta absoluta del proyecto para abrir la imagen
        self.img_add= PhotoImage(file=os.path.abspath("src/static/add.png"))
        self.img_update= PhotoImage(file=os.path.abspath("src/static/update.png"))
        self.img_delete= PhotoImage(file=os.path.abspath("src/static/delete.png"))
        self.img_view= PhotoImage(file=os.path.abspath("src/static/view.png"))
        self.img_duplicate_data= PhotoImage(file=os.path.abspath("src/static/duplicate-data.png"))
        self.img_refresh= PhotoImage(file=os.path.abspath("src/static/refresh.png"))
        
       





        # Botones de la aplicacion

        # Creamos los botones que van a realizar las opciones de nuestra aplicacion
        ttk.Button(frame01, image=self.img_open_database, command=self.open_file_database).grid(row=0, column=0, sticky = W)
        ttk.Button(frame01, image=self.img_create_database, command=self.create_file_database).grid(row=0, column=1, sticky = W)
        ttk.Button(frame01, image=self.img_update_application, command=self.update_application).grid(row=0, column=2, sticky = W)
        ttk.Button(frame01, image=self.img_settings, command=self.settings).grid(row=0, column=4, sticky = W)
        
        








        # Creamos los botones que van a realizar el CRUD

        # image = esta propiedad permite poner una imagen en el boton
        ttk.Button(frame, image=self.img_add, command=self.add_window).grid(row=0, column=0, sticky = W)
        ttk.Button(frame, image=self.img_update, command=self.update_window).grid(row=0, column=1, sticky = W)
        ttk.Button(frame, image=self.img_delete, command=self.delete_window).grid(row=0, column=2, sticky = W)
        ttk.Button(frame, image=self.img_view, command=self.view_window).grid(row=0, column=3, sticky = W)
        ttk.Button(frame, image=self.img_duplicate_data, command=self.duplicate_data).grid(row=0, column=4, sticky = W)
        ttk.Button(frame, image=self.img_refresh, command=self.validation_database_options).grid(row=0, column=5, sticky = W)
        
        





        # Creamos un label y un campo de texto donde podremos buscar algun dato
        # que necesitemos
        Label(frame, text = 'Search:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row=0, column=6)

        entry_t = Entry(frame, font=("{}".format(self.file_font_type), self.file_font_size))
        entry_t.grid(row=0, column=7, sticky = W+E)
        entry_t.bind('<KeyRelease>', self.scankey_t)
        









        # Creamos un label que va a funcionar como mensaje despues de realizar una accion

        # Creamos el label y lo almacenamos en una propiedad con el nombre de "message"

        # text='' = aqui no le pasamos ningun texto ya que desde las otras funciones le vamos 
        #           a pasar un texto propio que queramos

        # fg='green' = esto indica el color que va a tener el mensaje
        self.message = Label(text='', font=("{}".format(self.file_font_type), self.file_font_size), fg='green')

        # Posicionamos el label dentro del Frame
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)







        # Creamos una tabla para que liste los datos

        # Guardamos la tabla en una propieedad de la clase

        # .tree = nombre de la tabla que va a ser llamada en diferentes funciones
        # ttk.Treeview = esto permite crear una tabla o grilla desde Tkinter
        # height=10 = estas son la cantidad de filas que va a mostrar la tabla
        # columns=("Firtsname", "module") =  estas son la cantidad de columnas que va a mostrar la tabla
        self.tree = ttk.Treeview(height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8'))

        # Ahora damos una posicion a la tabla para que se muestre
        self.tree.grid(row=4, column=0, columnspan=2)



        # Ahora agregamos encabezados a la tabla

        # '#0' = esto indica el numero de columna donde va a ir el encabezado
        # text= 'word' = este va a ser el nombre que el encabezado va a mostrar
        # anchor=CENTER = esto es para indicarle que el encabezado vaya centrado
        self.tree.heading('#0', text= 'N°', anchor=CENTER) 
        self.tree.heading('#1', text= '', anchor=CENTER)
        self.tree.heading('#2', text= 'Word', anchor=CENTER)
        self.tree.heading('#3', text= 'Phonemic', anchor=CENTER)
        self.tree.heading('#4', text= 'Pronunciation', anchor=CENTER)
        self.tree.heading('#5', text= 'Type', anchor=CENTER)
        self.tree.heading('#6', text= 'Lesson', anchor=CENTER)
        self.tree.heading('#7', text= 'Module', anchor=CENTER)
        self.tree.heading('#8', text= 'Meaning', anchor=CENTER)
        



        # Cambiamos el tamaño de las columnas para que no se vea tan separado
        self.tree.column('#0', width=40)

        # stretch=NO = con esto evitamos que la columna se muestre, esta es la columna del id, y la
        #              necesitamos para actualizar los datos
        self.tree.column('#1', width=0, stretch=NO)
        self.tree.column('#2', width=self.file_size_components_grid)
        self.tree.column('#3', width=self.file_size_components_grid)
        self.tree.column('#4', width=self.file_size_components_grid)
        self.tree.column('#5', width=self.file_size_components_grid)
        self.tree.column('#6', width=self.file_size_components_grid)
        self.tree.column('#7', width=self.file_size_components_grid)
        self.tree.column('#8', width=self.file_size_components_grid)



        # Creamos un estilo para cambiar el tamaño de letra de las cabeceras de las columnas de
        # nuestra lista

        # font=(None, 10) = aqui establecemos el  tamaño de letra, en "None", ponemos el tipo de letra
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("{}".format(self.file_font_type), self.file_font_size, "bold"))
        style.configure("Treeview", font=("{}".format(self.file_font_type), self.file_font_size))


        
        # Ahora agregamos unn scrollbar a la lista 
        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=4, column=2, sticky='ns')








        # Creamos un Label para mostrar la ruta de la base de datos que hemos guardado
        Label(text = 'Saved database path: ', font=("{}".format(self.file_font_type), 9)).grid(row=5, column=0, columnspan=2, sticky=W)
        
        # Label que va a recibir la ruta de base de datos o un mensaje de que no existe
        self.path_database = Label(text='', font=("{}".format(self.file_font_type), 9), fg='blue')
        self.path_database.grid(row=5, column=1, sticky=W)







        # Llamammos a la funcion que permite validar las opciones de nuestra base de datos, como indicarnos el path de la
        # base de datos, si se ha cargado la base de datos, etc, con esto evitamos que se cree la base de datos automaticamente
        # en el caso que no exista
        self.validation_database_options()
    


        

      
       


        

















   
    # FUNCIONES PARA MOSTRAR LAS VENTANAS


    # Creamos una funcion para mostrar una ventana flotante en donde vamos a
    # ingresar los datos
    def add_window(self):

        # Aqui abrimos una nueva ventana para agergar los datos

        # Creamos una ventana encima de la anterior y la almacenamos en una variable

        # self.edit_wind = variable que va almacenar la nueva variable
        # Toplevel() = esto crea una ventana encima de la anterior
        self.add_window = Toplevel()

        # Creamos un titulo para la nueva ventana y la almacenamos en una variable
        self.add_window.title = 'Add Dictionary'




        # Evitamos que el usuario pueda maximizar la ventana y tambien bloqueamos el boton de maximizar
        self.add_window.resizable(width=False, height=False)




        # Damos una resolucion a nuestra venta con la finalidad de que todos los campos que vamos 
        # agregando a nuestra lista entren y la ventana no se muestre en cualquier parte de la ventana,
        # si no en el centro este metodo lo hemos usado para centrar en la pantalla
        w = self.add_window.winfo_reqwidth()
        h = self.add_window.winfo_reqheight()


        ws = self.add_window.winfo_screenwidth()
        hs = self.add_window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.add_window.geometry('+%d+%d' % (x, y))




        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario

        # self.wind = aqui indicamos donde va a estar posicionado el Frame, aqui le estamos
        #             indicando que va a estar dentro de la ventana "window"

        # text = '' = aqui le estoy indicando el titulo que va a tener
        #             el Frame
        frame = LabelFrame(self.add_window, text = 'Register a dictionary', font=("{}".format(self.file_font_type), self.file_font_size, "bold"))




        # Ahora posicionamoe el Frame que hemos creado

        # frame = variable que almacena el Frame que anteriormente hemos creado

        # grid = metodo que nos permite indicar en que posicion de la ventana va a estar nuestro boton
        #        o entrada de texto, esto es una grilla invisible, que nos ayudara a colocar  nuestros
        #        elementos de acuerdo a la posicion que queramos

        # row=0 = esto indica que este elemento va a estar en la fila 0 de nuestra grilla, el valor
        #         se lo indica en pixeles

        # column=0 = esto indica que este elemento va a estar en la columna 0 de nuestra grilla

        # columnspan=3 = esto indica cuantas columnas de nuestra grilla va abarcar nuestra ventana
        #                es decir va a ser columnas vacias sin nada de contenido, es decir con esto vamos
        #                a centrar el frame

        # pady=20= esto es un padding, indica un espaciado ineterno de cada elemento, para que los elementos no
        #          se vean tan juntos, aqui le indicamos en pixeles el espaciado de arriba y abajo
        frame.grid(row=0, column=0, columnspan=3, pady=20)





        # Creamos un label y una caja de texto para ingresar el nuevo "word"

        # Label = permite crear un texto en la ventana

        # frame = aqui indicamos donde va a estar posicionado el Label, aqui le estamos
        #         indicando que va a estar dentro del Frame que hemos creado anteriormente

        # text='word: ' = aqui le estoy indicando el texto del label

        # grid() = esto permite posicionar el elemento Label(), como anteriormente se ha hecho
        #          con el frame

        # font() = aqui establecemos el tipo y tamaño de letra

        # self.file_font_type = aqui se encuentra el tipo de letra que hemos importado de nuestro archivo
        #                       .txt, en la funcion principal de este archivo

        # self.file_font_size = aqui se encuentra el tamaño de letra que hemos importado de nuestro archivo
        #                       .txt, en la funcion principal de este archivo
        Label(frame, text = 'Word:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 1, column = 1)

        # Creamos un campo de entrada para ingresar el word

        # word = aqui guardamos el campo de texto en una variable

        # Entry(frame) = esto representa una entrada, es decir una caja de texto donde
        #              insertaremos los valores

        # self.ffile_size_components = aqui se encuentra el tamaño de los componentes que hemos importado de nuestro archivo
        #                              .txt, en la funcion principal de este archivo
        word = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))

        # Ahora posicionamos el campo de entrada
        word.grid(row = 1, column = 2)

        
        
        Label(frame, text = 'Phonemic:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 3, column = 1)
        phonemic = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        phonemic.grid(row = 3, column = 2)


        Label(frame, text = 'Pronunciation:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 5, column = 1)
        pronunciation = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        pronunciation.grid(row = 5, column = 2)


        Label(frame, text = 'Type:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 7, column = 1)
        type = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        type.grid(row = 7, column = 2)


        
        Label(frame, text = 'Lesson:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 9, column = 1)
        lesson= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        lesson.grid(row = 9, column = 2)

        
        Label(frame, text = 'Module:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 11, column = 1)
        module= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        module.grid(row = 11, column = 2)

        # Creamos un label y una caja de texto para ingresar el nuevo "meaning"

        # Text = aqui en vez de crear una caja de texto normal creamos un Text Area, ya
        #        que vamos a ingresar un texto un poco largo
        Label(frame, text = 'Meaning:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 13, column = 1)
        meaning= Text(frame, width=self.file_size_components, height = 3, font=("{}".format(self.file_font_type), self.file_font_size))
        meaning.grid(row = 13, column = 2)



        # Creamos un label que va a funcionar como mensaje despues de realizar una accion
        self.message_aw = Label(frame, text='', font=("{}".format(self.file_font_type), self.file_font_size), fg='red')
        self.message_aw.grid(row=14, column=2, sticky=W+E)



        # Creamos un boton para poder insertar los datos

        # lambda = permite ejecutar una funcion en esta misma ventana
        # add_dictionary() = funcion que va a permitir insertar los datos
        # word.get(), lesson.get()....) = son parametros que espera recibir la funcion
        # sticky=W+E = esto indica que abarque todo el ancho posible de nuestra ventana, de Oeste a Este
        # meaning.get(1.0, "end-1c") = para obtener la informacion ingresada en el Text Area, es obligatorio agregar estos parametros
        Button(frame, text = 'Add', font=("{}".format(self.file_font_type), self.file_font_size), command = lambda: self.add_dictionary(
            word.get(), phonemic.get(), pronunciation.get(), type.get(), lesson.get(), module.get(), meaning.get(1.0, "end-1c"))).grid(row = 15, column = 2, sticky=W+E)
        
        # Ejecutamos los eventos de la ventana
        self.add_window.mainloop()












    # Creamos una funcion para mostrar una ventana flotante en donde vamos a
    # editar los datos
    def update_window(self):

        # Realizamos una limpieza de nuestro mensaje o label, en el caso que tenga algun dato
        self.message['text'] = ''

        # Creamos un try-catch, para evitar errores, en el caso que el usuario no  haya
        # seleccionado ningun dato para actualizar

        # En el caso que se haya selleccionado una fila de datos, vamos a obtener los
        # datos y los almacenamos en variables

        # Aqui no agregamos el campo "meaning", ya que este valor va directo en el Text Area,
        # porque es la unica manera que hemos encontrado para pasarle el valor
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            word = self.tree.item(self.tree.selection())['values'][1]
            phonemic = self.tree.item(self.tree.selection())['values'][2]
            pronunciation = self.tree.item(self.tree.selection())['values'][3]
            type = self.tree.item(self.tree.selection())['values'][4]
            lesson = self.tree.item(self.tree.selection())['values'][5]
            module = self.tree.item(self.tree.selection())['values'][6]
            meaning = self.tree.item(self.tree.selection())['values'][7]

        # Mostramos un mensaje de error para que el usuario seleccione una fila de datos
        # que necesita editar
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return

       


        # Aqui abrimos una nueva ventana para editar los datos
        self.update_window = Toplevel()
        self.update_window.title = 'Update Dictionary'



        # Evitamos que el usuario pueda maximizar la ventana y tambien bloqueamos el boton de maximizar
        self.update_window.resizable(width=False, height=False)



        # Damos una resolucion a nuestra venta con la finalidad de que todos los campos que vamos 
        # agregando a nuestra lista entren y la ventana no se muestre en cualquier parte de la ventana,
        # si no en el centro este metodo lo hemos usado para centrar en la pantalla
        w = self.update_window.winfo_reqwidth()
        h = self.update_window.winfo_reqheight()


        ws = self.update_window.winfo_screenwidth()
        hs = self.update_window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.update_window.geometry('+%d+%d' % (x, y))






        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario
        frame = LabelFrame(self.update_window, text = 'Update Dictionary', font=("{}".format(self.file_font_type), self.file_font_size, "bold"))

        # Ahora posicionamos el Frame que hemos creado
        frame.grid(row=0, column=0, columnspan=3, pady=20)


        # Creamos los labels y cajas de texto
        Label(frame, text = 'Word:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 1, column = 1)
        word = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = word))
        word.grid(row = 1, column = 2)

        Label(frame, text = 'Phonemic:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 3, column = 1)
        phonemic = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = phonemic))
        phonemic.grid(row = 3, column = 2)

        Label(frame, text = 'Pronunciation:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 5, column = 1)
        pronunciation = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = pronunciation))
        pronunciation.grid(row = 5, column = 2)

        Label(frame, text = 'Type:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 7, column = 1)
        type = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = type))
        type.grid(row = 7, column = 2)

        Label(frame, text = 'Lesson:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 9, column = 1)
        lesson= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = lesson))
        lesson.grid(row = 9, column = 2)
        
        Label(frame, text = 'Module:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 11, column = 1)
        module= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = module))
        module.grid(row = 11, column = 2)
       
        # Aqui para poder insertarle un valor al Text Area usamos .insert() y le pasamos
        # como valor todo el codigo que hubieramos usado en el try{} catch{} anterior, esto
        # lo hacemos ya que es la unica manera en que recozca el valor dentro del Text Area
        Label(frame, text = 'Meaning:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 13, column = 1)
        meaning= Text(frame, width=self.file_size_components, height = 3, font=("{}".format(self.file_font_type), self.file_font_size))
        meaning.insert(INSERT, self.tree.item(self.tree.selection())['values'][7])
        meaning.grid(row = 13, column = 2)
        


        # Creamos un label que va a funcionar como mensaje despues de realizar una accion
        self.message_uw = Label(frame, text='', font=("{}".format(self.file_font_type), self.file_font_size), fg='red')
        self.message_uw.grid(row=14, column=2, sticky=W+E)


        # Creamos un boton para poder insertar los datos
        Button(frame, text = 'Update', font=("{}".format(self.file_font_type), self.file_font_size), command = lambda: self.update_dictionary(
            id, word.get(), phonemic.get(), pronunciation.get(), type.get(), lesson.get(), module.get(), meaning.get(1.0, "end-1c"))).grid(row = 15, column = 2, sticky=W+E)
        
        # Ejecutamos los eventos de la ventana
        self.update_window.mainloop()








    # Creamos una funcion para mostrar un mensaje en donde vamos a
    # eliminar los datos
    def delete_window(self):



        # Realizamos una limpieza de nuestro mensaje o label, en el caso que tenga algun dato
        self.message['text'] = ''

        # Creamos un try-catch, para evitar errores, en el caso que el usuario no  haya
        # seleccionado ningun dato para actualizar
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
          
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return



        # Mostramos un mensaje de dialogo, para decidir si eliminamos o no los datos
        res = messagebox.askquestion('Delete Dictionary', 'Do you want to delete this data?')
        
        if res == 'yes' :

            # Ejecutamos la funcion para eliminar los datos pasandole el id
            self.delete_dictionary(id)

            messagebox.OK

            # LLamamos al label que va a actuar commo mensaje
            self.message.config(fg='green')
            self.message['text'] = 'Dictionary deleted successfully'
            
        else :
            messagebox.CANCEL



    





    # Creamos una funcion para mostrar una ventana flotante en donde vamos a
    # mostrar los datos
    def view_window(self):

        # Realizamos una limpieza de nuestro mensaje o label, en el caso que tenga algun dato
        self.message['text'] = ''

        # Creamos un try-catch, para evitar errores, en el caso que el usuario no  haya
        # seleccionado ningun dato para actualizar

        # En el caso que se haya selleccionado una fila de datos, vamos a obtener los
        # datos y los almacenamos en variables
        try:
            word = self.tree.item(self.tree.selection())['values'][1]
            phonemic = self.tree.item(self.tree.selection())['values'][2]
            pronunciation = self.tree.item(self.tree.selection())['values'][3]
            type = self.tree.item(self.tree.selection())['values'][4]
            lesson = self.tree.item(self.tree.selection())['values'][5]
            module = self.tree.item(self.tree.selection())['values'][6]
            meaning = self.tree.item(self.tree.selection())['values'][7]
            

        # Mostramos un mensaje de error para que el usuario seleccione una fila de datos
        # que necesita editar
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return




        # Aqui abrimos una nueva ventana para editar los datos
        self.view_window = Toplevel()
        self.view_window.title = 'View Dictionary'




        # Evitamos que el usuario pueda maximizar la ventana y tambien bloqueamos el boton de maximizar
        self.view_window.resizable(width=False, height=False)




        # Damos una resolucion a nuestra venta con la finalidad de que todos los campos que vamos 
        # agregando a nuestra lista entren y la ventana no se muestre en cualquier parte de la ventana,
        # si no en el centro este metodo lo hemos usado para centrar en la pantalla
        w = self.view_window.winfo_reqwidth()
        h = self.view_window.winfo_reqheight()


        ws = self.view_window.winfo_screenwidth()
        hs = self.view_window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.view_window.geometry('+%d+%d' % (x, y))






        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario
        frame = LabelFrame(self.view_window, text = 'View dictionary', font=("{}".format(self.file_font_type), self.file_font_size, "bold"))

        # Ahora posicionamos el Frame que hemos creado
        frame.grid(row=0, column=0, columnspan=3, pady=20)


        # Creamos los labels y cajas de texto
        Label(frame, text = 'Word:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 1, column = 1)
        word = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), state = 'readonly', textvariable = StringVar(frame, value = word))
        word.grid(row = 1, column = 2)

        Label(frame, text = 'Phonemic:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 3, column = 1)
        phonemic = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = phonemic))
        phonemic.grid(row = 3, column = 2)

        Label(frame, text = 'Pronunciation:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 5, column = 1)
        pronunciation = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = pronunciation))
        pronunciation.grid(row = 5, column = 2)

        Label(frame, text = 'Type:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 7, column = 1)
        type = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = type))
        type.grid(row = 7, column = 2)

        Label(frame, text = 'Lesson:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 9, column = 1)
        lesson= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), state = 'readonly', textvariable = StringVar(frame, value = lesson))
        lesson.grid(row = 9, column = 2)
        
        Label(frame, text = 'Module:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 11, column = 1)
        module= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), state = 'readonly', textvariable = StringVar(frame, value = module))
        module.grid(row = 11, column = 2)
       
        # En este campo de Text Area lo ponemos disabled, para inabilitra su edicion

        # insert(1.0) = lo ponemos de esta manera para que no se vea tan opaco el texto
        Label(frame, text = 'Meaning:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 13, column = 1)
        meaning= Text(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), height = 3)
        meaning.insert(1.0, self.tree.item(self.tree.selection())['values'][7])
        meaning.config(state= DISABLED)
        meaning.grid(row = 13, column = 2)


        # Creamos un boton para poder cerrar la ventana
        Button(frame, text = 'Cerrar', font=("{}".format(self.file_font_type), self.file_font_size), command=self.view_window.destroy).grid(row = 14, column = 2, sticky=W+E)
        
        # Ejecutamos los eventos de la ventana
        self.view_window.mainloop()








    # Creamos una funcion para duplicar el registro que necesitemos
    def duplicate_data(self):

        from controller.insert import Insert


        # Realizamos una limpieza de nuestro mensaje o label, en el caso que tenga algun dato
        self.message['text'] = ''

        # Creamos un try-catch, para evitar errores, en el caso que el usuario no  haya
        # seleccionado ningun dato para actualizar

        # En el caso que se haya selleccionado una fila de datos, vamos a obtener los
        # datos y los almacenamos en variables
        try:
            word = self.tree.item(self.tree.selection())['values'][1]
            phonemic = self.tree.item(self.tree.selection())['values'][2]
            pronunciation = self.tree.item(self.tree.selection())['values'][3]
            type = self.tree.item(self.tree.selection())['values'][4]
            lesson = self.tree.item(self.tree.selection())['values'][5]
            module = self.tree.item(self.tree.selection())['values'][6]
            meaning = self.tree.item(self.tree.selection())['values'][7]

            # duplicado, esta variable la pasaremos para poder insertarla
            word_duplicate = word+" Duplicate"
            

        # Mostramos un mensaje de error para que el usuario seleccione una fila de datos
        # que necesita editar
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return

        
        # Llamamos a la funcion add_dictionary(), de la clase Insert, ubicada en el archivo
        # src/controller/insert.py, la cual va a permitir insertar los datos

        # word, lesson... = estos son los valores que vamos a insertar
        Insert.add_dictionary(word_duplicate, phonemic, pronunciation, type, lesson, module, meaning)


        # LLamamos al label que va a actuar commo mensaje para indicar que el registro se ha insertado
        self.message.config(fg='green')
        self.message['text'] = 'Data successfully duplicated'


        # LLamamos a la funcion get_dictionary(), para que se actualicen los datos despues que
        # ingresemos
        self.get_dictionary()





    

    
    

    


























    # FUNCIONES PARA REALIZAR EL CRUD 



    # Creamos una funcion para obtener la lista de productos
    def get_dictionary(self):
        
        # Importamos las clases donde se va a realizar un CRUD

        # list = se refiere al archivo "src/list.py"
        # List = nombre de la clase que contiene "src/list.py"
        from controller.list import List
    
        
        # Obtenemos todos los elementos de la tabla, con la finalidad de realizar
        # una limpieza de la tabla, en el caso que exista algun dato

        # .tree = nombre de la tabal que hemos creado anteriormente
        # get_children() = este metodo permite obtener los datos de la tabla
        records = self.tree.get_children()





        # Recorremos los elementos de la tabla para poder limpiarlos

        # Medinte un loop o for recorremos los elementos

        # element = variable que va a eliminar cada elemento de la tabla
        for element in records:
            # Eliminamos cada elemento de la tabla

            # delete() = metodo que permite eliminar elementos de la tabla
            self.tree.delete(element)

        




        # LLamamos a la funcion list_word(), que va a traer la lista de
        # estudiantes de la base de datos
        lista = List.list_dictionary()

    



        # Creamos un contador y lo iniciamos, con la finalidad de saber la cantidad de datos
        # que tenemos registrados
        self.i = 1

       
        

        # LLenamos los datos obtenidos de la consulta en la tabla

        # a,b,c,d = variables que almacenan los datos obtenidos de nuestra consulta
        for id, word, phonemic, pronunciation, type, lesson, module, meaning  in zip(*lista): 

            # Insertamos los datos de nuestra conulta en la tabla

            # insert() = este metodo permirte insertar valores dentro de la tabla

            # '', 0 = aqui le indicamos que la posicion 0 de la consulta, no inserte ningun valor
            #         en la tabla

            # text = self.i = aqui le indicamos que el contador lo inserte en la posicion 0 de la 
            #                 tabla como texto

            # values = row[2] = aqui le indicamos que la posicion 2 de la consulta, inserte en la 
            #                   tabla como valor, aqui otenemos el precio del producto
            self.tree.insert('', 0, text = self.i, values = (id, word, phonemic, pronunciation, type, lesson, module, meaning))

            # Incrementamos el contador creado anteriormente
            self.i = self.i + 1








   
    # Creamos una funcion que va a llamar a la funcion de insercion de los datos
    # ubicada en src/insert.py
    def add_dictionary(self, word, phonemic, pronunciation, type, lesson, module, meaning):

        from controller.insert import Insert

        # LLamamos a la funcion de validacion_add_window(), para comprobar que el usuario esta ingresando
        # los datos en las cajas de texto

        # validation_add_window() = esta funcion como primer valor va a retornar un true, caso contrario un false
        if self.validation_add_window(word, phonemic, pronunciation, type, lesson, module, meaning):

            # Llamamos a la funcion add_dictionary(), de la clase Insert, ubicada en el archivo
            # src/controller/insert.py, la cual va a permitir insertar los datos

            # word, lesson... = estos son los valores que vamos a insertar
            Insert.add_dictionary(word, phonemic, pronunciation, type, lesson, module, meaning)

            # Cerramos la ventana una vez que se actualicen los datos
            self.add_window.destroy()


            # LLamamos al label que va a actuar commo mensaje para indicar que el registro se ha insertado

            # message['text'] = llamamos a la propiedad "text" del label, para poder pasarle el mensaje que
            #                   queremos mostrar

            # {} = esto permite agregar un valor dentro del mensaje

            # format() = permite pasarle un valor dentro de las llaves {}
            self.message.config(fg='green')
            self.message['text'] = 'Dictionary added successfully'


            # LLamamos a la funcion get_dictionary(), para que se actualicen los datos despues que
            # ingresemos
            self.get_dictionary()
        

  
       



        



    # Creamos una funcion que va a llamar a la funcion de actualizacion de los datos
    # ubicada en src/update.py
    def update_dictionary(self, id, word, phonemic, pronunciation, type, lesson, module, meaning):

        from controller.update import Update

        # LLamamos a la funcion de validacion_update_window(), para comprobar que el usuario esta ingresando
        # los datos en las cajas de texto

        # validation_update_window() = esta funcion como primer valor va a retornar un true, caso contrario un false
        if self.validation_update_window(word, phonemic, pronunciation, type, lesson, module, meaning):

            # Llamamos a la funcion update_dictionay(), de la clase Update, ubicada en el archivo
            # src/controller/update.py, la cual va a permitir actualizar los datos

            # word, lesson... = estos son los valores que vamos a insertar

            Update.update_dictionaryt(id, word, phonemic, pronunciation, type, lesson, module, meaning)

            # Cerramos la ventana una vez que se actualicen los datos
            self.update_window.destroy()

            # LLamamos al label que va a actuar commo mensaje
            self.message.config(fg='green')
            self.message['text'] = 'Dictionary updated successfully'

            # LLamamos a la funcion get_dictionary(), para que se actualicen los datos despues que
            # ingresemos
            self.get_dictionary()

    






    # Creamos una funcion que va a llamar a la funcion de eliminacion de los datos
    # ubicada en src/controller/delete.py
    def delete_dictionary(self, id):

        from controller.delete import Delete

        Delete.delete_dictionary(id)

        # LLamamos a la funcion get_dictionary(), para que se actualicen los datos despues que
        # ingresemos
        self.get_dictionary()










   
    # Creamos una funcion que permite buscar en la base de datos por un dato que ingresemos
    def search_dictionary(self, data):

        from controller.search import Search


        # Aqui aplicamos lo mismo que usamos al obtener la lista de datos

        records = self.tree.get_children()

        for element in records:
            self.tree.delete(element)



        # Llamamos a la funcion search_word(), de la clase Search, ubicada en el archivo
        # src/controller/search.py

        # data = este es el valor por el cual vamos a buscar en la base de datos
        lista_search = Search.search_dictionary(data)

    
        self.i = 1


        for id, word, phonemic, pronunciation, type, lesson, module, meaning in zip(*lista_search): 

            self.tree.insert('', 0, text = self.i, values = (id, word, phonemic, pronunciation, type, lesson, module, meaning))
            self.i = self.i + 1






    # Creamos una funcion la cual va a permitir obtener el valor que ingresemos en la
    # caja de texto de una forma rapida
    def scankey_t(self, event):
        
        # Obtenemos el dato que ingresamos en la caja de texto
        # en tiempo real

        # event.widget.get() = permite obtener el valor ingresado en la caja de texto en 
        #                      tiempo real
        val = event.widget.get()

        


        # Validamos si no existe ningun valor en la caja de texto, mostraremos
        # toda la lista de datos
        if val == '':
            self.get_dictionary()
        # Caso contrario pasamos el dato que hemos ingresado en la caja de texto
        # para que busque en la base de datos
        else:
            self.search_dictionary(val)





























    # FUNCIONES DE LAS OPCIONES DE NUESTRA APLICACION


    # Creamos esta funcion que va a permitir abrir el archivo de base de datos
    def open_file_database(self):
        
        # Abrimos el archivo .txt que contiene la ruta de la base de datos que queremos guardar
        #f = open('src/settings/route-o-database.txt', 'r')
        #route_database = f.read()
        #f.close()


        # Abrimos una ventana para buscar el archivo de base de datos
        x = filedialog.askopenfilename(title = "Open File", filetypes=[('Database','*.db')])



        if (x==() or x==''):

            self.message.config(fg='orange')
            self.message['text'] = 'No database has been selected'

        else:

            # Guardamos la ruta de base de datos en nuestro archivo .txt
            with open('src/settings/route-o-database.txt', 'w') as f:
                f.write(x)
        
        
           
            # Damos un tamaño de letra al texto de nuestro cuadro de dialogo
            window.option_add('*Dialog.msg.font', 'Helvetica 11')
            # Mostramos un mensaje de dialogo, para decidir si guardamos o no la ruta de la base de datos
            res = messagebox.askquestion('Do you want to save the database path?', '{}'.format(x))
            

            if res == 'yes' :

                # Insertamos el id 1 en nuestro archivo .txt, para indicarle que se ha guardado la ruta de 
                # base de datos y ya no volver a buscar el archivo de base de datos
                with open('src/settings/id-s-database.txt', 'w') as f:
                    f.write("1")

                self.message.config(fg='green')
                self.message['text'] = 'Database loaded correctly'


                # Abrimos el archivo .txt que contiene la ruta de donde se va abrir la base de datos
                # para despues actualizar automaticamente la ruta de la base de datos que va a contener
                # nuestr label 
                f_route_open_database = open('src/settings/route-o-database.txt', 'r')
                route_open_database = f_route_open_database.read()
                f_route_open_database.close()
            

                # Actualizamos la ruta de base de datos a nuestro label que va a contener el path
                self.path_database['text'] = route_open_database


                # Mostramos la lista de datos en el caso que existan
                self.get_dictionary()


                messagebox.OK

                
                
            else :

                # Insertamos el id 0 en nuestro archivo .txt, para indicarle que no guarde la ruta de base de
                # datos y volver a abrirla
                with open('src/settings/id-s-database.txt', 'w') as f:
                    f.write("0")

                self.message.config(fg='orange')
                self.message['text'] = 'Database loaded correctly, but the path has not been saved.'

                # Mostramos un mensaje que no existe ruta guardada la base de datos
                self.path_database['text'] = "No saved database path exists"


                # Mostramos la lista de datos en el caso que existan
                self.get_dictionary()


                messagebox.CANCEL







    # Creamos esta funcion que va a permitir crear el archivo de base de datos
    def create_file_database(self):

        x = filedialog.askdirectory(title = "Open Directory")


        if (x==() or x==''):

            self.message.config(fg='orange')
            self.message['text'] = 'No directory has been selected'
            
        else:
            
            # Guardamos la ruta de base de datos en nuestro archivo .txt
            with open('src/settings/route-c-database.txt', 'w') as f:
                f.write(x)

            # Llamamos al archivo que va a crear la base de datos
            subprocess.call("python src/model/database_create.py", shell=True)

            self.message.config(fg='green')
            self.message['text'] = 'Database created correctly and path saved'


            # Abrimos el archivo .txt que contiene la ruta de donde se va abrir la base de datos
            # para despues actualizar automaticamente la ruta de la base de datos que va a contener
            # nuestr label 
            f_route_open_database = open('src/settings/route-o-database.txt', 'r')
            route_open_database = f_route_open_database.read()
            f_route_open_database.close()
        

            # Actualizamos la ruta de base de datos a nuestro label que va a contener el path
            self.path_database['text'] = route_open_database
            







    # Creamos esta funcion que va a permitir actualizar nuestra aplicacion
    def update_application(self):

        # Damos un tamaño de letra al texto de nuestro cuadro de dialogo
        window.option_add('*Dialog.msg.font', 'Helvetica 11')
        # Mostramos un mensaje de dialogo, para decidir si guardamos o no la ruta de la base de datos
        res = messagebox.askquestion(title = "Update", message = "If you update the application will the programme close?")
        

        if res == 'yes' :
        
            window.destroy()
            
            #subprocess.call("", shell=True)
            #subprocess.call('sh -c "./update-gnu-linux.sh; echo; ${SHELL:-bash}"', shell=True)

            #os.system("xfce4-terminal -e 'bash -c \"cp ~/dictionary-english/update-gnu-linux.sh ~ && cd ~ && ./update-gnu-linux.sh; bash\" '")
            os.system("ls")

            messagebox.OK

            
        
        else:

            messagebox.CANCEL

    






    # Creamos una funcion para mostrar una ventana flotante en donde vamos a
    # mostrar los ajustes visuales de la aplicacion
    def settings(self):

        
        self.settings = Toplevel()
        self.settings.title = 'Settings'


        # Evitamos que el usuario pueda maximizar la ventana y tambien bloqueamos el boton de maximizar
        self.settings.resizable(width=False, height=False)



        # Damos una resolucion a nuestra venta con la finalidad de que todos los campos que vamos 
        # agregando a nuestra lista entren y la ventana no se muestre en cualquier parte de la ventana,
        # si no en el centro este metodo lo hemos usado para centrar en la pantalla
        w = self.settings.winfo_reqwidth()
        h = self.settings.winfo_reqheight()


        ws = self.settings.winfo_screenwidth()
        hs = self.settings.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.settings.geometry('+%d+%d' % (x, y))






        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario
        frame = LabelFrame(self.settings, text = 'Settings', font=("{}".format(self.file_font_type)))
        frame.grid(row=0, column=0, columnspan=3, pady=20)





      

        





        # Creamos un label y una caja de texto para ingresar el tipo de letra
        Label(frame, text = 'Font type:', font=("{}".format(self.file_font_type))).grid(row = 1, column = 1)
        
        # Creamos el ListBox y agregamos su configuracion
        self.font_type = Listbox(frame, width=self.file_size_components, font=("{}".format(self.file_font_type)), height = 5)
        self.font_type.grid(row = 1, column = 2)
        
        # Creamos esta configuracion para nuestro Listbox para evitar que Listbox pierda su selección 
        # al hacer clic en otra parte del formulario
        self.font_type.configure(exportselection=False)

        # Llamamos a todos los tipos de letra de Tkinter
        fonts=list(font.families())
        fonts.sort()

        # Creamos un for para recorrer la lista de todos los tipos de letras que existe
        # en Tkinter en insertarlo en nuestro Listbox
        for item in fonts:
            # Isertamos en el Listbox la lista de datos
            self.font_type.insert(END, item)

        


        # Creamos un OptionMenu, para seleccionar el porcentaje de los elementos que va a tener nuestra aplicacion
        Label(frame, text = 'Size:', font=("{}".format(self.file_font_type))).grid(row = 3, column = 1)

        OPTIONS = [
        "10%",
        "15%",
        "20%",
        "25%"
        ] #etc

        
        self.variable = StringVar(frame)
        self.variable.set(OPTIONS[0]) # default value



        self.size = OptionMenu(frame, self.variable, *OPTIONS)
        self.size.grid(row = 3, column = 2)
        self.size.config(width=self.file_size_components, font=("{}".format(self.file_font_type)))


        #font_type = Arial
        #font_size = 10
        #size_components = 50
        #size_components_grid = 120





        # Creamos un boton para poder insertar los datos

        # lambda = permite ejecutar una funcion en esta misma ventana
        # add_dictionary() = funcion que va a permitir insertar los datos
        # word.get(), lesson.get()....) = son parametros que espera recibir la funcion
        # sticky=W+E = esto indica que abarque todo el ancho posible de nuestra ventana, de Oeste a Este
        # meaning.get(1.0, "end-1c") = para obtener la informacion ingresada en el Text Area, es obligatorio agregar estos parametros
        Button(frame, text = 'Apply', font=("{}".format(self.file_font_type)), 
               command = lambda: self.get_settings(self.font_type.get(self.font_type.curselection()) , self.variable.get())).grid(row = 9, column = 2, sticky=W+E)

        
        # Ejecutamos los eventos de la ventana
        self.settings.mainloop()

    


   

    





    # Creamos una funcion que va a guradar las configuraciones del programa en archivos de texto 
    def get_settings(self, font_type, size):


        # Realizamos una validacion del campo de size para despues usando regla de 3
        # calcular automaticamente los pixeles que va a tener nuestra ventana

        if (size == "10%"):

            print("Es el 10%")
            
            font_size = "10"
            size_components = "50"
            size_components_grid = "120"
        
        elif (size == "15%"):
            print("Es el 15%")

            font_size = "15"
            size_components = "75"
            size_components_grid = "180"

        elif (size == "20%"):
            print("Es el 20%")

            font_size = "20"
            size_components = "100"
            size_components_grid = "240"
        
        elif (size == "25%"):
            print("Es el 25%")

            font_size = "25"
            size_components = "125"
            size_components_grid = "300"
        
        
        
        


      

        
        # Damos un tamaño de letra al texto de nuestro cuadro de dialogo
        window.option_add('*Dialog.msg.font', 'Helvetica 11')
        # Mostramos un mensaje de dialogo, para decidir si guardamos o no la ruta de la base de datos
        res = messagebox.askquestion(title = "Apply settings", message = "The application will restart to apply the changes")
        
        
        if res == 'yes' :

             # Guardamos el tipo de letra de nuestros formularios en nuestro archivo .txt
            with open('settings/font-type.txt', 'w') as f:
                f.write(font_type)

            # Guardamos el tamaño de letra de nuestros formularios en nuestro archivo .txt
            with open('settings/font-size.txt', 'w') as f:
                f.write(font_size)

            # Guardamos el tamaño de los componentes de nuestros formularios en nuestro archivo .txt
            with open('settings/size-components.txt', 'w') as f:
                f.write(size_components)
            
            # Guardamos el tamaño de los componentes de nuestros formularios en nuestro archivo .txt
            with open('settings/size-component-grid.txt', 'w') as f:
                f.write(size_components_grid)
        
            # Cerramos la ventana
            window.destroy()
            


            messagebox.OK

            
        
        else:

            
            messagebox.CANCEL

            self.settings.destroy()

        





    






















    # FUNCIONES QUE VAN A VALIDAR VALIDAR NUESTRA APLICACION



    # Funciones de va a validar las cajas de texto


    # Creamos una funcion que va a permitir validar que las cajas de texto no esten vacias
    # en el formulario de agregar estudiante
    def validation_add_window(self, word, phonemic, pronunciation, type, lesson, module, meaning):

        # Llamamos al siguiente archivo y a su clase para comprobar si la palabra existe
        from controller.data_exists import DataExists

        # Obtenemos la cantidad de datos existentes para despues validar
        word_count = DataExists.data_exists_dictionary(word)






        # Validamos que las cajas de texto no no esten vacias

        # len = metodo que permite obtener la longitud de un elemento
        # == 0 = aqui le indicamos que la longitud del valor ingresado sea igual a 0
        if(len(word) == 0):

            # LLamamos al label que va a actuar commo mensaje para indicar que el registro se ha insertado
            self.message_aw['text'] = 'Word is required'

        elif(len(phonemic) == 0):

            self.message_aw['text'] = 'Phonemic is required'

        elif(len(pronunciation) == 0):

            self.message_aw['text'] = 'Pronunciation is required'

        elif(len(type) == 0):

            self.message_aw['text'] = 'Type is required'

        elif(len(lesson) == 0):

            self.message_aw['text'] = 'Lesson is required'

        elif(len(module) == 0):

            self.message_aw['text'] = 'Module is required'
        
        elif(len(meaning) == 0):

            self.message_aw['text'] = 'Meaning is required'
        
        # Validamos si existe mas de 1 palabra igual vamos a mostrar el siguinte mensaje, para que no vuelva
        # a ingresar la misma palabra
        elif(word_count > 0):

            self.message_aw['text'] = 'This word already exists in the database'

        # Caso contrario retornamos los valores de los datos para insertarlos
        else:
            return word and lesson and module and meaning






    # Creamos una funcion que va a permitir validar que las cajas de texto no esten vacias
    # en el formulario de actualizar estudiante
    def validation_update_window(self, word, phonemic, pronunciation, type, lesson, module, meaning):


        if(len(word) == 0):

            self.message_uw['text'] = 'Word is required'
        
        elif(len(phonemic) == 0):

            self.message_uw['text'] = 'Phonemic is required'

        elif(len(pronunciation) == 0):

            self.message_uw['text'] = 'Pronunciation is required'
        
        elif(len(type) == 0):

            self.message_uw['text'] = 'Type is required'
        
        elif(len(lesson) == 0):

            self.message_uw['text'] = 'Lesson is required'

        elif(len(module) == 0):

            self.message_uw['text'] = 'Module is required'
        
        elif(len(meaning) == 0):

            self.message_uw['text'] = 'Meaning is required'
        

        else:
            return word and lesson and module and meaning
        







    # Funciones que va a usar nuestra aplicacion

    # Creamos esta funcion que permite validar las opciones de nuestra base de datos, como indicarnos el path de la
    # base de datos, si se ha cargado la base de datos etc
    def validation_database_options(self):

        # Validamos que exista la ruta y el archivo de base de datos

        # Abrimos el archivo .txt que contiene el id de si hemos o no guardado
        # la ruta de base de datos
        f_id_save_database = open('src/settings/id-s-database.txt', 'r')
        id_save_database = f_id_save_database.read()
        f_id_save_database.close()



        # Abrimos el archivo .txt que contiene la ruta de donde se va abrir la base de datos
        f_route_open_database = open('src/settings/route-o-database.txt', 'r')
        route_open_database = f_route_open_database.read()
        f_route_open_database.close()



        # Convertimos de String a entero para que podamos validar el valor que obtenemos del .txt
        # ya que este se obtiene en formato String
        id_save_database_var = int(id_save_database)



        # Realizamos una validacion para saber si hemos o no guardado la ruta de base de datos
        # 1 = indica que hemos decidido guardar lla ruta de base de datos
        # 0 = indica que no hemos guardado la ruta de base de datos  
        if id_save_database_var == 1:

            # Validamos si existe el directorio y dentro de este el archivo de base de datos
            database_file = os.path.exists(os.path.join("{}".format(route_open_database)))


            # La variable anterior nos va a dar un true, si existe el directorio y el archivo de base de datos
            # de lo contrario un false
            if database_file:

                # Si existe, mostramos un mensaje por consola
                print("Database exists")

                # Si existe la base de datos creamos una variable donde va a almacenar la ruta de base de datos
                self.path_database['text'] = route_open_database

                # Enviamos a nuestra variable el path o el mensaje de que la base de datos existe o no
                #self.path_database['text'] = route_open_database_var
                self.get_dictionary()

                
                
            else:

                # Si existe, mostramos un mensaje por consola
                print("Database no exists")
                
                # Mostramos una mensaje de que la base de datos no existe
                self.message.config(fg='red')
                self.message['text'] = 'No database file loaded, you must create or open a database.'


                # Si existe la base de datos creamos una variable donde va a almacenar la ruta de base de datos
                self.path_database['text'] = route_open_database

                
            
            
        else:

            print("No saved database path exists")

            # Mostramos una mensaje de que la base de datos no existe
            self.message.config(fg='red')
            self.message['text'] = 'No database file loaded, you must create or open a database.'

            # Si no existe la base de datos creamos una variable donde va a almacenar un mensaje que no existe 
            # ruta guardada la base de datos
            self.path_database['text'] = "No saved database path exists"







# ARRANCANDO LA APLICACION

# Comprobamos si este archivo es con el que va arrancar nuetra aplicacion
# para despues mostrar la ventana con interfaz grafica
if __name__ == '__main__':

    # Iniciando el modulo que va arrancar la ventana y almacenandolo
    # en una variable

    # Tk() = este sera el modulo con el que va a iniciar nuestra ventana y que hemos
    #        importado inicialmente
    window = Tk()



    # Evitamos que el usuario pueda maximizar la ventana y tambien bloqueamos el boton de maximizar
    window.resizable(width=False, height=False)

    

    # Instanciamos a la clase "Product" y la almacenamos en una variable

    # window = parametro que le pasamos a la clase "Product", la cual contendra el
    #          arranque de la ventana
    application = Ventana(window)



    # Arrrancamos la ventana

    # window.mainloop () = le dice a Python que ejecute el ciclo de eventos Tkinter.
    #                      Este método detecta eventos, como clics de botones o
    #                      pulsaciones de teclas, y bloquea la ejecución de cualquier
    #                      código que venga después hasta que se cierra la ventana a
    #                      la que se llama.
    window.mainloop()
