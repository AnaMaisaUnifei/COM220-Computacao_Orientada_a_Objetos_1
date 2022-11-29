from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula

    def getCargaHoraria(self):
        return self.__cargaHoraria

    @abstractmethod
    def getSalario(self):
        pass

    @abstractmethod
    def getSalarioLiquido(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salario):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salario = salario

    def setSalario(self, salario):
        self.__salario = salario

    def getSalario(self):
        return self.__salario
    
    def getSalarioLiquido(self):
        salario_prev = self.getSalario() - self.getSalario()* 0.11;
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
        


class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    def setSalarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def getSalarioHora(self):
        return self.__salarioHora

    def getSalario(self):
        return self.__salarioHora * self.getCargaHoraria()

    def getSalarioLiquido(self):
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

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    profs = [prof1, prof2, prof3]
    for prof in profs:
        print ('Nome: {} - Salário: {}'.format(prof.getNome(), prof.getSalarioLiquido()))

