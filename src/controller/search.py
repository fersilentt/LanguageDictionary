from sqlalchemy.orm import sessionmaker
import model.database

# Importamos la variable que conetiene la ruta de donde se creara
# la base de datos para evitar
from model.database import engine


class Search:


    # Creamos una funcion que va buscar los datos

    # data = este va a ser el dato por el cual se va a buscar en la base de datos el
    #        cual vamos a pasarle desde la caja de texto
    def search_dictionary(data):


        # Creamos la sesion
        Session = sessionmaker(bind=engine)
        session = Session()
        

        # Creamos arreglos vacios para almacenar la informacion que obtendremos
        # al recorrer el for
        id = []
        word = []
        phonemic = []
        pronunciation = []
        type = []
        lesson = []
        module = []
        meaning = []

        

        # Aqui realizamos la busquema mediante varios campos, aqui usamos un like 
        # como en SQL , pero buscamos por varios campos usando or, como lo hariamos 
        # en SQL

        # all() = esto permite obtener toda la lista de datos que tiene similitud
        # or_( = esto indica que la conulta va usar OR y no AND
        # {} = esto permite agregar un valor dentro del mensaje
        # format() = permite pasarle un valor dentro de las llaves {}
        # data = aqui va el dato por el cual se va a buscar en la base de datos
        for student in session.query(model.database.Dictionary).filter(model.database.or_(
            model.database.Dictionary.word.like('%{}%'.format(data)),
            model.database.Dictionary.phonemic.like('%{}%'.format(data)),
            model.database.Dictionary.pronunciation.like('%{}%'.format(data)),
            model.database.Dictionary.type.like('%{}%'.format(data)),
            model.database.Dictionary.lesson.like('%{}%'.format(data)), 
            model.database.Dictionary.module.like('%{}%'.format(data)))).all():


            
            id.append(student.id)
            word.append(student.word)
            phonemic.append(student.phonemic)
            pronunciation.append(student.pronunciation)
            type.append(student.type)
            lesson.append(student.lesson)
            module.append(student.module)
            meaning.append(student.meaning)

        
        
        # Creamos un nuevo arreglo con la lista de arreglos obtenidos
        # para despues recorrerlos y mostrarlos en la vista
        my_list = [(id), (word), (phonemic), (pronunciation), (type), (lesson), (module), (meaning)]



        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
