# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Prova 2 - Ordem de Serviços
# Nome: Ana Maísa do Nascimento Santos - 2021002575

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Veiculo:

    def __init__(self, placa, marca, modelo):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo

    @property
    def placa(self):
        return self.__placa

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo
    
    def infosVeiculo(self):
        str = "Placa: {} | Marca: {} | Modelo: {}\n".format(self.placa, self.marca, self.modelo)
        
        return str

class LimiteCadastraVeiculo(tk.Toplevel):
    def __init__(self, controle, clientes):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Novo Veículo")
        self.controle = controle

        self.frameClientes = tk.Frame(self)
        self.framePlaca = tk.Frame(self)
        self.frameMarca = tk.Frame(self)
        self.frameModelo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameClientes.pack()
        self.framePlaca.pack()
        self.frameMarca.pack()
        self.frameModelo.pack()
        self.frameButton.pack()

        # Clientes
        self.labelClientes = tk.Label(self.frameClientes,text="Cliente: ")
        self.labelClientes.pack(side="left")
        self.escolhaCliente = tk.StringVar()
        self.comboboxClientes = ttk.Combobox(self.frameClientes, width = 25 ,values=clientes, textvariable = self.escolhaCliente)
        self.comboboxClientes.pack(side="left")

        # Placa
        self.labelPlaca = tk.Label(self.framePlaca,text="Placa: ")
        self.labelPlaca.pack(side="left")
        self.inputPlaca = tk.Entry(self.framePlaca, width=20)
        self.inputPlaca.pack(side="left")

        # Marca
        self.labelMarca = tk.Label(self.frameMarca,text="Marca: ")
        self.labelMarca.pack(side="left")
        self.inputMarca = tk.Entry(self.frameMarca, width=20)
        self.inputMarca.pack(side="left")

        # Modelo
        self.labelModelo = tk.Label(self.frameModelo,text="Modelo: ")
        self.labelModelo.pack(side="left")
        self.inputModelo = tk.Entry(self.frameModelo, width=20)
        self.inputModelo.pack(side="left") 

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar veículo")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaVeiculo(tk.Toplevel):
    def __init__(self, controle, clientes):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Consultar Veículos")
        self.controle = controle

        self.frameClientes = tk.Frame(self)
        self.frameVeiculos = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameClientes.pack()
        self.frameVeiculos.pack()
        self.frameButton.pack()

        # Clientes
        self.labelClientes = tk.Label(self.frameClientes,text="Cliente: ")
        self.labelClientes.pack(side="left")
        self.escolhaCliente = tk.StringVar()
        self.comboboxClientes = ttk.Combobox(self.frameClientes, width = 25 ,values=clientes, textvariable = self.escolhaCliente)
        self.comboboxClientes.pack(side="left")
        self.comboboxClientes.bind("<<ComboboxSelected>>", self.controle.mostraVeiculo)
    
        self.textVeiculos = tk.Text(self.frameVeiculos, height=20,width=40)
        self.textVeiculos.pack()
        self.textVeiculos.config(state=tk.DISABLED)



class CtrlVeiculo():       
    def __init__(self, controlePrincipal):
        self.ctrlPrin = controlePrincipal

    def cadastraVeiculo(self):
        self.limiteCad = LimiteCadastraVeiculo(self, self.ctrlPrin.ctrlFuncCliServ.listaNomesClientes())

    def consultaVeiculo(self):
        self.limiteCons = LimiteConsultaVeiculo(self, self.ctrlPrin.ctrlFuncCliServ.listaNomesClientes())

    def enterHandler(self, event):
        cliente = self.ctrlPrin.ctrlFuncCliServ.getCliente(self.limiteCad.comboboxClientes.get())
        placa = self.limiteCad.inputPlaca.get()
        marca = self.limiteCad.inputMarca.get()
        modelo = self.limiteCad.inputModelo.get()
        veiculo = Veiculo(placa, marca, modelo)

        cliente.addVeiculo(veiculo)

        self.limiteCad.mostraJanela("Sucesso!", "Veículo cadastrado com sucesso!")

        self.clearHandler(event)
  
    def clearHandler(self, event):
        self.limiteCad.comboboxClientes.config(state='normal')
        self.limiteCad.comboboxClientes.set("---")
        self.limiteCad.inputPlaca.delete(0, len(self.limiteCad.inputPlaca.get()))
        self.limiteCad.inputMarca.delete(0, len(self.limiteCad.inputMarca.get()))
        self.limiteCad.inputModelo.delete(0, len(self.limiteCad.inputModelo.get()))

    def fechaHandler(self, event):
        self.limiteCad.destroy()

    def mostraVeiculo(self, event):
        cliente = self.ctrlPrin.ctrlFuncCliServ.getCliente(self.limiteCons.comboboxClientes.get())
        self.limiteCons.comboboxClientes.set("---")
        semVeiculos = 0
        
        self.limiteCons.textVeiculos.config(state='normal')
        self.limiteCons.textVeiculos.delete("1.0", tk.END)
        
        for veiculo in cliente.veiculos:
            self.limiteCons.textVeiculos.insert(1.0, veiculo.infosVeiculo())
            semVeiculos = 1
        
        if semVeiculos == 0:
            self.limiteCons.textVeiculos.insert(1.0, "{} não tem veículos cadastrados!".format(cliente.nome))

        self.limiteCons.textVeiculos.config(state = 'disable')
    
    def listaPlacas(self, cliente):
        listaPlacas = []

        for veiculo in cliente.veiculos:
            listaPlacas.append(veiculo.placa)
        
        return listaPlacas

    def getVeiculo(self, cliente, placa):
        veiRet = None
        for veiculo in cliente.veiculos:
            if veiculo.placa == placa:
                veiRet = veiculo
        return veiRet       