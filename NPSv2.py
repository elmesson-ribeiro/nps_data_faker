import pandas as pd
import faker
import random
import numpy as np
from datetime import datetime

# Criando um objeto Faker para gerar dados falsos
fake = faker.Faker('pt_BR')  # Define a localidade para o português brasileiro

# Definindo os setores e seus respectivos IDs
setores = [
    {'nome': 'Transporte', 'id': 'id1'},
    {'nome': 'Logística', 'id': 'id2'},
    {'nome': 'Manutenção', 'id': 'id3'},
    {'nome': 'Administrativo', 'id': 'id4'},
    {'nome': 'Tecnologia da Informação', 'id': 'id5'},
    {'nome': 'Qualidade e Segurança', 'id': 'id6'}
]

# Função para gerar notas aleatórias seguindo a distribuição especificada
def gerar_nota():
    rand = random.random()
    if rand <= 0.53:
        return random.randint(0, 6)
    elif rand <= 0.67:
        return random.randint(7, 8)
    else:
        return random.randint(9, 10)

# Criando uma lista para armazenar os dados
dados = []
for i in range(1000):
    setor = random.choice(setores)
    dados.append({
        'ID do Candidato': fake.unique.random_int(min=10000, max=99999),
        'Nome do Candidato': fake.name(),
        'Data': fake.date_between_dates(datetime(year=2023, month=5, day=1), datetime(year=2024, month=5, day=31)),
        'Data_Nascimento': fake.date_between(start_date='-30y', end_date='-20y'),
        'Genero': random.choice(['Masculino', 'Feminino']),
        'Estado_Civil': random.choice(['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)']),
        'Escolaridade': random.choice(['Ensino Fundamental', 'Ensino Médio', 'Superior', 'Pós-graduação']),
        'Raca': random.choice(['Branca', 'Negra', 'Amarela', 'Indígena', 'Parda']),
        'Email': fake.email(),
        'Setor de Contratação': setor['nome'],
        'id setor': setor['id'],
        'Data_Respostas': fake.date_between_dates(datetime(year=2023, month=5, day=1), datetime(year=2024, month=5, day=31)),
        'Nota': gerar_nota()
    })
    
# Criando o DataFrame
df = pd.DataFrame(dados)
# Gerando um array de valores booleanos com 30% de False
num_rows = len(dados)
taxa_respostas_bool = np.random.choice([True, False], size=num_rows, p=[0.7, 0.3])

# Mapeando os valores booleanos para "SIM" e "NÃO"
taxa_respostas = np.where(taxa_respostas_bool, "SIM", "NÃO")

# Definindo Data_Respostas como nulo para respostas NÃO
df.loc[df['Taxa de Respostas'] == 'NÃO', 'Data_Respostas'] = np.nan

# Adicionando a coluna ao DataFrame
for i in range(len(dados)):
    dados[i]['Taxa de Respostas'] = taxa_respostas[i]

# Salvando o DataFrame em um arquivo Excel
df.to_excel('nps_fake.xlsx', index=False)

print("Base de dados gerada com sucesso!")