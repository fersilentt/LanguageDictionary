from sqlalchemy.orm import sessionmaker
import model.database

# We import the variable that contains the path where the database will be 
# created
from model.database import engine


class Search:


    # We create a function that will look for the data

    # data = this is going to be the data for which we are going to search in 
    #        the database the which we will pass it from the text box
    def search_dictionary(data):


        # Create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        

       # We create empty arrays to store the information that we will get when traversing 
       # the for
        id = []
        word = []
        phonemic = []
        pronunciation = []
        type = []
        lesson = []
        module = []
        meaning = []
        color = []

        

        # Here we search by several fields, here we use a like as in SQL , but we search by 
        # several fields using or, as we would do it in SQL

        # all() = this allows to get the whole list of data that have similarity
        # or_( = this indicates that the query is going to use OR and not AND
        # {} = this allows to add a value inside the message
        # format() = this allows to pass a value inside the {} braces
        # data = this is the data to be searched for in the database
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
            color.append(student.color)

        
        
        # We create a new array with the list of arrays obtained.
        # and then traverse and display them in the view.
        my_list = [(id), (word), (phonemic), (pronunciation), (type), (lesson), (module), (meaning), (color)]



        # We return the new array with the list of arrays in order to import it later
        return my_list
