from util import numero_invalido, titulo, vida_cheia, primeiros_titulos
from hp import exibir_hp
import jogo
import time

def ver_mochila():
    primeiros_titulos("🎒 Itens da sua mochila 🎒")
    time.sleep(0.5)
    if not jogo.mochila:
        print("Sua mochila está vazia...")
    else:
        itens_contados = {}
        for item in jogo.mochila:
            itens_contados[item] = itens_contados.get(item, 0) + 1
        for item, qtd in itens_contados.items():
            print(f"• {item} (x{qtd})")
            time.sleep(0.5)
    time.sleep(1.0)

def usar_item():
    ver_mochila()

    item = input("\n🎯 Digite o nome do item que deseja usar: ").title()

    if item not in jogo.mochila:
        print("\n🔍 Você não possui esse item.")
        return

    if item not in ["Poção", "Super Poção", "Reviver"]:
        print(f"\n⛔ O item '{item}' não pode ser usado agora.")
        return

    print("\n🛡️  Time Atual:")
    for i, p in enumerate(jogo.time_principal):
        status = f"{p.nome} (HP: {p.hp})"
        print(f"{i+1}. {status}")

    try:
        escolha = int(input("\n🎯 Escolha o número do Pokémon para usar o item: ")) - 1
        if 0 <= escolha < len(jogo.time_principal):
            pokemon = jogo.time_principal[escolha]

            if item == "Poção":
                if pokemon.hp >= 100:
                    print(vida_cheia())
                    return
                else:
                    cura = min(20, 100 - pokemon.hp)
                    pokemon.hp += cura
            elif item == "Super Poção":
                if pokemon.hp >= 100:
                    print(vida_cheia())
                    return
                else:
                    cura = min(50, 100 - pokemon.hp)
            elif item == "Reviver":
                if pokemon.hp > 0:
                    print(f"\n⛔ {pokemon.nome} não está desacordado.")
                    return
                else:
                    pokemon.hp = 50
                    jogo.mochila.remove(item)
                    print(f"\n✨ {pokemon.nome} foi revivido e está com {pokemon.hp} de HP!")
                    return

            if pokemon.hp == 0:
                print(f"\n💤 {pokemon.nome} está desacordado! Use um Reviver primeiro.")
                return

            pokemon.hp += cura
            jogo.mochila.remove(item)
            print(f"\n🔺{pokemon.nome} recuperou {cura} de HP!")
            print(f"\n❤️  HP atual de {pokemon.nome}: {exibir_hp(pokemon)}")
        else:
            print(numero_invalido())
    except ValueError:
        print(numero_invalido())

def ver_pokemons_capturados():
    titulo("📦 Pokémons capturados 📦")
    time.sleep(0.5)
    if not jogo.pokemons_capturados:
        print("\nTodos os seus Pokémons estão no seu time principal, capture mais Pokémons...")
    else:
        for p in jogo.pokemons_capturados:
            p.mostrar()
            time.sleep(0.5)
    time.sleep(1.0)

def ver_time_principal():
    titulo("🛡️  Seu time principal 🛡️")
    for i, p in enumerate(jogo.time_principal):
        print(f"{i+1}. {p.nome}")
        time.sleep(0.5)
    time.sleep(1.0)
    deseja_gerenciar_time = input("\nDeseja mudar seu time principal? (S/N) ").upper()
    if deseja_gerenciar_time == "S":
        if len(jogo.time_principal) < 5:
            print("\n❌ Você ainda não possui 5 Pokémons para gerenciar o time principal ❌")
        else:
            gerenciar_time()
    else:
        return

def gerenciar_time():
    while True:
        titulo("⚙️  Gerenciar Time Pokémon ⚙️")

        print("\n📦 Pokémons Capturados:")
        for i, p in enumerate(jogo.pokemons_capturados):
            print(f"{i+1}. {p.nome}")

        print("\n🛡️  Time Atual:")
        for i, p in enumerate(jogo.time_principal):
            print(f"{i+1}. {p.nome}")

        print("\nDeseja trocar um Pokémon do time por um capturado?")
        print("1. Sim")
        print("2. Voltar")

        try:
            escolha = int(input("\n🎯 Opção: "))
            if escolha == 1:
                if not jogo.pokemons_capturados:
                    print("\n❌ Você não tem Pokémons capturados fora os do time. ❌\n")
                    return

                idx_capturado = int(input("\n🎯 Digite o número do Pokémon que deseja adicionar ao time principal: ")) - 1
                idx_time = int(input("🎯 Digite o número do Pokémon do time que deseja substituir: ")) - 1

                if 0 <= idx_capturado < len(jogo.pokemons_capturados) and 0 <= idx_time < len(jogo.time_principal):
                    capturado = jogo.pokemons_capturados[idx_capturado]
                    removido = jogo.time_principal[idx_time]

                    jogo.time_principal[idx_time] = capturado
                    jogo.pokemons_capturados[idx_capturado] = removido

                    print(f"\n✅ {capturado.nome} foi adicionado ao time com sucesso!")
                    print(f"📦 {removido.nome} foi movido para os seus Pokémons.")
                    time.sleep(1.5)
                else:
                    print(numero_invalido())
            else:
                break
        except ValueError:
            print(numero_invalido())
