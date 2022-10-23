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
  
  def getNumConta(self):
    return self.__numConta

  def getNome(self):
    return self.__nome
  
  def getSaldo(self):
    return self.__saldo
  
  def setSaldo(self, valor):
    self.__saldo += valor
  
  def getListaTrans(self):
    return self.__listaTrans
  
  def setListaTrans(self, trans):
    self.__listaTrans.append(trans)
  
  def deposito(self, valorDep):
    transacao = Transacao(valorDep, 'Crédito')
    self.setListaTrans(transacao)
    self.__saldo += valorDep
    print('{} depositou R${}! Saldo atual: R${}'.format(self.getNome(), valorDep, self.getSaldo()))
  
  def retirada(self, valorRet):
    if(self.getSaldo() >= valorRet):
      transacao = Transacao(-valorRet, 'Débito')
      self.setListaTrans(transacao)
      self.__saldo -= valorRet
      print('{} retirou R${}! Saldo atual: R${}'.format(self.getNome(), valorRet, self.getSaldo()))
    else:
      print('Não é possível realizar a operação! Seu saldo é de R${}'.format(self.getSaldo()))
  
  @abstractmethod
  def imprimirExtrato(self):
    pass

class ContaComum(Conta):
  def __init__(self, numConta, nome, saldo):
    super().__init__(numConta, nome, saldo)
  
  def imprimirExtrato(self):
    print('Nº da Conta: {}'.format(self.getNumConta()))
    print('Nome: {}'.format(self.getNome()))
    print('Saldo: R${}'.format(self.getSaldo()))
    print('Transações:')
    for trans in self.getListaTrans():
      print('Tipo: {} | Valor: R${}'.format(trans.getDesc(), trans.getValor()))
  
class ContaPoupanca(Conta):
  def __init__(self, numConta, nome, saldo, diaAniverConta):
    super().__init__(numConta, nome, saldo)
    self.__diaAniverConta = diaAniverConta
  
  def getDiaAniverConta(self):
    return self.__diaAniverConta
  
  def imprimirExtrato(self):
    print('Nº da Conta: {}'.format(self.getNumConta()))
    print('Nome: {}'.format(self.getNome()))
    print('Saldo: R${}'.format(self.getSaldo()))
    print('Dia do Aniversário: {}'.format(self.getDiaAniverConta()))
    print('Transações:')
    for trans in self.getListaTrans():
      print('Tipo: {} | Valor: R${}'.format(trans.getDesc(), trans.getValor()))
    

class ContaComLimite(Conta):
  def __init__(self, numConta, nome, saldo, valorLimite):
    super().__init__(numConta, nome, saldo)
    self.__valorLimite = valorLimite
  
  def getValorLimite(self):
    return self.__valorLimite
  
  def retirada(self, valorRet):
    if(self.getSaldo()+self.getValorLimite() >= valorRet):
      transacao = Transacao(-valorRet, 'Débito')
      self.setListaTrans(transacao)
      self.setSaldo(-valorRet)
      print('{} retirou R${}! Saldo atual: R${}'.format(self.getNome(), valorRet, self.getSaldo()))
    else:
      print('Não é possível realizar a operação! Seu saldo é de R${} e seu limite é de R${}'.format(self.getSaldo(), self.getValorLimite()))
  
  def imprimirExtrato(self):
    print('Nº da Conta: {}'.format(self.getNumConta()))
    print('Nome: {}'.format(self.getNome()))
    print('Saldo: R${}'.format(self.getSaldo()))
    print('Limite: R${}'.format(self.getValorLimite()))
    print('Transações:')
    for trans in self.getListaTrans():
      print('Tipo: {} | Valor: R${}'.format(trans.getDesc(), trans.getValor()))


class Transacao():
  def __init__(self, valor, desc):
    self.__valor = valor
    self.__desc = desc
  
  def getValor(self):
    return self.__valor

  def getDesc(self):
    return self.__desc

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