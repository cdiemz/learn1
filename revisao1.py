# Opa. Aqui vai uma pequena revisão do que vimos na quinta-feira,
# 22/fev. Essa revisão é parte do nosso exercício de 'repetição
# espaçada'

# Lembrando: todas as linhas de código Python que começam com '#' são
# 'comentários', ou seja, são ignoradas pelo Python, e têm como função
# permitir a um programador deixar uma mensagem para outros

# O igual '=' em Python faz um 'assignment', ou seja, 'liga' uma
# variável a um valor. É importante, como David comentou na
# quinta-feira, distinguir o '=' do '=='. O segundo é usado não para
# assignments, mas para checar se dois valores são iguais (examplos
# abaixo)

########################################
# Tipos de dados (estrutura de dados)

# um número inteiro é um 'int' ou 'integer'
numero_inteiro = 1

# um 'float'
numero_decimal = 1.5

# uma 'string'
palavras = 'rock n roll'

# um 'list'
lista_de_items = [4, 5.3, 'abc']

# um 'dict'
dicionario = {
    'quantidade': 3,
    'outro_numero': 3.2,
    'cantar': 'verbo',
    'outra_lista': [3, 5, 7, 8],
    'outro_dicionario': {
        'rua': 'rua do sol'
    }
}

# O Python determina o tipo de variável a ser criado baseado no
# 'conteúdo' da variável, então, por exemplo, se o conteúdo de uma
# variável é {'quantidade': ... } o Python entende que isso é 'dict',
# e não um 'int'

##################################################
# Estruturas de controle

# Lembrando, ainda da quinta-feira:
# a) programação = envio de comandos ao computador
# b) modelo de um programa: input -> algoritmo -> output

# Considerando o b) acima: quando o programa recebe o input, ele vai
# executar um algoritmo que vai utilizar o input. É possível que o
# programador queira, dependendo do input, fazer coisas
# diferentes. Exemplo: se o input for '1', mostre na tela a palavra
# 'um'; se o input for '2', mostre na tela a palavra 'dois'. O
# programador, para programar essas possibilidades, vai usar a
# estrutura de controle 'if'

# No exemplo abaixo, o programa faz:
#
# if             :         se o usuario disse 1, então...
# elif (else if) : se não, se o usuario disse 2, então...
# else           : se não, (não há condição),    então...

usuario_disse = 1

if usuario_disse == 1:
    print('um')
elif usuario_disse == 2:
    print('dois')
else:
    print('nem um nem dois')

# Explicar depois
    
for i in range(10):
    print('1')

# Explicar depois

while True:
    print('1')
    break
