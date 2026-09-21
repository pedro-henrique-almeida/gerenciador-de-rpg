
import copy
import random



cenarios = []


def criar_cenario():

    participantes = []

    nome = input("Digite o nome do local: ")

    integrantes = ficha_player + criaturas

    while True:

        print("\n=== PARTICIPANTES ===")

        for numero, integrante in enumerate(integrantes, start=1):
            print("  [", numero, "] ", integrante["nome"], sep="")

        print("  [0] Encerrar")

        try:
            escolha = int(
                input("Escolha o número dos participantes (0 para encerrar): ")
            )
        except ValueError:
            print("Digite um número.")
            continue

        if escolha == 0:
            break

        try:
            integrante = integrantes[escolha - 1]
        except IndexError:
            print("Opção inválida.")
            continue

        if isinstance(integrante, npc):

            quantidade = 0

            for criatura in participantes:
                if isinstance(criatura, npc):
                    if criatura.tipo == integrante.tipo:
                        quantidade += 1

            nova_criatura = deepcopy(integrante)

            nova_criatura.nome = nova_criatura.tipo + str(quantidade + 1)

            participantes.append(nova_criatura)

            print(f"{nova_criatura.nome} adicionado ao combate.")

        else:

            participantes.append(integrante)

            print(f"{integrante['nome']} adicionado ao combate.")

    cenario = {
        "nome": nome,
        "participantes": participantes,
    }

    cenarios.append(cenario)


def exibir_cenarios():
    if not cenarios:
        print("Nenhum cenário criado.")
        return

    print("\n=== CENÁRIOS ===")
    for numero, cenario in enumerate(cenarios, start=1):
        print(f"{numero}. {cenario['nome']}")

        print("   Participantes:")

        for participante in cenario["participantes"]:

            print(f"     - {participante['nome']}")
    input("\nPressione ENTER para continuar...")


def escolher_cenario():
    if not cenarios:
        print("Nenhum cenário criado.")
        return None

    print("\n=== ESCOLHER CENÁRIO ===")

    for numero, cenario in enumerate(cenarios, start=1):
        print(f"{numero}. {cenario['nome']}")

    while True:
        try:
            escolha = int(input("Escolha o número do cenário (0 para cancelar): "))
        except ValueError:
            print("Digite um número.")
            continue

        if escolha == 0:
            return None

        try:
            cenario = cenarios[escolha - 1]
            return cenario
        except IndexError:
            print("Opção inválida.")