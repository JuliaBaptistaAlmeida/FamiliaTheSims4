"""
Sistema de Famílias Aleatórias
Em The Sims 4
Criado por Julia Baptista
"""

import random
from time import sleep

# Criando as listas
generos = ['Masculino', 'Feminino']

criaturas = [
    'Humano', 'Vampiro', 'Sereia', 'Fada', 'Feiticeiro', 'Lobisomem', 'Alien'
]

idades = [
    'Bebê de Colo', 'Bebê', 'Criança', 'Adolescente', 'Jovem Adulto', 'Adulto', 'Idoso'
]

traços_bebedecolo = ['Agitado', 'Calmo', 'Cauteloso', 'Intenso', 'Sensível', 'Vibrante']

traços_bebe = [
    'Angelical', 'Bobo', 'Curioso', 'Encantador', 'Grudento', 'Incansável', 
    'Independente', 'Irritável'
    ]

traços_criança = [
    'A Pratica Leva À Perfeição', 'Alegre', 'Cabeça Quente', 'Criativo', 'Errático', 'Genial', 
    'Nauseento', 'Pateta', 'Seguro de Si', 'Soturno', 'Adora o Ar Livre', 'Amante da Arte', 
    'Amante da Música', 'Devorador de Livros', 'Geek', 'Reciclador', 'Amigo da Natureza', 
    'Asseado', 'Ativo', 'Aventureiro', 'Cleptomaníaco', 'Competitivo', 'Filho da Ilha',
    'Filho do Oceano', 'Glutão', 'Intolerante à Lactose', 'Perfeccionista', 'Preguiçoso', 
    'Provinciano', 'Relaxado', 'Vegetariano', 'Amante de Cavalos', 'Amante de Cachorros', 
    'Amante de Gatos', 'Amante de Plantas', 'Bondoso', 'Engajado', 'Extrovertido', 'Fã de Animais',
    'Maldoso', 'Maligno', 'Respeitoso', 'Solitário'
]

traços_adultos = [
    'A Pratica Leva À Perfeição', 'Alegre', 'Ambicioso', 'Cabeça Quente', 'Criativo', 'Desajeitado',
    'Errático', 'Exigente', 'Genial', 'Infantil', 'Nauseento', 'Não Paqurador', 'Paranoico',
    'Pateta', 'Romanticamente Reservado', 'Romântico', 'Seguro de Si', 'Sentimental', 'Soturno',
    'Adora o Ar Livre', 'Amante da Arte', 'Amante da Música', 'Criador', 'Devorador de Livros',
    'Gastrônomo', 'Geek', 'Máquina de Dança', 'Reciclador', 'Além das Expectativas',
    'Amigo da Natureza', 'Asseado', 'Ativo', 'Aventureiro', 'Cleptomaníaco', 'Competitivo',
    'Cético', 'Filho da Ilha', 'Filho do Oceano', 'Freegano', 'Glutão', 'Incoveniente',
    'Intolerante à Lactose', 'Macabro', 'Materialista', 'Místico', 'Perfeccionista',
    'Perseguido pela Morte', 'Preguiçoso', 'Provinciano', 'Rancheiro', 'Relaxado',
    'Vegetariano', 'Amante de Cavalos', 'Amante de Cachorros', 'Amante de Gatos',
    'Amante de Plantas', 'Benevolente', 'Bondoso', 'Chegado', 'Ciumento', 'Desonesto',
    'Egocêntrico', 'Engajado', 'Esnobe', 'Evasivo', 'Extrovertido', 'Familiar',
    'Fã de Animais', 'Grande Festeiro', 'Idealista', 'Leal', 'Maldoso', 'Maligno',
    'Odeia Crianças', 'Respeitoso', 'Sem Noção', 'Socialmete Desconfortável',
    'Solitário', 'Xereta'
]

pets = ['Cachorro', 'Gato', 'Cavalo']
sexo_pet = ['Macho', 'Fêmea']
idades_pet = ['Filhote', 'Adulto', 'Idoso']

traços_cachorro = [
    'Agressivo', 'Amigável', 'Arisco', 'Ativo', 'Aventureiro', 'Brincalhão',
    'Caçador', 'Conversador', 'Encrenqueiro', 'Glutão', 'Independente',
    'Inteligente', 'Investigador', 'Leal', 'Náufrago do Sofá', 'Peludo', 'Teimoso'
]

traços_gato = [
    'Amigável', 'Animado', 'Arisco', 'Arredio', 'Brincalhão', 'Carinhoso',
    'Curioso', 'Esperto', 'Espírito Livre', 'Falador', 'Felpudo', 'Gatuno',
    'Glutão', 'Mimado', 'Preguiçoso', 'Territorial', 'Travesso'
]

traços_cavalo = [
    'Agressivo', 'Amigável', 'Elétrico', 'Espírito Livre', 'Grudento',
    'Independente', 'Inteligente', 'Medroso', 'Rebelde', 'Tranquilo', 'Valente'
]

cidades = [
    'Willow Creek', 'Oasis Springs', 'San Myshuno', 'Windenburg',
    'Brindleton Bay', 'Del Sol Valley', 'Sulani', 'Strangerville',
    'Henford-on-Bagley', 'Moonwood Mill', 'Copperdale'
]

