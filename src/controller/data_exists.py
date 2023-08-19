from sqlalchemy.orm import sessionmaker
import model.database

# We import the variable that contains the path where the database will be 
# created 
from model.database import engine


class DataExists:


    # We create a function that goes the word to check if it exists

    # word = this is going to be the data for which we are going to 
    #        search in the database the which we are going to pass it from the text box
    def data_exists_dictionary(word):


        # Create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # We count the amount of data that are repeated 
        word_count = session.query(model.database.Dictionary).filter(model.database.Dictionary.word == word).count()
        
        # We return the amount of data found
        return word_count