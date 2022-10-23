from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisc):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade 
        self.__listaDisc = listaDisc       

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade
    
    def getListaDisc(self):
        return self.__listaDisc
    
    def insereDisc(self, disc):
        self.__listaDisc.append(disc)

    @abstractmethod
    def printDescricao(self): #contrato para que as classes filhas tenham esse método declarado concretamente
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Titulação: {}'.format(self.getTitulacao()))
        print('Disciplinas ministradas: ')
        for disc in self.getListaDisc():
            print('Nome: {} | Carga Horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))    

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Curso: {}'.format(self.getCurso()))
        print('Disciplinas cursadas: ')
        for disc in self.getListaDisc():
            print('Nome: {} | Carga Horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))

class Disciplina():
    def __init__(self, nomeDisc, cargaHoraria):
        self.__nomeDisc = nomeDisc
        self.__cargaHoraria = cargaHoraria
    
    def getNomeDisc(self):
        return self.__nomeDisc
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

if __name__ == "__main__":
    COM220 = Disciplina('Programação OO', 64)
    LET012 = Disciplina('Libras II', 48)
    BD1 = Disciplina('Banco de Dados I', 64)

    prof = Professor('Gui', 'AV BPS', 32, 'Doutorado', [])
    prof.insereDisc(LET012)
    prof.insereDisc(BD1)
    prof.printDescricao()

    print()

    aluno = Aluno('Ana Maísa', 'Rua Mário Braz', 20, 'CCO', [])
    aluno.insereDisc(COM220)
    aluno.insereDisc(BD1)
    aluno.printDescricao()