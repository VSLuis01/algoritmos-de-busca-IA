"""
:param graph -> problem de entra
:param start -> nodo inicial
:param end -> nodo objetivo
:param showPath -> caso True, vai mostrar o caminho, mesmo nao tendo achado o objetivo; caso False nao mostra quando nao achar o objetivo
:return a solucao caso achar o node end, None caso contrário
"""


def depthLimitedSearch(graph, start, end, limit, solution=None, showPath=False):
    if solution is None:
        solution = []
    solution.append(start)
    if start == end:
        return solution

    if limit <= 0:
        if showPath:
            return solution
        else:
            return None

    for i in graph[start]:
        if depthLimitedSearch(graph, i[0], end, limit - 1, solution):
            return solution
    if showPath:
        return solution
    else:
        return None
