from sqlalchemy.orm import sessionmaker
import model.database


# Importamos la variable que conetiene la ruta de donde se creara
# la base de datos para evitar
from model.database import engine


class Insert:

    # Creamos una funcion que va a insertar los datos
    def add_dictionary(word, phonemic, pronunciation, type, lesson, module, meaning, color):


        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        dictionary = model.database.Dictionary(word, phonemic, pronunciation, type, lesson, module, meaning, color)
        session.add(dictionary)

        
        # Hacemos un commit en la base de datos
        session.commit()
