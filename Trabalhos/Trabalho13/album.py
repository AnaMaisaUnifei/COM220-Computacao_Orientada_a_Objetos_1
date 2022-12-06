import tkinter as tk
import tkinter as ttk
from tkinter import messagebox

class Album:
  def __init__(self, titulo, ano, artista, faixas):
    self.__titulo = titulo
    self.__ano = ano
    self.__artista = artista
    self.__faixas = faixas

  @property
  def titulo(self):
    return self.__titulo
  
  @property
  def ano(self):
    return self.__ano
  
  @property
  def artista(self):
    return self.__artista
  
  @property
  def faixas(self):
    return self.__faixas

class LimiteCadastraAlbum(tk.Toplevel):
  def __init__(self, controle, artistas, musicas):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title("Novo Álbum")
    self.controle = controle

    self.frameTitulo = tk.Frame(self)
    self.frameAno = tk.Frame(self)
    self.frameArtista = tk.Frame(self)
    self.frameMusicas = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameTitulo.pack()
    self.frameAno.pack()
    self.frameMusicas.pack()
    self.frameButton.pack()
  
    self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
    self.labelTitulo.pack(side="left")
    self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
    self.inputTitulo.pack(side="left")

    self.labelAno = tk.Label(self.frameAno,text="Ano: ")
    self.labelAno.pack(side="left")
    self.inputAno = tk.Entry(self.frameAno, width=20)
    self.inputAno.pack(side="left")

    self.labelArtista = tk.Label(self.frameArtista,text="Artista: ")
    self.labelArtista.pack(side="left")
    self.escolhaArtista = tk.StringVar()
    self.comboboxArtista = ttk.Combobox(self.frameArtista, width = 15 ,values=artistas, textvariable = self.escolhaArtista)
    self.comboboxArtista.pack(side="left")

    self.labelMusicas = tk.Label(self.frameMusicas,text="Escolha a música: ")
    self.labelMusicas.pack(side="left") 
    self.listbox = tk.Listbox(self.frameMusicas)
    self.listbox.pack(side="left")
    for musica in musicas:
        self.listbox.insert(tk.END, musica)

    self.buttonInsere = tk.Button(self.frameButton ,text="Insere Música")           
    self.buttonInsere.pack(side="left")
    self.buttonInsere.bind("<Button>", controle.insereMusica)     
  
    self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.enterHandler)

    self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
    self.buttonFecha.pack(side="left")
    self.buttonFecha.bind("<Button>", controle.fechaHandler)

  def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum():
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
    self.__listaAlbuns= []
    self.controle = controle

  @property
  def listaAlbuns(self):
    return self.__listaAlbuns

  def cadastraAlbum(self):
    self.listaFaixas = []
    listaArtistas = self.controle.ctrlArtistas.listaNomesArtistas
    listaMusicas = self.controle.ctrlEstudante.listaTitulosMusicas
    self.limiteCad = LimiteCadastraAlbum(self, listaArtistas, listaMusicas)
  
  def consultaAlbum(self):
      self.limiteCons = LimiteConsultaAlbum(self)
  
  def insereMusica(self, event):
    musicaSel = self.limiteCad.listbox.get(tk.ACTIVE)
    musica = self.controle.ctrlMusica.musica(musicaSel)
    self.listaFaixas.append(musica)
    self.limiteCad.mostraJanela('Sucesso', 'Música adicionada')
    self.limiteCad.listbox.delete(tk.ACTIVE)

  def enterHandler(self, event):
    titulo = self.limiteCad.inputTitulo.get()
    ano = self.limiteCad.inputAno.get()
    artista = self.limiteCad.escolhaArtista
    faixas = self.listaFaixas
    album = Album(titulo, ano, artista, faixas)
    self.listaAlbuns.append(album)
    self.limiteCad.mostraJanela('Sucesso', 'Álbum cadastrado com sucesso!')
    self.clearHandler(event)

  def fechaHandler(self, event):
    self.limiteCad.destroy()
    