from sqlalchemy.orm import sessionmaker
import model.database

# Importamos la variable que conetiene la ruta de donde se creara
# la base de datos para evitar
from model.database import engine

class Update:

    # Creamos una funcion que va actualizar los datos
    def update_dictionaryt(id, word, phonemic, pronunciation, type, lesson, module, meaning):


        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        student = session.query(model.database.Dictionary).filter(model.database.Dictionary.id == id)
        student.update({model.database.Dictionary.word: word})
        student.update({model.database.Dictionary.phonemic: phonemic})
        student.update({model.database.Dictionary.pronunciation: pronunciation})
        student.update({model.database.Dictionary.type: type})
        student.update({model.database.Dictionary.lesson: lesson})
        student.update({model.database.Dictionary.module: module})
        student.update({model.database.Dictionary.meaning: meaning})

        
        # Hacemos un commit en la base de datos
        session.commit()
