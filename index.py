from tkinter import *

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x720')
        self.root.title('Gestion des Archives')
        self.root.configure(background="lightBlue")
        self.root.resizable(False,False)
        title = Label(self.root, 
            text='systeme de l"archivage',
            bg='blue',
            fg='white'
        )
        title.pack()
        
        


root = Tk()

Std_Obj = Student(root)

root.mainloop()