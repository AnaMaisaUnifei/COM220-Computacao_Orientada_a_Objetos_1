# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 14 - Cupom Fiscal
# Nome: Ana Maísa do Nascimento Santos - 2021002575

import tkinter as tk
from tkinter import messagebox
import produto as prod
import cupom as cupom

class LimitePrincipal():
  def __init__(self, root, controle):
    self.controle = controle
    self.root = root
    self.root.geometry('350x250')
    self.menubar = tk.Menu(self.root)        
    self.produtoMenu = tk.Menu(self.menubar)
    self.cupomMenu = tk.Menu(self.menubar)
    self.sairMenu = tk.Menu(self.menubar) 

    #Menu Produto
    self.produtoMenu.add_command(label="Cadastrar", \
                command=self.controle.cadastraProduto)
    self.produtoMenu.add_command(label="Consultar", \
                command=self.controle.consultaProduto)
    self.menubar.add_cascade(label="Produto", \
                menu=self.produtoMenu)

    #Menu Cupom Fiscal
    self.cupomMenu.add_command(label="Criar", \
                command=self.controle.cadastraCupom)
    self.cupomMenu.add_command(label="Consultar", \
                command=self.controle.consultaCupom)        
    self.menubar.add_cascade(label="Cupom Fiscal", \
                menu=self.cupomMenu) 

    #Menu Sair - Salvar Dados
    self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
    self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)      

    self.root.config(menu=self.menubar)
    
class ControlePrincipal():       
  def __init__(self):
      self.root = tk.Tk()

      self.ctrlProduto = prod.CtrlProduto()
      self.ctrlCupom = cupom.CtrlCupom(self)

      self.limite = LimitePrincipal(self.root, self) 

      self.root.title("Trabalho 14 - Cupom Fiscal")
      # Inicia o mainloop
      self.root.mainloop()
      
  def cadastraProduto(self):
    self.ctrlProduto.cadastraProduto()

  def consultaProduto(self):
    self.ctrlProduto.consultaProduto()

  def cadastraCupom(self):
    self.ctrlCupom.cadastraCupom()

  def consultaCupom(self):
    self.ctrlCupom.consultaCupom()
  
  def salvaDados(self):
    self.ctrlProduto.salvaProdutos()
    self.ctrlCupom.salvaCupons()
    self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()