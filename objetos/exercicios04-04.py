# Exercicio 1
class Circulo: 
    def __init__(self,raio):
        self.raio = raio

    def area(self):
        area = ((self.raio ** 2)*3,14)
        return area
    def perimetro(self):
        perimetro = (2*3,14*self.raio)
        return perimetro
# Exercicio 2
class ContaBancaria:
    def __init__(self,numero_conta,nome,saldo=0.0):
        self.numero_conta = int(numero_conta)
        self.nome = nome
        self.saldo = float(saldo)
    def deposito(self,depositar):
        self.saldo += int(depositar)
        return self.saldo
    def sacar(self,sacar):
        self.saldo -= sacar
        return self.saldo

conta1 = ContaBancaria(22,"carlos",5)
print(conta1.deposito(5))

# Exercico 3
class Retangulo:
    def __init__(self,altura,largura):
        self.altura = int(altura)
        self.largura = int(largura)
    def area(self):
        area = (self.altura * self.largura)
        return area
    def perimetro(self):
        perimetro = ((self.altura*2)+(self.largura*2))
        return perimetro

# Exercicio 4
class Aluno:
    def __init__(self,nome,matricula,notas):
        self.nome = nome
        self.matricula = int(matricula)
        self.notas = float(notas)

    def media(self):
        total = (self.notas.value())
        quantidade = len(self.notas)
        media = (total/quantidade)
        return media
    def situação(self):
        media = self.media()
        if media >= 7:
            return "Aprovado!"
        else:
            return "Reprovado!" 

# Exercicio 5
class LojaVirtual:
    def __init__(self):
        self.produtos = {}  
        self.carrinho = []  

    def cadastrar_produto(self, nome, preco):
        self.produtos[nome] = preco

    def adicionar_ao_carrinho(self, nome_produto, quantidade=1):
        if nome_produto in self.produtos:
            for _ in range(quantidade):
                self.carrinho.append((nome_produto, self.produtos[nome_produto]))
        else:
            print(f"Produto '{nome_produto}' não encontrado.")

    def aplicar_desconto(self, percentual_desconto):
        for i, (nome_produto, preco) in enumerate(self.carrinho):
            desconto = preco * percentual_desconto / 100
            self.carrinho[i] = (nome_produto, preco - desconto)

    def calcular_total(self):
        return sum(preco for _, preco in self.carrinho)

loja = LojaVirtual()

loja.cadastrar_produto("Camisa", 50.0)
loja.cadastrar_produto("Calça", 80.0)
loja.cadastrar_produto("Tênis", 120.0)

loja.adicionar_ao_carrinho("Camisa")
loja.adicionar_ao_carrinho("Calça", quantidade=2)
loja.adicionar_ao_carrinho("Tênis")

loja.aplicar_desconto(10)

total_compra = loja.calcular_total()
print("Total da compra:", total_compra)

# Exercicio 6

class RedeSocial:
    def __init__(self):
        self.usuarios = {} 
        self.posts = {}  

    def adicionar_usuario(self, nome_usuario):
        if nome_usuario not in self.usuarios:
            self.usuarios[nome_usuario] = set()

    def adicionar_amigo(self, usuario, amigo):
        if usuario in self.usuarios and amigo in self.usuarios:
            self.usuarios[usuario].add(amigo)
            self.usuarios[amigo].add(usuario)
        else:
            print("Usuário ou amigo não encontrado.")

    def publicar_post(self, usuario, mensagem):
        if usuario in self.usuarios:
            if usuario not in self.posts:
                self.posts[usuario] = []
            self.posts[usuario].append(mensagem)
        else:
            print("Usuário não encontrado.")

    def comentar_post(self, usuario, autor_post, mensagem_comentario):
        if autor_post in self.posts and usuario in self.usuarios:
            comentario = f"{usuario}: {mensagem_comentario}"
            self.posts[autor_post].append(comentario)
        else:
            print("Autor do post ou usuário não encontrado.")

    def buscar_usuario(self, nome_usuario):
        if nome_usuario in self.usuarios:
            return nome_usuario
        else:
            print("Usuário não encontrado.")




        

        
    

        

        

        