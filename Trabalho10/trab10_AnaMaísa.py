# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 10 - Exceptions
# Nome: Ana Maísa do Nascimento Santos - 2021002575

from abc import ABC, abstractmethod

# Definição das Excpetions
class naoDr(Exception):
  # Se o professor não for doutor
  pass

class idadeProfessor(Exception):
  # Se o professor não tiver idade maior ou igual a 30
  pass

class naoCCOouSIN(Exception):
  # Se o aluno não for de CCO ou SIN
  pass

class idadeAluno(Exception):
  # Se o aluno não tiver idade maior ou igual a 18
  pass

class cpfIgual(Exception):
  # Pessoas com mesmo CPF
  pass

# Classes
class Pessoa(ABC):
  def __init__(self, nome, cpf, endereco, idade):
    self.nome = nome
    self.cpf = cpf
    self.endereco = endereco
    self.idade = idade
  
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome):
    self.__nome = nome
  
  @property
  def cpf(self):
    return self.__cpf
  
  @cpf.setter
  def cpf(self, cpf):
    self.__cpf = cpf
  
  @property
  def endereco(self):
    return self.__endereco
  
  @endereco.setter
  def endereco(self, endereco):
    self.__endereco = endereco
  
  @property
  def idade(self):
    return self.__idade
  
  @idade.setter
  def idade(self, idade):
    self.__idade = idade
  
  @abstractmethod
  def printDescricao(self):
    pass

class Professor(Pessoa):
  def __init__(self, nome, cpf, endereco, idade, titulacao):
    super().__init__(nome, cpf, endereco, idade)
    self.titulacao = titulacao
  
  @property
  def titulacao(self):
    return self.__titulacao
  
  @titulacao.setter
  def titulacao(self, titulacao):
    self.__titulacao = titulacao
  
  def printDescricao(self):
    print("Professor(a) {}".format(self.nome))
    print("CPF: {}".format(self.cpf))
    print("Endereço: {}".format(self.endereco))
    print("Idade: {}".format(self.idade))
    print("Titulação: {}".format(self.titulacao))
    print()
    print('**************************')


class Aluno(Pessoa):
  def __init__(self, nome, cpf, endereco, idade, curso):
    super().__init__(nome, cpf, endereco, idade)
    self.curso = curso
  
  @property
  def curso(self):
    return self.__curso
  
  @curso.setter
  def curso(self, curso):
    self.__curso = curso
  
  def printDescricao(self):
    print("Aluno(a) {}".format(self.nome))
    print("CPF: {}".format(self.cpf))
    print("Endereço: {}".format(self.endereco))
    print("Idade: {}".format(self.idade))
    print("Curso: {}".format(self.curso))
    print()
    print('**************************')

if __name__ == "__main__":
  # Para fazer apenas uma lista, coloquei dentre os dados mais uma informação, que será um "P" para professor e um "A" para aluno. Assim, consigo diferenciar de que Pessoa é o dado antes de instanciar e com apenas uma lista. OBS.: Esse dado não será cadastrado, é só pra ter controle das instancias que vão ser criadas
  listaDados = [
    ('P',"Laércio Baldochi", "78545862312", "Av. BPS, 1100", 40, "Doutor"),
    ('P',"Isabella Neves", "4513812025X", "Av. BPS, 356", 35, "Doutor"),
    ('P',"Melise Veiga", "451897122366", "Rua Mário Braz, 356", 45, "Mestre"), # Não é doutora
    ('P',"Phyllipe", "152698771025", "Av. BPS, 356", 35, "Doutor"),
    ('P',"Vania Adalva", "4513812025X", "Av. BPS, 356", 35, "Doutor"), # Mesmo CPF de Isabella
    ('P',"Cores Roque", "45669320145", "Av. Surubim, 356", 20, "Doutor"), # Tem menos de 30 anos
    ('A',"Ana Maísa", "23037389893", "Av. Mario Braz, 4856", 18, "CCO"),
    ('A',"Marina Baeta", "4512688655", "Rua Prefeito Tigre Maia, 256", 20, "ECO"), # Não é de CCO ou SIN
    ('A',"Maíssa Maniezzo", "15646221559X", "Av. Mario Braz, 124", 17, "CCO"), # Tem menos de 18 anos
    ('A',"Gabriel Ciriaco", "21665981264", "Av. Mario Braz, 4856", 22, "CCO"),
    ('A',"Pedro Lucas", "15481598222", "Av. Masseli, 548", 21, "SIN"),
    ('A',"Guiherme Teodoro", "5454548235", "Av. Itajuba, 456", 18, "SIN"),
    ('A',"Guilherme Thiesen", "23037389893", "Av. Mario Braz, 4856", 18, "SIN") # Tem o mesmo CPF de Ana Maísa
  ]

  cadastros = []

  for tipo, nome, cpf, endereco, idade, ct in listaDados:
    try:
      for pessoa in cadastros:
        if(pessoa.cpf == cpf):
          raise cpfIgual

      if (tipo == 'P'):
        if(ct != "Doutor"):
          raise naoDr
        
        if(idade < 30):
          raise idadeProfessor
      else:
        if(ct != "CCO" and ct != "SIN"): 
          raise naoCCOouSIN
        
        if(idade < 18):
          raise idadeAluno        
    except naoDr:
      print('Dado Inválido! O(a) professor(a) {} não é doutor(a)!'.format(nome))
      print()
    except idadeProfessor:
      print('Dado Inválido! O(a) professor(a) {} tem menos de 30 anos!'.format(nome))
      print()
    except naoCCOouSIN:
      print('Dado Inválido! O(a) aluno(a) {} não é dos cursos de CCO ou SIN!'.format(nome))
      print()
    except idadeAluno:
      print('Dado Inválido! O(a) aluno(a) {} tem menos de 18 anos!'.format(nome))
      print()
    except cpfIgual:
      print('Dado Inválido! Já existe um cadastro com o CPF de {}!'.format(nome))
      print()
    else:
      if(tipo == 'P'):
        cadastros.append(Professor(nome, cpf, endereco, idade, ct))
      else:
        cadastros.append(Aluno(nome, cpf, endereco, idade, ct))
  
  print('Cadastros realizados:')
  print('************************')
  for cadastro in cadastros:
    cadastro.printDescricao()
    print()