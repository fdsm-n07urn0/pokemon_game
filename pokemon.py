import random

class Pokemon:                       
    def __init__(self, especie, level=None, nome=None):   # Esse metodo é chamado de construtor ( __init__(self) )
        self.especie = especie

        if level:
            self.level = level    
        else:
            self.level = random.randint(1, 100)   # Se não passar o level o level fica aleatorio

        if nome:               
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5   # Pontos de ataque (Se o level for 1 ataque vai ser 5 -> 5x1=5) quanto maior for o level maior o ataque
        self.vida = self.level * 10    # Quanto maior o level maior é a vida

        
    def __str__(self):            

        return '{}({})'.format(self.nome, self.level)
        

    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))  # Deixa o ponto de ataque de 0 a 6 aleatorio (o ataque mais efetivo é o 6)
        pokemon.vida -= ataque_efetivo  
        print('{} perdeu {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True                                # Se retorna True o adiversario foi derrotado
        else:
            return False

                                      
class PokemonEletrico(Pokemon):       
    tipo = 'eletrico'    
    def atacar(self, pokemon):        
        print('{} lançou raio do trovão em {}'.format(self, pokemon))    # Substituiu o atacar de cima (class pai)
        return super().atacar(pokemon)

    
class PokemonFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print('{} lançou uma bola de fogo na cabeça de {}'.format(self, pokemon))
        return super().atacar(pokemon)  # Chama o atacar da class pai e recebi True ou False e manda de volta


class PokemonAgua(Pokemon):
    tipo = 'Água'
    def atacar(self, pokemon):
        print("{} lançou um jato d'água em {}".format(self, pokemon))
        return super().atacar(pokemon)
