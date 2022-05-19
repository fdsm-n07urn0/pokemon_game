# random.random() -> Cria números aleatorios entre 0 e 1 (EX: 0.33781071197240986)
# random.randint() -> Precisa passar dois argumentos (Ex: random.randint(1, 6) vai gerar números entre 1 a 6
# random.choice(lista) -> Escolhe número dentro de uma lista aleatoriamente (Ex: lista = ['a', 'b', 'c'])

# Pode importar class especificar que estar em outro arquivo (Ex: PokemonEletrico do pokemon.py)

import random
from pokemon import *   # Colocando o * importa tudo

NOMES = [
    'João', 'Isabela', 'Lorena', 'Francisco', 'Ricardo', 'Diego',
    'Patrícia', 'Marcelo', 'Gustavo', 'Gerônimo', 'Gary'
]

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Flarion'),
    PokemonFogo('Charmilion'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Magicarp'),
]

class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)    # Pegar um nome aleatorio que esta dentro da lista
        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome    # Faz retornar o nome (Não vai mostrar que é um objeto (Ex: Objeto do tipo player))

    def mostrar_pokemons(self):
        if self.pokemons:       # Verifica se tem pokemons na lista
            print('Pokemons de {}:'.format(self))
            for index, pokemon in enumerate(self.pokemons):   # Não vai mostrar que é do tipo pokemom (Faz mostrar os nomes dos pokemons)
                print('{} - {}'.format(index, pokemon))       # enumerate -> Enumera lista (enumerate retorna uma tupla)
        else:                                                 # Pode dar um for no index e no pokemon (mostra o index e o pokemon Ex: 0 - pikachu)
            print('{} não tem nenhum pokemon'.format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} escolheu {}'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('ERRO: Esse jogador não possui nenhum pokemon para ser escolhido')

    def mostrar_dinheiro(self):
        print('Você possui $ {} na sua conta'.format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        #self.dinheiro = self.dinheiro + quantidade
        self.dinheiro += quantidade
        print('Você ganhou $ {}'.format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print('{} iniciou uma batalha com {}'.format(self, pessoa))
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} ganhou a batalha'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)   # Level 1 ganha 100 level 2 ganha 200 etc...
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha'.format(pessoa))
                    break
        else:
            print('Essa batalha não pode ocorrer')


class Player(Pessoa):
    tipo = 'player'
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)    # Adiciona o pokemon que ser capturado na lista (self.pokemons)
        print('{} capturou {}'.format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input('Escolha o seu Pokemon: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print('{} eu escolho você!!!'.format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print('Escolha inválida')
        else:
            print('ERRO: Esse jogador não possui nenhum pokemon para ser escolhido')

    def explorar(self):
        if random.random() <= 0.3:  # Se o número for menor ou igual 0.3 (30% de chance de aparecer um pokemon)
            pokemon = random.choice(POKEMONS)
            print('Um pokemon selvagem apareceu {}'.format(pokemon))

            while True:
                escolha = input('Deseja capturar pokemon? (S/N)').upper()
                if escolha == 'S':
                    if random.random() >= 0.5:  # Se o número for maior ou igual 0.5 (50% de chance de capturar um pokemon)
                        self.capturar(pokemon)
                        break
                    else:
                        print('{} fugiu, que pena!!!'.format(pokemon))
                        break
                elif escolha == 'N':
                    print('Ok, boa viagem')
                    break
                else:
                    print('Opção invalida!!!')
        else:
            print('Essa exploração não deu em nada')


class Inimigo(Pessoa):
    tipo = 'inimigo'
    def __init__(self, nome=None, pokemons=None):  # Faz aparecer inimigo com nome, pokemon e level aleatorio, se quizer pode adicionar pokemons para um inimigo especifico
        if not pokemons:
            pokemons_aleatorios = []
            #for i in range(6):
            for i in range(random.randint(1, 6)):     # Faz o inimigo ficar de 1 a 6 pokemons aleatoriamente
                pokemons_aleatorios.append(random.choice(POKEMONS))   # Pega de 1 a 6 pokemons aleatorios na lista POKEMONS
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)   # super() chama o __init__ da class pai para não ter que repetir codigo
        else:
            super().__init__(nome=nome, pokemons=pokemons)
# Em (nome=nome, pokemons=pokemons) entrara o nome do inimigo e do pokemon aleatorio ou especificado no __init__ do inimigo

#if __name__ == '__main__':
    #print('Estou testando esse arquivo')


#meu_inimigo = Inimigo(nome='Valter', pokemons=[PokemonEletrico('Raichu'), PokemonAgua('Squirtle')])
#meu_inimigo = Inimigo(nome='Valter')
#meu_inimigo = Inimigo()
#print(meu_inimigo)
#meu_inimigo.mostrar_pokemons()

#meu_pokemom = PokemonFogo('charmander') # Pode colocar o level se quizer (level=1) se não colocar vai ficar aleatorio
#print(meu_pokemom)

#eu = Player()    # Se não especificar um nome vai mostrar um nome aleatorio que esta na lista
#print(eu)

#eu = Player(nome='Guilherme')
#pokemon_selvagem = PokemonFogo('charmander')

#print('Antes de capturar')
#eu.mostrar_pokemons()

#eu.capturar(pokemon_selvagem)
#eu.mostrar_pokemons()

#meu_pokemon = PokemonEletrico('pikachu')   # Importados de outro arquivo (pokemon.py)
#meu_pokemon2 = PokemonFogo('charmander')

#eu = Player(nome='Guilherme', pokemons=[meu_pokemon, meu_pokemon2])

#print(eu)
#eu.mostrar_pokemons()  # Chama o metodo mostrar_pokemons e mostra os nomes na tela

#print(eu.mostrar_pokemons())   # Colocando print faz retornar none
#print(eu.pokemons)    # Mostra que é um objeto do tipo pokemon