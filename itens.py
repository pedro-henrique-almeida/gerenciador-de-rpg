# ========== ITENS ==========
espada = {
    "nome": "espada comum",
    "dano": 10,
    "descriçao": "uma espada de ferro comum, essencial em aventuras",
}

flecha_madeira = {
    "nome": "flecha de madeira",
    "quantidade": 10,
    "dano": 2,
    "descriçao": "uma flecha de madeira simples, usada com arcos",
}

arco_madeira = {
    "nome": "arco de madeira simples",
    "dano": 5,
    "flecha de madeira": 5,
    "descriçao": "um arco de madeira simples, adequado para ataques a longa distancia",
}

machado = {
    "nome": "machado de batalha",
    "dano": 12,
    "descriçao": "um machado de batalha pesado, ideal para combates corpo a corpo",
}

katana = {
    "nome": "katana afiada",
    "dano": 15,
    "descriçao": "uma katana afiada, perfeita para ataques rápidos e precisos",
}

lança = {
    "nome": "lança longa",
    "dano": 8,
    "descriçao": "uma lança longa, usada para ataques a longa distância",
}

corda = {
    "nome": "corda resistente",
    "dano": 0,
    "descriçao": "uma corda resistente, útil para escaladas e amarrações",
}

adaga = {
    "nome": "adaga pequena",
    "dano": 4,
    "descriçao": "uma adaga pequena, ideal para ataques furtivos",
}

besta = {
    "nome": "besta pesada",
    "dano": 12,
    "descriçao": "uma besta pesada, capaz de disparar projéteis com grande força",
}

maos = {
    "nome": "mãos",
    "dano": 6,
    "descriçao": "esmurra seus oponentes",
}

# Lista global de todos os itens disponíveis
itens = [
    espada,
    flecha_madeira,
    arco_madeira,
    machado,
    katana,
    lança,
    corda,
    adaga,
    besta,
    maos,
]

# ========== FUNÇÕES DE ITENS ==========


def novo_item():
    print("=== CRIE SEU ITEM ===")
    nome = input("escolha o nome: ")
    try:
        dano = int(input("escolha o dano: "))
    except ValueError:
        print("Dano deve ser um número. Usando 0.")
        dano = 0
    descriçao = input("escolha a descriçao: ")
    item_novo = {
        "nome": nome,
        "dano": dano,
        "descriçao": descriçao,
    }
    itens.append(item_novo)
    print("Item adicionado com sucesso!")


def listar_itens():
    print("== Lista de Itens ==")
    for numero, arma in enumerate(itens, start=1):
        print(numero, "-", arma["nome"])
    while True:
        try:
            escolha = int(input("Escolha um item (0 para sair): "))
        except ValueError:
            print("Digite um número.")
            continue
        if escolha == 0:
            break
        try:
            item = itens[escolha - 1]
        except IndexError:
            print("Opção inválida.")
            continue
        for chave, valor in item.items():
            print(chave, ":", valor)
        input("\nPressione ENTER para continuar...")


def remover_item():
    print("=== REMOVER ITEM ===")
    if not itens:
        print("Nenhum item para remover.")
        return
    for numero, arma in enumerate(itens, start=1):
        print(numero, "-", arma["nome"])
    print("0 - Cancelar")
    try:
        escolha = int(input("Número do item a remover: "))
    except ValueError:
        print("Digite um número.")
        return
    if escolha == 0:
        print("Operação cancelada.")
        return
    try:
        item = itens[escolha - 1]
    except IndexError:
        print("Opção inválida.")
        return
    nome = item["nome"]
    confirm = input(f"Remover '{nome}'? (s/N): ")
    if confirm.lower() == "s":
        itens.pop(escolha - 1)
        print("Item removido.")
    else:
        print("Remoção cancelada.")
