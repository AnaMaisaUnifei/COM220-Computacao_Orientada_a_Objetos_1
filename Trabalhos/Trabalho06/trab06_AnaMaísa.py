# Disciplina: Computação Orientada a Objetos I (COM220)
# Professor: Laércio Augusto Baldochi Junior
# Trabalho 06 - Sistema Acadêmico
# Nome: Ana Maísa do Nascimento Santos - 2021002575

class Aluno():
  def __init__(self, nroMatric, nome, curso):
    self.nroMatric = nroMatric
    self.nome = nome
    self.curso = curso
    self.__historico = Historico()

  @property
  def nroMatric(self):
    return self.__nroMatric
  
  @nroMatric.setter
  def nroMatric(self, nro):
    self.__nroMatric = nro

  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome):
    self.__nome = nome
  
  @property
  def curso(self):
    return self.__curso
  
  @curso.setter
  def curso(self, curso):
    self.__curso = curso
  
  @property
  def historico(self):
    return self.__historico
  
  @historico.setter
  def historico(self, disc):
    if self.historico.discs == []:
      for dis in self.curso.grade.discs:
        self.__historico.discs = dis
    self.__historico.discs = disc

class Curso():
  def __init__(self, nome, grade):
    self.nome = nome
    self.grade = grade
  
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome):
    self.__nome = nome
  
  @property
  def grade(self):
    return self.__grade
  
  @grade.setter
  def grade(self, grade):
    self.__grade = grade


class Grade():
  def __init__(self, ano, discs):
    self.ano = ano
    self.__discs = discs
  
  @property
  def ano(self):
    return self.__ano
  
  @ano.setter
  def ano(self, ano):
    self.__ano = ano

  @property
  def discs(self):
    return self.__discs
  
  @discs.setter
  def discs(self, disc):
    self.__discs.append(disc)

class Disciplina():
  def __init__(self, codigo, nome, cargaHoraria):
    self.codigo = codigo
    self.nome = nome
    self.cargaHoraria = cargaHoraria
  
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
  def cargaHoraria(self):
    return self.__cargaHoraria
  
  @cargaHoraria.setter
  def cargaHoraria(self, cargaHoraria):
    self.__cargaHoraria = cargaHoraria
  
class Historico():
  def __init__(self):
    self.__discs = []
  
  @property
  def discs(self):
    return self.__discs
  
  @discs.setter
  def discs(self, discs):
    self.__discs.append(discs)

if __name__ == "__main__":
  let007 = Disciplina('LET007', 'Língua Brasileira de Sinais I', 32)
  com220 = Disciplina('COM220', 'Computação Orientada a Objetos I', 64)
  com312 = Disciplina('COM312', 'Informática e Sociedade', 32)
  let012 = Disciplina('LET012', 'Língua Brasileira de Sinais II', 32)
  com112 = Disciplina('COM112', 'Algoritmos e Estruturas de Dados II', 64)

  grade1 = Grade(2016, [let007, let012])
  grade2 = Grade(2021, [com220, com112])
  grade3 = Grade(2020, [com220, com312])

  cco = Curso('Ciência da Computação', grade2)
  sin = Curso('Sistemas de Informação', grade3)
  ll = Curso('Letras - Libras', grade1)

  al1 = Aluno(132, 'Ana Maísa', cco)
  al2 = Aluno(543, 'Teodoro', sin)
  al3 = Aluno(342, 'Ricardo', ll)

  al1.historico = let007
  al2.historico = let012
  al3.historico = com112

  alunos = [al1, al2, al3]
  obrigatorias = 0
  eletivas = 0

  for aluno in alunos:
    print('Matrícula: {} | Aluno: {}'.format(aluno.nroMatric, aluno.nome))
    print('Histórico:')
    for disc in aluno.historico.discs:
      if disc in aluno.curso.grade.discs:
        obrigatorias += disc.cargaHoraria
      else:
        eletivas += disc.cargaHoraria

      print('Código: {} | Nome: {} | Carga Horária: {}h'.format(disc.codigo, disc.nome, disc.cargaHoraria))
    
    print('Carga horária das obrigatórias cursadas: {}h'.format(obrigatorias))
    print('Carga horária das eletivas cursadas: {}h'.format(eletivas))
    print()
    obrigatorias = 0
    eletivas = 0





