from sqlalchemy.orm import sessionmaker
import model.database

# We import the variable that contains the path where the database will be 
# created
from model.database import engine




class List:


    def list_dictionary():
        
        #engine = create_engine('sqlite:///student.db', echo=True)


        # Create a Session
        Session = sessionmaker(bind=engine)
        session = Session()


        # We create empty arrays to store the information that we will 
        # get when traversing the for
        id = []
        word = []
        phonemic = []
        pronunciation = []
        type = []
        lesson = []
        module = []
        meaning = []
        color = []



        # We traverse the object where the information is stored 

        # dictionary = variable that stores the data obtained from our query 
        # desc() = here we tell it to sort the query in descending order by the field we have set up 
        for dictionary in session.query(model.database.Dictionary).order_by(model.database.Dictionary.id.asc()):
            
            # We create a new array, filled with arrays obtained from the data
            # we get from the for

            # append = allows you to create an array from the data obtained from the for
            id.append(dictionary.id)
            word.append(dictionary.word)
            phonemic.append(dictionary.phonemic)
            pronunciation.append(dictionary.pronunciation)
            type.append(dictionary.type)
            lesson.append(dictionary.lesson)
            module.append(dictionary.module)
            meaning.append(dictionary.meaning)
            color.append(dictionary.color)


        # We create a new array with the list of arrays obtained and then scroll through them 
        # and display them in the view
        my_list = [(id), (word), (phonemic), (pronunciation), (type), (lesson), (module), (meaning), (color)]
          
           
        

        # We return the new array with the list of arrays in order to import it later
        return my_list
    

    
    
 