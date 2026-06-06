from tkinter import *


class Courrier:
    def __init__(self, root):
        self.root = root
        self.root.geometry(
            f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}"
        )
        self.root.title("Gestion des Archives")
        self.root.configure(background="#7AE2CF")
        self.root.resizable(False, False)
        title = Label(
            self.root,
            text="systeme de l'archivage",
            bg="#077A7D",
            fg="white",
            font=("monospace", 12, "bold"),
        )
        title.pack(fill=X)

        Manage_Frame = Frame(self.root, bg="white")
        Manage_Frame.place(x=1130, y=25, width=400, height=850)

        # inputs
        self.Msg_input = self.create_input(Manage_Frame, "Numéro du message")
        self.Msg_date_input = self.create_input(Manage_Frame, "Date du message")
        self.Msg_office_input = self.create_input(Manage_Frame, "Bureau")
        self.Msg_objet_input = self.create_input(Manage_Frame, "Objet")
        self.Msg_receveres_input = self.create_input(Manage_Frame, "Destinataires")

    def create_input(self, parent, label_text):
        label = Label(
            parent,
            text=label_text,
            bg="#007979",
            fg="white",
            font=("Helvetica", 11, "bold"),
            padx=10,
            pady=5,
        )

        entry = Entry(
            parent,
            bd=1,
            font=("Helvetica", 11),
            width=60,
            relief=SOLID,
            justify="center",
        )

        label.pack(pady=(10, 5), fill=X)
        entry.pack(padx=10, pady=(0, 15))

        return entry


root = Tk()

Courrier_Obj = Courrier(root)

root.mainloop()


# 06202B
# FDEB9E
# 007979
# 303841
