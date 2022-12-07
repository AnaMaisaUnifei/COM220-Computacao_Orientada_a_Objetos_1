# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 14 - Cupom Fiscal
# Nome: Ana Maísa do Nascimento Santos - 2021002575

import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class CupomFiscal:
  def __init__(self, nroCupom, itensCupom):
    self.nroCupom = nroCupom
    self.__itensCupom = itensCupom

  @property
  def nroCupom(self):
    return self.__nroCupom
  
  @nroCupom.setter
  def nroCupom(self, nroCupom):
    self.__nroCupom = nroCupom
  
  @property
  def itensCupom(self):
    return self.__itensCupom

class LimiteCadastraCupomFiscal(tk.Toplevel):
  def __init__(self, controle, listaCodsProds):
    tk.Toplevel.__init__(self)
    self.geometry('250x250')
    self.title("Novo Cupom Fiscal")
    self.controle = controle

    self.frameNroCupom = tk.Frame(self)
    self.frameItensCupom = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNroCupom.pack()
    self.frameItensCupom.pack()
    self.frameButton.pack()
  
    self.labelNroCupom = tk.Label(self.frameNroCupom,text="Nro. Cupom: ")
    self.labelNroCupom.pack(side="left")
    self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
    self.inputNroCupom.pack(side="left")

    self.labelItens = tk.Label(self.frameItensCupom,text="Escolha o produto: ")
    self.labelItens.pack(side="left") 
    self.listbox = tk.Listbox(self.frameItensCupom)
    self.listbox.pack(side="left")
    for cod in listaCodsProds:
      self.listbox.insert(tk.END, cod)       
  
    self.buttonInsere = tk.Button(self.frameButton ,text="Insere Produto")           
    self.buttonInsere.pack(side="left")
    self.buttonInsere.bind("<Button>", controle.insereProduto)

    self.buttonCria = tk.Button(self.frameButton ,text="Fechar Cupom")           
    self.buttonCria.pack(side="left")
    self.buttonCria.bind("<Button>", controle.criaCupom) 

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimiteConsultaCupomFiscal(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('400x400')
    self.title("Consultar Cupom Fiscal")
    self.ctrl = controle

    self.frameNroCupom = tk.Frame(self)
    self.frameItens = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNroCupom.pack()
    self.frameItens.pack()
    self.frameButton.pack()

    self.labelNroCupom = tk.Label(self.frameNroCupom,text="Nro. Cupom: ")
    self.labelNroCupom.pack(side="left")
    self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
    self.inputNroCupom.pack(side="left")

    self.textItens = tk.Text(self.frameItens, height=20,width=40)
    self.textItens.pack()
    self.textItens.config(state=tk.DISABLED)
  
    self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.consultaItens)
    
class CtrlCupom():       
  def __init__(self, controlePrincipal):
    self.listaProdutosCupom = []
    self.ctrlPrincipal = controlePrincipal

    if not os.path.isfile("cupom.pickle"):
      self.listaCupons =  []
    else:
      with open("cupom.pickle", "rb") as f:
        self.listaCupons= pickle.load(f)
  
  def salvaCupons(self):
    if len(self.listaCupons) != 0:
      with open("cupom.pickle","wb") as f:
        pickle.dump(self.listaCupons, f)

  def cadastraCupom(self):
    self.listaProdutosCupom = []
    self.listaCodsProds = self.ctrlPrincipal.ctrlProduto.getListaCodigosProdutos()
    self.limiteCad = LimiteCadastraCupomFiscal(self, self.listaCodsProds)
  
  def consultaCupom(self):
    self.limiteCons = LimiteConsultaCupomFiscal(self)
  
  def insereProduto(self, event):
    prodSel = self.limiteCad.listbox.get(tk.ACTIVE)
    produto = self.ctrlPrincipal.ctrlProduto.getProduto(prodSel)
    self.listaProdutosCupom.append(produto)
    self.limiteCad.mostraJanela('Sucesso!', 'Produto Inserido no Cupom Fiscal')
  
  def criaCupom(self, event):
    nroCupom = self.limiteCad.inputNroCupom.get()
    cupom = CupomFiscal(nroCupom, self.listaProdutosCupom)
    self.listaCupons.append(cupom)
    self.limiteCad.mostraJanela('Sucesso!', 'Cupom criado com Sucesso')
    self.limiteCad.destroy()
  
  def consultaItens(self, event):
    nroCupom = self.limiteCons.inputNroCupom.get()
    self.limiteCons.textItens.config(state='normal')
    self.limiteCons.textItens.delete("1.0", tk.END)
    itens = ''
    impressos = []
    qtd = 0
    total = 0

    for cupom in self.listaCupons:
      if cupom.nroCupom == nroCupom:
        itens += 'Nro. Cupom: ' + nroCupom + '\nItens:\n'
        itens += 'Qtd.-- Cód.---- Desc ---- Valor \n'
        for item in cupom.itensCupom:
          if not item.codigo in impressos:
            for outro in cupom.itensCupom:
              if item.codigo == outro.codigo:
                qtd += 1
            itens += str(qtd) + ' | ' + item.codigo + ' | ' + item.desc + ' | R$' + str(qtd*float(item.valorUni)) + '\n'
            impressos.append(item.codigo)
            qtd = 0
          total += float(item.valorUni)
        itens += 'Total do Cupom Fiscal: R$' + str(total)
    
    if itens == '':
      self.limiteCons.textItens.insert(1.0, 'Cupom não encontrado!')
      self.limiteCons.inputNroCupom.delete(0, len(self.limiteCons.inputNroCupom.get()))
      self.limiteCons.textItens.config(state = 'disable')
    else:
      self.limiteCons.textItens.insert(1.0, itens)
      self.limiteCons.inputNroCupom.delete(0, len(self.limiteCons.inputNroCupom.get()))
      self.limiteCons.textItens.config(state = 'disable')
        