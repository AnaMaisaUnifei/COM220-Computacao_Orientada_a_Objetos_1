# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 16 - Campeonato de Futebol
# Nome: Ana Maísa do Nascimento Santos - 2021002575

class Estudante():
  def __init__(self, nroMatric, nome, curso):
    self.nroMatric = nroMatric
    self.nome = nome
    self.curso = curso
  
  @property
  def sigla(self):
    return self.__sigla
  
  @sigla.setter
  def sigla (self, sigla):
    self.__sigla = sigla
  
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome (self, nome):
    self.__nome = nome
  
  @property
  def curso(self):
    return self.__curso
  
  @curso.setter
  def curso (self, curso):
    self.__curso = curso

class Curso():
  def __init__(self, sigla, nome):
    self.sigla = sigla
    self.nome = nome
  
  @property
  def sigla(self):
    return self.__sigla
  
  @sigla.setter
  def sigla (self, sigla):
    self.__sigla = sigla
  
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome (self, nome):
    self.__nome = nome


class CtrlEstudanteCurso():
  def __init__(self):
    c1 = Curso("CCO", "Ciência da Computação")
    c2 = Curso("SIN", "Sistemas de Informação")
    c3 = Curso("EEL", "Engenharia Elétrica")
    c4 = Curso("ECO", "Engenharia da Computação")

    self.listaCurso = []

    self.listaCurso.append(c1)
    self.listaCurso.append(c2)
    self.listaCurso.append(c3)
    self.listaCurso.append(c4)

    self.listaEstudante = []

    self.listaEstudante.append(Estudante(1001, "José da Silva", c1))
    self.listaEstudante.append(Estudante(1002, "João de Souza", c1))
    self.listaEstudante.append(Estudante(1003, "Rui Santos", c2))
    self.listaEstudante.append(Estudante(1004, "Fábio Amorelli", c3))
    self.listaEstudante.append(Estudante(1005, "Marina Baeta", c4))
    self.listaEstudante.append(Estudante(1006, "Vitor Hermetto", c1))
    self.listaEstudante.append(Estudante(1007, "Guilherme Teodoro", c2))
    self.listaEstudante.append(Estudante(1008, "Chaquel Alcino", c3))
    self.listaEstudante.append(Estudante(1009, "Guilherme Martins", c4))
    self.listaEstudante.append(Estudante(1010, "Elis Ferreira", c2))
    self.listaEstudante.append(Estudante(1011, "Jhonatan Alcebiades", c3))
    self.listaEstudante.append(Estudante(1012, "Rafael Hadzick", c4))
  
  def listaNroMatric(self):
    listaMatric = []

    for est in self.listaEstudante:
      listaMatric.append(est.nroMatric)
    
    return listaMatric
  
  def listaNomesCursos(self):
    listaNomes = []

    for curso in self.listaCurso:
      listaNomes.append(curso.nome)
    
    return listaNomes
  
  def listaSiglasCursos(self):
    listaSiglas = []

    for curso in self.listaCurso:
      listaSiglas.append(curso.sigla)
    
    return listaSiglas
  
  def getCurso(self, nome):
    cursoRet = None
    for curso in self.listaCurso:
      if curso.nome == nome:
          cursoRet = curso
    return cursoRet
  
  def getCursoSigla(self, sigla):
    cursoRet = None
    for curso in self.listaCurso:
      if curso.sigla == sigla:
          cursoRet = curso
    return cursoRet
