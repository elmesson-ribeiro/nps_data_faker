import pandas as pd
import faker
import random
from datetime import datetime

# Criando um objeto Faker para gerar dados falsos
fake = faker.Faker()

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
        'ID do Candidato': i+1,
        'Nome do Candidato': fake.name(),
        'Data': fake.date_between_dates(datetime(year=2023, month=5, day=1), datetime(year=2024, month=5, day=31)),
        'Email': fake.email(),
        'Setor de Contratação': setor['nome'],
        'id setor': setor['id'],
        'Nota': gerar_nota()
    })

# Criando o DataFrame
df = pd.DataFrame(dados)

# Salvando o DataFrame em um arquivo Excel
df.to_excel('nps_fake.xlsx', index=False)

print("Base de dados gerada com sucesso!")