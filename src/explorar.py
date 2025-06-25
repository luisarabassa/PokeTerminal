from util import numero_invalido, titulo, primeiros_titulos
from jogo import lista_pokemons, locais
from xp import ganhar_experiencia
from batalhar import batalha
import random
import jogo
import time
import copy

def explorar():
    itens_possiveis = ["Poção", "Poção", "Reviver", "Reviver", "Super Poção", "Pokébola" ]
    time.sleep(0.5)
    primeiros_titulos("🔍 Onde deseja explorar? 🔍")
    for num, (nome, _) in locais.items():
        print(f"{num}. {nome}")

    while True:
        try:
            escolha = int(input("\n🎯 Escolha o local: "))
            if escolha in locais:
                nome_local, locais_possiveis = locais[escolha]
                primeiros_titulos(f"🗺️  Explorando a {nome_local}... 🗺️")
                time.sleep(1.0)

                chance = random.randint(1, 100)
                # if False:
                if chance >= 2:
                    item = random.choice(itens_possiveis)
                    jogo.mochila.append(item)
                    print(f"\n🎁 Encontrou um item: {item}!")
                    ganhar_experiencia(5)
                    time.sleep(1.0)
                # if True:
                elif chance == 1:
                    lendarios = [p for p in lista_pokemons if p.lendario]
                    if lendarios:
                        pokemon_lendario = copy.deepcopy(random.choice(lendarios))
                        pokemon_lendario.hp = 100
                        print(f"\n⭐ Um Pokémon lendário apareceu: {pokemon_lendario.nome}") 
                        time.sleep(2.5)
                        batalha(pokemon_lendario)
                        ganhar_experiencia(20)
                        time.sleep(0.5)
                else:
                    print("\n🌫️  Parece não haver nada interessante por aqui desta vez...")
                    time.sleep(1.0)
                break
            else:
                print(numero_invalido())
        except ValueError:
            print(numero_invalido())
