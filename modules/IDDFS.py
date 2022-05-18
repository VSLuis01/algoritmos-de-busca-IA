from modules.DLS import depthLimitedSearch

"""
:param graph -> problem de entra
:param start -> nodo inicial
:param end -> nodo objetivo
:param maxDepth -> profundidade maxima que vai iterar
:param solution -> gambiarra para retornar a solucao
:param showPath -> caso True, vai mostrar o caminho, mesmo nao tendo achado o objetivo; caso False nao mostra quando nao achar o objetivo
:return a solucao caso achar o node end, None caso contrário
"""


def iterativeDeepeningDepthFirstSearch(graph, start, end, maxDepth, solution=None, showPath=False):
    if solution is None:
        solution = []
    for i in range(maxDepth):
        if depthLimitedSearch(graph, start, end, maxDepth, solution):
            return solution
    if showPath:
        return solution
    else:
        return None
