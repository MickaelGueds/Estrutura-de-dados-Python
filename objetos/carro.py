class Carro:
    pass

class Carro:
    def __init__(self,color,modelo, aceleração):
        self.color = color
        self.modelo = modelo
        self.aceleração = aceleração
        self.velocidade = 0
    def acelerar(self):
        self.velocidade = self.velocidade+self.aceleração
        print(f"O {self.modelo} está acelerando, velocidade atual é: {self.velocidade} Km/H")
    def freiar(self):
        print(f"O {self.modelo} esta freiando")
    def ligar_farois(self):
        self.ligar_farois = True
        print("Farois Ligados!")
    def desligar_farois(self):
        self.ligar_farois = False
        print("Farois Desligados!")



carro1 = Carro("vermelho","fusca", 10)
carro2 = Carro("azul","bmw", 50)
carro1.acelerar()
print(carro1.color)
print(id(carro1))