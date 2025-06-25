class Pokemon:
    def __init__(self, dados):
        self.nome = dados.get("nome") or dados.get("name")
        self.hp = int(dados['hp'])
        self.ataque = int(dados['attack'])
        self.defesa = int(dados['defense'])
        self.tipo1 = dados['type1']
        self.tipo2 = dados['type2']
        self.lendario = int(dados["is_legendary"])
        self.base_total = int(dados['base_total'])
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "hp": self.hp,
            "attack": self.ataque,
            "defense": self.defesa,
            "type1": self.tipo1,
            "type2": self.tipo2,
            "is_legendary": self.lendario,
            "base_total": self.base_total
        }

    def mostrar(self):
        tipo2 = f" / {self.tipo2}" if self.tipo2 else ""
        print(f"{self.nome} | Tipo: {self.tipo1}{tipo2} | HP: {self.hp} | ATK: {self.ataque} | DEF: {self.defesa}")
    def mostrar_nome(self):
        print(f"{self.nome}")