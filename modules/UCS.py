# Fila de prioridade
class PriorityQueue:

    def __init__(self):
        self.queue = []

    # Checar se está vazia
    def isEmpty(self):
        return len(self.queue) == 0

    # Inserir elemento
    def enqueue(self, data):
        self.queue.append(data)

    # pop no elemento de maior prioridade, ou seja, menor custo
    def dequeue(self):
        try:
            min_val = 0
            it = 0
            for i in self.queue:
                if i[1] < self.queue[min_val][1]:
                    min_val = it
                it += 1
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print()
            exit()


"""
:param graph -> problem de entra
:param start -> nodo inicial
:param end -> nodo objetivo
:param showPath -> caso True, vai mostrar o caminho, mesmo nao tendo achado o objetivo; caso False nao mostra quando nao achar o objetivo
:return a solucao caso achar o node end, None caso contrário
"""


def uniformCostSearch(graph, start, end, showPath=False):
    solution = []

    queue = PriorityQueue()

    visited = []

    # adiciona o primeiro no na fila, que tem custo zero
    queue.enqueue((start, 0))

    while not queue.isEmpty():

        # nome da cidade, custo
        current, currentCost = queue.dequeue()

        # encontrou nodo objetivo
        if current == end:
            solution.append((current, currentCost))
            return solution

        solution.append((current, currentCost))

        # expande o nó current e soma seu custo
        if current not in visited:
            for neighbour in graph[current]:
                # gambiarra para somar o custo, pq eu fiz uma tupla, ao inves de lista e não quis mudar
                cumulative_cost = neighbour[1] + currentCost
                lst = list(neighbour)
                lst[1] = cumulative_cost
                neighbour = tuple(lst)

                queue.enqueue(neighbour)
        visited.append(current)
    if showPath:
        return solution
    else:
        return None
