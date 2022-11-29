# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Nome: Ana Maísa do Nascimento Santos - 2021002575

from abc import ABC, abstractmethod

class Conta(ABC):
  def __init__(self, numConta, nome, saldo):
    self.__numConta = numConta
    self.__nome = nome
    self.__saldo = saldo
    self.__listaTrans = []
  
  @property
  def numConta(self):
    return self.__numConta

  @property
  def nome(self):
    return self.__nome
  
  @property
  def saldo(self):
    return self.__saldo
  
  @saldo.setter
  def saldo(self, valor):
    self.__saldo += valor
  
  @property
  def listaTrans(self):
    return self.__listaTrans
  
  @listaTrans.setter
  def listaTrans(self, trans):
    self.__listaTrans.append(trans)
  
  def deposito(self, valorDep):
    transacao = Transacao(valorDep, 'Crédito')
    self.listaTrans = transacao
    self.saldo = valorDep
    print('{} depositou R${}! Saldo atual: R${}'.format(self.nome, valorDep, self.saldo))
  
  def retirada(self, valorRet):
    if(self.saldo >= valorRet):
      transacao = Transacao(-valorRet, 'Débito')
      self.listaTrans = transacao
      self.saldo = -valorRet
      print('{} retirou R${}! Saldo atual: R${}'.format(self.nome, valorRet, self.saldo))
    else:
      print('Não é possível realizar a operação! Seu saldo é de R${}'.format(self.saldo))
  
  @abstractmethod
  def imprimirExtrato(self):
    pass

class ContaComum(Conta):
  def __init__(self, numConta, nome, saldo):
    super().__init__(numConta, nome, saldo)
  
  def imprimirExtrato(self):
    print('Nº da Conta: {}'.format(self.numConta))
    print('Nome: {}'.format(self.nome))
    print('Saldo: R${}'.format(self.saldo))
    print('Transações:')
    for trans in self.listaTrans:
      print('Tipo: {} | Valor: R${}'.format(trans.desc, trans.valor))
  
class ContaPoupanca(Conta):
  def __init__(self, numConta, nome, saldo, diaAniverConta):
    super().__init__(numConta, nome, saldo)
    self.diaAniverConta = diaAniverConta
  
  @property
  def diaAniverConta(self):
    return self.__diaAniverConta
  
  @diaAniverConta.setter
  def diaAniverConta(self, dia):
    self.__diaAniverConta = dia
  
  def imprimirExtrato(self):
    print('Nº da Conta: {}'.format(self.numConta))
    print('Nome: {}'.format(self.nome))
    print('Saldo: R${}'.format(self.saldo))
    print('Dia do Aniversário: {}'.format(self.diaAniverConta))
    print('Transações:')
    for trans in self.listaTrans:
      print('Tipo: {} | Valor: R${}'.format(trans.desc, trans.valor))
    

class ContaComLimite(Conta):
  def __init__(self, numConta, nome, saldo, valorLimite):
    super().__init__(numConta, nome, saldo)
    self.valorLimite = valorLimite
  
  @property
  def valorLimite(self):
    return self.__valorLimite

  @valorLimite.setter
  def valorLimite(self, valor):
    self.__valorLimite = valor
  
  def retirada(self, valorRet):
    if(self.saldo+self.valorLimite >= valorRet):
      transacao = Transacao(-valorRet, 'Débito')
      self.listaTrans = transacao
      self.saldo = -valorRet
      print('{} retirou R${}! Saldo atual: R${}'.format(self.nome, valorRet, self.saldo))
    else:
      print('Não é possível realizar a operação! Seu saldo é de R${} e seu limite é de R${}'.format(self.saldo, self.valorLimite))
  
  def imprimirExtrato(self):
    print('Nº da Conta: {}'.format(self.numConta))
    print('Nome: {}'.format(self.nome))
    print('Saldo: R${}'.format(self.saldo))
    print('Limite: R${}'.format(self.valorLimite))
    print('Transações:')
    for trans in self.listaTrans:
      print('Tipo: {} | Valor: R${}'.format(trans.desc, trans.valor))


class Transacao():
  def __init__(self, valor, desc):
    self.valor = valor
    self.desc = desc
  
  @property
  def valor(self):
    return self.__valor

  @valor.setter
  def valor (self, valor):
    self.__valor = valor
  
  @property
  def desc(self):
    return self.__desc

  @desc.setter
  def desc (self, desc):
    self.__desc = desc

if __name__ == "__main__":
  cc1 = ContaComum(120, 'Ana Maísa', 5000.00)
  cp1 = ContaPoupanca(851, 'José', 2038.00, 25)
  cl1 = ContaComLimite(412, 'Teo', 100.00, 1000.00)

  cc1.deposito(300.00)
  cc1.retirada(100.00)
  cp1.retirada(38.00)
  cl1.retirada(200.00)

  print()

  contas = [cc1, cp1, cl1]

  for conta in contas:
    conta.imprimirExtrato()
    print()