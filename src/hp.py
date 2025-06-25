def exibir_hp(pokemon):
    total = 20
    hp_ratio = max(0, pokemon.hp / 100)
    barras_preenchidas = int(hp_ratio * total)
    barras = '█' * barras_preenchidas + '▒' * (total - barras_preenchidas)
    return f"[{barras}] {pokemon.hp} HP"