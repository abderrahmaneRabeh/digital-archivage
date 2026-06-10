from tkinter import *
from tkinter import ttk


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
        Manage_Frame.place(x=1130, y=25, width=400, height=420)

        # inputs
        self.Msg_input = self.create_input(Manage_Frame, "Numéro du message")
        self.Msg_date_input = self.create_input(Manage_Frame, "Date du message")
        self.Msg_office_input = self.create_input(Manage_Frame, "Bureau")
        self.Msg_objet_input = self.create_input(Manage_Frame, "Objet")
        self.Msg_receveres_input = self.create_input(Manage_Frame, "Destinataires")

        # buttons

        Btn_frame = Frame(self.root, bg="#66B7B7")
        Btn_frame.place(x=1130, y=450, width=400, height=420)
        Btn_frame_title = Label(
            Btn_frame,
            text="Controle Panel",
            bg="#0F3939",
            fg="white",
            font=("monospace", 12, "bold"),
            pady=5,
        )
        Btn_frame_title.pack(fill=X)

        Add_Btn = self.create_btn(Btn_frame, "Ajouter l'archive", 20, 40, 360, 30)
        Modify_Btn = self.create_btn(Btn_frame, "Modifier l'archive", 20, 80, 360, 30)
        Delete_Btn = self.create_btn(Btn_frame, "Supprimer l'archive", 20, 120, 360, 30)
        Clear_Btn = self.create_btn(Btn_frame, "Clear l'archive", 20, 160, 360, 30)
        Exit_Btn = self.create_btn(Btn_frame, "Fermer", 20, 200, 360, 30)

        # Search

        Search_frame = Frame(self.root, bg="white")
        Search_frame.place(x=10, y=30, width=1110, height=50)

        label_search = Label(
            Search_frame, text="Rechercher", bg="white", font=("monospace", 10)
        )
        label_search.place(x=10, y=15)

        search_checkbox = ttk.Combobox(Search_frame, justify="left")
        search_checkbox["value"] = (
            "Numéro du message",
            "Bureau",
            "Destinataires",
        )
        search_checkbox.place(x=90, y=15)

        search_input = Entry(Search_frame, justify="left", border=2)
        search_input.place(x=250, y=15)

        search_btn = Button(Search_frame, text="Rechercher", bg="#207A7A", fg="white")
        search_btn.place(x=390, y=13, width=130, height=21)

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

    def create_btn(self, parent, btn_text, x, y, wdt, heigh):

        button = Button(
            parent,
            text=btn_text,
            bg="white",
            fg="#257171",
            font=("Helvetica", 10, "bold"),
        )
        button.place(x=x, y=y, width=wdt, height=heigh)

        return button


root = Tk()

Courrier_Obj = Courrier(root)

root.mainloop()


# 06202B
# FDEB9E
# 007979
# 303841
