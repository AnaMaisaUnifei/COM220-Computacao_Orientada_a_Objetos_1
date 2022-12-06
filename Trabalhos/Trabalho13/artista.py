import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Artista:
  def __init__(self, nome):
    self.__nome = nome

  @property
  def nome(self):
    return self.__nome

class LimiteCadastraArtista(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title("Novo(a) Artista")
    self.controle = controle

    self.frameNome = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNome.pack()
    self.frameButton.pack()
  
    self.labelNome = tk.Label(self.frameNome,text="Nome: ")
    self.labelNome.pack(side="left")

    self.inputNome = tk.Entry(self.frameNome, width=20)
    self.inputNome.pack(side="left")           
  
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

class LimiteConsultarArtista():
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('400x250')
    self.title("Consultar Artistas")
    self.ctrl = controle

    self.frameNome = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNome.pack()
    self.frameButton.pack()

    self.labelNome = tk.Label(self.frameNome,text="Nome: ")
    self.labelNome.pack(side="left")  

    self.inputNome = tk.Entry(self.frameNome, width=20)
    self.inputNome.pack(side="left")            
  
    self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.exibirAlbuns) 

    self.frameAlbuns = tk.Frame(self)
    self.frameAlbuns.pack()
    self.textAlbuns = tk.Text(self.frameAlbuns, height=20,width=40)
    self.textAlbuns.pack()
    self.textAlbuns.config(state=tk.DISABLED)

class CtrlArtista():       
  def __init__(self, controle):
    self.__listaArtistas= [Artista('Burna Boy'), Artista('James Blunt'), Artista('Sia')]
    self.controle = controle

  @property
  def listaArtistas(self):
    return self.__listaArtistas

  def cadastraArtista(self):
      self.limiteCad = LimiteCadastraArtista(self)
  
  def consultaArtista(self):
      self.limiteCons = LimiteConsultarArtista(self)

  @property
  def listaNomesArtistas(self):
    listaNomes = []
    for artista in self.listaArtistas:
      listaNomes.append(artista.nome)
    return listaNomes
  
  def exibeAlbuns(self):
    artista = self.limiteCons.inputNome.get()
    self.limiteCons.textAlbuns.config(state='normal')
    self.limiteCons.textAlbuns.delete("1.0", tk.END)
    for album in self.controle.ctrlAlbum.listaAlbuns:
        if(album.artista.nome == artista):
            albuns = album.infos + '/n/n'
            self.limiteCons.textAlbuns.insert(1.0, albuns)
    self.limiteCons.textAlbuns.config(state = 'disable')

  def enterHandler(self, event):
    nome = self.limiteCad.inputNome.get()
    artista = Artista(nome)
    self.listaArtistas.append(artista)
    self.limiteCad.mostraJanela('Sucesso', 'Artista cadastrado(a) com sucesso!')
    self.clearHandler(event)

  def clearHandler(self, event):
    self.limiteCad.inputNome.delete(0, len(self.limiteCad.inputNome.get()))

  def fechaHandler(self, event):
    self.limiteCad.destroy()
    