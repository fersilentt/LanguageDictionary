from sqlalchemy.orm import sessionmaker
import model.database

# Importamos la variable que conetiene la ruta de donde se creara
# la base de datos para evitar
from model.database import engine



class Delete:

    # Creamos una funcion que va actualizar los datos
    def delete_dictionary(id):

        
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        dictionay = session.query(model.database.Dictionary).filter(model.database.Dictionary.id == id)
        dictionay.delete()

        
        # Hacemos un commit en la base de datos
        session.commit()