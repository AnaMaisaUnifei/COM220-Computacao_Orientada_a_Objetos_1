from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.cargaHoraria = cargaHoraria #Chama o setter (ativa a função) e passa o valor do construtor
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @cargaHoraria.setter
    def cargaHoraria(self, valor):
        if valor > 160:
            print('Ajustando o valor da Carga Horária.')
            self.__cargaHoraria = 160
        else:
            self.__cargaHoraria = valor
    
    @abstractmethod
    def salarioLiquido():
        pass

    @abstractmethod
    def imprimeDados():
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salario):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    
    def salarioLiquido(self):
        salario_prev = self.salario - self.salario* 0.11;
        if(salario_prev < 1903.98):
            return salario_prev
        elif(salario_prev < 2826.65):
            return salario_prev - salario_prev * 0.075
        elif(salario_prev < 3751.05):
            return salario_prev - salario_prev * 0.15
        elif(salario_prev < 4664.68):
            return salario_prev - salario_prev*0.225
        else:
            return salario_prev - salario_prev*0.275
    
    def imprimeDados(self):
        print('Nome: {}'.format(self.nome))
        print('Matrícula: {}'.format(self.matricula))
        print('Carga Horárioa: {}'.format(self.cargaHoraria))
        print('Salário Líquido: {}'.format(self.salarioLiquido()))
        print()
        


class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def getSalario(self):
        return self.salarioHora * self.cargaHoraria

    def salarioLiquido(self):
        if(self.getSalario() < 1903.98):
            return self.getSalario()
        elif(self.getSalario() < 2826.65):
            return self.getSalario() - self.getSalario() * 0.075
        elif(self.getSalario() < 3751.05):
            return self.getSalario() - self.getSalario() * 0.15
        elif(self.getSalario() < 4664.68):
            return self.getSalario() - self.getSalario()*0.225
        else:
            return self.getSalario() - self.getSalario()*0.275
    
    def imprimeDados(self):
        print('Nome: {}'.format(self.nome))
        print('Matrícula: {}'.format(self.matricula))
        print('Carga Horária: {}'.format(self.cargaHoraria))
        print('Salário hora: {}'.format(self.salarioHora))
        print('Salário Líquido: {}'.format(self.salarioLiquido()))
        print()
        

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    profs = [prof1, prof2, prof3]
    for prof in profs:
        prof.imprimeDados()
    
    print('---------------')
    prof1.salario = 6000
    prof2.salarioHora = 85
    prof3.salarioHora = 105

    for prof in profs:
        prof.imprimeDados()

