from sqlalchemy.orm import sessionmaker
import model.database


# We import the variable that contains the path where the database will be 
# created
from model.database import engine


class Insert:

    # We create a function that will insert the data
    def add_dictionary(word, phonemic, pronunciation, type, lesson, module, meaning, color):


        # Create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        dictionary = model.database.Dictionary(word, phonemic, pronunciation, type, lesson, module, meaning, color)
        session.add(dictionary)

        
        # We commit to the database
        session.commit()
