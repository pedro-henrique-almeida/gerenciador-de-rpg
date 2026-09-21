class npc:
    def __init__(self, nome, vida, mana, classe, arma, inventario, atributos):
        self.nome = nome
        self.tipo = nome
        self.vida = vida
        self.vida_maxima = vida
        self.mana = mana
        self.classe = classe
        self.arma = arma
        self.inventario = inventario
        self.atributos = atributos

    def __getitem__(self, chave):
        return getattr(self, chave)


orc = npc(
    "Orc",
    50,
    10,
    "Guerreiro",
    {"nome": "Machado", "dano": 15},
    [{"nome": "Machado", "dano": 15}],
    {"força": 15, "agilidade": 6, "inteligencia": 3, "carisma": 2},
)

goblin = npc(
    "Goblin",
    30,
    20,
    "Ladino",
    {"nome": "Adaga", "dano": 8},
    [{"nome": "Adaga", "dano": 8}],
    {"força": 5, "agilidade": 14, "inteligencia": 7, "carisma": 4},
)

cavaleiro = npc(
    "Cavaleiro",
    80,
    5,
    "Paladino",
    {"nome": "Espada", "dano": 12},
    [{"nome": "Espada", "dano": 12}, {"nome": "Escudo", "defesa": 10}],
    {"força": 14, "agilidade": 7, "inteligencia": 8, "carisma": 12},
)

mago = npc(
    "Mago",
    35,
    60,
    "Mago",
    {"nome": "Cajado", "dano": 10},
    [{"nome": "Cajado", "dano": 10}, {"nome": "Poção", "cura": 20}],
    {"força": 3, "agilidade": 6, "inteligencia": 18, "carisma": 10},
)


criaturas = [orc, goblin, cavaleiro, mago]


def monstros():
    while True:
        print("==== MONSTROS ====")

        for i, criatura in enumerate(criaturas, start=1):
            print(f"{i}. {criatura.nome}")

        print("0. Voltar")

        try:
            escolha = int(input("Escolha o monstro: "))
        except ValueError:
            print("Digite um número.")
            continue

        if escolha == 0:
            break

        try:
            mob = criaturas[escolha - 1]
        except IndexError:
            print("Opção inválida.")
            continue

        print(f"\n=== {mob.nome.upper()} ===")

        for chave, valor in mob.__dict__.items():

            if chave == "arma":
                print("Arma:", valor["nome"])

            elif chave == "inventario":
                print("Inventário:", end=" ")

                for item in valor:
                    print(item["nome"], end=", ")

                print()

            elif chave == "atributos":
                print("Atributos:")

                for atributo, valor_atributo in valor.items():
                    print(f"  {atributo.capitalize()}: {valor_atributo}")

            else:
                print(f"{chave.capitalize()}: {valor}")

        input("\nPressione ENTER para continuar...")


# CRIAR NPC NO GERAL


def novo_npc():
    print("=== CRIE SEU NPC ===")
    nome = input("informe o nome: ")
    try:
        vida = int(input("informe a vida: "))
    except ValueError:
        print("Vida deve ser número. Usando 50.")
        vida = 50
    try:
        mana = int(input("informe a mana: "))
    except ValueError:
        print("Mana deve ser número. Usando 10.")
        mana = 10
    classe = input("informe a classe: ")

    print("== Lista de Itens ==")
    for numero, arma in enumerate(itens, start=1):
        print(numero, "-", arma["nome"])

    while True:
        try:
            escolha = int(input("Escolha o número da arma inicial: "))
        except ValueError:
            print("Digite um número.")
            continue
        try:
            arma = itens[escolha - 1]
            break
        except IndexError:
            print("Opção inválida.")

    print("==== ESCOLHA SEUS ATRIBUTOS ====")
    pontos = int(input("Informe a quantidade de pontos para distribuir: "))

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

    npc_novo = npc(nome, vida, mana, classe, arma, [arma], atributos)

    criaturas.append(npc_novo)
    print("npc criado com sucesso!")


def selecionar_npc(participantes):

    print("\nEscolha a criatura:")

    for numero, criatura in enumerate(criaturas, start=1):
        print(numero, "-", criatura.nome)

    escolha = int(input("Escolha: "))

    classe_escolhida = criaturas[escolha - 1]

    quantidade = 0

    for criatura in participantes:
        if criatura.tipo == classe_escolhida.tipo:
            quantidade += 1

    if isinstance(classe_escolhida, npc):
        nova_criatura = deepcopy(classe_escolhida)

        nova_criatura.nome = nova_criatura.tipo + str(quantidade + 1)

        participantes.append(nova_criatura)

        print(nova_criatura.nome, "adicionado ao combate!")