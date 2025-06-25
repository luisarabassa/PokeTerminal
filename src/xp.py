import jogo

def ganhar_experiencia(pontos):
    jogo.experiencia += pontos
    print(f"\n✨ Você ganhou {pontos} pontos de experiência!")

    if jogo.experiencia >= jogo.nivel_jogador * 100:
        jogo.experiencia -= jogo.nivel_jogador * 100
        jogo.nivel_jogador += 1
        print(f"\n🎉 Parabéns! Você subiu para o nível {jogo.nivel_jogador}!")