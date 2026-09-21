
#imports 


import itens



# ========== PLAYERS ==========



kai = {
    "nome": "Kai",
    "nivel": 1,
    "vida": 80,
    "mana": 10,
    "classe": "Guerreiro",
    "arma": itens.espada,
    "inventario": [itens.machado, itens.lança, itens.maos],
    "atributos": {
        "força": 4,
        "agilidade": 2,
        "inteligencia": 4,
        "carisma": 1,
    },
}

any = {
    "nome": "any",
    "nivel": 1,
    "vida": 50,
    "mana": 50,
    "arma": itens.arco_madeira,
    "classe": "arqueira",
    "inventario": [itens.flecha_madeira, itens.besta, itens.maos],
    "atributos": {
        "força": 2,
        "agilidade": 4,
        "inteligencia": 3,
        "carisma": 2,
    },
}

lee = {
    "nome": "lee",
    "nivel": 1,
    "vida": 40,
    "mana": 20,
    "arma": itens.katana,
    "classe": "espadachim",
    "inventario": [itens.adaga, itens.corda, itens.maos],
    "atributos": {
        "força": 3,
        "agilidade": 4,
        "inteligencia": 2,
        "carisma": 1,
    },
}

ficha_player = [kai, any, lee]

# ========== FUNÇÕES DE PLAYERS ==========


def novo_jogador():
    print("=== CRIE SEU PERSONAGEM ===")
    nome = input("informe o nome: ")
    try:
        vida = int(input("informe a vida: "))
    except ValueError:
        print("Vida deve ser número. tente novamente")
        vida = int(input("informe a vida: "))
    try:
        mana = int(input("informe a mana: "))
    except ValueError:
        print("Mana deve ser número. tente novamente")
        mana = int(input("informe a mana: "))
    classe = input("informe a classe: ")

    print("== Lista de Itens ==")
    for numero, arma in enumerate(itens.itens, start=1):
        print(numero, "-", arma["nome"])

    while True:
        try:
            escolha = int(input("Escolha o número da arma inicial: "))
        except ValueError:
            print("Digite um número.")
            continue
        try:
            arma = itens.itens[escolha - 1]
            break
        except IndexError:
            print("Opção inválida.")

    print("==== ESCOLHA SEUS ATRIBUTOS ====")
    atributos = int(input("Informe a quantidade de pontos para distribuir"))


    pontos =  atributos

    while True:
        try:
            força = int(input("Informe sua força: "))
        except ValueError:
            print("Digite um número.")
            continue
        if força <= pontos:
            pontos -= força
            break
        print("Você não possui essa quantidade de pontos.")
    print("Pontos restantes:", pontos)

    while True:
        try:
            agilidade = int(input("Informe sua agilidade: "))
        except ValueError:
            print("Digite um número.")
            continue
        if agilidade <= pontos:
            pontos -= agilidade
            break
        print("Você não possui essa quantidade de pontos.")
    print("Pontos restantes:", pontos)

    while True:
        try:
            inteligencia = int(input("Informe sua inteligência: "))
        except ValueError:
            print("Digite um número.")
            continue
        if inteligencia <= pontos:
            pontos -= inteligencia
            break
        print("Você não possui essa quantidade de pontos.")
    print("Pontos restantes:", pontos)

    while True:
        try:
            carisma = int(input("Informe seu carisma: "))
        except ValueError:
            print("Digite um número.")
            continue
        if carisma <= pontos:
            pontos -= carisma
            break
        print("Você não possui essa quantidade de pontos.")
    print("Pontos restantes:", pontos)

    atributos = {
        "força": força,
        "agilidade": agilidade,
        "inteligencia": inteligencia,
        "carisma": carisma,
    }

    novo_player = {
        "nome": nome,
        "vida": vida,
        "mana": mana,
        "classe": classe,
        "arma": arma,
        "inventario": [arma],  # começa com a arma escolhida
        "atributos": atributos,
    }
    ficha_player.append(novo_player)
    print("Personagem criado com sucesso!")


def remover_jogador():
    print("=== REMOVER PLAYER ===")
    if not ficha_player:
        print("Nenhum player para remover.")
        return
    for numero, jogador in enumerate(ficha_player, start=1):
        print(numero, "-", jogador["nome"])
    print("0 - Cancelar")
    try:
        escolha = int(input("Número do player a remover: "))
    except ValueError:
        print("Digite um número.")
        return
    if escolha == 0:
        print("Operação cancelada.")
        return
    try:
        jogador = ficha_player[escolha - 1]
    except IndexError:
        print("Opção inválida.")
        return
    nome = jogador["nome"]
    confirm = input(f"Remover '{nome}'? (s/N): ")
    if confirm.lower() == "s":
        ficha_player.pop(escolha - 1)
        print("Player removido.")
    else:
        print("Remoção cancelada.")


# ========== GERENCIAMENTO DE INVENTÁRIO ==========


