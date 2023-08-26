

<h1 align="center">Language Dictionary</h1>

<p align="center">
  <img src="https://github.com/tarantulaman/LanguageDictionary/blob/master/resources/language-dictionary.png" width="8%" />
</p>


<br/>
    <i>This program allows you to add words of any language as if it were a dictionary, with the purpose of being a support tool when we start learning a new language.</i>
<br/>
<br/>

<p align="center">
  <img src="https://github.com/tarantulaman/LanguageDictionary/blob/master/resources/project-image-01.png" width="20%" />
</p>


- [Requirements](#requirements)
- [License](#license)


---

#### TABLE OF CONTENTS:
---

- [IMPORTANTE](#IMPORTANTE)
- [COMANDOS USADOS](#COMANDOS-USADOS)
- [COMANDOS PARA CREAR EL ICONO EN MAC](#COMANDOS-PARA-CREAR-EL-ICONO-EN-MAC)

---

#### IMPORTANTE

1. Debemos tener instalado "pip 3" de "python 3", de acuerdo al sistema
   operativo donde nos encontremos

2. Debemos tener instalado "pipenv" de "python 3", de acuerdo al sistema
   operativo donde nos encontremos
   
3. El archivo "Pipfile"  es un archivo que contine informacion de nuestro 
   proyecto como el nombre, los paquetes que necesita para funcionar, etc
   lo incluimos en nuestro proyecto porque no pesa mucho, pero la recomendacion
   es borralo en instalo desde cero para ver como crear este archivo

4. No existe un script de base de datos, antes de ejecutar la aplicacion
   ya que directamente las tablas las creamos desde el codigo

5. Debemos tener instalado "Tkinter" de "python 3", de acuerdo al sistema
   operativo donde nos encontremos

6. Para iniciar nuestro proyecto ejecutamos los comandos de la seccion
   **[COMANDOS USADOS](#COMANDOS-USADOS)**

---

#### COMANDOS USADOS

1. Los siguientes comandos los vamos a ejecutar dentro de la carpeta de
   nuestro proyecto

2. Creamos y activamos nuestro entorno de **pipenv**, dentro del directorio
   de nuestro proyecto mediante el siguiente comando

```
pipenv shell
```
* *Si se ha activado pipenv, debera mostrarnos de la siguiente
   manera la ruta de nuestro proyecto y se creara un archivo
  llamado **Pipfile***

```
(nombre_del_proyecto) $
```

* *Tambien si nos salimos de nuestro entorno virtual podemos 
   volver a activarlo con el comando anterior*


3. Instalamos el modulo SQAlchemy

```
pipenv install sqlalchemy
```

4. Instalamos el modulo de py2app

```
pipenv install py2app
```

5. Iniciamos nuestra aplicacion

```
python src/app.py
```

#### COMANDOS PARA CREAR EL ICONO EN MAC

1. Creamos el ejcutable para contruir nuestra aplicacion con "py2applet"

```
py2applet --make-setup LanguageDictionary.py resources/language-dictionary.icns
```

2. Construimos nuestra aplicacion, para que cree nuestro archivo .app

```
python setup.py py2app
```

3. Copiamos el contenido del codigo faltante siguiendo los siguientes pasos

```
a. Entramos a la carpeta "dist"
b. En la aplicacion creada damos clic en "Mostrar el contenido del paquete"
c. Copiamos la carpeta "src", en dentro de "/Contents/Resources"
```

## Requirements

- Supported operating system (macOS)

## License

Language Dictionary is released under the [MIT license](https://github.com/tarantulaman/LanguageDictionary/blob/master/LICENCE).



