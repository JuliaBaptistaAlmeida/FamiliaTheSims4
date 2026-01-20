"""
Sistema de Famílias Aleatórias
Em The Sims 4
Criado por Julia Baptista
"""

import random
from time import sleep

generos = ['Masculino', 'Feminino']

criaturas = [
    'Humano', 'Vampiro', 'Sereia',
    'Fada', 'Bruxo', 'Lobisomem', 'Alien'
]

idades = [
    'Bebê de Colo', 'Bebê', 'Criança',
    'Adolescente', 'Jovem Adulto',
    'Adulto', 'Idoso'
]

pets = ['Cachorro', 'Gato', 'Cavalo']
sexo_pet = ['Macho', 'Fêmea']
idades_pet = ['Filhote', 'Adulto', 'Idoso']

cidades = [
    'Willow Creek', 'Oasis Springs', 'San Myshuno',
    'Windenburg', 'Brindleton Bay', 'Del Sol Valley',
    'Sulani', 'Strangerville', 'Henford-on-Bagley',
    'Moonwood Mill', 'Copperdale'
]

# Função de criar um integrante
def criar_integrante():
    tipo = random.choice(['Pessoa', 'Pet'])

    if tipo == 'Pessoa':
        genero = random.choice(generos)
        criatura = random.choice(criaturas)
        idade = random.choice(idades)

        return {
            'tipo': 'Pessoa',
            'sexo': genero,
            'raca': criatura,
            'idade': idade
        }

    else:
        animal = random.choice(pets)
        sexo = random.choice(sexo_pet)
        idade = random.choice(idades_pet)

        return {
            'tipo': 'Pet',
            'raca': animal,
            'sexo': sexo,
            'idade': idade
        }

# Função de criar uma família
def criar_familia(qtd):

    while True:
        familia = []

        for i in range(qtd):
            membro = criar_integrante()
            familia.append(membro)

        # Faz com que tenha sempre um adulto na família
        adultos = 0
        for membro in familia:
            if membro['tipo'] == 'Pessoa':
                if membro['idade'] in ['Jovem Adulto', 'Adulto', 'Idoso']:
                    adultos += 1
        if adultos >= 1:
            return familia

print('\n🎲 GERADOR DE FAMÍLIA - THE SIMS 🎲')
sleep(1)

while True:
    while True:
        qtd = int(input('\nQuantos integrantes terá a família (1 a 8)? '))
        if qtd < 1 or qtd > 8:
            print('\nDigite um número entre 1 e 8!')
        else:
            break

    familia = criar_familia(qtd)
    cidade = random.choice(cidades)

    print('\n🏠 FAMÍLIA SENDO GERADA...\n')
    sleep(1)

    for i, membro in enumerate(familia, start=1):
        print(f'--- {i}º INTEGRANTE ---')
        print(f"Raça: {membro['raca']}")
        print(f"Sexo: {membro['sexo']}")
        print(f"Idade: {membro['idade']}")
        print()

    print(f'🌆 Cidade onde vão morar: {cidade}\n')

    while True:
        opcao = input('Deseja gerar outra família? (S/N): ').upper().strip()
        if opcao == 'S':
            break
        elif opcao == 'N':
            print('\nPrograma encerrado! Boa gameplay! 🎮✨\n')
            exit()
        else:
            print('\nDigite apenas S para sim ou N para não!\n')
