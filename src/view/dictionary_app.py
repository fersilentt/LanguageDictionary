# IMPORTING MODULES


# We import the Tkinter library that allows us to design
# the whole interface

# ttk = Tkinter library that allows to design the whole interface
from tkinter import ttk


# Import the whole Tkinter module

# tkinter = allows to create Desktop interfaces with Python
from tkinter import *


# We import the Message Box module

# messagebox = this module allows us to display dialog messages, we will use it to
#              we are going to use it to delete the data
from tkinter import messagebox


# We import the Tkinter module again, in order to be able to
# add the scroll to treeview
import tkinter as tk



# We import this module to get an absolute path to our project, so we can import 
# images for  our buttons
import os



# We import this module to be able to execute Python scripts
import subprocess




# Import this module in order to open the database file and the directory where the 
# database is going to be created
from tkinter import filedialog



# We import our fonts from Tkinter, and then display them in a Listbox
from tkinter import font







# We import this module to be able to inert the path, where the CRUD files 
# are located, in this way we will be able to import our files independently 
# of any folder where they are located.
import sys

# os.path.abspath("src") = we get the absolute path of the project and then we import the files
file = os.path.abspath("src")

# We add the absolute path of our project, so that it recognizes the import path. of the files that 
# make the CRUD
sys.path.insert(0, file)































