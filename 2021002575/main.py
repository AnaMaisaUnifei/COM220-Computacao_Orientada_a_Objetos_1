# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Prova 2 - Ordem de Serviços
# Nome: Ana Maísa do Nascimento Santos - 2021002575

import tkinter as tk
from tkinter import messagebox
import func_cliente_serv as dados
import veiculo
import ordem_de_serv as ordem

class LimitePrincipal():
  def __init__(self, root, controle):
    self.controle = controle
    self.root = root
    self.root.geometry('350x250')
    self.menubar = tk.Menu(self.root)
    self.cliMenu = tk.Menu(self.menubar)        
    self.osMenu = tk.Menu(self.menubar)        

    #Menu Cliente
    self.cliMenu.add_command(label="Cadastrar Veículo", command=self.controle.cadastraVeiculo)
    self.cliMenu.add_command(label="Mostrar Veículos", command=self.controle.mostraVeiculo)
    self.menubar.add_cascade(label="Cliente", menu=self.cliMenu)

    #Menu OS
    self.osMenu.add_command(label="Cadastrar OS", command=self.controle.cadastraOS)
    self.osMenu.add_command(label="Imprimir OS", command=self.controle.imprimeOS)
    self.menubar.add_cascade(label="Ordem de Serviço", menu=self.osMenu)
     

    self.root.config(menu=self.menubar)
    
class ControlePrincipal():       
  def __init__(self):
    self.root = tk.Tk()

    self.ctrlFuncCliServ = dados.CtrlFuncCliServ()
    self.ctrlVeiculo = veiculo.CtrlVeiculo(self)
    self.ctrlOS = ordem.CtrlOS(self)

    self.limite = LimitePrincipal(self.root, self) 

    self.root.title("Prova 2 - Ordem de Serviço")
    
    # Inicia o mainloop
    self.root.mainloop()
      
  def cadastraVeiculo(self):
    self.ctrlVeiculo.cadastraVeiculo()

  def mostraVeiculo(self):
    self.ctrlVeiculo.consultaVeiculo()

  def imprimeOS(self):
    self.ctrlOS.imprimeOS()

  def cadastraOS(self):
    self.ctrlOS.cadastraOS()


if __name__ == '__main__':
    c = ControlePrincipal()