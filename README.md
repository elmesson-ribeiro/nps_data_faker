# nps_data_faker
Gerador de dados Fake para Analises de dados NPS
Análise Detalhada do Código
Objetivo
O código tem como principal objetivo gerar um conjunto de dados fictícios que simulem resultados de um processo seletivo em uma empresa. Esses dados podem ser utilizados para diversas finalidades, como:

Testar algoritmos de machine learning: Treinar modelos de classificação para prever o sucesso de candidatos, por exemplo.
Criar dashboards e relatórios: Visualizar a distribuição de candidatos por setor, notas obtidas, etc.
Simular cenários: Analisar o impacto de diferentes políticas de recrutamento e seleção.
Funcionamento Passo a Passo
Importação de Bibliotecas:

pandas: Utilizado para manipulação e análise de dados em formato tabular (DataFrames).
faker: Gera dados falsos de forma realista, como nomes, datas, e-mails, etc.
random: Permite gerar números aleatórios.
datetime: Manipulação de datas e horários.
Criação de Dados Falsos:

Objeto Faker: Instancia um objeto da biblioteca Faker para gerar dados aleatórios.
Setores: Define uma lista de dicionários, onde cada dicionário representa um setor com nome e ID.
Função gerar_nota: Gera uma nota aleatória entre 0 e 10, seguindo uma distribuição específica (53% notas entre 0 e 6, 14% entre 7 e 8, 33% entre 9 e 10).
Geração dos Dados:

Lista de dados: Cria uma lista vazia para armazenar os dados de cada candidato.
Loop: Itera 1000 vezes para gerar 1000 candidatos.
Dados do candidato: Para cada candidato, são gerados dados aleatórios como nome, data, e-mail, setor, ID do setor e nota.
Adiciona à lista: Os dados de cada candidato são adicionados à lista.
Criação do DataFrame:

DataFrame: Converte a lista de dados em um DataFrame do pandas, facilitando a manipulação e análise dos dados.
Salvando em Excel:

to_excel: Salva o DataFrame em um arquivo Excel com o nome "nps_fake.xlsx".
Estrutura dos Dados Gerados
O DataFrame resultante terá as seguintes colunas:

ID do Candidato: Um número único para cada candidato.
Nome do Candidato: Um nome fictício gerado pela biblioteca Faker.
Data: Uma data aleatória entre 01/05/2023 e 31/05/2024.
Email: Um endereço de e-mail fictício.
Setor de Contratação: O nome do setor para o qual o candidato se candidatou.
id setor: O ID do setor (usado para identificar o setor de forma única).
Nota: A nota obtida pelo candidato no processo seletivo.
Personalizações Possíveis
Aumentar o número de candidatos: Modificar o valor de range(1000) para gerar mais linhas de dados.
Adicionar mais colunas: Incluir outras informações relevantes, como experiência, habilidades, etc.
Ajustar a distribuição das notas: Modificar os valores nos if da função gerar_nota para obter uma distribuição diferente de notas.
Alterar os setores: Adicionar ou remover setores da lista setores.
Gerar dados mais complexos: Utilizar outras funcionalidades da biblioteca Faker para gerar dados mais elaborados, como endereços, telefones, etc.
Em resumo:

Este código fornece uma base sólida para a geração de dados sintéticos para diversos fins relacionados a processos seletivos. Ao personalizar o código, você pode criar conjuntos de dados mais específicos e complexos para atender às suas necessidades.