class Ventana:


    # We create a function, to create a constructor of the class "Window".

    # self = is a reference to the current instance of the class, and is used to access the variables that belong
    #        to the class, we can call it whatever we want, but has to be the first parameter of any function in the class.

    # window = parameter that the constructor of the class expects to receive and that will have the
    #          initiation of the method that will start the window.
    def __init__(self, window):



        # Open the files containing the configuration of the application interface
        
        # Open the .txt file containing the font of the form components
        f_font_type = open('src/settings/font-type.txt', 'r')
        self.file_font_type = f_font_type.read()
        f_font_type.close()


        # We open the .txt file containing the font size of the form components
        f_font_size = open('src/settings/font-size.txt', 'r')
        self.file_font_size = f_font_size.read()
        f_font_size.close()


        # We open the .txt file containing the size of the form components
        f_size_components = open('src/settings/size-components.txt', 'r')
        self.file_size_components = f_size_components.read()
        f_size_components.close()


        # We open the .txt file containing the size of the Grid headers
        f_size_components_grid = open('src/settings/size-components-grid.txt', 'r')
        self.file_size_components_grid = f_size_components_grid.read()
        f_size_components_grid.close()





        # We store the "window" parameter received by the constructor in a property named
        # "self.wind"

        # self. = first parameter of the constructor and refers to the current instance
        #         of the class

        # .wind = property where the "window" parameter will be stored, it can have any name
        self.wind = window



        # Add a title to the window
        self.wind.title('Dictionary English')






        # We give a resolution to our sale in order that all the fields that we add to our list 
        # enter and the window is not displayed in any part of the window, if not in the center 
        # this method we have used it to center in the screen.
        w = self.wind.winfo_reqwidth()
        h = self.wind.winfo_reqheight()


        ws = self.wind.winfo_screenwidth()
        hs = self.wind.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.wind.geometry('+%d+%d' % (x, y))




       
        


        # We create a Frame that is going to work as a container and we store it in a variable to position it,
        # this Frame we create to show an outline on our form

        # self.wind = here we indicate where it is going to be positioned the Frame, here we are
        #             indicating that it will be inside the window.

        # text = '' = here I'm indicating the title that the Frame will have, here it's not going to have a title.
        frame = LabelFrame(self.wind, text = '')


        # We create a frame that will contain the buttons of the options of our application.
        frame01 = LabelFrame(self.wind, text = '')









        

        # Now we position the Frame of the CRUD buttons

        # frame = variable that stores the Frame that we have previously created

        # grid = method that allows us to indicate in which position of the window is going to be our 
        #        button or text entry, this is an invisible grid, that will help us to place our elements 
        #        according to the position we want to place them. elements according to the position that we want.

        # row=0 = this indicates that this element will be in row 0 of our grid, the value is indicated in pixels.

        # column=0 = this indicates that this element will be in column 0 of our grid.

        # columnspan=3 = this indicates how many columns of our grid will cover our window, that is to say, it will 
        #                be empty columns without any content, that is to say with this we will to center the frame

        # pady=5 = this is a padding, it indicates an internal spacing of each element, so that the elements are not 
        #          so close together. here we indicate in pixels the spacing at the top and at the bottom of each element.
        frame.grid(row=1, column=0, columnspan=3, pady=5, sticky = W)

        # Now we position the Frame of our application's options
        frame01.grid(row=0, column=0, columnspan=3, sticky = W)

        









        # We import the images of our project to use them as icons in our buttons.

        # Images of our application options
        self.img_open_database = PhotoImage(file=os.path.abspath("src/static/open-database.png"))
        self.img_create_database = PhotoImage(file=os.path.abspath("src/static/create-database.png"))
        #self.img_update_application = PhotoImage(file=os.path.abspath("src/static/update-application.png"))
        self.img_settings = PhotoImage(file=os.path.abspath("src/static/settings.png"))


        # CRUD images of our application

        # PhotoImage = this function allows to import images.
        # file = this allows to give the path of where the image is located
        # os.path.abspath("src/static/add.png") = we get the absolute path of the project to open the image
        self.img_add= PhotoImage(file=os.path.abspath("src/static/add.png"))
        self.img_update= PhotoImage(file=os.path.abspath("src/static/update.png"))
        self.img_delete= PhotoImage(file=os.path.abspath("src/static/delete.png"))
        self.img_view= PhotoImage(file=os.path.abspath("src/static/view.png"))
        self.img_duplicate_data= PhotoImage(file=os.path.abspath("src/static/duplicate-data.png"))
        self.img_refresh= PhotoImage(file=os.path.abspath("src/static/refresh.png"))
        self.img_order_number= PhotoImage(file=os.path.abspath("src/static/order-number.png"))
        self.img_order_word= PhotoImage(file=os.path.abspath("src/static/order-word.png"))
        
       





        # Application buttons

        # We create the buttons that will perform the options of our application.
        ttk.Button(frame01, image=self.img_open_database, command=self.open_file_database).grid(row=0, column=0, sticky = W)
        ttk.Button(frame01, image=self.img_create_database, command=self.create_file_database).grid(row=0, column=1, sticky = W)
        #ttk.Button(frame01, image=self.img_update_application, command=self.update_application).grid(row=0, column=2, sticky = W)
        ttk.Button(frame01, image=self.img_settings, command=self.settings).grid(row=0, column=4, sticky = W)
        
        








        # We create the buttons that will perform the CRUD

        # image = this property allows to put an image on the button
        ttk.Button(frame, image=self.img_add, command=self.add_window).grid(row=0, column=0, sticky = W)
        ttk.Button(frame, image=self.img_update, command=self.update_window).grid(row=0, column=1, sticky = W)
        ttk.Button(frame, image=self.img_delete, command=self.delete_window).grid(row=0, column=2, sticky = W)
        ttk.Button(frame, image=self.img_view, command=self.view_window).grid(row=0, column=3, sticky = W)
        ttk.Button(frame, image=self.img_duplicate_data, command=self.duplicate_data).grid(row=0, column=4, sticky = W)
        ttk.Button(frame, image=self.img_refresh, command=self.validation_database_options).grid(row=0, column=5, sticky = W)
        ttk.Button(frame, image=self.img_order_number, command=self.get_dictionary).grid(row=0, column=6, sticky = W)
        ttk.Button(frame, image=self.img_order_word, command=self.get_dictionary_order_word).grid(row=0, column=7, sticky = W)
        
        





        # We create a label and a text field where we can look for any data we need we need
        Label(frame, text = 'Search:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row=0, column=8)

        entry_t = Entry(frame, font=("{}".format(self.file_font_type), self.file_font_size))
        entry_t.grid(row=0, column=9, sticky = W+E)
        entry_t.bind('<KeyRelease>', self.scankey_t)
        









        # We create a label that will function as a message after performing an action

        # We create the label and store it in a property with the name "message"

        # text='' = here we don't pass any text since from the other functions we are 
        #           going to pass a text of our own that we pass a text of our own that 
        #           we want

       # fg='green' = this indicates the color the message will have
        self.message = Label(text='', font=("{}".format(self.file_font_type), self.file_font_size), fg='green')

        # Position the label inside the Frame
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)







        # We create a table to list the data

        # We store the table in a property of the class

        # .tree = name of the table that is going to be called in different functions
        # ttk.Treeview = this allows you to create a table or grid from Tkinter
        # height=15 = these are the number of rows that the table will display
        # columns=('#1', '#2') = these are the number of columns that the table will display
        self.tree = ttk.Treeview(height=15, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'))

        # Now we give a position to the table to be shown
        self.tree.grid(row=4, column=0, columnspan=2)






        # We give the colors that each row will have, with its respective alias, by means 
        # of which each color is going to be called, for each row
		
		# 'Lightgreen' = this is the alias by which each row will be identified in order to 
        #                give it its color
		
		# background='lightgreen' = this is the color that each row will have according to its alias
        self.tree.tag_configure('Green', background='lightgreen')
        self.tree.tag_configure('Orange', background='orange')
        self.tree.tag_configure('Blue', background='dodgerblue')
        self.tree.tag_configure('Purple', background='royalblue')






        # Now we add headers to the table

        # '#0' = this indicates the column number where the header will go
        # text= 'word' = this will be the name that the header will display
        # anchor=CENTER = this is to indicate that the header is to be centered
        self.tree.heading('#0', text= 'N°', anchor=CENTER) 
        self.tree.heading('#1', text= '', anchor=CENTER)
        self.tree.heading('#2', text= 'Word', anchor=CENTER)
        self.tree.heading('#3', text= 'Phonemic', anchor=CENTER)
        self.tree.heading('#4', text= 'Pronunciation', anchor=CENTER)
        self.tree.heading('#5', text= 'Type', anchor=CENTER)
        self.tree.heading('#6', text= 'Lesson', anchor=CENTER)
        self.tree.heading('#7', text= 'Module', anchor=CENTER)
        self.tree.heading('#8', text= 'Meaning', anchor=CENTER)
        self.tree.heading('#9', text= '', anchor=CENTER)
       
        



        # We change the size of the columns so that it does not look so far apart
        self.tree.column('#0', width=40)

        # stretch=NO = with this we prevent the column from being displayed, this is the id column, 
        #              and we need it to update the data. we need it to update the data
        self.tree.column('#1', width=0, stretch=NO)
        self.tree.column('#2', width=self.file_size_components_grid)
        self.tree.column('#3', width=self.file_size_components_grid)
        self.tree.column('#4', width=self.file_size_components_grid)
        self.tree.column('#5', width=self.file_size_components_grid)
        self.tree.column('#6', width=self.file_size_components_grid)
        self.tree.column('#7', width=self.file_size_components_grid)
        self.tree.column('#8', width=self.file_size_components_grid)
        self.tree.column('#9', width=0, stretch=NO)



        # We create a style to change the font size of the column headers of our list

        # font=(None, 10) = here we set the font size, in "None", we set the font type
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("{}".format(self.file_font_type), self.file_font_size, "bold"))
        style.configure("Treeview", font=("{}".format(self.file_font_type), self.file_font_size))


        
        # Now we add a scrollbar to the list 
        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=4, column=2, sticky='ns')








        # We create a Label to show the path to the database we have saved.
        Label(text = 'Saved database path: ', font=("{}".format(self.file_font_type), 9)).grid(row=5, column=0, columnspan=2, sticky=W)
        
        # Label that is going to receive the database path or a message that it does not exist
        self.path_database = Label(text='', font=("{}".format(self.file_font_type), 9), fg='blue')
        self.path_database.grid(row=5, column=1, sticky=W)







        # We call the function that allows to validate the options of our database, 
        # like indicating us the path of the database, if the database has been loaded, 
        # etc, with this we avoid to create the database automatically in the case that 
        # it does not exist
        self.validation_database_options()
    


        

      
       


        

















   
    # FUNCTIONS TO DISPLAY WINDOWS


    # We create a function to display a floating window where we are going to enter the 
    # data
    def add_window(self):

        # Here we open a new window to add the data.

        # We create a window on top of the previous one and store it in a variable

        # self.edit_wind = variable that will store the new variable
        # Toplevel() = this creates a window on top of the previous one.
        self.add_window = Toplevel()

        # We create a title for the new window and store it in a variable
        #self.add_window.title = 'Add Dictionary'




        # We prevent the user from maximizing the window and also block the maximize button
        self.add_window.resizable(width=False, height=False)




        # We give a resolution to our sale in order that all the fields that we add to our list 
        # enter and the window is not displayed in any part of the window, if not in the center 
        # this method we have used it to center in the screen.
        w = self.add_window.winfo_reqwidth()
        h = self.add_window.winfo_reqheight()


        ws = self.add_window.winfo_screenwidth()
        hs = self.add_window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.add_window.geometry('+%d+%d' % (x, y))




        # We create a Frame that will work as a container and we store it in a variable to position it, 
        # we create this Frame to show an outline in our form

        # self.wind = here we indicate where the Frame is going to be positioned, here we are indicating 
        # that it will be inside the "window" window.

        # text = '' = aqui le estoy indicando el titulo que va a tener el Frame
        frame = LabelFrame(self.add_window, text = 'Register a dictionary', font=("{}".format(self.file_font_type), self.file_font_size, "bold"))




        # Now we position the Frame that we have created

        # frame = variable that stores the Frame that we have previously created

        # grid = method that allows us to indicate in which position of the window is going to be our button 
        #        or text input, this is an invisible grid, that will help us to place our elements according 
        #        to the position we want

        # row=0 = this indicates that this element will be in row 0 of our grid, the value is indicated in pixels

        # column=0 = this indicates that this element will be in column 0 of our grid

        # columnspan=3 = this indicates how many columns of our grid will cover our window, that is to say, it will 
        #                be empty columns without any content, that is to say with this we will to center the frame

        # pady=20 = this is a padding, it indicates an internal spacing of each element, so that the elements are not 
        #          so close together. here we indicate in pixels the spacing at the top and at the bottom of each element
        frame.grid(row=0, column=0, columnspan=3, pady=20)





        # We create a label and a text box to enter the new "word"

        # Label = allows you to create a text in the window

        # frame = here we indicate where the Label will be positioned, here we are indicating that it will be inside the Frame
        #         we have previously created.

        # text='word: ' = here I am indicating the text of the label

        # grid() = this allows the positioning of the Label() element, as previously done with the frame

        # font() = here we set the font type and size

        # self.file_font_type = here is the font we have imported from our .txt file. .txt file, in the main function of this file.

        # self.file_font_size = here is the font size that we have imported from our .txt file. .txt file, in the main function of 
        #                       this file.
        Label(frame, text = 'Word:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 1, column = 1)


        # We create an input field to enter the data.

        # word = here we store the text field in a variable

        # Entry(frame) = this represents an entry, that is a text box where we will insert the values

        # self.file_size_components = here is the size of the components that we have imported from our file .txt file, in the main 
        #                             function of this file
        word = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))

        # Now we position the input field
        word.grid(row = 1, column = 2)

        
        
        Label(frame, text = 'Phonemic:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 3, column = 1)
        phonemic = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        phonemic.grid(row = 3, column = 2)


        Label(frame, text = 'Pronunciation:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 5, column = 1)
        pronunciation = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        pronunciation.grid(row = 5, column = 2)


        Label(frame, text = 'Type:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 7, column = 1)
        type = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        type.grid(row = 7, column = 2)


        
        Label(frame, text = 'Lesson:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 9, column = 1)
        lesson= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        lesson.grid(row = 9, column = 2)

        
        Label(frame, text = 'Module:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 11, column = 1)
        module= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size))
        module.grid(row = 11, column = 2)

        # We create a label and a text box to enter the new "meaning".

        # Text = here instead of creating a normal text box we create a Text Area, since we are going to enter a long text. we are 
        #        going to enter a long text
        Label(frame, text = 'Meaning:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 13, column = 1)
        meaning= Text(frame, width=self.file_size_components, height = 3, font=("{}".format(self.file_font_type), self.file_font_size))
        meaning.grid(row = 13, column = 2)



        # Create an OptionMenu, to select the color that each row will have
        Label(frame, text = 'Color:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 15, column = 1)

        OPTIONS = [
        "White",
        "Green",
        "Orange",
        "Blue",
        "Purple"
        ] #etc

        
        self.variable_color = StringVar(frame)
        self.variable_color.set(OPTIONS[0]) # default value

        # We obtain the data for the OptionMenu and execute a function to change the color

        # command=self.change_color = we call this function to change the color of the OptionMenu
        self.color = OptionMenu(frame, self.variable_color, *OPTIONS, command=self.change_color)
        self.color.grid(row = 15, column = 2)
        self.color.config(width=self.file_size_components, font=("{}".format(self.file_font_type)))



        # We create a label that will function as a message after performing an action
        self.message_aw = Label(frame, text='', font=("{}".format(self.file_font_type), self.file_font_size), fg='red')
        self.message_aw.grid(row=16, column=2, sticky=W+E)



        # Create a button to insert the data

        # lambda = allows to execute a function in this same window
        # add_dictionary() = function that will allow the insertion of data
        # word.get(), lesson.get()....) = these are parameters that the function expects to receive
        # sticky=W+E = this indicates that it should cover the full width of our window, from West to East.
        # meaning.get(1.0, "end-1c") = to get the information entered in the Text Area, it is mandatory to add these parameters
        Button(frame, text = 'Add', font=("{}".format(self.file_font_type), self.file_font_size), command = lambda: self.add_dictionary(
            word.get(), phonemic.get(), pronunciation.get(), type.get(), lesson.get(), module.get(), meaning.get(1.0, "end-1c"), self.variable_color.get())).grid(row = 17, column = 2, sticky=W+E)
        

        # We execute the window events
        self.add_window.mainloop()

    


    

    







    # We create a function to display a floating window where we are going to edit the data
    def update_window(self):

        # We clean up our message or label, in case it has any data
        self.message['text'] = ''

        # We create a try-catch, to avoid errors, in case the user has not selected any data. selected any data to update

        # In the case that a row of data has been selected, we will obtain the data and store them in variables

        # Here we do not add the "meaning" field, as this value goes directly into the Text Area, because it is the only 
        # way we have found to pass it the value
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            word = self.tree.item(self.tree.selection())['values'][1]
            phonemic = self.tree.item(self.tree.selection())['values'][2]
            pronunciation = self.tree.item(self.tree.selection())['values'][3]
            type = self.tree.item(self.tree.selection())['values'][4]
            lesson = self.tree.item(self.tree.selection())['values'][5]
            module = self.tree.item(self.tree.selection())['values'][6]
            meaning = self.tree.item(self.tree.selection())['values'][7]
            color = self.tree.item(self.tree.selection())['values'][8]

        # We display an error message for the user to select a data row that needs to be edited
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return


        self.update_window = Toplevel()
        
        self.update_window.resizable(width=False, height=False)



        w = self.update_window.winfo_reqwidth()
        h = self.update_window.winfo_reqheight()

        ws = self.update_window.winfo_screenwidth()
        hs = self.update_window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.update_window.geometry('+%d+%d' % (x, y))




        frame = LabelFrame(self.update_window, text = 'Update Dictionary', font=("{}".format(self.file_font_type), self.file_font_size, "bold"))
        frame.grid(row=0, column=0, columnspan=3, pady=20)


        
        Label(frame, text = 'Word:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 1, column = 1)
        word = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = word))
        word.grid(row = 1, column = 2)

        Label(frame, text = 'Phonemic:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 3, column = 1)
        phonemic = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = phonemic))
        phonemic.grid(row = 3, column = 2)

        Label(frame, text = 'Pronunciation:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 5, column = 1)
        pronunciation = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = pronunciation))
        pronunciation.grid(row = 5, column = 2)

        Label(frame, text = 'Type:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 7, column = 1)
        type = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = type))
        type.grid(row = 7, column = 2)

        Label(frame, text = 'Lesson:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 9, column = 1)
        lesson= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = lesson))
        lesson.grid(row = 9, column = 2)
        
        Label(frame, text = 'Module:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 11, column = 1)
        module= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = module))
        module.grid(row = 11, column = 2)
       
        # Here to insert a value to the Text Area we use .insert() and pass as value all the code we used in the previous 
        # try{} catch{}, this is the only way to get the value inside the Text Area.
        Label(frame, text = 'Meaning:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 13, column = 1)
        meaning= Text(frame, width=self.file_size_components, height = 3, font=("{}".format(self.file_font_type), self.file_font_size))
        meaning.insert(INSERT, self.tree.item(self.tree.selection())['values'][7])
        meaning.grid(row = 13, column = 2)



        Label(frame, text = 'Color:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 15, column = 1)

        OPTIONS = [
        "White",
        "Green",
        "Orange",
        "Blue",
        "Purple"
        ] #etc


        # We get the value position in our array according to the color we get from our database field
        id_array = OPTIONS.index(color)

        self.variable_color = StringVar(frame)

        
        # Here we send the id of the array value, to show the color we have in our selected row
        
        # id_array = position of the array value
        self.variable_color.set(OPTIONS[id_array]) # default value


        self.color = OptionMenu(frame, self.variable_color, *OPTIONS, command=self.change_color)
        self.color.grid(row = 15, column = 2)
        self.color.config(width=self.file_size_components, font=("{}".format(self.file_font_type)))

        # We get the color of our field to give the background color to our OptionMenu.
        self.color.config(bg=color)
        
        



        self.message_uw = Label(frame, text='', font=("{}".format(self.file_font_type), self.file_font_size), fg='red')
        self.message_uw.grid(row=16, column=2, sticky=W+E)


        Button(frame, text = 'Update', font=("{}".format(self.file_font_type), self.file_font_size), command = lambda: self.update_dictionary(
            id, word.get(), phonemic.get(), pronunciation.get(), type.get(), lesson.get(), module.get(), meaning.get(1.0, "end-1c"), self.variable_color.get())).grid(row = 17, column = 2, sticky=W+E)
        

        self.update_window.mainloop()



    
    







    # We create a function to display a message where we are going to delete the data
    def delete_window(self):
        
        self.message['text'] = ''

        try:
            id = self.tree.item(self.tree.selection())['values'][0]
          
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return



        # We show a dialog message, to decide whether or not to delete the data
        res = messagebox.askquestion('Delete Dictionary', 'Do you want to delete this data?')
        
        if res == 'yes' :

            # We execute the function to delete the data passing the id to it
            self.delete_dictionary(id)

            messagebox.OK

            # We call the label that is going to act as message
            self.message.config(fg='green')
            self.message['text'] = 'Dictionary deleted successfully'
            
        else :
            messagebox.CANCEL



    





    # We create a function to display the data
    def view_window(self):

        self.message['text'] = ''


        try:
            word = self.tree.item(self.tree.selection())['values'][1]
            phonemic = self.tree.item(self.tree.selection())['values'][2]
            pronunciation = self.tree.item(self.tree.selection())['values'][3]
            type = self.tree.item(self.tree.selection())['values'][4]
            lesson = self.tree.item(self.tree.selection())['values'][5]
            module = self.tree.item(self.tree.selection())['values'][6]
            meaning = self.tree.item(self.tree.selection())['values'][7]
            color = self.tree.item(self.tree.selection())['values'][8]
            
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return

       
        self.view_window = Toplevel()
        

        self.view_window.resizable(width=False, height=False)



        w = self.view_window.winfo_reqwidth()
        h = self.view_window.winfo_reqheight()

        ws = self.view_window.winfo_screenwidth()
        hs = self.view_window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.view_window.geometry('+%d+%d' % (x, y))




        frame = LabelFrame(self.view_window, text = 'View dictionary', font=("{}".format(self.file_font_type), self.file_font_size, "bold"))
        frame.grid(row=0, column=0, columnspan=3, pady=20)


        Label(frame, text = 'Word:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 1, column = 1)
        word = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), state = 'readonly', textvariable = StringVar(frame, value = word))
        word.grid(row = 1, column = 2)

        Label(frame, text = 'Phonemic:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 3, column = 1)
        phonemic = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = phonemic))
        phonemic.grid(row = 3, column = 2)

        Label(frame, text = 'Pronunciation:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 5, column = 1)
        pronunciation = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = pronunciation))
        pronunciation.grid(row = 5, column = 2)

        Label(frame, text = 'Type:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 7, column = 1)
        type = Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), textvariable = StringVar(frame, value = type))
        type.grid(row = 7, column = 2)

        Label(frame, text = 'Lesson:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 9, column = 1)
        lesson= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), state = 'readonly', textvariable = StringVar(frame, value = lesson))
        lesson.grid(row = 9, column = 2)
        
        Label(frame, text = 'Module:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 11, column = 1)
        module= Entry(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), state = 'readonly', textvariable = StringVar(frame, value = module))
        module.grid(row = 11, column = 2)
       
        Label(frame, text = 'Meaning:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 13, column = 1)
        meaning= Text(frame, width=self.file_size_components, font=("{}".format(self.file_font_type), self.file_font_size), height = 3)
        meaning.insert(1.0, self.tree.item(self.tree.selection())['values'][7])
        meaning.config(state= DISABLED)
        meaning.grid(row = 13, column = 2)


        Label(frame, text = 'Color:', font=("{}".format(self.file_font_type), self.file_font_size)).grid(row = 15, column = 1)
        
        OPTIONS = [
        "White",
        "Green",
        "Orange",
        "Blue",
        "Purple"
        ] #etc

        id_array = OPTIONS.index(color)
        self.variable_color = StringVar(frame)
        self.variable_color.set(OPTIONS[id_array]) 

        self.color = OptionMenu(frame, self.variable_color, *OPTIONS, command=self.change_color)
        self.color.grid(row = 15, column = 2)
        self.color.config(width=self.file_size_components, font=("{}".format(self.file_font_type)))

        self.color.config(bg=color, state="disabled")


        Button(frame, text = 'Cerrar', font=("{}".format(self.file_font_type), self.file_font_size), command=self.view_window.destroy).grid(row = 16, column = 2, sticky=W+E)
        
        
        self.view_window.mainloop()








    # We create a function to duplicate the record we need
    def duplicate_data(self):

        from controller.insert import Insert

        self.message['text'] = ''

        try:
            word = self.tree.item(self.tree.selection())['values'][1]
            phonemic = self.tree.item(self.tree.selection())['values'][2]
            pronunciation = self.tree.item(self.tree.selection())['values'][3]
            type = self.tree.item(self.tree.selection())['values'][4]
            lesson = self.tree.item(self.tree.selection())['values'][5]
            module = self.tree.item(self.tree.selection())['values'][6]
            meaning = self.tree.item(self.tree.selection())['values'][7]
            color = self.tree.item(self.tree.selection())['values'][8]

            # word_duplicate = this variable will be passed in order to insert it
            word_duplicate = word+" Duplicate"
            
        except IndexError as e:
            self.message.config(fg='orange')
            self.message['text'] = 'Please select a record'
            return

        # We apply the same as in the "add_dictionary() function
        Insert.add_dictionary(word_duplicate, phonemic, pronunciation, type, lesson, module, meaning, color)

        self.message.config(fg='green')
        self.message['text'] = 'Data successfully duplicated'

        self.get_dictionary()








    # We create this function to change the color of the OptionMenu in the add and edit windows, each time we select a 
    # different color 
    def change_color(self, choice):

        # Here we get the color that has been selected in the OptionMenu.
        choice = self.variable_color.get()
        
        # Here we give the color to our OptionMenu
        self.color.config(bg=choice)






    

    

    
    

    


























    # FUNCTIONS TO PERFORM THE CRUD



    # We create a function to obtain the list of data
    def get_dictionary(self):

        # We import the classes where a CRUD is going to be made.

        # list = refers to the file "src/controller/list.py".
        # list = name of the class that contains "src/controller/list.py"
        from controller.list import List

        
        


        # We give the color styles that our "Treeview" will have, so that the rows are shown with their respective 
        # color
        self.style = ttk.Style()
        self.style.map("Treeview", foreground=self.fixed_map("foreground"), background=self.fixed_map("background"))
    
        




        # We obtain all the elements of the table, with the purpose of performing cleaning of the table, in case there 
        # is any data in the table.

        # .tree = name of the table we have created previously
        # get_children() = this method allows to get the data of the table
        records = self.tree.get_children()





        # We go through the elements of the table in order to clean them.

        # By means of a loop or for we go through the elements

        # element = variable that will delete each element in the table
        for element in records:
            # We remove each element from the table

            # delete() = method for deleting elements from the table
            self.tree.delete(element)

        




        # We call the following function, which will fetch the list of data from the database
        lista = List.list_dictionary()

    



        # We create a counter and start it, with the purpose of knowing the amount of data we have registered
        self.i = 1

       
        

        # We fill the data obtained from the query into the table

        # id, word, phonemic, pronunciation, type... = variables storing the data obtained from our query
        for id, word, phonemic, pronunciation, type, lesson, module, meaning, color  in zip(*lista): 

            # We insert the data of our query in the table.

            # insert() = este metodo permirte insertar valores dentro de la tabla

            # '', 0 = here we indicate that position 0 of the query, do not insert any value in the table in the table

            # text = self.i = here we tell it to insert the counter in position 0 of the table as text

            # values = row[2] = here we indicate that the position 2 of the query, insert in the table as a value, here 
            #                   we have the price of the product

            # tags=(color,) = here we give the alias to show the color, for each row

            # color = this data will not be displayed in the Treeview, it will only be used to obtain the alias and thus 
            #         display the color for each row.
            self.tree.insert('', 0, text = self.i, values = (id, word, phonemic, pronunciation, type, lesson, module, meaning, color), tags=(color,))

           # We increment the counter created above
            self.i = self.i + 1








   
    # We create a function that will insert the data
    def add_dictionary(self, word, phonemic, pronunciation, type, lesson, module, meaning, color):

        from controller.insert import Insert

        # We call the validation_add_window() function, to check that the user is entering the data in the text boxes

        # validation_add_window() = this function will return true as first value, otherwise false
        if self.validation_add_window(word, phonemic, pronunciation, type, lesson, module, meaning):

            # We call the function add_dictionary(), of the Insert class, located in the file src/controller/insert.py, 
            # which will allow us to insert the data

            # word, lesson... = these are the values that we are going to insert
            Insert.add_dictionary(word, phonemic, pronunciation, type, lesson, module, meaning, color)

           # We close the window once the data is inserted.
            self.add_window.destroy()


            # We call the label that will act as a message to indicate that the record has been inserted

            # message['text'] = we call the "text" property of the label, in order to pass it the message we want to display 
            #                   we want to display

            # {} = this allows to add a value inside the message

            # format() = allows you to pass a value inside the braces {}
            self.message.config(fg='green')
            self.message['text'] = 'Dictionary added successfully'


            # we call the function get_dictionary(), so that the data is updated after we we enter
            self.get_dictionary()
        

  
       



        



    # We create a function that will update the data
    def update_dictionary(self, id, word, phonemic, pronunciation, type, lesson, module, meaning, color):

        from controller.update import Update

        if self.validation_update_window(word, phonemic, pronunciation, type, lesson, module, meaning):

            Update.update_dictionaryt(id, word, phonemic, pronunciation, type, lesson, module, meaning, color)

            self.update_window.destroy()

            self.message.config(fg='green')
            self.message['text'] = 'Dictionary updated successfully'

            self.get_dictionary()

    






    # We create a function that will delete the data
    def delete_dictionary(self, id):

        from controller.delete import Delete

        Delete.delete_dictionary(id)

        self.get_dictionary()


    









    # We create a function to obtain the list of products sorted in descending alphabetical order
    def get_dictionary_order_word(self):

        from controller.list_order_word import ListOrderWord

        # We apply the same procedure we used to obtain the list of data
        self.style = ttk.Style()
        self.style.map("Treeview", foreground=self.fixed_map("foreground"), background=self.fixed_map("background"))
    
        records = self.tree.get_children()

        for element in records:
            self.tree.delete(element)

        lista = ListOrderWord.list_dictionary_order_word()


        self.i = 1

        for id, word, phonemic, pronunciation, type, lesson, module, meaning, color  in zip(*lista): 
            self.tree.insert('', 0, text = self.i, values = (id, word, phonemic, pronunciation, type, lesson, module, meaning, color), tags=(color,))
            self.i = self.i + 1










   
    # We create a function that allows us to search the database for a data that we enter
    def search_dictionary(self, data):

        from controller.search import Search

        # We apply the same procedure we used to obtain the list of data
        self.style = ttk.Style()
        self.style.map("Treeview", foreground=self.fixed_map("foreground"), background=self.fixed_map("background"))

        records = self.tree.get_children()

        for element in records:
            self.tree.delete(element)


        # We call the function search_word(), of the Search class, located in the file src/controller/search.py

        # data = this is the value for which we are going to search the database
        lista_search = Search.search_dictionary(data)

    
        self.i = 1

        for id, word, phonemic, pronunciation, type, lesson, module, meaning, color in zip(*lista_search): 

            self.tree.insert('', 0, text = self.i, values = (id, word, phonemic, pronunciation, type, lesson, module, meaning, color), tags=(color,))
            self.i = self.i + 1






    # We create a function which will allow us to obtain the value that we enter in the text box in a quick way
    def scankey_t(self, event):
        
        # We obtain the data we entered in the text box in real time

        # event.widget.get() = permite obtener el valor ingresado en la caja de texto en 
        #                      tiempo real
        val = event.widget.get()

        


        # Validate if no value exists in the text box, we will show the whole list of data
        if val == '':
            self.get_dictionary()
        # Otherwise we pass the data that we have entered in the text box to search the database
        else:
            self.search_dictionary(val)





























    # FUNCTIONS OF OUR APPLICATION OPTIONS


    # We create this function that will allow us to open the database file
    def open_file_database(self):
        
        # We open the .txt file containing the path to the database we want to save
        #f = open('src/settings/route-o-database.txt', 'r')
        #route_database = f.read()
        #f.close()


        # We open a window to browse for the database file
        x = filedialog.askopenfilename(title = "Open File", filetypes=[('Database','*.db')])


        # We perform a validation to check that the path of the database file  is not empty
        if (x==() or x==''):

            self.message.config(fg='orange')
            self.message['text'] = 'No database has been selected'

        else:

            # We save the database path in our .txt file
            with open('src/settings/route-o-database.txt', 'w') as f:
                f.write(x)
        
        
           
            # We give a font size to the text in our dialog box
            window.option_add('*Dialog.msg.font', 'Helvetica 11')
            # We show a dialog message, to decide whether or not to save the database path
            res = messagebox.askquestion('Do you want to save the database path?', '{}'.format(x))
            

            # We validate our message
            if res == 'yes' :

                # We insert the id 1 in our .txt file, to indicate that it has saved the path to the 
                # database and no longer look for the database file again
                with open('src/settings/id-s-database.txt', 'w') as f:
                    f.write("1")

                self.message.config(fg='green')
                self.message['text'] = 'Database loaded correctly'


                # We open the .txt file that contains the path where the database will be opened and then 
                # automatically update the database path that it will contain our label
                f_route_open_database = open('src/settings/route-o-database.txt', 'r')
                route_open_database = f_route_open_database.read()
                f_route_open_database.close()
            

                # We update the database path to our label that will contain the path
                self.path_database['text'] = route_open_database


                # We show the list of data in case they exist
                self.get_dictionary()


                messagebox.OK

                
                
            else :

                # We insert the id 0 in our .txt file, to tell it not to save the database 
                # path and reopen it. and reopen it
                with open('src/settings/id-s-database.txt', 'w') as f:
                    f.write("0")

                self.message.config(fg='orange')
                self.message['text'] = 'Database loaded correctly, but the path has not been saved.'

                # We display a message that there is no saved path to the database
                self.path_database['text'] = "No saved database path exists"


                # We show the list of data in case they exist
                self.get_dictionary()


                messagebox.CANCEL







    # We create this function that will allow to create the database file
    def create_file_database(self):

        # We open a window to search for the directory where the database will be created
        x = filedialog.askdirectory(title = "Open Directory")


        if (x==() or x==''):

            self.message.config(fg='orange')
            self.message['text'] = 'No directory has been selected'
            
        else:
            
            # We save the database path in our .txt file
            with open('src/settings/route-c-database.txt', 'w') as f:
                f.write(x)

            # We call the file that is going to create the database
            subprocess.call("python src/model/database_create.py", shell=True)

            self.message.config(fg='green')
            self.message['text'] = 'Database created correctly and path saved'


            # We open the .txt file that contains the path where the database will be opened 
            # and then automatically update the database path that it will contain our label
            f_route_open_database = open('src/settings/route-o-database.txt', 'r')
            route_open_database = f_route_open_database.read()
            f_route_open_database.close()
        

            # We update the database path to our label that will contain the path
            self.path_database['text'] = route_open_database
            







    # Creamos esta funcion que va a permitir actualizar nuestra aplicacion
    def update_application(self):

        window.option_add('*Dialog.msg.font', 'Helvetica 11')
        # Mostramos un mensaje de dialogo, para decidir si guardamos o no la ruta de la base de datos
        res = messagebox.askquestion(title = "Update", message = "If you update the application will the programme close?")
        

        if res == 'yes' :
        
            window.destroy()
            
            #subprocess.call("", shell=True)
            #subprocess.call('sh -c "./update-gnu-linux.sh; echo; ${SHELL:-bash}"', shell=True)

            #os.system("xfce4-terminal -e 'bash -c \"cp ~/dictionary-english/update-gnu-linux.sh ~ && cd ~ && ./update-gnu-linux.sh; bash\" '")
            os.system("ls")

            messagebox.OK

            
        
        else:

            messagebox.CANCEL

    






    # We create a function to show a floating window where we are going to show the visual settings 
    # of the application
    def settings(self):

        
        self.settings = Toplevel()
        self.settings.title = 'Settings'


        # We prevent the user from maximizing the window and also block the maximize button
        self.settings.resizable(width=False, height=False)



        # We give a resolution to our sale with the purpose that all the fields that we are adding 
        # to our list enter and the window is not shown in any part of the window, if not in the center 
        # this method we have used it to center in the screen
        w = self.settings.winfo_reqwidth()
        h = self.settings.winfo_reqheight()


        ws = self.settings.winfo_screenwidth()
        hs = self.settings.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.settings.geometry('+%d+%d' % (x, y))






        # We create a Frame that will work as a container and we store it in a variable to position it, we 
        # create this Frame to show an outline in our form
        frame = LabelFrame(self.settings, text = 'Settings', font=("{}".format(self.file_font_type)))
        frame.grid(row=0, column=0, columnspan=3, pady=20)





        # We create a label and a text box to enter the font type
        Label(frame, text = 'Font type:', font=("{}".format(self.file_font_type))).grid(row = 1, column = 1)
        
        # We create the ListBox and add its configuration
        self.font_type = Listbox(frame, width=self.file_size_components, font=("{}".format(self.file_font_type)), height = 5)
        self.font_type.grid(row = 1, column = 2)
        
        # We create this configuration for our Listbox to prevent Listbox from losing its selection when clicking 
        # on another part of the form
        self.font_type.configure(exportselection=False)

        # We call all Tkinter typefaces
        fonts=list(font.families())
        fonts.sort()

        # We create a for to go through the list of all the fonts that exist in Tkinter and insert it in our Listbox
        for item in fonts:
            # We insert in the Listbox the list of data
            self.font_type.insert(END, item)

        


        # We create an OptionMenu, to select the percentage of the elements that our application will have
        Label(frame, text = 'Size:', font=("{}".format(self.file_font_type))).grid(row = 3, column = 1)

        OPTIONS = [
        "10%",
        "15%",
        "20%",
        "25%"
        ] #etc

        
        self.variable = StringVar(frame)
        self.variable.set(OPTIONS[0]) # default value



        self.size = OptionMenu(frame, self.variable, *OPTIONS)
        self.size.grid(row = 3, column = 2)
        self.size.config(width=self.file_size_components, font=("{}".format(self.file_font_type)))


        #font_type = Arial
        #font_size = 10
        #size_components = 50
        #size_components_grid = 120





        # We create a button to be able to insert the data

        # lambda = allows you to execute a function in this same window
        # add_dictionary() = function that will allow you to insert the data
        # word.get(), lesson.get()....) = are parameters that the function expects to receive
        # sticky=W+E = this indicates that it should cover the entire possible width of our window, from West to East.
        # meaning.get(1.0, "end-1c") = to obtain the information entered in the Text Area, it is mandatory to add the following parameters
        Button(frame, text = 'Apply', font=("{}".format(self.file_font_type)), 
               command = lambda: self.get_settings(self.font_type.get(self.font_type.curselection()) , self.variable.get())).grid(row = 9, column = 2, sticky=W+E)

        
        # We execute the events of the window
        self.settings.mainloop()

    


   

    





    # We create a function that will save the program configurations in text files 
    def get_settings(self, font_type, size):


        # We perform a validation of the size field and then using a rule of 3 automatically 
        # calculate the pixels that our window will have

        if (size == "10%"):

            print("Es el 10%")
            
            font_size = "10"
            size_components = "50"
            size_components_grid = "120"
        
        elif (size == "15%"):
            print("Es el 15%")

            font_size = "15"
            size_components = "75"
            size_components_grid = "180"

        elif (size == "20%"):
            print("Es el 20%")

            font_size = "20"
            size_components = "100"
            size_components_grid = "240"
        
        elif (size == "25%"):
            print("Es el 25%")

            font_size = "25"
            size_components = "125"
            size_components_grid = "300"
        
        
        
        


      

        
        # We give a font size to the text in our dialog box
        window.option_add('*Dialog.msg.font', 'Helvetica 11')
        # We show a dialog message, to decide whether or not to save the database path
        res = messagebox.askquestion(title = "Apply settings", message = "The application will restart to apply the changes")
        
        
        if res == 'yes' :

             # We save the typeface of our forms in our .txt file
            with open('settings/font-type.txt', 'w') as f:
                f.write(font_type)

            # We save the font size of our forms in our .txt file
            with open('settings/font-size.txt', 'w') as f:
                f.write(font_size)

            # We save the size of the components of our forms in our .txt file
            with open('settings/size-components.txt', 'w') as f:
                f.write(size_components)
            
            # We save the size of the components of our forms in our .txt file
            with open('settings/size-component-grid.txt', 'w') as f:
                f.write(size_components_grid)
        
            # Close the window
            window.destroy()
            


            messagebox.OK

            
        
        else:

            
            messagebox.CANCEL

            self.settings.destroy()

        





    






















    # FUNCTIONS THAT ARE GOING TO VALIDATE OUR APPLICATION



    # Functions to validate the text boxes


    # We create a function to validate that the text boxes are not empty.
    def validation_add_window(self, word, phonemic, pronunciation, type, lesson, module, meaning):

        # We call the following file and its class to check if the word exists
        from controller.data_exists import DataExists

        # We obtain the amount of existing data to then validate
        word_count = DataExists.data_exists_dictionary(word)






        # Validate that the text boxes are not empty

        # len = method for obtaining the length of an element
        # == 0 = here we indicate that the length of the entered value is equal to 0
        if(len(word) == 0):

            # We call the label that will act as a message to indicate that the record has been inserted
            self.message_aw['text'] = 'Word is required'

        elif(len(phonemic) == 0):

            self.message_aw['text'] = 'Phonemic is required'

        elif(len(pronunciation) == 0):

            self.message_aw['text'] = 'Pronunciation is required'

        elif(len(type) == 0):

            self.message_aw['text'] = 'Type is required'

        elif(len(lesson) == 0):

            self.message_aw['text'] = 'Lesson is required'

        elif(len(module) == 0):

            self.message_aw['text'] = 'Module is required'
        
        elif(len(meaning) == 0):

            self.message_aw['text'] = 'Meaning is required'
        
        # Validate if there is more than 1 word, we will show the following message, so that you do not enter 
        # the same word again
        elif(word_count > 0):

            self.message_aw['text'] = 'This word already exists in the database'

        # Otherwise, we return the data values to insert them
        else:
            return word and lesson and module and meaning






    #  Let's create a function that will allow to validate that the text boxes are not empty in the update form
    def validation_update_window(self, word, phonemic, pronunciation, type, lesson, module, meaning):


        if(len(word) == 0):

            self.message_uw['text'] = 'Word is required'
        
        elif(len(phonemic) == 0):

            self.message_uw['text'] = 'Phonemic is required'

        elif(len(pronunciation) == 0):

            self.message_uw['text'] = 'Pronunciation is required'
        
        elif(len(type) == 0):

            self.message_uw['text'] = 'Type is required'
        
        elif(len(lesson) == 0):

            self.message_uw['text'] = 'Lesson is required'

        elif(len(module) == 0):

            self.message_uw['text'] = 'Module is required'
        
        elif(len(meaning) == 0):

            self.message_uw['text'] = 'Meaning is required'
        

        else:
            return word and lesson and module and meaning
        







    # Functions to be used by our application

    # We create this function that allows to validate the options of our database, like indicating us the 
    # path of the database, if the database has been loaded, etc
    def validation_database_options(self):

        # Validate that the database file and path exist

        # We open the .txt file that contains the id of whether we have saved or not the database path
        f_id_save_database = open('src/settings/id-s-database.txt', 'r')
        id_save_database = f_id_save_database.read()
        f_id_save_database.close()



        # Open the .txt file containing the path where the database will be opened
        f_route_open_database = open('src/settings/route-o-database.txt', 'r')
        route_open_database = f_route_open_database.read()
        f_route_open_database.close()



        # We convert from String to integer so that we can validate the value that we obtain from the .txt 
        # since it is obtained in String format
        id_save_database_var = int(id_save_database)



        # We perform a validation to know whether or not we have saved the database path
        # 1 = indicates that we have decided to save the database route
        # 0 = indicates that we have not saved the database path  
        if id_save_database_var == 1:

            # Validate if the directory exists and if the database file exists inside it
            database_file = os.path.exists(os.path.join("{}".format(route_open_database)))


            # The above variable will give us a true, if the directory and the database file exists otherwise a false
            if database_file:

                # If it exists, we display a message by console
                print("Database exists")

                # If the database exists we create a variable where the database path will be stored
                self.path_database['text'] = route_open_database

                # We send to our variable the path or the message that the database exists or not
                #self.path_database['text'] = route_open_database_var
                self.get_dictionary()

                
                
            else:

                # If it exists, we display a message by console
                print("Database no exists")
                
                # We display a message that the database does not exist
                self.message.config(fg='red')
                self.message['text'] = 'No database file loaded, you must create or open a database.'


                # If the database exists we create a variable where the database path will be stored
                self.path_database['text'] = route_open_database

            
        else:

            print("No saved database path exists")

            # We display a message that the database does not exist
            self.message.config(fg='red')
            self.message['text'] = 'No database file loaded, you must create or open a database.'

            # If the database does not exist we create a variable where it will store a message that does 
            # not exist saved path to the database
            self.path_database['text'] = "No saved database path exists"









    # We create this function that allows to add color to the different rows of the "Treeview" or list of data, 
    # in addition, it allows to show the row that we have selected with the mouese changing color, we add it at 
    # the end since for some reason it causes conflicts with the other functions if you put it at the top
    def fixed_map(self, option):
	    return [elm for elm in self.style.map("Treeview", query_opt=option) if elm[:2] != ("!disabled", "!selected")]



    










# STARTING THE APPLICATION

# We check if this file is the one that will start our application and then display the window with graphical interface
if __name__ == '__main__':

    # Initializing the module that will start the window and storing it in a variable in a variable

    # Tk() = this will be the module that will start our window and that we have imported initially imported initially
    window = Tk()



    # We prevent the user from maximizing the window and also block the maximize button
    window.resizable(width=False, height=False)

    

    # We instantiate the class and store it in a variable

    # window = parameter that we pass to the class, which will contain the startup of the window
    application = Ventana(window)



    # We start the window

    # window.mainloop () = tells Python to execute the Tkinter event loop. This method detects events, such as button 
    #                      clicks or keystrokes, and blocks the execution of any code that comes after it until the window 
    #                      is closed to which is called
    window.mainloop()
