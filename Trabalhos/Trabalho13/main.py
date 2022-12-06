import tkinter as tk
from tkinter import messagebox
import artista as art
import playlist as play
import album as album
import musica as musica

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.artistaMenu = tk.Menu(self.menubar)
        self.playMenu = tk.Menu(self.menubar)
        self.musicaMenu = tk.Menu(self.menubar)     
        self.albumMenu = tk.Menu(self.menubar)

        self.musicaMenu.add_command(label="Cadastrar", command=self.controle.cadastraMusica)
        self.musicaMenu.add_command(label="Listar", command=self.controle.listarMusicas)
        self.menubar.add_cascade(label="Músicas", menu=self.musicaMenu)  

        self.artistaMenu.add_command(label="Cadastrar", command=self.controle.cadastrarArtista)
        self.artistaMenu.add_command(label="Consultar", command=self.controle.consultarArtista)
        self.menubar.add_cascade(label="Artistas", menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", command=self.controle.cadastrarAlbum)
        self.albumMenu.add_command(label="Consultar", command=self.controle.consultarAlbum)        
        self.menubar.add_cascade(label="Álbum", menu=self.albumMenu)

        self.playMenu.add_command(label="Cadastrar", command=self.controle.cadastrarPlay)
        self.playMenu.add_command(label="Consultar", command=self.controle.consultarPlay)                     
        self.menubar.add_cascade(label="Playlist", menu=self.playMenu)        

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlMusica = musica.CtrlMusica()
        self.ctrlArtista = art.CtrlArtista(self)
        self.ctrlAlbum = album.CtrlAlbum(self)
        self.ctrlPlay = play.CtrlPlay(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trabalho 13 - Playlist MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrarMusica(self):
        self.ctrlMusica.cadastrarMusica()
    
    def consultarMusica(self):
        self.ctrlMusica.consultarMusica()
    
    def cadastrarAlbum(self):
        self.ctrlAlbum.cadastrarAlbum()
    
    def consultarAlbum(self):
        self.ctrlAlbum.consultarAlbum()

    def cadastrarArtista(self):
        self.ctrlArtista.cadastrarArtista()
    
    def consultarArtista(self):
        self.ctrlArtista.consultarArtista()
    
    def cadastrarPlay(self):
        self.ctrlPlay.cadastrarPlay()
    
    def consultarPlay(self):
        self.ctrlPlay.consultarPlay()

if __name__ == '__main__':
    c = ControlePrincipal()