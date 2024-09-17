lista_tarefas = []
tarefa = {}

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    #id criado a partir do maior 'id'
    if lista_tarefas:
        id = max(tarefa['id'] for tarefa in lista_tarefas)+1
    else:
        id = 1
    
    tarefa = {
        "id":id,
        "descricao":descricao,
        "status":status,
        "prioridade":prioridade
    }
    lista_tarefas.append(tarefa)

def visualizar_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        for k, v in tarefa.items():
            print(f"{k}: {v}", end=" / ")
        print()


def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = []
    if status != None and prioridade != None:
        tarefas_filtradas=[ tarefa for tarefa in lista_tarefas if tarefa['status'] == status and tarefa['prioridade'] == prioridade ]
    elif status != None or prioridade != None:
        tarefas_filtradas=[ tarefa for tarefa in lista_tarefas if tarefa['status'] == status or tarefa['prioridade'] == prioridade ]
    return tarefas_filtradas

def buscador(lista_tarefas, id):

    pos_ini = 0
    pos_fim = len(lista_tarefas) - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista_tarefas[pos_meio]['id'] == id:
            return lista_tarefas[pos_meio]
        if lista_tarefas[pos_meio]['id'] > id:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1

    return 'Não há tarefa com o ID fornecido'

def menu():
    print(f"{' Gerenciador de Tarefas ':=^40}")
    while True:
        opcao = ''
        while opcao not in ('0', '1', '2', '3', '4'):
            print('Escolha a funcionalidade:')
            print('[0] Adicionar tarefa')
            print('[1] Visualizar tarefas')
            print('[2] Filtrar tarefas')
            print('[3] Buscar tarefa')
            print('[4] Sair')
            opcao = input('>>> ')

        # adicionar tarefa
        if opcao == '0':
            descricao = input("Adicione a descrição: ")

            status = ''
            while status not in ('1', '2', '3'):
                print('Qual o status da tarefa?')
                print('[1] Pendente')
                print('[2] Em andamento')
                print('[3] Concluída')
                status = input('>>> ')

                if status == '1':
                    status = "pendente"
                    break
                elif status == '2':
                    status = "em andamento"
                    break
                elif status == '3':
                    status = "concluída"
                    break

            prioridade = ''
            while prioridade not in ('1', '2', '3'):
                print('Qual a prioridade da tarefa?')
                print('[1] Alta')
                print('[2] Media')
                print('[3] Baixa')
                prioridade = input('>>> ')

                if prioridade == '1':
                    prioridade = "alta"
                    break
                elif prioridade == '2':
                    prioridade = "média"
                    break
                elif prioridade == '3':
                    prioridade = "baixa"
                    break
            adicionar_tarefa(lista_tarefas, descricao, status, prioridade)

        #visualizar tarefas
        elif opcao == '1':
            visualizar_tarefas(lista_tarefas)

        # filtrar tarefas
        elif opcao == '2':
            status = ''
            while status not in ('1', '2', '3', '4'):
                print('Filtrar status:')
                print('[1] Pendente')
                print('[2] Em andamento')
                print('[3] Concluída')
                print('[4] Sem filtro')
                status = input('>>> ')
                
                if status == '1':
                    status = "pendente"
                    break
                elif status == '2':
                    status = "em andamento"
                    break
                elif status == '3':
                    status = "concluída"
                    break
                elif status == '4':
                    status = None
                    break
            prioridade = ''
            while prioridade not in ('1', '2', '3', '4'):
                print('Filtrar prioridade:')
                print('[1] Alta')
                print('[2] Media')
                print('[3] Baixa')
                print('[4] Sem filtro')
                prioridade = input('>>> ')

                if prioridade == '1':
                    prioridade = "alta"
                    break
                elif prioridade == '2':
                    prioridade = "média"
                    break
                elif prioridade == '3':
                    prioridade = "baixa"
                    break
                elif prioridade == '4':
                    prioridade = None
                    break
 
            print(filtrar_tarefas(lista_tarefas, status, prioridade))

        # buscar tarefa pelo id
        elif opcao == '3':
            procurar_id = int(input('Id a ser procurado: '))
            print(buscador(lista_tarefas, procurar_id))
            print()

        # fechar programa
        elif opcao == '4':
            break
 
menu()
