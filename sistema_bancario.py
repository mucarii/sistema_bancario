class Usuario:
    cpfs = set()

    def __init__(self, nome, data_nascimento, cpf, endereco):
        if cpf in Usuario.cpfs:
            raise ValueError("CPF ja registrado")
        Usuario.cpfs.add(cpf)

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def remover_conta(self, conta):
        self.contas.remove(conta)

class ContaBancaria:
    agencia_sequencial = 1

    def __init__(self, usuario):
        self.agencia = f"000{ContaBancaria.agencia_sequencial:04}"
        ContaBancaria.agencia_sequencial += 1
        self.numero_conta = f"{self.agencia}-{ContaBancaria.agencia_sequencial:07}"
        self.usuario = usuario
        self.saldo = 0
        self.movimentos = []

    def sacar(self, *, valor):
        if valor > self.saldo + self.limite_saque:
            print("Saldo insuficiente")
        elif self.numero_de_saques >= 3:
            print("Limite de saques diários atingido")
        else:
            self.saldo -= valor
            self.numero_de_saques += 1
            self.movimentos.append(f"Saque de R${valor:.2f}")

    def depositar(self, /, valor):
        self.saldo += valor
        self.movimentos.append(f"Deposito de R${valor:.2f}")

    def extrato(self, numero_conta, *, start_date=None, end_date=None):
        print("Extrato:")
        for movimento in self.movimentos:
            if start_date is None or end_date is None:
                print(movimento)
            elif start_date <= movimento.split(" ")[0] <= end_date:
                print(movimento)
        print(f"Seu saldo em {numero_conta} é R$ {self.saldo:.2f}")

usuarios = {}
contas = {}

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")

    usuario = Usuario(nome, senha)
    usuarios[nome] = usuario

def cadastrar_conta_bancaria():
    numero = input("Digite o número da conta bancária: ")
    saldo = float(input("Digite o saldo inicial da conta: "))
    limite_saque = float(input("Digite o limite de saque da conta: "))

    conta = ContaBancaria(numero, saldo, limite_saque, [])
    contas[numero] = conta

while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar usuário")
    print("2 - Cadastrar conta bancária")
    print("3 - Sacar")
    print("4 - Depositar")
    print("5 - Visualizar extrato")
    print("6 - Sair")

    opcao = int(input())

    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        cadastrar_conta_bancaria()
    elif opcao == 3:
        numero_conta = input("Digite o número da conta bancária: ")
        if numero_conta in contas:
            conta = contas[numero_conta]
            conta.sacar()
        else:
            print("Conta bancária não encontrada")
    elif opcao == 4:
        numero_conta = input("Digite o número da conta bancária: ")
        if numero_conta in contas:
            conta = contas[numero_conta]
            conta.depositar()
        else:
            print("Conta bancária não encontrada")
    elif opcao == 5:
        numero_conta = input("Digite o número da conta bancária: ")
        if numero_conta in contas:
            conta = contas[numero_conta]
            conta.extrato()
        else:
            print("Conta bancária não encontrada")
    elif opcao == 6:
        break