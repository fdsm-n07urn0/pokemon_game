import random

#class Pokemon:                   # Nome da class colocar com a primeira letra maiuscula ex: class Pokemon:
    #tipo = 'Fogo'                # Ou colocar o nome da class ex: class PokemonDeFogo:
    #especie = 'Charmander'       # class descrevi um determinado objeto (É como se fosse uma receita)

                            # Objeto é a estanciação da class
#meu_pokemon = Pokemon()    # Chama a class Pokemon
#print(meu_pokemon)
#print(type(meu_pokemon))

#pokemon_do_meu_amigo = Pokemon()

class Pokemon:                       # random.randint(1, 100) deixa o level aleatorio, o level aparece entre 1 e 100
    def __init__(self, especie, level=None, nome=None):   # Esse metodo é chamado de construtor ( __init__(self) )
        #self.tipo = tipo                 # self se refere ao proprio objeto (metodo ou atributo)
        self.especie = especie

        if level:
            self.level = level    # Se passar o level
        else:
            self.level = random.randint(1, 100)   # Se não passar o level o level fica aleatorio

        if nome:                # (Se nome tiver um nome nome = nome se nome não tiver nome nome = especie)
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5   # Pontos de ataque (Se o level for 1 ataque vai ser 5 -> 5x1=5) quanto maior for o level maior o ataque
        self.vida = self.level * 10    # Quanto maior o level maior é a vida

    def __str__(self):            # Não é obrigatorio definir __str__ mais é bom definir pra deixar melhor o codigo
        #return self.especie      # No __str__ você tem que definir alguma coisa  (retornar uma string)

        return '{}({})'.format(self.nome, self.level)
        #return 'Isso é um pokemon'

# Podemos definir nossos proprios metodos
    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))  # Deixa o ponto de ataque de 0 a 6 aleatorio (o ataque mais efetivo é o 6)
        #pokemon.vida = pokemon.vida - ataque_efetivo                # int transforma o número para inteiro
        pokemon.vida -= ataque_efetivo   # -= siginifica ->  pokemon.vida = pokemon.vida - ataque_efetivo
        print('{} perdeu {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True # Se retorna True o adiversario foi derrotado
        else:
            return False
                                            # Meu pokemon vai ser o self
        #print('{} atacou!'.format(self))   # Pega o format do __str__
        #print('{} atacou!'.format(self.especie))
        #print('{} atacou {}!'.format(self.especie, pokemon.especie))
        #print('{} atacou {}!'.format(self, pokemon))       # Pode passar so o self e pokemon sem especie
                                                            # Pega o format do __str__ também

        #print('O pokemon atacou')

                                      # A class filho erda as funções da class pai
class PokemonEletrico(Pokemon):       # class filho (Passar nome da class pai entre parentese
    tipo = 'eletrico'     # Colocando o tipo na class remove o da class __init__ o mesmo para a especie e etc...
    def atacar(self, pokemon):        # Se quiser acresentar mais class não precisa mecher na class pai
        print('{} lançou raio do trovão em {}'.format(self, pokemon))    # Substituiu o atacar de cima (class pai)
        return super().atacar(pokemon)
    #def dar_choque(self):     # Pode acresentar metodos na class filho ou modificar
        #print('Deu choque')

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

#class Pikachu(PokemonEletrico):     # class neto
    #especie = 'Pikachu'

#meu_pokemon = PokemonFogo('charmander')
#amigo_pokemon = PokemonEletrico('pikachu')

#print(meu_pokemon, meu_pokemon.tipo)
#print(amigo_pokemon, amigo_pokemon.tipo)

#meu_pokemon = Pokemon('fogo', 'charmander', nome='Gui', level=50)    # Define o tipo e a especie que é passado acima
#meu_pokemon = PokemonFogo('eletrico', 'pikachu')
#amigo_pokemon = Pokemon('fogo', 'charmander')    # Executa a função atacar da class pai

#pokemon_amigo = Pokemon('eletrico', 'Pikachu')        # Se não tirar o level vai pegar o padrão de cima level=1

#meu_pokemon.atacar(amigo_pokemon)
#amigo_pokemon.atacar(meu_pokemon)
#meu_pokemon.dar_choque()

#amigo_pokemon.dar_choque()   # Não tem o metodo dar_choque

#meu_pokemon.atacar(pokemon_amigo)
#pokemon_amigo.atacar(meu_pokemon)
#print(meu_pokemon.nome)
#print(meu_pokemon.nome, meu_pokemon.especie, meu_pokemon.level)

#print(meu_pokemon.tipo, meu_pokemon.especie)      # Para acessar um atributo

#print(pokemon_amigo.tipo, pokemon_amigo.especie)

#pokemon_do_meu_vizinho = Pokemon('eletrico', 'Pikachu')

#print(meu_pokemon)
#print(amigo_pokemon)
