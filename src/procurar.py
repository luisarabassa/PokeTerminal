from util import titulo, numero_invalido, primeiros_titulos
from jogo import locais, lista_pokemons
from batalhar import batalha
from jogo import nivel_jogador
import random
import time
import copy

def procurar_pokemon():
    primeiros_titulos("🔍 Escolha o local onde vai procurar 🔍")
    for num, (nome, tipos) in locais.items():
        print(f"{num}. {nome}")

    while True:
        try:
            escolha = int(input("\n🎯 Escolha o local: "))
            if escolha in locais:
                nome_local, tipos_desejados = locais[escolha]
                primeiros_titulos(f"🗺️  Procurando Pokémons na {nome_local}... 🗺️")
                time.sleep(1.5)

                encontrados = [
                    p for p in lista_pokemons 
                    if p.lendario == 0
                    and (p.tipo1 in tipos_desejados or p.tipo2 in tipos_desejados)
                    and p.base_total <= 300 + (nivel_jogador + 1) * 50
                ]

                if encontrados:
                    pokemon = copy.deepcopy(random.choice(encontrados))
                    print(f"\n✨ Um Pokémon apareceu: {pokemon.nome}!")
                    batalha(pokemon)
                else:
                    print("\n🌫️  Parece que você não encontrou nenhum Pokémon por aqui desta vez...")
                break
            else:
                print(numero_invalido())
        except ValueError:
            print(numero_invalido())
