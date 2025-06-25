import time
import jogo
import sys
import os

def numero_invalido():
    return "\n❌ Inválido! Por favor, digite um número inteiro. ❌"

def vida_cheia():
   return"\n⛔ Seu pokémon já está com a vida cheia!"

def titulo(texto):
  print()
  print()
  print(f"🎮  Jogador(a): {jogo.jogador} | 🏅  Nível: {jogo.nivel_jogador} | ⭐ XP: {jogo.experiencia} / {jogo.nivel_jogador * 100}".center(90))
  print('-' * 90)
  print(texto.center(90))
  print('-' * 90)

def primeiros_titulos(texto):
  print()
  print('-' * 90)
  print(texto.center(90))
  print('-' * 90)

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def escrever_lento(texto, delay=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animacao_final():
    limpar_console()
    mensagens = [
        f"Parabéns {jogo.jogador}!!!!",
        "Você venceu todos os ginásios... 🏛️🏆",
        "Conquistou todas as insígnias... 🎖️",
        "Você se tornou um verdadeiro Mestre Pokémon! 👑",
        "E concluiu a sua jornada...",
        "Obrigada por jogar! 🎮❤️"
    ]

    for msg in mensagens:
        limpar_console()
        escrever_lento(msg, 0.07)
        time.sleep(1.5)
