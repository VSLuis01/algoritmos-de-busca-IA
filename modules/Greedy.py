# Método de busca Greedy

# Método de busca Greedy

def pegaNoMenorHeuristicaDentroDaFila(heuristica, fila):
    menorHeuristica = -1
    noMenorHeuristica = None
    for no in fila:
        for item in heuristica:
            chaves = item.keys()
            itemChave = list(chaves)[0]  # Nome da cidade
            if (itemChave == no):
                noEncontrado = item
                break
            else:
                noEncontrado = None

        if (noEncontrado == None):
            return None

        if (noMenorHeuristica == None):
            noMenorHeuristica = noEncontrado
            menorHeuristica = noEncontrado[no]
        elif (noEncontrado[no] < menorHeuristica):
            noMenorHeuristica = noEncontrado
            menorHeuristica = noEncontrado[no]

    return noMenorHeuristica


def processoBuscaGreedy(origemChave, destinoChave, nos, heuristica):
    visitados = set()
    fila = []
    caminho = []
    custo = 0
    noAnterior = origemChave

    fila.insert(0, origemChave)  # Insere a origem na fila
    visitados.add(origemChave)
    while (len(visitados) > 0):
        noParaRemover = pegaNoMenorHeuristicaDentroDaFila(heuristica, fila)

        if (noParaRemover == None):
            print('Cidade não encontrada')
            return [], 0

        chaves = noParaRemover.keys()
        noCorrenteChave = list(chaves)[0]  # Nome da cidade

        if (noAnterior != noCorrenteChave):
            temp = next((item for item in nos if item.get(noAnterior)), None)
            for item in temp[noAnterior]:
                chaves = item.keys()
                itemChave = list(chaves)[0]  # Nome da cidade
                if (itemChave == noCorrenteChave):
                    c = item[itemChave]

            custo += c
            noAnterior = noCorrenteChave

        if (destinoChave == noCorrenteChave):
            caminho.append(noCorrenteChave)
            return caminho, custo

        caminho.append(noCorrenteChave)

        fila.remove(noCorrenteChave)

        noCorrente = next((sub for sub in nos if sub.get(noCorrenteChave)),
                          None)  # Traz toda a estrutura da cidade: {Cidade: [{CidadeVizinha: Custo}]}

        for vizinho in noCorrente[noCorrenteChave]:
            chaves = vizinho.keys()
            vizinhoChave = list(chaves)[0]  # Nome da cidade

            if (vizinhoChave not in visitados):
                fila.insert(0, vizinhoChave)  # Insere a cidade vizinha na fila
                visitados.add(vizinhoChave)  # Atualiza o nó como visitado

    return [], 0


def buscaGreedy(origemChave, destinoChave, nos, heuristica):
    caminho, custo = processoBuscaGreedy(origemChave, destinoChave, nos, heuristica)

    if (len(caminho) > 0):
        # mostrar caminho
        print("Custo gasto: " + str(custo))
        print('Caminho encontrado: ', end='')
        for p in caminho:
            print('-> ' + p, end='')
        print(flush=True)
    else:
        print("Cidade não Encontrada")
        return False


def smallerHeuristic(heuristic, queue):
    smaller = 9999
    smallerHeuristicNode = None

    for j in queue:
        if smaller > heuristic[j]:
            smaller = heuristic[j]
            smallerHeuristicNode = j

    return smallerHeuristicNode


def greedySeache(graph, heuristic, start, end, showPath=False):

    solution = []

    queue = [start]
    visited = []
    cost = 0

    while queue:
        current = smallerHeuristic(heuristic, queue)
        queue.clear()

        solution.append((current, heuristic[current]))

        if current == end:
            return solution

        for neighbour in graph[current]:
            if neighbour[0] not in visited:
                queue.append(neighbour[0])

        visited.append(current)
    if showPath:
        return solution
    else:
        return None
