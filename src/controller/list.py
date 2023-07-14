from sqlalchemy.orm import sessionmaker
import model.database

# Importamos la variable que conetiene la ruta de donde se creara
# la base de datos para evitar
from model.database import engine



# Creamos una clase la cual
class List:


    def list_dictionary():
        
        #engine = create_engine('sqlite:///student.db', echo=True)


        # Creamos una sesion
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
        color = []



        # Recorremos el objeto donde almacena la informacion 

        # dictionary = variable que almacena los datos obtenidos de nuestra consulta 
        # desc() = aqui le indicamos que ordene la consulta en forma descendente por el campo que hemos establecido 
        for dictionary in session.query(model.database.Dictionary).order_by(model.database.Dictionary.word.desc()):
            
            # Creamos un nuevo arreglo, llenos de arreglos obtenidos de los datos
            # que vamos obteniendo del for

            # append = permite crear un arreglo a partir de la obtencion de datos del for
            id.append(dictionary.id)
            word.append(dictionary.word)
            phonemic.append(dictionary.phonemic)
            pronunciation.append(dictionary.pronunciation)
            type.append(dictionary.type)
            lesson.append(dictionary.lesson)
            module.append(dictionary.module)
            meaning.append(dictionary.meaning)
            color.append(dictionary.color)


        # Creamos un nuevo arreglo con la lista de arreglos obtenidos
        # para despues recorrerlos y mostrarlos en la vista
        my_list = [(id), (word), (phonemic), (pronunciation), (type), (lesson), (module), (meaning), (color)]
          
           
        

        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
    

    
    
 