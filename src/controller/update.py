from sqlalchemy.orm import sessionmaker
import model.database

# We import the variable that contains the path where the database will be 
# created
from model.database import engine

class Update:

    # We create a function that will update the data
    def update_dictionaryt(id, word, phonemic, pronunciation, type, lesson, module, meaning, color):


        # Create a Session
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
        student.update({model.database.Dictionary.color: color})

        # We commit to the database
        session.commit()
