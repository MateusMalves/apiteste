todas_as_tarefas = {}

def criar_tarefas():
    tarefa = {}
    nome = input("Qual o Nome da tarefa: ")
    categoria = input("Qual a categoria da tarefa: ")
    prioridade = input("Qual a prioridade dessa tarefa (alta, média, baixa): ")
    descricao = input("Qual a sua descrição: ")

    tarefa["prioridade"] = prioridade
    tarefa["tarefa"] = nome
    tarefa["descricao"] = descricao
    tarefa["concluido"] = False

    if categoria not in todas_as_tarefas:
        todas_as_tarefas[categoria] = []

    todas_as_tarefas[categoria].append(tarefa)

def lista_de_tarefas():
    escolha = int(input("Como você deseja listar as tarefas?\n1 - Todas\n2 - Por Categoria\n3 - Por Prioridade\nEscolha: "))

    if escolha == 1: 
        for categoria, tarefas in todas_as_tarefas.items():
            print(f"Categoria: {categoria}")
            for tarefa in tarefas:
                print(f" - {tarefa['tarefa']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}) - {'Concluída' if tarefa['concluido'] else 'Não Concluída'}")

    elif escolha == 2: 
        categoria_escolhida = input("Qual categoria você deseja visualizar: ")

        if categoria_escolhida in todas_as_tarefas:
            for tarefa in todas_as_tarefas[categoria_escolhida]:
                print(f"{tarefa['tarefa']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}) - {'Concluída' if tarefa['concluido'] else 'Não Concluída'}")
        else:
            print("Categoria não encontrada!") 

    elif escolha == 3: 
        prioridade_escolhida = input("Qual a prioridade que deseja visualizar (alta, média, baixa): ")
        for categoria, listas_tarefa in todas_as_tarefas.items():
            for tarefa in listas_tarefa: 
                if tarefa["prioridade"] == prioridade_escolhida: 
                    print(f"{tarefa['tarefa']} - {tarefa['descricao']} (Categoria: {categoria}) - {'Concluída' if tarefa['concluido'] else 'Não Concluída'}")
    else: 
        print("Opção inválida")

def tarefa_concluida():
    categoria_tarefa = input("Qual a categoria da tarefa que você deseja marcar como concluída: \n")
    nome_tarefa = input("Qual o nome da tarefa que você deseja marcar como concluída: \n")
    
    if categoria_tarefa in todas_as_tarefas:
        tarefas = todas_as_tarefas[categoria_tarefa]
        for tarefa in tarefas:
            if tarefa["tarefa"] == nome_tarefa:
                tarefa_c = int(input("1 - para tarefa concluída\n2 - para não concluída: "))
                tarefa["concluido"] = True if tarefa_c == 1 else False
                print("Tarefa alterada com sucesso!")
                return
        print("Tarefa não encontrada na categoria especificada, tente novamente!")
    else:
        print("Categoria não encontrada, tente novamente!")

def editar_tarefa():
    nome_atual = input("Qual o nome da tarefa que deseja editar: ")
    for categoria, tarefas in todas_as_tarefas.items():
        for tarefa in tarefas:
            if tarefa["tarefa"] == nome_atual:
                novo_nome = input("Qual o novo nome da tarefa: ")
                nova_descricao = input("Qual a nova descrição da tarefa: ")
                tarefa["tarefa"] = novo_nome
                tarefa["descricao"] = nova_descricao
                print("Tarefa editada com sucesso!")
                return
    print("Tarefa não encontrada.")

def remover_tarefa(): 
    categoria_remover = input("De qual categoria você deseja remover a tarefa: ")
    nome_remover = input("Qual o nome da tarefa que você deseja remover: ")

    if categoria_remover in todas_as_tarefas:
        tarefas = todas_as_tarefas[categoria_remover]
        for tarefa in tarefas:
            if tarefa["tarefa"] == nome_remover:
                tarefas.remove(tarefa)
                print("Tarefa removida com sucesso!")
                return
        print("Tarefa não encontrada!")
    else:
        print("Categoria não encontrada!")

print("Bem-vindo ao tarefas CaioTesk")
while True: 
    print("O que deseja fazer agora com o CaioTesk? ")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar como concluído")
    print("4 - Editar Tarefa")
    print("5 - Excluir Tarefa")

    try:
        op = int(input("Qual ação deseja: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue
    
    if op == 1: 
        criar_tarefas()
    elif op == 2:
        lista_de_tarefas()
    elif op == 3:
        tarefa_concluida()
    elif op == 4:
        editar_tarefa()
    elif op == 5:
        remover_tarefa()
    else:
        print("Opção inválida! Tente novamente.")
