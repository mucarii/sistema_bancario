class Usuario:
    cpfs = set()

    def __init__(self, nome, data_nascimento, cpf, endereco):
        if cpf in Usuario.cpfs:
            raise ValueError("CPF já registrado")
        Usuario.cpfs.add(cpf)

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class ContaBancaria:
    agencia_sequencial = 0

    def __init__(self, usuario):
        self.agencia = f"000{ContaBancaria.agencia_sequencial:04}"
        ContaBancaria.agencia_sequencial += 1
        self.numero_conta = f"{self.agencia}-{ContaBancaria.agencia_sequencial:07}"
        self.usuario = usuario
        self.saldo = 0
        self.movimentos = []

    def depositar(self, valor):
        self.saldo += valor
        self.movimentos.append(("Depósito", valor))

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        self.movimentos.append(("Saque", -valor))

    def ver_extrato(self):
        print(f"Extrato da conta {self.numero_conta}:")
        for movimento, valor in self.movimentos:
            print(f"{movimento}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


usuarios = {}


def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (formato: DD/MM/AAAA): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário: ")

    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios[nome] = usuario
    print("Usuário cadastrado com sucesso!\n\n")


def cadastrar_conta_bancaria():
    nome = input("Digite o nome do usuário: ")
    if nome not in usuarios:
        print("Usuário não encontrado")
        return

    usuario = usuarios[nome]
    saldo = float(input("Digite o saldo inicial da conta: "))
    limite_saque = float(input("Digite o limite de saque da conta: "))

    conta = ContaBancaria(usuario)
    conta.depositar(saldo)
    usuario.conta_bancaria = conta
    print("Conta bancária cadastrada com sucesso!")


def sacar():
    nome = input("Digite o nome do usuário: ")
    if nome not in usuarios:
        print("Usuário não encontrado")
        return

    usuario = usuarios[nome]
    if not hasattr(usuario, "conta_bancaria"):
        print("Conta bancária não encontrada")
        return

    valor = float(input("Digite o valor a ser sacado: "))
    usuario.conta_bancaria.sacar(valor)
    print("Saque realizado com sucesso!")


def depositar():
    nome = input(" Digite o nome do usuário: ")
    if nome not in usuarios:
        print("Usuário não encontrado")
        return

    usuario = usuarios[nome]
    if not hasattr(usuario, "conta_bancaria"):
        print("Conta bancária não encontrada")
        return

    try:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor <= 0:
            raise ValueError("Valor inválido")
        usuario.conta_bancaria.depositar(valor)
        print("Depósito realizado com sucesso!")
    except ValueError:
        print("Valor inválido. Por favor, digite um valor positivo.")

def ver_extrato():
    nome = input(" Digite o nome do usuário: ")
    if nome not in usuarios:
        print("Usuário não encontrado")
        return

    usuario = usuarios[nome]
    if not hasattr(usuario, "conta_bancaria"):
        print("Conta bancária não encontrada")
        return

    usuario.conta_bancaria.ver_extrato()


def menu():
    while True:
        print("\n\nBem-vindo ao sistema de gerenciamento de contas bancárias!\n\n")
        print("1 - Cadastrar usuário")
        print("2 - Cadastrar conta bancária")
        print("3 - Sacar")
        print("4 - Ver extrato")
        print("5 - Depositar")
        print("6 - Sair")

        choice = input("\nDigite a opção desejada: \n")

        if choice == "1":
            cadastrar_usuario()
        elif choice == "2":
            cadastrar_conta_bancaria()
        elif choice == "3":
            sacar()
        elif choice == "4":
            ver_extrato()
        elif choice == "5":
            depositar()
        elif choice == "6":
            break


if __name__ == "__main__":
    menu()