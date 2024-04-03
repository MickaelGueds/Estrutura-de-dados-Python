class Pessoas:
    pass
class Pessoas:
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def nome_completo(self,Nome_completo):
        self.Nome_completo = Nome_completo
        print(self.nome_completo)
    def trocar_sobrenome(self,novo_sobrenome):
        self.sobrenome = novo_sobrenome
        print(f"Seu novo sobrenome é {self.sobrenome}")
    def fazer_aniversario(self,data_aniversario):
        self.aniversario = data_aniversario
        print(f"seu novo aniversario é {self.aniversario}")

pessoa1 = Pessoas("João","Carlos",20)
pessoa1.fazer_aniversario("25 novembro de 1981")

        