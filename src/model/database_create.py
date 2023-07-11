from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


# Abrimos el archivo .txt que contiene el directorio en donde se va a crear la 
# base de datos
f = open('src/settings/route-c-database.txt', 'r')
file_contents = f.read()
f.close()



# Creamos la ruta donde se va a crear la base de datos, de aqui los demas archivos
# del CRUD heredaran la ruta
#engine = create_engine('sqlite:///dictionary-english.db', echo=True)
engine = create_engine('sqlite:///{}/language-dictionary.db'.format(file_contents), echo=True)
Base = declarative_base()


# Abrimos el archivo .txt, para ingresarle la ruta de la base de datos que debe abrir
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

    #----------------------------------------------------------------------
    def __init__(self, word, phonemic, pronunciation, type, lesson, module, meaning):
        """"""
        self.word = word
        self.phonemic = phonemic
        self.pronunciation = pronunciation
        self.type = type
        self.lesson = lesson
        self.module = module
        self.meaning = meaning
    


# Creamos las tablas
Base.metadata.create_all(engine)