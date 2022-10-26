# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 09 - Folha de Pagamento
# Nome: Ana Maísa do Nascimento Santos - 2021002575

from abc import ABC, abstractmethod

class Funcionario(ABC):
  def __init__(self, codigo, nome):
    self.codigo = codigo
    self.nome = nome
    self.__pontoMensalFunc = []
  
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
  def pontoMensalFunc(self):
    return self.__pontoMensalFunc
  
  def adicionaPonto(self, mes, ano, faltas, atrasos):
    ponto = PontoFunc(mes, ano, faltas, atrasos)
    self.pontoMensalFunc.append(ponto)
  
  def lancaFaltas(self, mes, ano, faltas):
    for ponto in self.pontoMensalFunc:
      if(ponto.mes == mes and ponto.ano == ano):
        ponto.lancaFaltas(faltas)

  def lancaAtrasos(self, mes, ano, atrasos):
    for ponto in self.pontoMensalFunc:
      if(ponto.mes == mes and ponto.ano == ano):
        ponto.lancaAtrasos(atrasos)

  def imprimeFolha(self, mes, ano):
    print('Código: {}'.format(self.codigo))
    print('Nome: {}'.format(self.nome))
    print('Salário líquido: {}'.format(self.calculaSalario(mes, ano)))
    print('Bônus: {}'.format(self.calculaBonus(mes, ano)))

  @abstractmethod
  def calculaSalario(self, mes, ano):
    pass

  @abstractmethod
  def calculaBonus(self, mes, ano):
    pass

class PontoFunc():
  def __init__(self, mes, ano, nroFaltas, nroAtrasos):
    self.mes = mes
    self.ano = ano
    self.nroFaltas = nroFaltas
    self.nroAtrasos = nroAtrasos

  @property
  def mes(self):
    return self.__mes

  @mes.setter
  def mes(self, mes):
    self.__mes = mes
  
  @property
  def ano(self):
    return self.__ano

  @ano.setter
  def ano(self, ano):
    self.__ano = ano
  
  @property
  def nroFaltas(self):
    return self.__nroFaltas

  @nroFaltas.setter
  def nroFaltas(self, nroFaltas):
    self.__nroFaltas = nroFaltas
  
  @property
  def nroAtrasos(self):
    return self.__nroAtrasos

  @nroAtrasos.setter
  def nroAtrasos(self, nroAtrasos):
    self.__nroAtrasos = nroAtrasos
  
  def lancaFaltas(self, nroFaltas):
    self.nroFaltas += nroFaltas
  
  def lancaAtrasos(self, nroAtrasos):
    self.nroAtrasos += nroAtrasos

class Professor(Funcionario):
  def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
    super().__init__(codigo, nome)
    self.titulacao = titulacao
    self.salarioHora = salarioHora
    self.nroAulas = nroAulas
  
  @property
  def titulacao(self):
    return self.__titulacao

  @titulacao.setter
  def titulacao(self, titulacao):
    self.__titulacao = titulacao
  
  @property
  def salarioHora(self):
    return self.__salarioHora

  @salarioHora.setter
  def salarioHora(self, salarioHora):
    self.__salarioHora = salarioHora
  
  @property
  def nroAulas(self):
    return self.__nroAulas

  @nroAulas.setter
  def nroAulas(self, nroAulas):
    self.__nroAulas = nroAulas
  
  def calculaSalario(self, mes, ano):
    salario = self.salarioHora * self.nroAulas
    
    for ponto in self.pontoMensalFunc:
      if(ponto.mes == mes and ponto.ano == ano):
        salario -= (ponto.nroFaltas * self.salarioHora)
        return salario
    
    return 'Não há ponto desse funcionário nesse mês e ano'
  
  def calculaBonus(self, mes, ano):
    percentual = 10

    for ponto in self.pontoMensalFunc:
      if(ponto.mes == mes and ponto.ano == ano):
        percentual -= ponto.nroAtrasos

        if(percentual > 0):
          return self.calculaSalario(mes, ano)*(percentual/100)
        else:
          return 'Percentual abaixo de 0. Não há bônus'
    
    return 'Não há ponto desse funcionário nesse mês e ano'


class TecAdmin(Funcionario):
  def __init__(self, codigo, nome, funcao, salarioMensal):
    super().__init__(codigo, nome)
    self.funcao = funcao
    self.salarioMensal = salarioMensal
  
  @property
  def funcao(self):
    return self.__funcao

  @funcao.setter
  def funcao(self, funcao):
    self.__funcao = funcao
  
  @property
  def salarioMensal(self):
    return self.__salarioMensal

  @salarioMensal.setter
  def salarioMensal(self, salarioMensal):
    self.__salarioMensal = salarioMensal
  
  def calculaSalario(self, mes, ano):
    salario = self.salarioMensal
    
    for ponto in self.pontoMensalFunc:
      if(ponto.mes == mes and ponto.ano == ano):
        salario -= (ponto.nroFaltas * (self.salarioMensal/30))
        return salario
    
    return 'Não há ponto desse funcionário nesse mês e ano'
  
  def calculaBonus(self, mes, ano):
    percentual = 8

    for ponto in self.pontoMensalFunc:
      if(ponto.mes == mes and ponto.ano == ano):
        percentual -= ponto.nroAtrasos

        if(percentual > 0):
          return self.calculaSalario(mes, ano)*(percentual/100)
        else:
          return 'Percentual abaixo de 0. Não há bônus'
    
    return 'Não há ponto desse funcionário nesse mês e ano'

if __name__ == "__main__":
  funcionarios = []

  prof = Professor(1, 'João', 'Doutor', 45.35, 32)
  prof.adicionaPonto(4, 2021, 0, 0)
  prof.lancaFaltas(4, 2021, 2)
  prof.lancaAtrasos(4, 2021, 3)
  funcionarios.append(prof)

  tec = TecAdmin(2, 'Pedro', 'Analista Contábil', 3600)
  tec.adicionaPonto(4, 2021, 0, 0)
  tec.lancaFaltas(4, 2021, 3)
  tec.lancaAtrasos(4, 2021, 4)
  funcionarios.append(tec)

  for func in funcionarios:
    func.imprimeFolha(4, 2021)
    print()