# Conflitos de traços
conflitos_tracos = [
    {'Alegre', 'Cabeça Quente'}, {'Alegre', 'Soturno'}, {'Alegre', 'Macabro'},
    {'Ambicioso', 'Freegano'},{'Ambicioso', 'Preguiçoso'}, {'Cabeça Quente', 'Soturno'}, 
    {'Desajeitado', 'Criador'}, {'Infantil', 'Esnobe'}, {'Infantil', 'Maligno'}, 
    {'Infantil', 'Odeia Crianças'}, {'Nauseento', 'Adora o Ar Livre'},
    {'Nauseento', 'Freegano'}, {'Nauseento', 'Glutão'}, {'Nauseento', 'Relaxado'},
    {'Não Paquerador', 'Romanticamente Reservado'}, {'Não Paquerador', 'Romântico'},
    {'Não Paquerador', 'Sentimental'}, {'Paranoico', 'Extrovertido'}, {'Pateta', 'Esnobe'},
    {'Romanticamente Reservado', 'Romântico'}, {'Romanticamente Reservado', 'Sentimental'},
    {'Romanticamente Reservado', 'Extrovertido'}, {'Sentimental', 'Solitário'},
    {'Criador', 'Preguiçoso'}, {'Gastrônomo', 'Freegano'}, {'Cético', 'Macabro'}, 
    {'Cético', 'Místico'}, {'Competitivo', 'Preguiçoso'}, {'Asseado', 'Preguiçoso'},
    {'Asseado', 'Relaxado'}, {'Ativo', 'Preguiçoso'}, {'Filho da Ilha', 'Provinciano'},
    {'Cleptomaníaco', 'Bondoso'}, {'Freegano', 'Materialista'}, {'Freegano', 'Esnobe'}, 
    {'Glutão', 'Benevolente'}, {'Incoveniente', 'Macabro'}, {'Incoveniente', 'Místico'},
    {'Incoveniente', 'Respeitoso'}, {'Macabro', 'Místico'}, {'Materialista', 'Benevolente'},
    {'Místico', 'Perseguido pela Morte'}, {'Vegetariano', 'Amante das Plantas'},
    {'Relaxado', 'Respeitoso'}, {'Benevolente', 'Maldoso'}, {'Benevolente', 'Maligno'},
    {'Bondoso', 'Maldoso'}, {'Bondoso', 'Maligno'}, {'Desonesto', 'Idealista'},
    {'Engajado', 'Solitário'}, {'Evasivo', 'Familiar'}, {'Evasivo', 'Leal'},
    {'Extrovertido', 'Solitário'}, {'Extrovertido', 'Socialmente Desconfortável'},
    {'Familiar', 'Odeia Crianças'}, {'Grande Festeiro', 'Solitário'}, {'Maldoso', 'Respeitoso'}, 
    {'Respeitoso', 'Sem Noção'}, {'Grande Festeiro', 'Socialmente Desconfortável'}, 
    {'Agressivo', 'Amigável'}, {'Elétrico', 'Tranquilo'}, {'Grudento', 'Independente'},
    {'Medrosa', 'Valente'}, {'Ativo', 'Náufrago do Sofá'}, {'Independente', 'Leal'},
    {'Territorial', 'Amigável'}, {'Animado', 'Preguiçoso'}, {'Arredio', 'Carinhoso'},

]

# Funções para escolher traços
def tem_conflito(tracos):
    conjunto = set(tracos)
    for conflito in conflitos_tracos:
        if conflito.issubset(conjunto):
            return True
    return False

def sortear_tracos_pessoa(idade):
    if idade == 'Bebê de Colo':
        return random.sample(traços_bebedecolo, 1)
    elif idade == 'Bebê':
        return random.sample(traços_bebe, 1)
    elif idade == 'Criança':
        return random.sample(traços_criança, 2)
    else:
        return random.sample(traços_adultos, 3)

def sortear_tracos_pet(raca):
    if raca == 'Cachorro':
        return random.sample(traços_cachorro, 3)
    elif raca == 'Gato':
        return random.sample(traços_gato, 3)
    elif raca == 'Cavalo':
        return random.sample(traços_cavalo, 3)

def sortear_tracos_pessoa_sem_conflito(idade):
    while True:
        tracos = sortear_tracos_pessoa(idade)
        if not tem_conflito(tracos):
            return tracos

def sortear_tracos_pet_sem_conflito(raca):
    while True:
        tracos = sortear_tracos_pet(raca)
        if not tem_conflito(tracos):
            return tracos

# Função de criar integrante
def criar_integrante():
    tipo = random.choice(['Pessoa', 'Pet'])

    if tipo == 'Pessoa':
        genero = random.choice(generos)
        criatura = random.choice(criaturas)
        idade = random.choice(idades)
        tracos = sortear_tracos_pessoa_sem_conflito(idade)

        return {
            'tipo': 'Pessoa',
            'sexo': genero,
            'raca': criatura,
            'idade': idade,
            'tracos': tracos
        }

    else:
        animal = random.choice(pets)
        sexo = random.choice(sexo_pet)
        idade = random.choice(idades_pet)
        tracos = sortear_tracos_pet_sem_conflito(animal)

        return {
            'tipo': 'Pet',
            'raca': animal,
            'sexo': sexo,
            'idade': idade,
            'tracos': tracos
        }

# Função de criar família
def criar_familia(qtd):
    while True:
        familia = []

        for i in range(qtd):
            familia.append(criar_integrante())

        adultos = 0
        for membro in familia:
            if membro['tipo'] == 'Pessoa' and membro['idade'] in ['Jovem Adulto', 'Adulto', 'Idoso']:
                adultos += 1

        if adultos >= 1:
            return familia

# Programa Principal
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
        print(f"Traços: {', '.join(membro['tracos'])}")
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
