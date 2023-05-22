
class Alimento:
    def __init__(self):
        self.terrestresC = ["pollo crudo"]
        self.terrestresH = ["lechuga"]
        self.acuaticoC = ["sardinas"]
        self.acuaticoH = ["plangton"]
        self.semiAcuaticoC = ["ratones"]
        self.semiAcuaticoH = ["zanahoria"]
        self.voladorC = ["pollo crudo"]
        self.voladorH = ["semillas de girasol"]
        self.categorias = [
            self.terrestresC, self.terrestresH,
            self.acuaticoC, self.acuaticoH,
            self.semiAcuaticoC, self.semiAcuaticoH,
            self.voladorC, self.voladorH
        ]

    def addCarnivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresC.append(alimento)
        elif tipoAnimal == 2:
            self.acuaticoC.append(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoC.append(alimento)
        elif tipoAnimal == 4:
            self.voladorC.append(alimento)
    
    def addHerbivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresH.append(alimento)
        elif tipoAnimal == 2:
            self.acuaticoH.append(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoH.append(alimento)
        elif tipoAnimal == 4:
            self.voladorH.append(alimento)

