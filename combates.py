import random
import copy


def ataque(atacante, alvo):
    rolagem = dado(20)
    bonus_agilidade = atacante["atributos"]["agilidade"]
    teste = rolagem + bonus_agilidade

    print("\n" + "=" * 50)
    print(atacante["nome"].upper(), "ATACA", alvo["nome"].upper())
    print("=" * 50)
    print("\n--- ROLAGEM DE ATAQUE ---")
    print("D20:", rolagem)
    print("Bonus de Agilidade: +", bonus_agilidade)
    print("Total do teste:", teste)

    while True:
        print("\n" + "-" * 40)
        print("O MESTRE DECIDE:")
        print("   [S] - Acertou")
        print("   [N] - Errou")
        print("   [0] - Encerrar combate (Hit Kill)")
        decisao = input("Sua decisao: ").strip().upper()

        if decisao == "S":
            dano_arma = atacante["arma"]["dano"]
            dano_força = atacante["atributos"]["força"]
            dano_total = dano_arma + dano_força

            if isinstance(alvo, npc):
                vida_atual = alvo.vida
            else:
                vida_atual = alvo["vida"]

            vida_restante = vida_atual - dano_total

            print("\n" + "=" * 50)
            print(atacante["nome"], "ACERTOU", alvo["nome"], "!")
            print("=" * 50)
            print("\n--- CALCULO DO DANO ---")
            print("Dano da arma (", atacante["arma"]["nome"], "):", dano_arma)
            print("Bonus de Forca: +", dano_força)
            print("Dano total:", dano_total)

            if vida_restante <= 0:
                print("\n" + "=" * 50)
                print(alvo["nome"].upper(), "FOI ELIMINADO!")
                print("=" * 50)

                if isinstance(alvo, npc):
                    alvo.vida = alvo.vida_maxima
                else:
                    alvo["vida"] = alvo["vida_maxima"]

                return True

            else:
                if isinstance(alvo, npc):
                    alvo.vida = vida_restante
                else:
                    alvo["vida"] = vida_restante

                print("\n--- VIDA RESTANTE ---")
                print(alvo["nome"], "agora tem", vida_restante, "de vida")
                return False

        elif decisao == "N":
            print("\n" + "=" * 40)
            print(atacante["nome"], "ERROU o ataque!")
            print("=" * 40)
            return False

        elif decisao == "0":
            print("\n" + "=" * 50)
            print("HIT KILL! COMBATE ENCERRADO PELO MESTRE")
            print("=" * 50)

            if isinstance(alvo, npc):
                alvo.vida = alvo.vida_maxima
                print("Vida do alvo restaurada para", alvo.vida_maxima)
            else:
                alvo["vida"] = alvo["vida_maxima"]
                print("Vida do alvo restaurada para", alvo["vida_maxima"])

            return True

        else:
            print("Resposta invalida. Digite S, N ou 0.")


def menu_combate_cenarios():

    print("\n" + "=" * 50)
    print("MENU DE COMBATE")
    print("=" * 50)

    for numero, opcao in enumerate(menus_de_combate_com_cenarios, start=1):
        print(
            "  [", numero, "] ", opcao.__name__.replace("_", " ").capitalize(), sep=""
        )

    while True:

        try:
            escolha = int(input("Escolha uma opção (0 para voltar): "))
        except ValueError:
            print("Digite um número.")
            continue

        if escolha == 0:
            break

        try:
            combate_atual = menus_de_combate_com_cenarios[escolha - 1]()
        except IndexError:
            print("Opção inválida.")
            continue

        if combate_atual:
            participantes = combate_atual["participantes"]
            combate_com_alvo(participantes)


