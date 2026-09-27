from copy import deepcopy
import combates
import players
import npcs

personagens = players.ficha_player + npcs.criaturas
inimigos = npcs.criaturas


floresta = {
    "nome": "Floresta",
    "participantes": [
        npcs.criaturas[0],
        npcs.criaturas[1],
        npcs.criaturas[2],
    ],
}


cenarios = [floresta]


def criar_cenario():

    participantes = []

    nome = input("Digite o nome do local: ")

    integrantes = personagens
    monstros = inimigos

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

        if integrante in personagens:

            quantidade = 0

            for criatura in participantes:
                if criatura in inimigos:
                    if criatura.tipo == inimigos.tipo:
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



def iniciar_combate():
    if not cenarios:
        print("Nenhum cenário criado.")
        return

    while True:
        print("\n=== CENÁRIOS ===")

        for numero, cenario in enumerate(cenarios, start=1):
            print(f"{numero}. {cenario['nome']}")

        print("0. Voltar")

        try:
            escolha = int(input("Escolha um cenário: "))
        except ValueError:
            print("Digite um número.")
            continue

        if escolha == 0:
            return

        if escolha < 1 or escolha > len(cenarios):
            print("Opção inválida.")
            continue

        cenario = cenarios[escolha - 1]

        while True:
            print("\n" + "=" * 50)
            print(f"CENÁRIO: {cenario['nome'].upper()}")
            print("=" * 50)

            print("\nParticipantes:")
            for participante in cenario["participantes"]:
                print(f"- {participante.nome}")

            print("\n[1] Iniciar combate")
            print("[0] Sair do cenário")

            try:
                opcao = int(input("Escolha: "))
            except ValueError:
                print("Digite um número.")
                continue

            if opcao == 0:
                break

            if opcao == 1:
                combates.combate_com_alvo(cenario["participantes"])

            else:
                print("Opção inválida.")





def menu_cenarios():

    while True:

        print("\n=== MENU CENÁRIOS ===")

        print("\n" + "=" * 50)
        print("MENU PRINCIPAL")
        print("=" * 50)

        for numero, opcao in enumerate(menus_de_combate_com_cenarios, start=1):
            print(
                "  [", numero, "] ",
                opcao.__name__.replace("_", " ").capitalize(),
                sep=""
            )

        print("  [0] Sair")

        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Digite um numero.")
            continue

        if escolha == 0:
            print("Saindo do sistema...")
            break

        try:
            menus_de_combate_com_cenarios[escolha - 1]()
        except IndexError:
            print("Opção inválida.")


menus_de_combate_com_cenarios = [
    criar_cenario,
    exibir_cenarios,
    escolher_cenario,
    iniciar_combate,]