def equipar_arma(jogador):
    """Troca a arma equipada do jogador por uma do inventário."""
    print("\n=== EQUIPAR ARMA ===")
    print("Arma atual:", jogador["arma"]["nome"])
    if not jogador["inventario"]:
        print("Inventário vazio. Não é possível equipar nada.")
        return
    print("Itens no inventário:")
    for numero, item in enumerate(jogador["inventario"], start=1):
        print(numero, "-", item["nome"], "(dano:", item["dano"], ")")
    print("0 - Cancelar")
    try:
        escolha = int(input("Escolha o número do item para equipar: "))
    except ValueError:
        print("Digite um número.")
        return
    if escolha == 0:
        return
    try:
        nova_arma = jogador["inventario"][escolha - 1]
    except IndexError:
        print("Opção inválida.")
        return
    # Se a arma atual não estiver no inventário, adiciona
    if jogador["arma"] not in jogador["inventario"]:
        jogador["inventario"].append(jogador["arma"])
    # Remove a nova arma do inventário
    jogador["inventario"].pop(escolha - 1)
    # Equipa a nova arma
    jogador["arma"] = nova_arma
    print(f"{jogador['nome']} agora está equipado com {nova_arma['nome']}.")


def adicionar_item_ao_inventario(jogador):
    """Adiciona um item da lista global ao inventário do jogador."""
    print("\n=== ADICIONAR ITEM AO INVENTÁRIO ===")
    print("Itens disponíveis:")
    for numero, item in enumerate(itens, start=1):
        print(numero, "-", item["nome"], "(dano:", item["dano"], ")")
    print("0 - Cancelar")
    try:
        escolha = int(input("Escolha o número do item: "))
    except ValueError:
        print("Digite um número.")
        return
    if escolha == 0:
        return
    try:
        item = itens[escolha - 1]
    except IndexError:
        print("Opção inválida.")
        return
    # Verifica se o item já está no inventário (opcional)
    if item in jogador["inventario"]:
        print("Este item já está no inventário.")
        return
    jogador["inventario"].append(item)
    print(f"{item['nome']} adicionado ao inventário de {jogador['nome']}.")


def remover_item_do_inventario(jogador):
    """Remove um item do inventário do jogador."""
    print("\n=== REMOVER ITEM DO INVENTÁRIO ===")
    if not jogador["inventario"]:
        print("Inventário vazio.")
        return
    print("Itens no inventário:")
    for numero, item in enumerate(jogador["inventario"], start=1):
        print(numero, "-", item["nome"], "(dano:", item["dano"], ")")
    print("0 - Cancelar")
    try:
        escolha = int(input("Escolha o número do item a remover: "))
    except ValueError:
        print("Digite um número.")
        return
    if escolha == 0:
        return
    try:
        item = jogador["inventario"][escolha - 1]
    except IndexError:
        print("Opção inválida.")
        return
    # Não permite remover a arma equipada
    if item is jogador["arma"]:
        print("Não é possível remover a arma equipada. Equipe outra arma primeiro.")
        return
    jogador["inventario"].pop(escolha - 1)
    print(f"{item['nome']} removido do inventário.")


# ========== EXIBIÇÃO DETALHADA DO PLAYER ==========


def exibir_player_completo(jogador):
    """Mostra todas as informações do jogador e oferece opções de gerenciamento."""
    while True:
        print("\n" + "=" * 50)
        print("PLAYER:", jogador["nome"])
        print("=" * 50)
        print("Nível:", jogador["nivel"])
        print("Vida:", jogador["vida"])
        print("Mana:", jogador["mana"])
        print("Classe:", jogador["classe"])
        print(
            "Arma equipada:",
            jogador["arma"]["nome"],
            "(dano:",
            jogador["arma"]["dano"],
            ")",
        )
        print("\nATRIBUTOS:")
        for attr, val in jogador["atributos"].items():
            print("  ", attr.capitalize(), ":", val)
        print("\nINVENTÁRIO:")
        if jogador["inventario"]:
            for i, item in enumerate(jogador["inventario"], start=1):
                print("  ", i, "-", item["nome"], "(dano:", item["dano"], ")")
        else:
            print("  (vazio)")
        print("\n--- OPÇÕES ---")
        print("1 - Equipar arma")
        print("2 - Adicionar item ao inventário")
        print("3 - Remover item do inventário")
        print("4 - Recuperar vida")
        print("0 - Voltar")

        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Digite um número.")
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            equipar_arma(jogador)
        elif escolha == 2:
            adicionar_item_ao_inventario(jogador)
        elif escolha == 3:
            remover_item_do_inventario(jogador)

        elif escolha == 4:
            recuperar_vida(jogador)
        else:
            print("Opção inválida.")
        input("\nPressione ENTER para continuar...")

        def recuperar_vida(jogador):

            print("\n=== RECUPERAR VIDA ===")
            vida = int(input("Informe a quantidade de vida a recuperar: "))

            jogador["vida"] += vida
            print(f"{jogador['nome']} recuperou {vida} de vida.")
            print(f"\nVida atual: {jogador['vida']}")


# ========== LISTAGEM DE PLAYERS ==========


def listar_players():
    """Mostra a lista de players e permite selecionar um para gerenciar."""
    while True:
        print("\n=== LISTA DE PLAYERS ===")
        for numero, jogador in enumerate(ficha_player, start=1):
            print(numero, "-", jogador["nome"], "(classe:", jogador["classe"], ")")
        print("0 - Voltar")
        try:
            escolha = int(
                input("Escolha um player para gerenciar (ou 0 para voltar): ")
            )
        except ValueError:
            print("Digite um número.")
            continue
        if escolha == 0:
            break
        try:
            jogador = ficha_player[escolha - 1]
        except IndexError:
            print("Opção inválida.")
            continue
        exibir_player_completo(jogador)

novo_jogador()