def combate_com_alvo(participantes=ficha_player + criaturas):

    print("\n" + "=" * 50)
    print("INICIANDO COMBATE")
    print("=" * 50)

    print("\n--- ESCOLHA O ATACANTE ---")
    for numero, jogador in enumerate(participantes, start=1):
        print("  [", numero, "] ", jogador["nome"], sep="")

    try:
        escolha_atacante = int(input("Numero do atacante: "))
    except ValueError:
        print("Digite um numero.")
        return

    try:
        atacante = participantes[escolha_atacante - 1]
    except IndexError:
        print("Opcao invalida.")
        return

    print("\n--- ESCOLHA O ALVO ---")
    for numero, criatura in enumerate(participantes, start=1):
        print(
            "  [",
            numero,
            "] ",
            criatura["nome"],
            " (Vida: ",
            criatura["vida"],
            ")",
            sep="",
        )

    try:
        escolha_alvo = int(input("Numero do alvo: "))
    except ValueError:
        print("Digite um numero.")
        return

    try:
        alvo = participantes[escolha_alvo - 1]
    except IndexError:
        print("Opcao invalida.")
        return

    while True:

        print("\n" + "-" * 40)
        print("VIDA ATUAL DO ALVO:", alvo["nome"], "=", alvo["vida"])
        print("-" * 40)

        combate_terminou = ataque(atacante, alvo)

        if combate_terminou:
            print("\n" + "=" * 50)
            print("COMBATE ENCERRADO")
            print("=" * 50)
            input("\nPressione ENTER para voltar ao menu...")
            break

        print("\n" + "-" * 40)
        print("NOVO ATAQUE")
        print("-" * 40)

        print("--- ESCOLHA O ATACANTE ---")

        for numero, jogador in enumerate(participantes, start=1):
            print("  [", numero, "] ", jogador["nome"], sep="")

        print("  [0] Encerrar combate")

        try:
            escolha = int(input("Numero do atacante (0 para encerrar): "))
        except ValueError:
            print("Digite um numero.")
            continue

        if escolha == 0:

            print("\n" + "=" * 40)
            print("Combate encerrado pelo mestre.")
            print("=" * 40)

            if isinstance(alvo, npc):
                alvo.vida = alvo.vida_maxima
            else:
                alvo["vida"] = alvo["vida_maxima"]

            print("Vida do alvo restaurada para", alvo["vida_maxima"])

            input("\nPressione ENTER para voltar ao menu...")
            break

        try:
            atacante = participantes[escolha - 1]
        except IndexError:
            print("Opcao invalida. Tente novamente.")
            continue


def combate_livre():
    print("\n" + "=" * 40)
    print("COMBATE LIVRE")
    print("=" * 40)
    print("\n--- ESCOLHA O ATACANTE ---")
    for numero, jogador in enumerate(ficha_player, start=1):
        print("  [", numero, "] ", jogador["nome"], sep="")

    try:
        escolha = int(input("Numero do atacante: "))
    except ValueError:
        print("Digite um numero.")
        return

    try:
        atacante = ficha_player[escolha - 1]
    except IndexError:
        print("Opcao invalida.")
        return

    rolagem = dado(20)
    bonus_agilidade = atacante["atributos"]["agilidade"]
    teste = rolagem + bonus_agilidade
    dano_arma = atacante["arma"]["dano"]
    dano_força = atacante["atributos"]["força"]
    dano_total = dano_arma + dano_força

    print("\n" + "=" * 40)
    print(atacante["nome"].upper(), "ATACA!")
    print("=" * 40)
    print("\n--- ROLAGEM DE ATAQUE ---")
    print("D20:", rolagem)

    print("Bonus de Agilidade: +", bonus_agilidade)
    print("Total do teste:", teste)
    print("\n--- DANO POTENCIAL ---")
    print("Dano da arma (", atacante["arma"]["nome"], "):", dano_arma)
    print("Bonus de Forca: +", dano_força)
    print("Dano total:", dano_total)
    input("\nPressione ENTER para continuar...")


def rolagem_livre():
    print("\n" + "=" * 40)
    print("ROLAGEM LIVRE")
    print("=" * 40)
    print("\n--- ESCOLHA O PLAYER ---")
    for numero, jogador in enumerate(ficha_player, start=1):
        print("  [", numero, "] ", jogador["nome"], sep="")

    try:
        escolha = int(input("Numero do player: "))
    except ValueError:
        print("Digite um numero.")
        return

    try:
        jogador = ficha_player[escolha - 1]
    except IndexError:
        print("Opcao invalida.")
        return

    print("\n--- ATRIBUTOS DISPONIVEIS ---")
    lista_atributos = ["força", "agilidade", "inteligencia", "carisma"]
    for i, atributo in enumerate(lista_atributos, start=1):
        print(
            "  [",
            i,
            "] ",
            atributo.capitalize(),
            " (valor: ",
            jogador["atributos"][atributo],
            ")",
            sep="",
        )
    print("  [0] Cancelar")

    try:
        escolha_attr = int(input("Escolha o atributo: "))
    except ValueError:
        print("Digite um numero.")
        return

    if escolha_attr == 0:
        return

    try:
        atributo_escolhido = lista_atributos[escolha_attr - 1]
    except IndexError:
        print("Opcao invalida.")
        return

    valor_atributo = jogador["atributos"][atributo_escolhido]
    rolagem = dado(20)
    resultado = rolagem + valor_atributo

    print("\n" + "=" * 40)
    print("TESTE DE", atributo_escolhido.upper())
    print("=" * 40)
    print("D20:", rolagem)
    print("Bonus: +", valor_atributo)
    print("Resultado:", resultado)
    input("\nPressione ENTER para continuar...")