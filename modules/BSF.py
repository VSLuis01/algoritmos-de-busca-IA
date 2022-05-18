"""
:param graph -> problem de entra
:param start -> nodo inicial
:param end -> nodo objetivo
:param showPath -> caso True, vai mostrar o caminho, mesmo nao tendo achado o objetivo; caso False nao mostra quando nao achar o objetivo
:return a solucao caso achar o node end, None caso contrário
"""
def breadthSearchFirst(graph, start, end, showPath=False):
    solution = []

    queue = [start]
    visited = [start]

    while queue:
        # current é o nodo atual, isto é o próximo nó que será expandido
        current = queue.pop(0)
        solution.append(current)

        # encontrou o nodo objetivo
        if current == end:
            return solution

        for neighbour in graph[current]:
            # neighbour[0] está pegando apenas o nome da cidade. Ex='Arad'
            if neighbour[0] not in visited:
                visited.append(neighbour[0])
                queue.append(neighbour[0])
    if showPath:
        return solution
    else:
        return None
