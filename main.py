from modules.BSF import breadthSearchFirst
from modules.UCS import uniformCostSearch
from modules.DSF import depthSearchFirst
from modules.DLS import depthLimitedSearch
from modules.IDDFS import iterativeDeepeningDepthFirstSearch
from modules.Greedy import greedySeache
from modules.entry import *

while True:

    print(
        '\n1- Busca Primeiro na Largura'
        '\n2- Busca de Custo Uniforme'
        '\n3- Busca Primeiro na Profundidade'
        '\n4- Busca de Profundidade Limitada'
        '\n5- Busca de Aprofundamento Iterativo'
        '\n6- Busca Greedy'
        '\n0- Exit')
    option = int(input('Selecione um algoritmo: '))

    start = str(input('Informe o nodo start: '))
    end = str(input('Informe o nodo end: '))

    if option == 1:
        sol = breadthSearchFirst(graph, start, end, showPath=True)
        print(sol)
    elif option == 2:
        sol = uniformCostSearch(graph, start, end, showPath=True)
        print(sol)
    elif option == 3:
        sol = depthSearchFirst(graph, start, end, showPath=True)
        print(sol)
    elif option == 4:
        limit = int(input('Informe o limite: '))
        sol = depthLimitedSearch(graph, start, end, limit, showPath=True)
        print(sol)
    elif option == 5:
        limit = int(input('Informe o limite: '))
        sol = iterativeDeepeningDepthFirstSearch(graph, start, end, limit, showPath=True)
        print(sol)
    elif option == 6:
        sol = greedySeache(graph, heuristic_bucharest, start, end, showPath=True)
        print(sol)
        break
    elif option == 0:
        break
