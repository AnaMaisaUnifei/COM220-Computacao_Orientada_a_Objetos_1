# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 04 - Doméstica para República
# Nome: Ana Maísa do Nascimento Santos - 2021002575

from abc import ABC, abstractmethod

class EmpDomestica(ABC):
  def __init__(self, nome, telefone):
    self.__nome = nome
    self.__telefone = telefone
  
  def getNome(self):
    return self.__nome

  def setNome(self, nome):
    self.__nome = nome

  def getTelefone(self):
    return self.__telefone

  def setTelefone(self, telefone):
    self.__telefone = telefone

  @abstractmethod
  def getSalario(self):
    pass

class Horista(EmpDomestica):
  def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
    super().__init__(nome, telefone)
    self.__horasTrabalhadas = horasTrabalhadas
    self.__valorPorHora = valorPorHora

  def getHorasTrabalhadas(self):
    return self.__horasTrabalhadas
  
  def getValorPorHora(self):
    return self.__valorPorHora
  
  def getSalario(self):
    return self.getHorasTrabalhadas()*self.getValorPorHora()

class Diarista(EmpDomestica):
  def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
    super().__init__(nome, telefone)
    self.__diasTrabalhados = diasTrabalhados
    self.__valorPorDia = valorPorDia
  
  def getDiasTrabalhados(self):
    return self.__diasTrabalhados
  
  def getValorPorDia(self):
    return self.__valorPorDia
  
  def getSalario(self):
    return self.getDiasTrabalhados()*self.getValorPorDia()

class Mensalista(EmpDomestica):
  def __init__(self, nome, telefone, valorMensal):
    super().__init__(nome, telefone)
    self.__valorMensal = valorMensal

  def getValorMensal(self):
    return self.__valorMensal
  
  def getSalario(self):
    return self.getValorMensal()

if __name__ == "__main__":
  h = Horista('Horista Clara', '11999999999', 160, 12.00)
  d = Diarista('Diarista Velma', '35988888888', 20, 60.00)
  m = Mensalista('Mensalista Janete', '37955555555', 1200.00)

  domesticas = [h, d, m]
  vantagem = h

  for domestica in domesticas:
    print('Valor Mensal da {}: R${}'.format(domestica.getNome(), domestica.getSalario()))

    if(vantagem.getSalario() > domestica.getSalario()):
      vantagem = domestica
  
  print('Opção mais vantajosa:')
  print('Nome: {} | Telefone: {} | Salário a ser pago: R${}'.format(vantagem.getNome(), vantagem.getTelefone(), vantagem.getSalario()))



