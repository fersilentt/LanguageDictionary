from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


# Open the .txt file containing the directory where the database will be created. 
f = open('src/settings/route-c-database.txt', 'r')
file_contents = f.read()
f.close()



# We create the path where the database is going to be created, from here the rest of the 
# files CRUD files will inherit the path
#engine = create_engine('sqlite:///dictionary-english.db', echo=True)
engine = create_engine('sqlite:///{}/language-dictionary.db'.format(file_contents), echo=True)
Base = declarative_base()


# Open the .txt file, to enter the path to the database to be opened
with open('src/settings/route-o-database.txt', 'w') as f:
    f.write(file_contents+"/language-dictionary.db")


########################################################################
class Dictionary(Base):
    """"""
    __tablename__ = "dictionary"
 
    id = Column(Integer, primary_key=True)
    word = Column(String)
    phonemic = Column(String)
    pronunciation = Column(String)
    type = Column(String)
    lesson = Column(String)
    module = Column(String)
    meaning = Column(String)
    color = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, word, phonemic, pronunciation, type, lesson, module, meaning, color):
        """"""
        self.word = word
        self.phonemic = phonemic
        self.pronunciation = pronunciation
        self.type = type
        self.lesson = lesson
        self.module = module
        self.meaning = meaning
        self.color = color
    


# We create the tables
Base.metadata.create_all(engine)