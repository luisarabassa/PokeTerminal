from inventario import ver_mochila, ver_pokemons_capturados, ver_time_principal, usar_item
from util import numero_invalido, titulo, primeiros_titulos, limpar_console
from salvar import salvar_jogo, carregar_jogo
from jogo import inicial, lista_pokemons
from batalhar import batalhar_ginasio
from procurar import procurar_pokemon
from explorar import explorar
from pokemon import Pokemon
import jogo
import time
import csv

with open("../data/pokedex.csv", mode="r", encoding="utf-8") as arq:
    for linha in csv.DictReader(arq):
        jogo.lista_pokemons.append(Pokemon(linha))

limpar_console()
primeiros_titulos("✨ Bem-vindo(a) jogador(a) ✨")
print("Você está prestes a começar a sua aventura Pokémon.")
print("Mas primeiro...")
print("1. Comece uma nova jornada")
print("2. Carregar jornada salva anteriormente")

while True:
    escolha = input("\n🎯 Escolha: ")
    if escolha == "1":
        jogo.jogador = input("Insira seu nome: ").title()
        while True:
          try:
            idade = int(input("E sua idade: "))
            if idade < 10:
              print("❌ Você precisa ter, no mínimo, 10 anos para jogar este jogo. ❌")
              exit()
            else:
              print("\n🌠 Uma nova aventura está para começar...")
              time.sleep(1.0)
              
              def get_iniciais():
                nomes_iniciais = ['Bulbasaur', 'Charmander', 'Squirtle']
                return [p for p in lista_pokemons if p.nome in nomes_iniciais]


              primeiros_titulos("🌟 Escolha seu Pokémon inicial 🌟")
              opcoes = get_iniciais()
              emojis = {"Bulbasaur": "🌱", "Charmander": "🔥", "Squirtle": "💧"}

              for i, pokemon in enumerate(opcoes):
                emoji = emojis.get(pokemon.nome, "🪄")
                print(f"{i+1}. {emoji} ", end="")
                pokemon.mostrar_nome()
                time.sleep(0.5)

              while True:
                try:
                  escolha = int(input("\n🎯 Digite o número do Pokémon que deseja: "))
                  if 1 <= escolha <= 3:
                    inicial = opcoes[escolha - 1]
                    print(f"\n{emojis[inicial.nome]} {inicial.nome}, {jogo.jogador} escolheu você! ❤️‍🔥🕹️")

                    jogo.time_principal.append(inicial)

                    time.sleep(1.0)

                    jogo.mochila.extend(["Pokébola"] * 10)
                    jogo.mochila.append("Reviver")

                    primeiros_titulos("👤 Parece que você encontrou alguém antes de ir... 👤")
                    time.sleep(1.0)
                    print("\n🎁 Professor Carvalho te deu 10 Pokébolas e 1 Reviver!")
                    time.sleep(1.0)
                    break
                  else:
                    print(numero_invalido)
                except ValueError:
                  print(numero_invalido())
              break
          except ValueError:
            print(numero_invalido())
        break
    elif escolha == "2":
        if carregar_jogo():
            break
    else:
        print(numero_invalido())

time.sleep(1.0)



while True:
  titulo("🕹️  O que deseja fazer agora? 🕹️")
  print("1. Explorar livremente")
  print("2. Procurar Pokémons selvagens")
  print("3. Abrir mochila")
  print("4. Usar item da mochila")
  print("5. Seus Pokémons capturados (PC)")
  print("6. Seu Time principal")
  print("7. Enfrentrar Ginásio Pokémon")
  print("8. Salvar")
  print("9. Sair")

  try:
    opcao = int(input("\n🎯 Opção: "))
    if opcao == 1:
      explorar()
    elif opcao == 2:
      procurar_pokemon()
    elif opcao == 3:
      ver_mochila()
    elif opcao == 4:
      usar_item()
    elif opcao == 5:
      ver_pokemons_capturados()
    elif opcao == 6:
      ver_time_principal()
    elif opcao == 7:
      batalhar_ginasio()
    elif opcao == 8:
      salvar_jogo()
    elif opcao == 9:
      time.sleep(1.0)
      print("\nSalvando... ⏳")
      time.sleep(1.0)
      salvar_jogo()
      time.sleep(1.0)
      print(f"\nSaindo... Até a próxima {jogo.jogador}! ⌛")
      time.sleep(0.5)
      exit()
  except ValueError:
    print(numero_invalido())
