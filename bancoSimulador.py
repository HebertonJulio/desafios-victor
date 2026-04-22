import random


print("Bem vindo ao Banco Noovi")

saldoConta = round(random.uniform(0, 4999), 2)
cpfUsuario = ""

def validarCPF():
    repeticoes = 0

    while True:
        cpf = input("Informe seu CPF: ")

        if len(cpf) == 11 and cpf.isdigit():
            return cpf
        else:
            print("CPF inválido")
            repeticoes += 1

            if repeticoes >= 3:
                exit()


def visualizarSaldo(cpfUsuario, saldoConta):
    print(f"\nCPF: {cpfUsuario}")
    print(f"Saldo: R${saldoConta}")


def adicionarSaldo(cpfUsuario, saldoConta):
    valor = float(input("Quanto deseja adicionar?: "))
    saldoConta += valor
    print(f"Novo saldo: R${saldoConta}")
    return saldoConta


def transferirSaldo(saldoConta):
    valor = float(input("Quanto deseja transferir?: R$"))

    if valor > saldoConta:
        print("Saldo insuficiente.")
        return saldoConta

    saldoConta -= valor

    print("Transferência realizada.")
    print(f"Saldo atual: R${saldoConta:.2f}")

    return saldoConta


def menu():
    global saldoConta

    while True:
        opcao = int(input(
            "\n1 Ver saldo"
            "\n2 Adicionar saldo"
            "\n3 Transferir"
            "\n4 Sair\n"
        ))

        match opcao:
            case 1:
                visualizarSaldo(cpfUsuario, saldoConta)

            case 2:
                saldoConta = adicionarSaldo(cpfUsuario, saldoConta)

            case 3:
                saldoConta = transferirSaldo(saldoConta)

            case 4:
                exit()

cpfUsuario = validarCPF()
menu()


