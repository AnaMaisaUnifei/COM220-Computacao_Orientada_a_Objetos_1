import tkinter as tk
from tkinter import messagebox

class Musica:
  def __init__(self, titulo, nroFaixa):
    self.__titulo = titulo
    self.__nroFaixa = nroFaixa

  @property
  def titulo(self):
    return self.__titulo
  
  @property
  def nroFaixa(self):
    return self.__nroFaixa

class LimiteCadastraMusicas(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title("Nova Música")
    self.controle = controle

    self.frameNroFaixa = tk.Frame(self)
    self.frameTitulo = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNroFaixa.pack()
    self.frameTitulo.pack()
    self.frameButton.pack()
  
    self.labelNroFaixa = tk.Label(self.frameNroFaixa,text="Nro. Faixa: ")
    self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
    self.labelNroFaixa.pack(side="left")
    self.labelTitulo.pack(side="left")  

    self.inputNroFaixa = tk.Entry(self.frameNroFaixa, width=20)
    self.inputNroFaixa.pack(side="left")
    self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
    self.inputTitulo.pack(side="left")             
  
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

class LimiteListarMusicas():
    def __init__(self, str):
      messagebox.showinfo('Lista de Músicas', str)

class CtrlMusica():       
  def __init__(self):
    self.__listaMusicas = []

  @property
  def listaMusicas(self):
    return self.__listaMusicas
  
  @property
  def listaTitulosMusicas(self):
    listaTitulos = []
    for musica in self.listaMusicas:
      listaTitulos.append(musica.titulo)
    return listaTitulos
  
  @property
  def musica(self, titulo):
    musicaRet = None
    for musica in self.listaMusicas:
      if musica.titulo == titulo:
          musicaRet = musica
    return musicaRet

  def cadastraMusica(self):
      self.limiteCad = LimiteCadastraMusicas(self) 

  def ListarMusicas(self):
    str = 'Nro. Faixa -- Titulo\n'
    for musica in self.listaMusicas:
        str += musica.nroFaixa + ' -- ' + musica.titulo + '\n'
    self.limiteLista = LimiteListarMusicas(str)

  def enterHandler(self, event):
    nroFaixa = self.limiteCad.inputNroFaixa.get()
    titulo = self.limiteCad.inputTitulo.get()
    musica = Musica(nroFaixa, titulo)
    self.listaMusicas.append(musica)
    self.limiteCad.mostraJanela('Sucesso', 'Música cadastrada com sucesso!')
    self.clearHandler(event)

  def clearHandler(self, event):
    self.limiteCad.inputNroFaixa.delete(0, len(self.limiteCad.inputNroFaixa.get()))
    self.limiteCad.inputTitulo.delete(0, len(self.limiteCad.inputTitulo.get()))

  def fechaHandler(self, event):
    self.limiteCad.destroy()
    