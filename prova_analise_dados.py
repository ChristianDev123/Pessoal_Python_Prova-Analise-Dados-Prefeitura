import pandas as pd;

DBPrefeitura = pd.read_excel('ticPrefeituraSPExcel.xlsx')

# Questão 1 - Quantos órgãos responderam à pesquisa, por categoria?
def qtdOrgaosPorCategoria():
    print(DBPrefeitura["Q06"].value_counts())

# Questão 2 - Quantas pessoas trabalharam de forma dedicada à TI na Prefeitura de São Paulo?
def qtdPessoasTI():
    res = DBPrefeitura["Q201"].sum()
    return res

''' Questão 3 - 
    Qual proporção de pessoas trabalharam de forma dedicada à TI
    na Prefeitura de São Paulo por categoria?'''
def proporcaoPessoasTIPorCategoria():
    arrayCategorias = [
        DBPrefeitura["Q205[SQ002]"].sum(),
        DBPrefeitura["Q205[SQ003]"].sum(),
        DBPrefeitura["Q205[SQ004]"].sum(),
        DBPrefeitura["Q205[SQ005]"].sum(),
        DBPrefeitura["Q205[SQ006]"].sum(),
        DBPrefeitura["Q205[SQ007]"].sum(),
        DBPrefeitura["Q205[SQ008]"].sum(),
        DBPrefeitura["Q205[SQ009]"].sum(),
        DBPrefeitura["Q205[SQ010]"].sum(),
        DBPrefeitura["Q205[SQ011]"].sum(),
        DBPrefeitura["Q205[SQ012]"].sum(),
        DBPrefeitura["Q205[SQ013]"].sum(),
        DBPrefeitura["Q205[SQ014]"].sum(),
        DBPrefeitura["Q205[SQ015]"].sum(),
    ]
    arrayRespPossiveis = [
        'Estagiário(a/s)',
        'Servidor(es) efetivo(s) de nível básico',
        'Servidor(es) efetivo(s) de nível médio',
        'Servidor(es) efetivo(s) de nível superior',
        'DAI (qualquer)',
        'DAS9',
        'DAS10',
        'DAS11',
        'DAS12',
        'DAS13',
        'DAS14',
        'DAS15',
        'DAS16',
        'Terceirizados',
    ]
    arrayProporcaoPorCategoria = []
    i = 0
    for a in arrayCategorias:
        arrayProporcaoPorCategoria.append(f"{arrayRespPossiveis[i]}:{(a * 100 /qtdPessoasTI()):.2f}%")
        i+=1        
    for x in arrayProporcaoPorCategoria:
        print(x)
    
# Questão 4 - Quantos órgãos utilizam alguma metodologia para gerenciamento de projetos?
def qtdOrgaosMetodologiaGerProj():
    qtdOrgaos = DBPrefeitura["Q713"].value_counts()["Sim"]
    print(f"A quantidade de Orgãos que possuem metodologias de gerenciamento de projetos é: {qtdOrgaos}")

''' Questão 5 - 
    Considerando que todos os computadores locados possuem menos de 5 anos de uso,
    qual é a proporção de computadores que possuem mais de 5 anos
    e ainda são utilizados na Prefeitura de São Paulo?
'''
def proporcaoComputadoresMais5Anos():
    compProprio = DBPrefeitura["Q1001[SQ001_SQ008]"].sum()
    compProprioMais5 = DBPrefeitura["Q1002[SQ001]"].sum()
    print(f"{(compProprioMais5*100/compProprio):.2f}% dos computadores próprios tem mais de 5 anos de uso.")

''' Questão 6 -
    Qual o total de ativos de rede que estão sob
    gestão direta dos órgãos da Prefeitura de São Paulo
    por tipo?
'''
def ativosRedePrefeituraPorCategoria():
    ativosRede = [
        DBPrefeitura["Q1014[SQ001]"].sum(),
        DBPrefeitura["Q1014[SQ002]"].sum(),
        DBPrefeitura["Q1014[SQ003]"].sum(),
        DBPrefeitura["Q1014[SQ004]"].sum(),
        DBPrefeitura["Q1014[SQ005]"].sum(),
        DBPrefeitura["Q1014[SQ006]"].sum(),
        DBPrefeitura["Q1014[SQ007]"].sum(),
    ]
    arrayTiposPossiveis = [
        'Roteadores',
        'Switches',
        'Bridges',
        'Hubs',
        'Repetidores',
        'Firewalls',
        'Access Points',
    ]
    arrayTiposRedes = []
    i = 0
    for a in arrayTiposPossiveis:
        arrayTiposRedes.append(f"{a}: {ativosRede[i]}")
        i+=1
    for x in arrayTiposRedes:
        print(x)

while(True):
    arrayQuestao = [
        'Quantos órgãos responderam à pesquisa, por categoria?',
        'Quantas pessoas trabalharam de forma dedicada à TI na Prefeitura de São Paulo?',
        'Qual proporção de pessoas trabalharam de forma dedicada à TI na Prefeitura de São Paulo por categoria?',
        'Quantos órgãos utilizam alguma metodologia para gerenciamento de projetos?',
        'Considerando que todos os computadores locados possuem menos de 5 anos de uso, qual é a proporção de computadores que possuem mais de 5 anos e ainda são utilizados na Prefeitura de São Paulo?',
        'Qual o total de ativos de rede que estão sob gestão direta dos órgãos da Prefeitura de São Paulo por tipo?'
    ]
    i = 0
    print('Selecione a questão que deseja a resposta:')
    for a in arrayQuestao:
        print(f'[{i+1}] - {a}')
        i += 1
    print(' ')
    print('[0] Sair do programa')
    command = int(input())
    print('='*20)
    if(command != 0): print(arrayQuestao[command-1])
    else:print('Desligando o programa...')
    print(' ')
    if(command == 1):
        qtdOrgaosPorCategoria()
    elif(command == 2):
        print(f'{qtdPessoasTI()} pessoas')
    elif(command == 3):
        proporcaoPessoasTIPorCategoria()
    elif(command == 4):
        qtdOrgaosMetodologiaGerProj()
    elif(command == 5):
        proporcaoComputadoresMais5Anos()
    elif(command == 6):
        ativosRedePrefeituraPorCategoria()
    elif(command == 0):
        break
    print('='*20)