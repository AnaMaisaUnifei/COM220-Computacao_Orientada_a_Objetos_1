# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 14 - Cupom Fiscal
# Nome: Ana Maísa do Nascimento Santos - 2021002575

import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Produto:
  def __init__(self, codigo, desc, valorUni):
    self.codigo = codigo
    self.desc = desc
    self.valorUni = valorUni

  @property
  def codigo(self):
    return self.__codigo
  
  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo
  
  @property
  def desc(self):
    return self.__desc
  
  @desc.setter
  def desc(self, desc):
    self.__desc = desc
  
  @property
  def valorUni(self):
    return self.__valorUni
  
  @valorUni.setter
  def valorUni(self, valorUni):
    self.__valorUni = valorUni

class LimiteCadastraProduto(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title("Novo Produto")
    self.controle = controle

    self.frameCodigo = tk.Frame(self)
    self.frameDesc = tk.Frame(self)
    self.frameValor = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameDesc.pack()
    self.frameValor.pack()
    self.frameButton.pack()
  
    self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
    self.labelDesc = tk.Label(self.frameDesc,text="Descrição: ")
    self.labelValor = tk.Label(self.frameValor,text="Valor Unitário: ")
    self.labelCodigo.pack(side="left")
    self.labelDesc.pack(side="left")  
    self.labelValor.pack(side="left")  

    self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
    self.inputCodigo.pack(side="left")
    self.inputDesc = tk.Entry(self.frameDesc, width=20)
    self.inputDesc.pack(side="left")
    self.inputValor = tk.Entry(self.frameValor, width=20)
    self.inputValor.pack(side="left")          
  
    self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.enterHandler)
  
    self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controle.clearHandler)  

    self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
    self.buttonFecha.pack(side="left")
    self.buttonFecha.bind("<Button>", controle.fechaHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimiteConsultaProduto(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('200x200')
    self.title("Consultar Produtos")
    self.ctrl = controle

    self.frameCodigo = tk.Frame(self)
    self.frameProdutos = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameProdutos.pack()
    self.frameButton.pack()

    self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
    self.labelCodigo.pack(side="left")

    self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
    self.inputCodigo.pack(side="left")

    self.textProduto = tk.Text(self.frameProdutos, height=8,width=20)
    self.textProduto.pack()
    self.textProduto.config(state=tk.DISABLED)
  
    self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.buscaProduto)

    
class CtrlProduto():       
  def __init__(self):
    if not os.path.isfile("produto.pickle"):
      self.listaProdutos =  []
    else:
      with open("produto.pickle", "rb") as f:
        self.listaProdutos = pickle.load(f)
  
  def salvaProdutos(self):
    if len(self.listaProdutos) != 0:
      with open("produto.pickle","wb") as f:
          pickle.dump(self.listaProdutos, f)

  def cadastraProduto(self):
    self.limiteCad = LimiteCadastraProduto(self)
  
  def consultaProduto(self):
    self.limiteCons = LimiteConsultaProduto(self)

  def enterHandler(self, event):
    codigo = self.limiteCad.inputCodigo.get()
    desc = self.limiteCad.inputDesc.get()
    valor = self.limiteCad.inputValor.get()
    produto = Produto(codigo, desc, valor)
    self.listaProdutos.append(produto)
    self.limiteCad.mostraJanela('Sucesso!', 'Produto cadastrado com sucesso')
    self.clearHandler(event)
  
  def clearHandler(self, event):
    self.limiteCad.inputCodigo.delete(0, len(self.limiteCad.inputCodigo.get()))
    self.limiteCad.inputDesc.delete(0, len(self.limiteCad.inputDesc.get()))
    self.limiteCad.inputValor.delete(0, len(self.limiteCad.inputValor.get()))

  def fechaHandler(self, event):
    self.limiteCad.destroy()
  
  def buscaProduto(self, event):
    codigo = self.limiteCons.inputCodigo.get()
    self.limiteCons.textProduto.config(state='normal')
    self.limiteCons.textProduto.delete("1.0", tk.END)
    prodRet = None
    for prod in self.listaProdutos:
      if prod.codigo == codigo:
          prodRet = prod
    
    if prodRet == None:
      self.limiteCons.inputCodigo.delete(0, len(self.limiteCons.inputCodigo.get()))
      self.limiteCons.textProduto.insert(1.0, 'Produto não encontrado!')
    else:
      self.limiteCons.inputCodigo.delete(0, len(self.limiteCons.inputCodigo.get()))
      self.limiteCons.textProduto.insert(1.0, 'Código: {}\nDescrição: {}\nValor Uniátio: R${}'.format(prodRet.codigo, prodRet.desc, prodRet.valorUni))
    self.limiteCons.textProduto.config(state = 'disable')

  def getListaCodigosProdutos(self):
    codsProdutos = []
    for prod in self.listaProdutos:
      codsProdutos.append(prod.codigo)
    return codsProdutos
  
  def getProduto(self, codigo):
    prodRet = None
    for prod in self.listaProdutos:
      if prod.codigo == codigo:
          prodRet = prod
    return prodRet