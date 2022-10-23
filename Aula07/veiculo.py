class Veiculo:
  def __init__(self, marca, cor,motorligado):
    self.__marca = marca
    self.__cor = cor
    self.__motorligado = motorligado
  
  def getMarca(self):
    return self.__marca
  
  def getCor(self):
    return self.__cor
  
  def isMotorLigado(self): #variável booleana não pe get, é is
    return self.__motorligado
  
  def ligaMotor(self):
    if(self.__motorligado == True):
      print('O motor já está ligado!')
    else: 
      self.__motorligado = True
      print('O motor acaba de ser ligado')

class Carro(Veiculo):
  def __init__(self, marca, cor, motorligado, portaMalaCheio):
    super().__init__(marca, cor, motorligado)
    self.__portaMalaCheio = portaMalaCheio
  
  def isPortaMalaCheio(self):
    return self.__portaMalaCheio

  def encherPortaMala(self):
    if(self.__portaMalaCheio == True):
      print('O porta mala está cheio!')
    else: 
      self.__portaMalaCheio = True
      print('O porta malas acaba de ser cheio')
  
  def mostraAtributos(self):
    print('Este carro é um {} {}'.format(self.getMarca(), self.getCor()))

class Moto(Veiculo):
  def __init__(self, marca, cor, motorligado):
    super().__init__(marca, cor, motorligado)

