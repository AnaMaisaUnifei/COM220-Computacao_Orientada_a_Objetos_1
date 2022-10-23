# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 07 - Imobiliária
# Nome: Ana Maísa do Nascimento Santos - 2021002575

from abc import ABC, abstractmethod
from tkinter import commondialog

class Vendedor(ABC):
  def __init__(self, codigo, nome):
    self.codigo = codigo
    self.nome = nome
    self.__vendas = []

  @property
  def codigo(self):
    return self.__codigo
  
  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo
  
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome):
    self.__nome = nome
  
  @property
  def vendas(self):
    return self.__vendas
  
  @vendas.setter
  def vendas(self, venda):
    self.__vendas.append(venda)
  
  def adicionaVenda(self, pCodImovel, pMes, pAno, pValor):
    venda = Venda(pCodImovel, pMes, pAno, pValor)
    self.vendas = venda

  @abstractmethod
  def getDados(self):
    pass

  @abstractmethod
  def calculaRenda(self):
    pass

class Venda():
  def __init__(self, codImovel, mesVenda, anoVenda, valorVenda):
    self.codImovel = codImovel
    self.mesVenda = mesVenda
    self.anoVenda = anoVenda
    self.valorVenda = valorVenda
  
  @property
  def codImovel(self):
    return self.__codImovel
  
  @codImovel.setter
  def codImovel(self, codImovel):
    self.__codImovel = codImovel
  
  @property
  def mesVenda(self):
    return self.__mesVenda
  
  @mesVenda.setter
  def mesVenda(self, mesVenda):
    self.__mesVenda = mesVenda
  
  @property
  def anoVenda(self):
    return self.__anoVenda
  
  @anoVenda.setter
  def anoVenda(self, anoVenda):
    self.__anoVenda = anoVenda

  @property
  def valorVenda(self):
    return self.__valorVenda
  
  @valorVenda.setter
  def valorVenda(self, valorVenda):
    self.__valorVenda = valorVenda

class Contratado(Vendedor):
  def __init__(self, codigo, nome, salarioFixo, nroCartTrabalho):
    super().__init__(codigo, nome)
    self.nroCartTrabalho = nroCartTrabalho
    self.salarioFixo = salarioFixo
    self.comissao = 1

  @property
  def nroCartTrabalho(self):
    return self.__nroCartTrabalho
  
  @nroCartTrabalho.setter
  def nroCartTrabalho(self, nroCartTrabalho):
    self.__nroCartTrabalho = nroCartTrabalho
  
  @property
  def salarioFixo(self):
    return self.__salarioFixo
  
  @salarioFixo.setter
  def salarioFixo(self, salarioFixo):
    self.__salarioFixo = salarioFixo
  
  @property
  def comissao(self):
    return self.__comissao
  
  @comissao.setter
  def comissao(self, comissao):
    self.__comissao = comissao
  
  def getDados(self):
    return 'Nome: {} - Nro Carteira: {}'.format(self.nome, self.nroCartTrabalho)
  
  def calculaRenda(self, mes, ano):
    salario = self.salarioFixo

    for venda in self.vendas:
      if(venda.mesVenda == mes and venda.anoVenda == ano):
        salario += venda.valorVenda * (self.comissao/100)
    
    return salario

    

class Comissionado(Vendedor):
  def __init__(self, codigo, nome, nroCPF, comissao):
    super().__init__(codigo, nome)
    self.nroCPF = nroCPF
    self.comissao = comissao
  
  @property
  def nroCPF(self):
    return self.__nroCPF
  
  @nroCPF.setter
  def nroCPF(self, nroCPF):
    self.__nroCPF = nroCPF
  
  @property
  def comissao(self):
    return self.__comissao
  
  @comissao.setter
  def comissao(self, comissao):
    self.__comissao = comissao
  
  def getDados(self):
    return 'Nome: {} - Nro CPF: {}'.format(self.nome, self.nroCPF)
  
  def calculaRenda(self, mes, ano):
    salario = 0

    for venda in self.vendas:
      if(venda.mesVenda == mes and venda.anoVenda == ano):
        salario += venda.valorVenda * (self.comissao/100)
    
    return salario

if __name__ == "__main__":
  funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
  funcContratado.adicionaVenda(100, 3,2022, 200000)
  funcContratado.adicionaVenda(101, 3, 2022, 300000)
  funcContratado.adicionaVenda(102, 4, 2022, 600000)

  funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
  funcComissionado.adicionaVenda(200, 3, 2022, 200000)
  funcComissionado.adicionaVenda(201, 3, 2022, 400000)
  funcComissionado.adicionaVenda(202, 4, 2022, 500000)

  listFunc = [funcContratado, funcComissionado]

  for func in listFunc:
    print(func.getDados())
    print("Renda no mês 3 de 2022: ")
    print(func.calculaRenda(3, 2022))