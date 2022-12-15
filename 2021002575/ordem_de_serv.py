# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Prova 2 - Ordem de Serviços
# Nome: Ana Maísa do Nascimento Santos - 2021002575

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class OrdemServico:

    def __init__(self, cliente, veiculo, funcionario, nroOS, dataOS):
        self.__cliente = cliente
        self.__veiculo = veiculo
        self.__funcionario = funcionario
        self.__nroOS = nroOS
        self.__dataOS = dataOS

        self.__servicos = []

    @property
    def cliente(self):
        return self.__cliente

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def nroOS(self):
        return self.__nroOS

    @property
    def dataOS(self):
        return self.__dataOS

    @property
    def servicos(self):
        return self.__servicos

    def addServico(self, servico):
        self.__servicos.append(servico)

    def calculaValorOS(self):
        valor = 0
        for serv in self.__servicos:            
            valor += serv.valor
        if self.__cliente.tipoCliente == 'Vip':
            valor *= 0.9
        return valor
            
    def imprimeOS(self):
        servs = "\nCod. Serviço    Descrição"
        for serv in self.__servicos:
           servs += "\n" + str(serv.codigo) + "     " + str(serv.descricao)
        return "Número OS: " + str(self.__nroOS)\
        + "\nData: " + str(self.__dataOS)\
        + "\nPlaca do veículo: " + str(self.__veiculo.placa)\
        + "\nNome proprietário: " + str(self.__cliente.nome)\
        + "\nFunc responsável: " + str(self.__funcionario.nome)\
        + "\n---------------------------------"\
        + servs + "\n---------------------------------"\
        +"\nValor OS: R$" + str(self.calculaValorOS())\
        + "\n---------------------------------"
    
class LimiteCadastraOS(tk.Toplevel):
    def __init__(self, controle, clientes, funcs, servicos):
        tk.Toplevel.__init__(self)
        self.geometry('400x400')
        self.title("Nova Ordem de Serviço")
        self.controle = controle

        self.frameNroOS = tk.Frame(self)
        self.frameFunc = tk.Frame(self)
        self.frameClientes = tk.Frame(self)
        self.frameVeiculos = tk.Frame(self)
        self.frameServicos = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroOS.pack()
        self.frameFunc.pack()
        self.frameClientes.pack()
        self.frameVeiculos.pack()
        self.frameServicos.pack()
        self.frameButton.pack()

        self.labelNroOS = tk.Label(self.frameNroOS,text="Nro. OS: ")
        self.labelNroOS.pack(side="left")
        self.inputNroOS = tk.Entry(self.frameNroOS, width=20)
        self.inputNroOS.pack(side="left")

        self.labelFunc = tk.Label(self.frameFunc,text="Funcionário: ")
        self.labelFunc.pack(side="left")
        self.escolhaFunc = tk.StringVar()
        self.comboboxFunc = ttk.Combobox(self.frameFunc, width = 25 ,values=funcs, textvariable = self.escolhaFunc)
        self.comboboxFunc.pack(side="left")
    
        self.labelClientes = tk.Label(self.frameClientes,text="Cliente: ")
        self.labelClientes.pack(side="left")
        self.escolhaCliente = tk.StringVar()
        self.comboboxClientes = ttk.Combobox(self.frameClientes, width = 25 ,values=clientes, textvariable = self.escolhaCliente)
        self.comboboxClientes.pack(side="left")
        self.comboboxClientes.bind("<<ComboboxSelected>>", self.controle.inserePlacas)
    
        self.labelVeiculos = tk.Label(self.frameVeiculos,text="Veículo: ")
        self.labelVeiculos.pack(side="left")
        self.escolhaVeiculo = tk.StringVar()
        self.comboboxVeiculos = ttk.Combobox(self.frameVeiculos, width = 25 ,values=["---"], textvariable = self.escolhaVeiculo)
        self.comboboxVeiculos.pack(side="left")

        self.labelServicos = tk.Label(self.frameServicos,text="Escolha os serviços: ")
        self.labelServicos.pack(side="left") 
        self.listbox = tk.Listbox(self.frameServicos)
        self.listbox.pack(side="left")
        for cod in servicos:
            self.listbox.insert(tk.END, cod)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Adicionar Serviço")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.addServ)  

        self.buttonSubmit = tk.Button(self.frameButton ,text="Fecha OS")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteImprimeOS(tk.Toplevel):
    def __init__(self, controle, os):
        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Imprime OS")
        self.controle = controle

        self.frameOS = tk.Frame(self)
        self.frameDados = tk.Frame(self)
        self.frameOS.pack()
        self.frameDados.pack()

        self.labelOS = tk.Label(self.frameOS,text="OS: ")
        self.labelOS.pack(side="left")
        self.escolhaOS = tk.StringVar()
        self.comboboxOS = ttk.Combobox(self.frameOS, width = 25 ,values=os, textvariable = self.escolhaOS)
        self.comboboxOS.pack(side="left")
        self.comboboxOS.bind("<<ComboboxSelected>>", self.controle.mostraOS)
    
        self.textOS = tk.Text(self.frameDados, height=20,width=40)
        self.textOS.pack()
        self.textOS.config(state=tk.DISABLED)

