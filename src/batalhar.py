from util import titulo, numero_invalido, primeiros_titulos, animacao_final
from inventario import usar_item
from treinadores import treinadores
from xp import ganhar_experiencia
from hp import exibir_hp
import jogo
import random
import copy
import time

def batalha(pokemon_inimigo, contra_treinador=False):
    primeiros_titulos("⚔️  Batalha Pokémon ⚔️")

    pokemons_vivos = [p for p in jogo.time_principal if p.hp > 0]
    if not pokemons_vivos:
        time.sleep(0.5)
        print("\n💤 Todos os seus Pokémons estão desacordados! Você não pode batalhar sem Pokémons...")
        time.sleep(0.5)
        return

    seu_pokemon = pokemons_vivos[0]

    print(f"\n🕹️  Seu Pokémon: {seu_pokemon.nome} {exibir_hp(seu_pokemon)}\n")
    time.sleep(0.5)
    print(f"🔻 Oponente: {pokemon_inimigo.nome} {exibir_hp(pokemon_inimigo)}")
    time.sleep(1.0)

    while seu_pokemon.hp > 0 and pokemon_inimigo.hp > 0:
        print("\n+--------------------------+")
        print("| Escolha sua próxima ação |")
        print("+--------------------------+")
        print("| 1. Atacar                |")
        print("| 2. Trocar Pokémon        |")
        print("| 3. Usar item             |")
        print("| 4. Tentar capturar       |")
        print("| 5. Fugir da batalha      |")
        print("+--------------------------+")

        escolha = int(input("\n🎯 Sua escolha: "))
        if escolha == 1:
            dano = max(1, seu_pokemon.ataque - pokemon_inimigo.defesa // 2)
            pokemon_inimigo.hp = max(0, pokemon_inimigo.hp - dano)
            print(f"\n💥 {seu_pokemon.nome} atacou causando {dano} de dano!")
            time.sleep(0.5)
            print(f"🔻 {pokemon_inimigo.nome}: {exibir_hp(pokemon_inimigo)}")
            time.sleep(1.0)

        elif escolha == 2:
            seu_pokemon = escolher_pokemon()
            continue

        elif escolha == 3:
            usar_item()
            continue

        elif escolha == 4:
            capturado = tentar_captura(pokemon_inimigo)
            if capturado:
                return
            else:
                print(f"\n💨 {pokemon_inimigo.nome} escapou da pokébola!")
            time.sleep(1.0)

        elif escolha == 5:
            if random.random() < 0.5:
                print(f"\n💨 Você fugiu!!")
                return "derrota" if contra_treinador else "fuga"
            else:
                print(f"\n💥 A fuga falhou! {pokemon_inimigo.nome} te atacou!")
        else:
            print(numero_invalido())
            continue

        if pokemon_inimigo.hp <= 0:
            print(f"\n🎉 {pokemon_inimigo.nome} foi derrotado!")
            ganhar_experiencia(30)
            return "vitória"

        dano = max(1, pokemon_inimigo.ataque - seu_pokemon.defesa // 2)
        seu_pokemon.hp = max(0, seu_pokemon.hp - dano)
        print(f"\n💥 {pokemon_inimigo.nome} atacou causando {dano} de dano!")
        print(f"🎯 {seu_pokemon.nome}: {exibir_hp(seu_pokemon)}")
        time.sleep(1.0)

        if seu_pokemon.hp <= 0:
            print(f"\n💀 {seu_pokemon.nome} foi derrotado!")
            pokemons_vivos = [p for p in jogo.time_principal if p.hp > 0]
            if pokemons_vivos:
                print("\n🔁 Escolha outro Pokémon para continuar a batalha")
                seu_pokemon = escolher_pokemon()
            else:
                print("\n⛔ Todos os seus Pokémons foram derrotados!")
                return "derrota"


def escolher_pokemon():
    vivos = [p for p in jogo.time_principal if p.hp > 0]
    print("\n🔁 Pokémons disponíveis:\n")
    for i, p in enumerate(vivos):
        print(f"\n{i+1}. {p.nome} {exibir_hp(p)}")
    while True:
        try:
            escolha = int(input("\nEscolha seu Pokémon: ")) - 1
            if 0 <= escolha < len(vivos):
                return vivos[escolha]
            else:
                print(numero_invalido())
                return
        except ValueError:
            print(numero_invalido())
            return


def tentar_captura(pokemon):
    if "Pokébola" not in jogo.mochila:
        print("❌ Você não tem nenhuma Pokébola para tentar capturar! ❌")
    else:
        print(f"\nTentando capturar {pokemon.nome}...")
        jogo.mochila.remove("Pokébola")
        time.sleep(2.0)
        chance = random.randint(1, 100)
    if pokemon.hp <= 30 and chance > 15:
        print(f"🎉 Você capturou {pokemon.nome} com sucesso!")
        adicionar_ao_time(pokemon)
        ganhar_experiencia(20)
        return True
    else:
        time.sleep(1.0)
        return False


def adicionar_ao_time(novo_pokemon):
    if len(jogo.time_principal) < 5:
        jogo.time_principal.append(novo_pokemon)
        print(f"✅ {novo_pokemon.nome} foi adicionado ao seu time principal!")
    else:
        jogo.pokemons_capturados.append(novo_pokemon)
        print("✅ Este pokémon foi movido para os seus Pokémons capturados.")


def batalhar_treinador(treinador):
    primeiros_titulos(f"🏆 Batalha contra {treinador['nome']}! 🏆")

    clones_pokemons = [copy.deepcopy(p) for p in treinador["pokemons"]]

    for inimigo in clones_pokemons:
        print(f"\n⚔️   {treinador['nome']} lançou {inimigo.nome}!")
        time.sleep(1.0)

        resultado = batalha(inimigo, contra_treinador=True)

        if resultado == "derrota":
            print(f"\n❤️‍🩹 Você perdeu a batalha contra {treinador['nome']}!")
            return

    if treinador["insignia"] not in jogo.mochila:
        jogo.mochila.append(treinador["insignia"])
        jogo.mochila = list(set(jogo.mochila))
        print(f"\n🎖️  Você venceu {treinador['nome']} e recebeu a {treinador['insignia']}!")
    else:
        print(f"\n✅ Você já derrotou {treinador['nome']}.")


    if all(insignia in jogo.mochila for insignia in jogo.insignias):
        time.sleep(1.0)
        animacao_final()
        exit()



def batalhar_ginasio():
    titulo("🏛️  Desafiar ginásios 🏛️")
    for i, t in enumerate(treinadores):
        print(f"{i+1}. {t['ginasio']}, Liderado por: {t['nome']}")

    try:
        escolha = int(input("\n🎯 Escolha um ginásio para desafiar: ")) - 1
        if 0 <= escolha < len(treinadores):
            batalhar_treinador(treinadores[escolha])
        else:
            print(numero_invalido())
    except ValueError:
        print(numero_invalido())