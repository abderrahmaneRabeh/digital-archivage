from tkinter import *

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x720')
        self.root.title('Gestion des Archives')
        self.root.configure(background="#7AE2CF")
        self.root.resizable(False,False)
        title = Label(self.root, 
            text='systeme de l"archivage',
            bg='#077A7D',
            fg='white',
            font=('monospace',12,'bold')
        )
        title.pack(fill=X)
        
        


root = Tk()

Std_Obj = Student(root)

root.mainloop()


# 06202B
# FDEB9E
# 007979
# 303841
