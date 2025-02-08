from tkinter import *
import customtkinter as ctk

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To Do List")
        self.master.config(bg="#ffffff")
        self.task_counters = {
            "Lunes": 1,
            "Martes": 1,
            "Miercoles": 1,
            "Jueves": 1,
            "Viernes": 1,
            "Sabado": 1,
            "Domingo": 1
        }
        self.task_buttons = {}  
        self.marco()
        self.question()
    
    def marco(self):
        True
        self.lunes = ctk.CTkLabel(master=self.master, text="Lunes", text_color="#000000", font=("Arial", 16))
        self.lunes.grid(row=0, column=0, padx=15)
        self.martes = ctk.CTkLabel(master=self.master, text="Martes", text_color="#000000", font=("Arial", 16))
        self.martes.grid(row=0, column=1, padx=15)
        self.miercoles = ctk.CTkLabel(master=self.master, text="Miercoles", text_color="#000000", font=("Arial", 16))
        self.miercoles.grid(row=0, column=2, padx=15)
        self.jueves = ctk.CTkLabel(master=self.master, text="Jueves", text_color="#000000", font=("Arial", 16))
        self.jueves.grid(row=0, column=3, padx=15)
        self.viernes = ctk.CTkLabel(master=self.master, text="Viernes", text_color="#000000", font=("Arial", 16))
        self.viernes.grid(row=0, column=4, padx=15)
        self.sabado = ctk.CTkLabel(master=self.master, text="Sabado", text_color="#000000", font=("Arial", 16))
        self.sabado.grid(row=0, column=5, padx=15)
        self.domingo = ctk.CTkLabel(master=self.master, text="Domingo", text_color="#000000", font=("Arial", 16))
        self.domingo.grid(row=0, column=6, padx=15)
        
    def question(self):
        self.name = ctk.CTkEntry(master=self.master, placeholder_text="Ingresa el nombre de tu tarea", placeholder_text_color="#ffffff", fg_color="#797d7f", width=180)
        self.name.grid(row=1, column=7, pady=15)
        
        self.textday = ctk.CTkLabel(master=self.master, text="¿Que dia es tu tarea?", text_color="#000000")
        self.textday.grid(row=2, column=7)
        
        self.day = ctk.CTkComboBox(master=self.master, values=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"], fg_color="#797d7f")
        self.day.grid(row=3, column=7, pady=10)
        
        self.textpriority = ctk.CTkLabel(master=self.master, text="Elige la prioridad de tu tarea", text_color="#000000")
        self.textpriority.grid(row=4, column=7)
        
        self.pri = ctk.CTkComboBox(master=self.master, values=["Alta", "Media", "Baja"], fg_color="#797d7f")
        self.pri.grid(row=5, column=7, pady=10)
        
        self.quest = ctk.CTkButton(master=self.master, text="Agregar Tarea", command=self.add, fg_color="#797d7f")
        self.quest.grid(row=6, column=7, pady=20)
    
    def add(self):
        task_name = self.name.get()
        task_day = self.day.get()
        task_pri = self.pri.get()
        
        if task_pri == "Alta":
            color = "#c0392b"
            hcolor = "#922b21"
        elif task_pri == "Media":
            color = "#f1c40f"
            hcolor = "#b7950b"
        else:
            color = "#2e86c1"
            hcolor = "#21618c"
        
        if task_day in self.task_counters:
            row = self.task_counters[task_day]
            column = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"].index(task_day)
            task_button = ctk.CTkButton(master=self.master, text=task_name, text_color="#000000", command=lambda: self.verify(task_name), hover_color=hcolor, fg_color=color, width=120, height=30)
            task_button.grid(row=row, column=column, padx=15, pady=5)
            self.task_buttons[task_name] = task_button  
            self.task_counters[task_day] += 1
    
    def verify(self, task_name):
        self.emer = Toplevel(self.master)
        self.emer.title("Verify")
        task_pri = self.pri.get()
        
        self.text = ctk.CTkLabel(self.emer, text=f"Nombre de la tarea: {task_name}\n \n Prioridad de la tarea: {task_pri}", font=("Arial", 16), text_color="#000000")
        self.text.grid(padx=15, pady=15, row=1, column=1)
        
        def complete():
            self.task_buttons[task_name].configure(fg_color="#27ae60", hover_color="#1d8348")
            self.emer.destroy()
            
        def delete():
            self.task_buttons[task_name].destroy()
            del self.task_buttons[task_name]
            self.emer.destroy()
        
        self.complete_button = ctk.CTkButton(master=self.emer, text="Tarea completada", command=complete, fg_color="#797d7f")
        self.complete_button.grid(row=2, column=1, padx=15, pady=15)
        
        self.delete_button = ctk.CTkButton(master=self.emer, text="Eliminar Tarea", command=delete, fg_color="#797d7f")
        self.delete_button.grid(row=3, column=1, padx=15, pady=15)
        
yo = ToDoList(Tk())
yo.master.mainloop()