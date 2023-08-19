from sqlalchemy.orm import sessionmaker
import model.database

# We import the variable that contains the path where the database will be 
# created 
from model.database import engine



class Delete:

    # We create a function that will update the data
    def delete_dictionary(id):

        
        # Create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        dictionay = session.query(model.database.Dictionary).filter(model.database.Dictionary.id == id)
        dictionay.delete()

        
        # We commit to the database
        session.commit()