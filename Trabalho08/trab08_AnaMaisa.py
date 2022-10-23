from datetime import datetime

class Conta():
    def __init__(self, nroConta, nome, limite, senha):
        self.nroConta = nroConta
        self.nome = nome
        self.limite = limite
        self.senha = senha
        self.__transacoes = []
    
    @property
    def nroConta(self):
        return self.__nroConta
    
    @nroConta.setter
    def nroConta(self, nro):
        self.__nroConta = nro
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, novaSenha):
        self.__senha = novaSenha
    
    @property
    def transacoes(self):
        return self.__transacoes
    
    @transacoes.setter
    def transacoes(self, transacao):
        self.__transacoes.append(transacao)

    
    def adicionaDeposito(self, valor, data, nomeDepositante):
        dep = Deposito(valor, data, nomeDepositante)
        self.transacoes = dep
    
    def adicionaSaque(self, valor, data, senha):
        if (senha == self.senha and self.calculaSaldo() >= valor):
            saque = Saque(valor, data, senha)
            self.transacoes = saque
            return True
        else:
            return False
    
    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if (senha == self.senha and self.calculaSaldo() >= valor):
            transfD = Transferencia(valor, data, senha, 'D')
            transfC = Transferencia(valor, data, senha, 'C')
            self.transacoes = transfD
            contaFavorecido.transacoes = transfC
            return True
        else:
            return False
    
    def calculaSaldo(self):
        saldo = self.limite
    
        for trans in self.transacoes:
            if (type(trans).__name__ == 'Deposito'):
                saldo += trans.valor
            elif (type(trans).__name__ == 'Saque'):
                saldo -= trans.valor
            else:
                if(trans.tipoTransf == 'D'):
                    saldo -= trans.valor
                else:
                    saldo += trans.valor
                
        return saldo
            
    
class Transacao():
    def __init__(self, valor, data):
        self.valor = valor
        self.data = data
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.senha = senha
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
    
class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.nomeDepositante = nomeDepositante
    
    @property
    def nomeDepositante(self):
        return self.__nomeDepositante
    
    @nomeDepositante.setter
    def nomeDepositante(self, nomeDep):
        self.__nomeDepositante = nomeDep

class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.senha = senha
        self.tipoTransf = tipoTransf
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
    
    @property
    def tipoTransf(self):
        return self.__tipoTransf
    
    @tipoTransf.setter
    def tipoTransf(self, tipo):
        self.__tipoTransf = tipo

if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, datetime.today(), 'Antonio Maia')
    
    if c1.adicionaSaque(2000, datetime.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    
    if c1.adicionaSaque(1000, datetime.today(), 'senha-errada') == False: #deve falhar
        print('Não foi possível realizar o saque no valor de 1000')
    
    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, datetime.today(), 'Maria da Cruz')

    if c2.adicionaSaque(1500, datetime.today(),'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    
    if c2.adicionaTransf(5000, datetime.today(), 'senha2', c1) == False: #deve falhar
        print('Não foi possível realizar a transferência no valor de 5000')
    
    if c2.adicionaTransf(800, datetime.today(),'senha2', c1) == False:
        print('Não foi possível realizar o saque no valor de 800')
    
    print('-----------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) #deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) #deve imprimir 1700