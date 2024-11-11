
class Loja:

    def __init__(self, localização, unidade):
        self.localização = localização
        self.unidade = unidade
        self.funcionarios = {
            'Atendente' : [],
            'Gerente' : [],
            'Caixa' : [],
            'Faxineiro' : []
                             }
        
        self.estoque = {
            'Guitarra' : [],
            'Baixo' : [],
            'Violão' : []
        }
    
    def __str__(self):
        return f"Unidade {self.unidade} de {self.localização}"
    
    def adicionar_instrumento(self, instrumento):
        if not instrumento in self.estoque[instrumento.tipo]:
            self.estoque[instrumento.tipo].append(instrumento)
            instrumento.loja = self
        else:
            print(f"O instrumento do tipo: {instrumento.tipo}, da marca: {instrumento.marca}, e modelo : {instrumento.modelo}, já está no estoque")
    
    def remover_instrumento(self, instrumento):
        if instrumento in self.estoque[instrumento.tipo]:
            self.estoque[instrumento.tipo].remove(instrumento)
            instrumento = None
        else:
            print(f"O instrumento do tipo: {instrumento.tipo}, da marca: {instrumento.marca}, e modelo : {instrumento.modelo}, não está no estoque")

    def contratar_funcionario(self, funcionario):
        if not funcionario in self.funcionarios[funcionario.cargo]:
            self.funcionarios[funcionario.cargo].append(funcionario)
            funcionario.loja = self
        else:
            print(f"O funcionário de nome: {funcionario.nome}, cujo cpf é: {funcionario.cpf}, e com o cargo de: {funcionario.cargo}, já está na Loja")
    
    def demitir_funcionario(self, funcionario):
        if funcionario in self.funcionarios[funcionario.cargo]:
            self.funcionarios[funcionario.cargo].remove(funcionario)
            funcionario.loja = None
        else:
            print(f"O funcionário de nome: {funcionario.nome}, cujo cpf é: {funcionario.cpf}, e com o cargo de: {funcionario.cargo}, não está na Loja")

    def remanejar_funcionario(self, funcionario, loja):
        if funcionario in self.funcionarios[funcionario.cargo]:
            self.funcionarios[funcionario.cargo].remove(funcionario)
            loja.funcionarios[funcionario.cargo].append(funcionario)
            funcionario.loja = loja
        else:
            print(f"O funcionário de nome: {funcionario.nome}, cujo cpf é: {funcionario.cpf}, e com o cargo de: {funcionario.cargo}, não está na Loja")
    
    def funcionarios_por_cargo(self):
        self.funcionarios_por_cargo = {}

        for cargo, lista_funcionarios in self.funcionarios.items():
            self.funcionarios_por_cargo[cargo] = len(lista_funcionarios)
        print(self.funcionarios_por_cargo)
    
    def consultar_estoque(self):
        print(f"Guitarras na loja: {len(self.estoque['Guitarra'])}", 
              f"Violões na loja: {len(self.estoque['Violão'])}",
              f"Baixos na loja: {len(self.estoque['Baixo'])}")
        
class Instrumento:

    def __init__(self, tipo, marca, modelo, preço, numero_cordas):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.preço = preço
        self.numero_cordas = numero_cordas
        self.loja = None

    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo}"

class Funcionarios:
    def __init__(self, nome, cpf, salario, cargo):
        self.nome =  nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
        self.loja = None
        
    def __str__(self):
        return f"{self.nome} - {self.cargo}"

loja1 = Loja('Belo Horizonte', 1)
instrumento1 = Instrumento("Guitarra", "Tagima", "TG-520",1400, 6)
funcionario1 = Funcionarios("Gabriel", "123456789", 5000, "Gerente")

loja1.adicionar_instrumento(instrumento1)
print(instrumento1.loja)

loja1.contratar_funcionario(funcionario1)
print(funcionario1.loja)

print(instrumento1)
loja1.funcionarios_por_cargo()

loja1.consultar_estoque()
