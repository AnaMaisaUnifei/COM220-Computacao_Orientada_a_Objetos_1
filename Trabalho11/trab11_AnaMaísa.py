# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 11 - Consulta MVC
# Nome: Ana Maísa do Nascimento Santos - 2021002575

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email
    
    @property
    def codigo(self):
        return self.__codigo

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Código: ")
        self.labelInfo1.pack(side="left")
        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")

        self.labelInfo2 = tk.Label(self.frame2,text="Nome: ")
        self.labelInfo2.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")

        self.labelInfo3 = tk.Label(self.frame3,text="Email: ")
        self.labelInfo3.pack(side="left")
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.janela,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)

        self.buttonClientes = tk.Button(self.janela,text="Listar")      
        self.buttonClientes.pack(side="left")
        self.buttonClientes.bind("<Button>", controller.clientesHandler)

        self.buttonConsultaCodigo = tk.Button(self.janela,text="Consultar por Código")      
        self.buttonConsultaCodigo.pack(side="left")
        self.buttonConsultaCodigo.bind("<Button>", controller.consultaCodigo)   

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
    
    def consultaCodigo(self, titulo, label):
        return simpledialog.askstring(titulo, label, parent=self.master)
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x100')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Trabalho 11 - Consulta MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def enterHandler(self, event):
        codigoCli = self.view.inputText1.get()
        nomeCli = self.view.inputText2.get()
        emailCli = self.view.inputText3.get()
        cliente = ModelCliente(nomeCli, emailCli, codigoCli)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))
    
    def clientesHandler(self, event):
        self.msg = "Clientes cadastrados: \n"
        for cliente in self.listaClientes:
            self.msg += "Nome: " + cliente.nome + " | E-mail: " + cliente.email + " | Código: " + cliente.codigo + "\n"
        self.view.mostraJanela('Clientes cadastrados', self.msg)
    
    def consultaCodigo(self, event):
        codigo = self.view.consultaCodigo("Busca por código", "Qual código deseja buscar?")
        encontrado = 0

        if codigo is not None:
            for cliente in self.listaClientes:
                if (cliente.codigo == codigo):
                    self.msg = "Cliente encontrado\nNome: " + cliente.nome + " | E-mail: " + cliente.email + "\n"
                    encontrado = 1
                
            if (encontrado == 1):
                self.view.mostraJanela('Busca por código', self.msg) 
            else:
                self.view.mostraJanela('Busca por código', "Código não cadastrado")
        else:
            self.msg = "Nenhuma entrada digitada"

if __name__ == '__main__':
    c = Controller()