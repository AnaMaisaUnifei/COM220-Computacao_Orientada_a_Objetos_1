# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Prova 2 - Ordem de Serviços
# Nome: Ana Maísa do Nascimento Santos - 2021002575

from abc import ABC

class Pessoa(ABC):

    def __init__(self, cpf, nome, fone):
        self.__cpf = cpf
        self.__nome = nome
        self.__fone = fone

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def fone(self):
        return self.__fone

class Funcionario(Pessoa):

    def __init__(self, cpf, nome, fone, salario, funcao):
        super().__init__(cpf, nome, fone)
        self.__salario = salario
        self.__funcao = funcao

    @property
    def salario(self):
        return self.__salario

    @property
    def funcao(self):
        return self.__funcao

class Cliente(Pessoa):

    def __init__(self, cpf, nome, fone, tipoCliente):
        super().__init__(cpf, nome, fone)
        self.__tipoCliente = tipoCliente

        self.__veiculos = []

    @property
    def tipoCliente(self):
        return self.__tipoCliente

    @property
    def veiculos(self):
        return self.__veiculos

    def addVeiculo(self, veiculo):
        self.__veiculos.append(veiculo)

class Servico:

    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class CtrlFuncCliServ():
    def __init__(self):
        func1 = Funcionario('1001', 'Luis Silva', '98877665', 1800, 'Atendente')
        func2 = Funcionario('1002', 'Pedro Cruz', '97753684', 2200, 'Atendente')
        self.listaFunc = [func1, func2]

        cliente1 = Cliente('1003', 'João Souza', '997780855', 'Vip')
        cliente2 = Cliente('1004', 'Marina Lima', '987650355', 'Padrão')
        cliente3 = Cliente('1005', 'Márcio Santos', '997653385', 'Vip')
        self.listaCli = [cliente1, cliente2, cliente3]

        serv1 = Servico(100, 'Alinhamento direçao', 70)
        serv2 = Servico(101, 'Balanceamento rodas', 80)
        serv3 = Servico(102, 'Troca de óleo', 120)
        serv4 = Servico(103, 'Troca amortecedor', 150)
        serv5 = Servico(104, 'Troca pastilha freio', 180)
        self.listaServ = [serv1, serv2, serv3, serv4, serv5]
    
    def listaNomesClientes(self):
        listaNomes = []

        for cliente in self.listaCli:
            listaNomes.append(cliente.nome)
        
        return listaNomes
    
    def listaCodServ(self):
        listaCod = []

        for serv in self.listaServ:
            listaCod.append(serv.codigo)
        
        return listaCod
    
    def getCliente(self, nome):
        clienteRet = None
        for cliente in self.listaCli:
            if cliente.nome == nome:
                clienteRet = cliente
        return clienteRet
    
    def listaNomesFuncs(self):
        listaNomes = []

        for func in self.listaFunc:
            listaNomes.append(func.nome)
        
        return listaNomes
    
    def getServico(self, codigo):
        servRet = None
        for servico in self.listaServ:
            if servico.codigo == codigo:
                servRet = servico
        return servRet
    
    def getFunc(self, nome):
        funcRet = None
        for func in self.listaFunc:
            if func.nome == nome:
                funcRet = func
        return funcRet




