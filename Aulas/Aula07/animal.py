class Animal:

    #construtor
    def __init__(self,nome):
        self.__nome = nome

    #getter
    def getNome(self):
        return self.__nome

    #metodo
    def fazerCarinho(self):
        print("{} está recebendo carinho".format(self.__nome))

class Gato(Animal):

    #construtor
    def __init__(self, nome, vidas):
        #super é usado para permitir acessar métodos 
        #e propriedades da superclasse
        super().__init__(nome)
        self.__vidas = vidas

    #método
    def miar(self):
        print("Meow Meow")
    
    def getVidas(self):
        print("Este gato tem {}".format(self.__vidas))

class Cao(Animal):

    #construtor
    def __init__(self, nome):
        #super é usado para permitir acessar métodos 
        #e propriedades da superclasse
        super().__init__(nome)

    #método
    def latir(self):
        print("Au Au")     

if __name__ == "__main__":
    gato = Gato("Perola", 7)
    print(gato.getNome())
    gato.miar()
    gato.getVidas()
    gato.fazerCarinho()
    cao = Cao("Cleitin")
    print(cao.getNome())    
    cao.latir()    
    cao.fazerCarinho()