class CtrlOS():       
    def __init__(self, controlePrincipal):
        self.ctrlPrin = controlePrincipal
        self.listaOS = []
        self.listaServicos = []
  

    def cadastraOS(self):
        self.listaServicos = []
        clientes = self.ctrlPrin.ctrlFuncCliServ.listaNomesClientes()
        funcs = self.ctrlPrin.ctrlFuncCliServ.listaNomesFuncs()
        servicos = self.ctrlPrin.ctrlFuncCliServ.listaCodServ()
        self.limiteCad = LimiteCadastraOS(self, clientes, funcs, servicos)

    def imprimeOS(self):
        self.limiteImpr = LimiteImprimeOS(self, self.listaNros())

    def inserePlacas(self, event):
        cliente = self.ctrlPrin.ctrlFuncCliServ.getCliente(self.limiteCad.comboboxClientes.get())
        listaPlacas = self.ctrlPrin.ctrlVeiculo.listaPlacas(cliente)
        self.limiteCad.comboboxVeiculos.config(values=listaPlacas)
    
    def addServ(self, event):
        servSel = self.limiteCad.listbox.get(tk.ACTIVE)
        servico = self.ctrlPrin.ctrlFuncCliServ.getServico(servSel)
        self.listaServicos.append(servico)
        self.limiteCad.mostraJanela('Sucesso!', 'Serviço Inserido na OS')

    def enterHandler(self, event):
        nroOS = self.limiteCad.inputNroOS.get()
        func = self.ctrlPrin.ctrlFuncCliServ.getFunc(self.limiteCad.comboboxFunc.get())
        cliente = self.ctrlPrin.ctrlFuncCliServ.getCliente(self.limiteCad.comboboxClientes.get())
        veiculo = self.ctrlPrin.ctrlVeiculo.getVeiculo(cliente, self.limiteCad.comboboxVeiculos.get())

        os = OrdemServico(cliente, veiculo, func, nroOS, datetime.now())

        for serv in self.listaServicos:
            os.addServico(serv)

        self.listaOS.append(os)

        self.limiteCad.mostraJanela("Sucesso!", "OS cadastrada com sucesso!")

        self.listaServicos = []
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteCad.comboboxClientes.config(state='normal')
        self.limiteCad.comboboxClientes.set("---")
        self.limiteCad.comboboxFunc.config(state='normal')
        self.limiteCad.comboboxFunc.set("---")
        self.limiteCad.comboboxVeiculos.config(state='normal')
        self.limiteCad.comboboxVeiculos.set("---")
        self.listaServicos = []
        self.limiteCad.inputNroOS.delete(0, len(self.limiteCad.inputNroOS.get()))

    def mostraOS(self, event):
        os = self.getOS(self.limiteImpr.comboboxOS.get())
        self.limiteImpr.comboboxOS.set("---")
        
        self.limiteImpr.textOS.config(state='normal')
        self.limiteImpr.textOS.delete("1.0", tk.END)

        self.limiteImpr.textOS.insert(1.0, os.imprimeOS())
    
    def listaNros(self):
        listaNros = []

        for os in self.listaOS:
            listaNros.append(os.nroOS)
        
        return listaNros

    def getOS(self, nro):
        osRet = None
        for os in self.listaOS:
            if os.nroOS == nro:
                osRet = os
        return osRet 