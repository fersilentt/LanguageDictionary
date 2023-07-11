from sqlalchemy.orm import sessionmaker
import model.database

# Importamos la variable que conetiene la ruta de donde se creara
# la base de datos para evitar
from model.database import engine


class DataExists:


    # Creamos una funcion que va la palabra para comprobar si existe

    # word = este va a ser el dato por el cual se va a buscar en la base de datos el
    #        cual vamos a pasarle desde la caja de texto
    def data_exists_dictionary(word):


        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Contamos la cantidad de datos que se repiten 
        word_count = session.query(model.database.Dictionary).filter(model.database.Dictionary.word == word).count()
        
        # Retornamos la cantidad de datos encontrados
        return word_count