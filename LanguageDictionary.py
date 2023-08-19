# In this file we list all the libraries that our project needs to run
# we add in this file to be able to use py2app


# Modules of the file src/view/dictionary_app.py
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import subprocess
from tkinter import filedialog
from tkinter import font
import sys


# Modules of the src/controller files
from sqlalchemy.orm import sessionmaker


# Modules of src/model files
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref