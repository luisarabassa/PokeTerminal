from pokemon import Pokemon
import jogo
import json

def salvar_jogo():
    dados = {
        "jogador": jogo.jogador,
        "mochila": jogo.mochila,
        "nivel_jogador": jogo.nivel_jogador,
        "experiencia": jogo.experiencia,
        "time_principal": [p.to_dict() for p in jogo.time_principal],
        "pokemons_capturados": [p.to_dict() for p in jogo.pokemons_capturados]
    }

    with open("jogosalvo.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print("\n💾 Jogo salvo com sucesso! 💾")

def carregar_jogo():
    try:
        with open("jogosalvo.json", "r", encoding="utf-8") as f:
            dados = json.load(f)

        jogo.jogador = dados["jogador"]
        jogo.mochila = dados["mochila"]
        jogo.nivel_jogador = dados["nivel_jogador"]
        jogo.experiencia = dados["experiencia"]
        jogo.time_principal = [Pokemon(p) for p in dados["time_principal"]]
        jogo.pokemons_capturados = [Pokemon(p) for p in dados["pokemons_capturados"]]

        print(f"\n🔁 Jogo carregado! Bem-vindo(a) de volta, {jogo.jogador}!")
        return True
    except FileNotFoundError:
        print("\n❌ Nenhum jogo salvo encontrado ❌")
        return False