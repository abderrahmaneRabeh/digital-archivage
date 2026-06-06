from tkinter import *


class Courrier:
    def __init__(self, root):
        self.root = root
        # self.root.geometry('1440x900')
        self.root.geometry(
            f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}"
        )
        # This is called an f-string (formatted string).
        # winfo_screenwidth() → gets your screen width
        # winfo_screenheight() → gets your screen height
        # so the window adapts automatically
        self.root.title("Gestion des Archives")
        self.root.configure(background="#7AE2CF")
        self.root.resizable(False, False)
        title = Label(
            self.root,
            text='systeme de l"archivage',
            bg="#077A7D",
            fg="white",
            font=("monospace", 12, "bold"),
        )
        title.pack(fill=X)

        Manage_Frame = Frame(self.root, bg="white")
        Manage_Frame.place(x=1100, y=25, width=450, height=850)

        # inputs
        Num_Msg = Label(
            Manage_Frame,
            text="Numéro du message",
            bg="#007979",
            fg="white",
            font=("Helvetica", 11, "bold"),
            padx=10,
            pady=5,
        )
        Msg_input = Entry(
            Manage_Frame,
            bd=2,
            font=("Helvetica", 11),
            width=30,
            relief=SOLID,
        )
        Num_Msg.pack(pady=(10, 5), fill=X)
        Msg_input.pack(padx=10, pady=(0, 15))


root = Tk()

Courrier_Obj = Courrier(root)

root.mainloop()


# 06202B
# FDEB9E
# 007979
# 303841
